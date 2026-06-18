#!/usr/bin/env python3
"""
validate_workflow_graph.py — the graph-executability contract, made mechanical.

Both the architect (which *emits* the workflow graph) and ai-native-org (which
*operates* it) describe — in prose — the rules that make a workflow graph
runnable rather than decorative:

  - every node is typed (agent / human / policy) and reachable;
  - every parallel fan-out RECONVERGES at an explicit join (a node that declares
    its wait-set, `join_inputs:`), so a case can't complete while half its work
    floats;
  - any node with >1 inbound edge that gates an irreversible action or sits
    downstream of human judgment declares a `join_policy:` (all / quorum:N /
    mutually_exclusive_by:<guard>) — a bare two-edges-into-a-gate releases on
    whichever verdict arrives first, the exact failure the rule prevents;
  - every human/community judgment node declares its full verdict set
    (`verdicts:`), and each non-approve verdict terminates in a NAMED node
    (`routes:` or an edge annotated `on:`), so a "NO" fails loudly instead of
    silently deadlocking the join it was meant to protect;
  - every compounding-context claim is a real `feeds:` edge, not prose.

Until now every invocation re-verified this by eye. This script makes it a
deterministic check the model runs after emitting a graph, so the prose contract
and the artifact cannot drift. Stdlib only — runs anywhere python3 does.

USAGE
  python3 validate_workflow_graph.py <blueprint-or-graph-file> [more files...]
  python3 validate_workflow_graph.py --self-test      # verify the validator itself
  python3 validate_workflow_graph.py --strict <file>  # warnings count as failures

INPUT
  A markdown blueprint containing one or more ```yaml fenced graph blocks, OR a
  raw graph file. A graph block is any YAML block containing a `nodes:` key. The
  node lines use the template's readable DSL
  (`- id: x ; type: agent ; owner: "" ; parallelizable: true`) and/or flow maps
  (`- { id: x, type: agent }`); edges use flow maps
  (`- { from: a, to: b, trigger: "...", feeds: "...", on: decline }`).

EXIT  0 = no errors (PASS).  1 = one or more errors (FAIL).  2 = usage error.
"""

import sys
import re

NODE_TYPES = {"agent", "human", "policy"}
# verdict tokens that count as an "approve" (everything else is a non-approve
# verdict that MUST route to a named node):
APPROVE_TOKENS = {"approve", "approved", "accept", "accepted", "pass", "passed",
                  "yes", "advance", "proceed", "sign", "signed", "ship", "go"}
# id substrings that make a zero-outbound node a plausible true terminal (not a
# stranded branch):
TERMINAL_HINTS = ("deliver", "ship", "done", "end", "terminal", "abort",
                  "decline", "reject", "archive", "close", "publish", " d_", "out")
# id / type substrings that imply an irreversible real-world action needing a gate:
IRREVERSIBLE_HINTS = ("deploy", "ship", "send", "delete", "migrat", "pay", "wire",
                      "publish", "grant", "issue", "launch", "destroy", "submit",
                      "file", "release", "merge")


class Graph:
    def __init__(self, name, nodes, edges, anchors, gates):
        self.name = name
        self.nodes = nodes            # id -> dict of attrs
        self.edges = edges            # list of dicts {from,to,...}
        self.anchors = anchors        # list of ids
        self.gates = gates            # list of ids


# --------------------------------------------------------------------------- #
# Tolerant parsing (no PyYAML dependency — the node DSL isn't strict YAML)
# --------------------------------------------------------------------------- #

def _split_top(s, sep=","):
    """Split on `sep` characters not inside quotes/brackets/braces."""
    out, depth, q, buf = [], 0, None, []
    for ch in s:
        if q:
            buf.append(ch)
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            buf.append(ch)
        elif ch in "[{(":
            depth += 1
            buf.append(ch)
        elif ch in "]})":
            depth -= 1
            buf.append(ch)
        elif ch in sep and depth == 0:
            out.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if buf:
        out.append("".join(buf))
    return [x.strip() for x in out if x.strip()]


def _split_top_commas(s):
    return _split_top(s, ",")


def _split_fields(s):
    """Node DSL uses ';' between fields; flow maps use ','. Pick whichever is a
    real top-level separator (a ';' inside a quoted trigger must not split)."""
    semi = _split_top(s, ";")
    return semi if len(semi) > 1 else _split_top(s, ",")


def _strip_inline_comment(s):
    """Drop a trailing ` # comment` when the '#' is outside quotes/brackets."""
    depth, q = 0, None
    for i, ch in enumerate(s):
        if q:
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
        elif ch in "[{(":
            depth += 1
        elif ch in "]})":
            depth -= 1
        elif ch == "#" and depth == 0:
            return s[:i].rstrip()
    return s


def _unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def _coerce(v):
    v = _unquote(v)
    low = v.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    return v


def _parse_kv_pairs(s):
    """Parse `key: value ; key: value` or `key: value, key: value` into a dict.
    Values may be lists `[a, b]`. Tolerant of both `;` and top-level `,`."""
    d = {}
    parts = _split_fields(s)
    for p in parts:
        if ":" not in p:
            continue
        k, _, v = p.partition(":")
        k = k.strip()
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            d[k] = [_coerce(x) for x in _split_top_commas(v[1:-1])]
        elif v.startswith("{") and v.endswith("}"):
            inner = {}
            for kv in _split_top_commas(v[1:-1]):
                if ":" in kv:
                    ik, _, iv = kv.partition(":")
                    inner[ik.strip()] = _coerce(iv)
            d[k] = inner
        else:
            d[k] = _coerce(v)
    return d


def _extract_blocks(text):
    """Return the bodies of fenced code blocks that look like a graph (contain a
    `nodes:` key), or the whole text if it's a raw graph file. Scans fences
    line-by-line so interleaved non-YAML blocks (e.g. a Mermaid diagram between
    two YAML graphs) can't mis-pair the fences."""
    blocks, in_fence, lang, buf = [], False, "", []
    for line in text.splitlines():
        stripped = line.strip()
        if not in_fence:
            m = re.match(r"^`{3,}\s*([A-Za-z0-9_-]*)\s*$", stripped)
            if m:
                in_fence, lang, buf = True, m.group(1).lower(), []
        else:
            if re.match(r"^`{3,}\s*$", stripped):
                body = "\n".join(buf)
                if (lang in ("", "yaml", "yml", "graph")
                        and re.search(r"^\s*nodes\s*:", body, re.MULTILINE)):
                    blocks.append(body)
                in_fence, lang, buf = False, "", []
            else:
                buf.append(line)
    if not blocks and re.search(r"^\s*nodes\s*:", text, re.MULTILINE):
        blocks.append(text)
    return blocks


def parse_graph(block):
    """Tolerant of two equivalent forms: join/verdict info inline on the node
    (`- id: x ; join_inputs: [...] ; verdicts: [...] ; routes: {...}`) OR in
    separate top-level `joins:` and `verdict_sets:` sections. Both are merged
    onto the node dict before checking."""
    name, nodes, edges, anchors, gates = "(unnamed)", {}, [], [], []
    joins, verdict_sets = [], {}
    section, cur_join = None, None
    for raw in block.splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        line = _strip_inline_comment(raw.strip())
        if not line:
            continue
        is_item = line.startswith("-")
        m = re.match(r"^(\w+)\s*:\s*(.*)$", line)
        # top-level keys (column 0, not a list item)
        if m and not is_item and indent == 0:
            key, rest = m.group(1), m.group(2).strip()
            cur_join = None
            if key == "workflow":
                name = _unquote(rest) or name
                section = None
            elif key in ("nodes", "edges", "joins"):
                section = key
            elif key == "verdict_sets":
                section = "verdict_sets"
            elif key in ("judgment_anchors", "policy_gates"):
                section = None
                if rest.startswith("[") and rest.endswith("]"):
                    vals = [_coerce(x) for x in _split_top_commas(rest[1:-1])]
                    (anchors if key == "judgment_anchors" else gates).extend(vals)
            else:
                section = None
            continue
        # verdict_sets rows:  nodeid: { approve: a, decline: b }
        if section == "verdict_sets" and not is_item and ":" in line:
            nid, _, rest = line.partition(":")
            rest = rest.strip()
            if rest.startswith("{") and rest.endswith("}"):
                routes = {}
                for kv in _split_top_commas(rest[1:-1]):
                    if ":" in kv:
                        vk, _, vv = kv.partition(":")
                        routes[vk.strip()] = _coerce(vv)
                verdict_sets[nid.strip()] = routes
            continue
        if is_item:
            body = line[1:].strip()
            if body.startswith("{") and body.endswith("}"):
                body = body[1:-1]
            attrs = _parse_kv_pairs(body)
            if section == "nodes":
                nid = attrs.get("id")
                if nid is not None:
                    nodes[str(nid)] = attrs
            elif section == "edges":
                if "from" in attrs and "to" in attrs:
                    edges.append(attrs)
            elif section == "joins":
                cur_join = attrs
                joins.append(cur_join)
            continue
        # continuation line inside a joins item (indented key: value)
        if section == "joins" and cur_join is not None and ":" in line:
            cur_join.update(_parse_kv_pairs(line))
            continue

    # merge the sectioned forms onto their nodes
    for j in joins:
        jid = str(j.get("id", ""))
        if jid in nodes:
            for k in ("join_inputs", "join_policy"):
                if k in j:
                    nodes[jid][k] = j[k]
    for nid, routes in verdict_sets.items():
        if nid in nodes:
            nodes[nid]["verdicts"] = list(routes.keys())
            nodes[nid]["routes"] = routes
    return Graph(name, nodes, edges, anchors, gates)


# --------------------------------------------------------------------------- #
# The checks
# --------------------------------------------------------------------------- #

class Finding:
    def __init__(self, level, code, msg):
        self.level, self.code, self.msg = level, code, msg


def _is_approve(token):
    return str(token).strip().lower() in APPROVE_TOKENS


def check_graph(g):
    f = []
    err = lambda c, m: f.append(Finding("ERROR", c, m))
    warn = lambda c, m: f.append(Finding("WARN", c, m))

    if not g.nodes:
        err("E_EMPTY", "graph has no nodes")
        return f

    # inbound / outbound maps
    inbound, outbound = {nid: [] for nid in g.nodes}, {nid: [] for nid in g.nodes}
    for e in g.edges:
        frm, to = str(e.get("from")), str(e.get("to"))
        if frm not in g.nodes:
            err("E_EDGE_UNKNOWN_NODE", f"edge from unknown node '{frm}'")
        else:
            outbound[frm].append(e)
        if to not in g.nodes:
            err("E_EDGE_UNKNOWN_NODE", f"edge to unknown node '{to}'")
        else:
            inbound[to].append(e)

    # node-level checks
    types_seen = set()
    for nid, n in g.nodes.items():
        t = str(n.get("type", "")).strip().lower()
        types_seen.add(t)
        if not t:
            err("E_NODE_UNTYPED", f"node '{nid}' has no type")
        elif t not in NODE_TYPES:
            err("E_NODE_BAD_TYPE",
                f"node '{nid}' has type '{t}' (expected agent / human / policy)")

        # A branching human judgment node needs a full verdict set; a terminal
        # human sink (a decline/exit node with no onward branch) does not.
        is_terminal = bool(n.get("terminal")) or not outbound.get(nid)
        is_human_judgment = ((t == "human") or (nid in g.anchors)) and not is_terminal
        # full verdict set on every human/community judgment node
        if is_human_judgment:
            verdicts = n.get("verdicts")
            if not verdicts:
                err("E_NO_VERDICT_SET",
                    f"human judgment node '{nid}' declares no verdict set "
                    f"(add e.g. verdicts: [approve, decline, amend])")
            else:
                if isinstance(verdicts, str):
                    verdicts = [verdicts]
                non_approve = [v for v in verdicts if not _is_approve(v)]
                routes = n.get("routes") or {}
                edge_verdicts = {str(e.get("on", "")).lower()
                                 for e in outbound.get(nid, []) if e.get("on")}
                for v in non_approve:
                    covered = (str(v) in routes) or (str(v).lower() in edge_verdicts)
                    if not covered:
                        err("E_VERDICT_UNROUTED",
                            f"node '{nid}' verdict '{v}' has no named destination "
                            f"(a 'NO' wired only into an all-join silently deadlocks "
                            f"it). Add routes:{{{v}: <node>}} or an edge on: {v}.")

    # forward reachability (to tell a concurrent fan-out join from a loop-back).
    adj = {nid: [str(e.get("to")) for e in outbound[nid] if str(e.get("to")) in g.nodes]
           for nid in g.nodes}
    _reach_cache = {}

    def reachable_from(start):
        if start in _reach_cache:
            return _reach_cache[start]
        seen, stack = set(), list(adj.get(start, []))
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            stack.extend(adj.get(cur, []))
        _reach_cache[start] = seen
        return seen

    # reconvergence + join semantics — only CONCURRENT inbound edges count as a
    # fan-out join; a back edge (re-review / renegotiate loop-back) does not.
    for nid in g.nodes:
        n = g.nodes[nid]
        # an edge is a loop-back iff its source is reachable FROM nid:
        concurrent = [e for e in inbound[nid]
                      if str(e.get("from")) not in reachable_from(nid)]
        if len(concurrent) >= 2:
            if "join_inputs" not in n:
                err("E_IMPLICIT_JOIN",
                    f"node '{nid}' has {len(concurrent)} concurrent inbound edges "
                    f"but is not an explicit join (declare join_inputs: [...] — an "
                    f"implicit join either deadlocks or races).")
            t = str(n.get("type", "")).lower()
            sources_are_judgment = any(
                (str(e.get("from")) in g.anchors)
                or (str(g.nodes.get(str(e.get("from")), {}).get("type", "")).lower() == "human")
                for e in concurrent)
            if (t == "policy" or sources_are_judgment) and "join_policy" not in n:
                err("E_NO_JOIN_POLICY",
                    f"gate '{nid}' has {len(concurrent)} inbound edges and gates an "
                    f"irreversible action / sits downstream of human judgment, "
                    f"but declares no join_policy (all / quorum:N / "
                    f"mutually_exclusive_by:<guard>). It would release on the "
                    f"first verdict to arrive.")
            jp = n.get("join_policy")
            if jp is not None:
                jps = str(jp).strip().lower()
                if not (jps == "all" or jps.startswith("quorum")
                        or jps.startswith("mutually_exclusive")):
                    err("E_BAD_JOIN_POLICY",
                        f"node '{nid}' join_policy '{jp}' is not one of "
                        f"all / quorum:N / mutually_exclusive_by:<guard>")

    # dangling branches / terminals
    entries = [nid for nid in g.nodes if not inbound[nid]]
    if len(entries) == 0 and g.nodes:
        warn("W_NO_ENTRY", "no entry node (every node has an inbound edge — cyclic?)")
    for nid in g.nodes:
        if not outbound[nid]:
            looks_terminal = (bool(g.nodes[nid].get("terminal"))
                              or any(h in nid.lower() for h in TERMINAL_HINTS))
            t = str(g.nodes[nid].get("type", "")).lower()
            if not looks_terminal and t != "policy":
                warn("W_DANGLING",
                     f"node '{nid}' has no outgoing edge and doesn't look like a "
                     f"true terminal — a stranded branch lets a case finish while "
                     f"part of its work floats. Route it to a join or a named end.")

    # compounding context must be a real edge
    if not any(e.get("feeds") for e in g.edges):
        warn("W_NO_FEEDS",
             "no edge declares feeds: — nothing writes compounding context, so "
             "the self-improving loop lives only in prose (M.03/M.04).")

    # judgment scarcity sanity
    human_nodes = [nid for nid, n in g.nodes.items()
                   if str(n.get("type", "")).lower() == "human"]
    if not human_nodes and "human" not in types_seen:
        warn("W_NO_HUMAN",
             "no human node at all — either judgment is fully automated (check "
             "the stop-lines / sacred core) or the judgment node is missing.")
    if g.edges and human_nodes:
        human_edge_targets = sum(1 for e in g.edges
                                 if str(e.get("to")) in human_nodes)
        if human_edge_targets >= max(2, len(g.edges) * 0.6):
            warn("W_HUMAN_DENSE",
                 "a human sits on most edges — that's approval density / vigilance "
                 "decay, not scarce judgment. Concentrate the human at the few "
                 "irreducible nodes.")

    # anchors / gates reference real nodes of the right type
    for a in g.anchors:
        if str(a) not in g.nodes:
            err("E_ANCHOR_UNKNOWN", f"judgment_anchors lists unknown node '{a}'")
        elif str(g.nodes[str(a)].get("type", "")).lower() != "human":
            warn("W_ANCHOR_NOT_HUMAN",
                 f"judgment_anchor '{a}' is not a human node")
    for gt in g.gates:
        if str(gt) not in g.nodes:
            err("E_GATE_UNKNOWN", f"policy_gates lists unknown node '{gt}'")
        elif str(g.nodes[str(gt)].get("type", "")).lower() != "policy":
            warn("W_GATE_NOT_POLICY", f"policy_gate '{gt}' is not a policy node")

    # irreversible action without a gate in front of it
    gate_ids = set(map(str, g.gates)) | {nid for nid, n in g.nodes.items()
                                         if str(n.get("type", "")).lower() == "policy"}
    for nid in g.nodes:
        if any(h in nid.lower() for h in IRREVERSIBLE_HINTS) and nid not in gate_ids:
            preds = {str(e.get("from")) for e in inbound[nid]}
            if not (preds & gate_ids):
                warn("W_IRREVERSIBLE_UNGATED",
                     f"node '{nid}' looks irreversible but no policy gate precedes "
                     f"it — an irreversible/adverse action belongs behind a gate.")

    return f


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #

def report(path, graphs_findings, strict):
    total_err = total_warn = 0
    print(f"\n=== {path} ===")
    if not graphs_findings:
        print("  (no workflow-graph blocks found — nothing to validate)")
        return 0, 0
    for i, (g, findings) in enumerate(graphs_findings, 1):
        errs = [x for x in findings if x.level == "ERROR"]
        warns = [x for x in findings if x.level == "WARN"]
        total_err += len(errs)
        total_warn += len(warns)
        print(f"\n  [graph {i}: {g.name}]  {len(g.nodes)} nodes, {len(g.edges)} edges")
        for x in findings:
            print(f"    {x.level:5}  {x.code:24}  {x.msg}")
        if not findings:
            print("    OK — no issues")
        eff_err = len(errs) + (len(warns) if strict else 0)
        verdict = "FAIL" if eff_err else "PASS"
        print(f"    -> {verdict}: {len(errs)} error(s), {len(warns)} warning(s)")
    return total_err, total_warn


SELF_TEST_GOOD = """
```yaml
workflow: refund-approval
nodes:
  - id: intake     ; type: agent  ; owner: ""            ; parallelizable: false
  - id: scan_a     ; type: agent  ; owner: ""            ; parallelizable: true
  - id: scan_b     ; type: agent  ; owner: ""            ; parallelizable: true
  - id: synth      ; type: agent  ; owner: ""            ; join_inputs: [scan_a, scan_b]
  - id: judge      ; type: human  ; owner: "reviewer"    ; verdicts: [approve, decline, amend] ; routes: {decline: abort, amend: respec}
  - id: pay_gate   ; type: policy ; owner: "finance"     ; join_inputs: [judge] ; join_policy: all
  - id: respec     ; type: agent  ; owner: ""
  - id: abort      ; type: agent  ; owner: ""
edges:
  - { from: intake, to: scan_a, trigger: "request in", feeds: "ctx/raw" }
  - { from: intake, to: scan_b, trigger: "request in", feeds: "ctx/raw" }
  - { from: scan_a, to: synth,  trigger: "scan done",  feeds: "ctx/findings" }
  - { from: scan_b, to: synth,  trigger: "scan done",  feeds: "ctx/findings" }
  - { from: synth,  to: judge,  trigger: "ready",       feeds: "ctx/memo" }
  - { from: judge,  to: pay_gate, trigger: "approved",  feeds: "ctx/decision-log", on: approve }
  - { from: judge,  to: abort,  trigger: "declined",    on: decline }
  - { from: judge,  to: respec, trigger: "amend",       on: amend }
  - { from: respec, to: judge,  trigger: "re-review" }
judgment_anchors: [judge]
policy_gates: [pay_gate]
```
"""

SELF_TEST_BAD = """
```yaml
workflow: grafted-pipeline
nodes:
  - id: intake   ; type: agent
  - id: scan_a   ; type: agent
  - id: scan_b   ; type: agent
  - id: judge    ; type: human
  - id: pay_gate ; type: policy
edges:
  - { from: intake, to: scan_a, trigger: "in" }
  - { from: intake, to: scan_b, trigger: "in" }
  - { from: scan_a, to: pay_gate, trigger: "done" }
  - { from: scan_b, to: pay_gate, trigger: "done" }
  - { from: pay_gate, to: judge, trigger: "review" }
  - { from: judge,  to: missing_node, trigger: "ok" }
```
"""
# Expected errors in the bad graph:
#   E_NO_VERDICT_SET (judge), E_IMPLICIT_JOIN (pay_gate, 2 concurrent inbound),
#   E_NO_JOIN_POLICY (pay_gate gates an irreversible action), E_EDGE_UNKNOWN_NODE.


def self_test():
    good = check_graph(parse_graph(_extract_blocks(SELF_TEST_GOOD)[0]))
    bad = check_graph(parse_graph(_extract_blocks(SELF_TEST_BAD)[0]))
    good_err = [x for x in good if x.level == "ERROR"]
    bad_err = [x for x in bad if x.level == "ERROR"]
    print("SELF-TEST")
    print(f"  good graph: {len(good_err)} errors (expect 0), "
          f"{len([x for x in good if x.level=='WARN'])} warnings")
    for x in good_err:
        print(f"    unexpected: {x.code} {x.msg}")
    print(f"  bad graph:  {len(bad_err)} errors (expect >=3)")
    for x in bad:
        print(f"    {x.level:5} {x.code:24} {x.msg}")
    ok = (len(good_err) == 0) and (len(bad_err) >= 3)
    print("  RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    flags = {a for a in argv if a.startswith("--")}
    if "--self-test" in flags:
        return self_test()
    if not args:
        print(__doc__)
        return 2
    strict = "--strict" in flags
    grand_err = grand_warn = 0
    for path in args:
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as e:
            print(f"cannot read {path}: {e}")
            grand_err += 1
            continue
        gf = [(g, check_graph(g)) for g in
              (parse_graph(b) for b in _extract_blocks(text))]
        e, w = report(path, gf, strict)
        grand_err += e
        grand_warn += w
    eff = grand_err + (grand_warn if strict else 0)
    print(f"\nSUMMARY: {'FAIL' if eff else 'PASS'} — "
          f"{grand_err} error(s), {grand_warn} warning(s)"
          f"{' (strict: warnings fail)' if strict else ''}.")
    return 1 if eff else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
