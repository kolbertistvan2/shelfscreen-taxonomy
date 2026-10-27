"""Assemble the category tree (v0.3, 2026-10-27): Shopify v2026-08 backbone, Hungarian and English renames, own nodes,
the Racket Sports group, node moves, links, Shopify's full attribute lists as filters (plus the filter additions of
v0.3), and Arukereso categories with their listed product counts (v0.3 remaps applied first). Every node is shown
(operator 2026-10-26: "mindent"); has_products_hu stays null until our own shop reads fill it."""
import collections, json, re, sys
from pathlib import Path

T = Path(sys.argv[1])


def jl(name):
    p = T / "work" / name
    return [json.loads(l) for l in open(p, encoding="utf-8")] if p.exists() else []


nodes = {}
for line in open(T / "work/shopify-v2026-08.tsv", encoding="utf-8"):
    p = line.rstrip("\n").split("\t")
    if p[0] == "id":
        continue
    nid, en, hu = p
    parent = nid.rsplit("-", 1)[0] if "-" in nid else None
    nodes[nid] = {"id": nid, "parent_id": parent, "name_en": en.split(" > ")[-1], "name_hu": hu.split(" > ")[-1],
                  "source": "shopify-v2026-08", "renamed_hu_from": None, "renamed_en_from": None, "arukereso": [],
                  "filters": [], "links": []}

renamed = 0
for i in (1, 2, 3):
    for r in jl(f"hu-renames-{i}.jsonl"):
        n = nodes[r["id"]]
        n["renamed_hu_from"], n["name_hu"] = n["name_hu"], r["new_hu"]
        renamed += 1

own_rows = jl("own-nodes.jsonl")
for r in own_rows:
    nodes[r["id"]] = {"id": r["id"], "parent_id": r["parent_id"], "name_en": r["name_en"], "name_hu": r["name_hu"],
                      "source": "own", "renamed_hu_from": None, "renamed_en_from": None, "arukereso": [], "filters": [],
                      "links": [], "reason": r["reason"]}
    if r.get("evidence"):
        nodes[r["id"]]["evidence"] = r["evidence"]

# Racket Sports: one family under Sporting Goods > Athletics
nodes["own-racket-sports"] = {"id": "own-racket-sports", "parent_id": "sg-1", "name_en": "Racket Sports",
                              "name_hu": "Ütős sportok", "source": "own", "renamed_hu_from": None, "renamed_en_from": None,
                              "arukereso": [], "filters": [], "links": [],
                              "reason": "Tennis, padel, pickleball, squash, badminton and table tennis as one family."}
for nid in ("sg-1-20", "own-padel", "sg-4-14-6", "sg-1-15", "sg-4-14-1", "sg-3-6"):
    nodes[nid]["parent_id"] = "own-racket-sports"
# The platform tennis node keeps no padel and no paddle wording
nodes["sg-4-14-7"].update(name_en="Platform Tennis", name_hu="Platformtenisz")
for nid, en, hu in (("sg-4-14-7-1", "Platform Tennis Rackets", "Platformtenisz-ütők"),
                    ("sg-4-14-7-4", "Platform Tennis Grips & Tape", "Platformtenisz markolatok"),
                    ("sg-4-14-7-5", "Platform Tennis Bags", "Platformtenisz-táskák"),
                    ("sg-4-14-7-6", "Platform Tennis Shoes", "Platformtenisz-cipők")):
    nodes[nid].update(name_en=en, name_hu=hu)

# Table tennis in European English, without the paddle wording; mixing paddles are rods
for nid, n in nodes.items():
    if nid == "sg-3-6" or nid.startswith("sg-3-6-"):
        n["name_en"] = n["name_en"].replace("Ping Pong", "Table Tennis").replace("Paddles", "Bats").replace("Paddle", "Bat")
nodes["ha-14-14"]["name_en"] = "Mixing Rods"

# v0.2: English renames (Football (Soccer)), Hungarian renames of the v0.2 review, node moves, links
for r in jl("en-renames.jsonl"):
    n = nodes[r["id"]]
    assert n["name_en"] == r["old_en"], r
    n["renamed_en_from"], n["name_en"] = n["name_en"], r["new_en"]
renamed4 = 0
for r in jl("hu-renames-4.jsonl"):
    n = nodes[r["id"]]
    assert n["name_hu"] == r["old_hu"] or n["source"] == "own", (r, n["name_hu"])
    if n["renamed_hu_from"] is None and n["source"] != "own":
        n["renamed_hu_from"] = n["name_hu"]
    n["name_hu"] = r["new_hu"]
    renamed4 += 1
renamed5 = 0
for r in jl("hu-renames-5.jsonl"):  # v0.3: the name review of the nodes v0.2 did not review, with the consistency fixes
    n = nodes[r["id"]]
    assert n["name_hu"] == r["old_hu"], (r, n["name_hu"])
    if n["renamed_hu_from"] is None and n["source"] != "own":
        n["renamed_hu_from"] = n["name_hu"]
    n["name_hu"] = r["new_hu"]
    renamed5 += 1
renamed6 = 0
for r in jl("hu-renames-6.jsonl"):  # v0.3.1: fix round 1 of the v0.3.0 review, own-node name checks and the consistency fixes
    n = nodes[r["id"]]
    assert n["name_hu"] == r["old_hu"], (r, n["name_hu"])
    if n["renamed_hu_from"] is None and n["source"] != "own":
        n["renamed_hu_from"] = n["name_hu"]
    n["name_hu"] = r["new_hu"]
    renamed6 += 1
renamed7 = 0
for r in jl("hu-renames-7.jsonl"):  # v0.5.0: shop words for nodes the tree gaps showed (Búvárkomputerek, Radlerek és sörkoktélok)
    n = nodes[r["id"]]
    assert n["name_hu"] == r["old_hu"], (r, n["name_hu"])
    if n["renamed_hu_from"] is None and n["source"] != "own":
        n["renamed_hu_from"] = n["name_hu"]
    n["name_hu"] = r["new_hu"]
    renamed7 += 1
for r in jl("node-moves.jsonl"):
    assert r["new_parent_id"] in nodes, r
    old = r.get("old_parent_id") or r["id"].rsplit("-", 1)[0]
    assert nodes[r["id"]]["parent_id"] == old, (r, nodes[r["id"]]["parent_id"])
    nodes[r["id"]]["parent_id"] = r["new_parent_id"]
    nodes[r["id"]]["moved_from"] = old
n_links = 0
for r in jl("links.jsonl"):
    for t in r["to"]:
        assert t in nodes, (r["from"], t)
    nodes[r["from"]]["links"] = sorted(set(nodes[r["from"]]["links"]) | set(r["to"]))
n_links = sum(len(n["links"]) for n in nodes.values())

# Hungarian review scope: v0.1 reviewed the nodes that held Arukereso categories, v0.2 the sport, shoes and clothing branches
reviewed = {}
for line in open(T / "work/hu-review-scope.tsv", encoding="utf-8"):
    nid, rev = line.rstrip("\n").split("\t")
    if nid != "id":
        reviewed[nid] = rev
for n in nodes.values():
    n["name_hu_reviewed"] = n["id"] in reviewed  # v0.3.1: own nodes too need a scope line

# Arukereso categories: own node when the own-nodes step placed them, else the mapped Shopify node
own_of = {p: r["id"] for r in own_rows for p in r["arukereso_paths"]}
remap = {}
for r in jl("arukereso-remaps.jsonl"):  # v0.3: an Arukereso category moved to another existing node, with its reason
    remap[r["arukereso_path"]] = r
not_counted = {r["arukereso_path"] for r in jl("arukereso-not-counted.jsonl")}
for m in jl("mapping-arukereso.jsonl"):
    nid = own_of.get(m["arukereso_path"], m["shopify_id"])
    if m["arukereso_path"] in remap:
        r = remap.pop(m["arukereso_path"])
        assert r["old_id"] == nid and r["new_id"] in nodes, (r, nid)
        nid = r["new_id"]
    nodes[nid]["arukereso"].append({"path": m["arukereso_path"], "url": m["url"], "relation": m["relation"],
                                    "listed_products": m.get("products_listed_2026_10_19"),
                                    "counted": m["arukereso_path"] not in not_counted})

# Filters. Shopify's attribute list of the node's category, all values; an own node takes the list of the category
# named in its filters_from, else of its nearest Shopify ancestor. Names: the v0.2 review, then v0.1, then Shopify.
VAL = re.compile(r"gid://shopify/TaxonomyValue/(\d+)\s+: (.*) \[(.*)\]$")
NAME = re.compile(r"gid://shopify/TaxonomyAttribute/(\d+)\s+: (.*)$")


def names(path, rx):
    out = {}
    for line in open(T / path, encoding="utf-8"):
        m = rx.match(line.rstrip("\n"))
        if m:
            out[m.group(1)] = m.group(2)
    return out


val_en, val_hu = names("sources/shopify-v2026-08/attribute_values.en.txt", VAL), names("sources/shopify-v2026-08/attribute_values.hu.txt", VAL)
attr_hu = names("sources/shopify-v2026-08/attributes.hu.txt", NAME)
A = {}
for line in open(T / "work/shopify-v2026-08-attributes.tsv", encoding="utf-8"):
    h, gid, en, base, vids = line.rstrip("\n").split("\t")
    if h == "handle":
        continue
    A[h] = {"attribute_id": h, "shopify_id": gid or None, "base_attribute_id": base or None, "name_en": en,
            "name_hu": attr_hu.get(gid), "name_hu_reviewed": False, "vids": vids.split(",") if vids else []}
for h, a in A.items():
    if a["base_attribute_id"]:
        b = A[a["base_attribute_id"]]
        a["vids"], a["name_hu"] = b["vids"], b["name_hu"]
VH = {v: {"en": val_en[v], "hu": val_hu.get(v), "hu_reviewed": False, "renamed_hu_from": None} for a in A.values() for v in a["vids"]}
# v0.1 filter names (node-attributes.jsonl, source shopify) override Shopify's Hungarian
for r in jl("node-attributes.jsonl"):
    if r["source"] == "shopify" and r["attribute_id"] in A:
        a = A[r["attribute_id"]]
        a["name_hu"], a["name_hu_reviewed"] = r["name_hu"], True
        by_en = {VH[v]["en"]: v for v in a["vids"]}
        for v in r["values"]:
            if v["en"] in by_en and v.get("hu"):
                VH[by_en[v["en"]]].update(hu=v["hu"], hu_reviewed=True)
# v0.2 review: an attribute in the review scope has a reviewed name; a value counts as reviewed only when its id is
# in filter-values-checked.txt (checked one by one) or it was corrected in filter-renames.jsonl
scope = [l.strip() for l in open(T / "work/filter-hu-review-scope.txt", encoding="utf-8") if l.strip() and not l.startswith("#")]
for h in scope:
    A[h]["name_hu_reviewed"] = True
checked = [l.strip() for l in open(T / "work/filter-values-checked.txt", encoding="utf-8") if l.strip() and not l.startswith("#")]
for v in checked:
    VH[v]["hu_reviewed"] = True
filter_renamed = 0
for r in jl("filter-renames.jsonl"):
    x = A[r["attribute_id"]] if r["kind"] == "attribute" else VH[r["value_id"]]
    key = "name" if r["kind"] == "attribute" else ""
    en_k, hu_k = ("name_en", "name_hu") if key else ("en", "hu")
    if "new_en" in r:
        assert x[en_k] == r["old_en"], r
        x[en_k] = r["new_en"]
    if "new_hu" in r:
        assert x[hu_k] == r["old_hu"], (r, x[hu_k])
        x["renamed_hu_from"], x[hu_k] = x[hu_k], r["new_hu"]
        x["name_hu_reviewed" if key else "hu_reviewed"] = True
    filter_renamed += 1
for a in A.values():  # an extended attribute keeps its own English name but takes a reviewed base name only if unreviewed
    if a["base_attribute_id"] and not a["name_hu"]:
        a["name_hu"] = A[a["base_attribute_id"]]["name_hu"]

cat_attrs = {}
for line in open(T / "work/shopify-v2026-08-category-attributes.tsv", encoding="utf-8"):
    cid, hs = line.rstrip("\n").split("\t")
    if cid != "id":
        cat_attrs[cid] = [h for h in hs.split(",") if h]
filters_from = {r["id"]: r.get("filters_from") for r in own_rows}


def attr_source(nid):
    n = nodes[nid]
    if n["source"] != "own":
        return nid
    if filters_from.get(nid):
        return filters_from[nid]
    return attr_source(n["parent_id"])


used = set()
for nid, n in nodes.items():
    src = attr_source(nid)
    hs = list(cat_attrs.get(src, []))
    if src != nid:
        n["filters_from"] = src
    n["filters"] = [{"attribute_id": h, "source": "shopify"} for h in hs]
for r in jl("node-attributes.jsonl"):
    n = nodes[r["shopify_id"]]
    have = {f["attribute_id"] for f in n["filters"]}
    if r["source"] == "own":
        n["filters"].append({"attribute_id": r["attribute_id"], "source": "own", "name_en": r["name_en"], "name_hu": r["name_hu"],
                             "name_hu_reviewed": True, "values": [{"en": v.get("en"), "hu": v.get("hu")} for v in r["values"]]})
    elif r["attribute_id"] not in have and r["attribute_id"] in A:
        n["filters"].append({"attribute_id": r["attribute_id"], "source": "shopify"})
assert not remap, remap
filters_added = 0
for r in jl("filter-adds.jsonl"):  # v0.3: a filter the node lacked, each with its reason
    n = nodes[r["id"]]
    assert not any(f["attribute_id"] == r["attribute_id"] for f in n["filters"]), r
    if r["source"] == "shopify":
        assert r["attribute_id"] in A, r
        n["filters"].append({"attribute_id": r["attribute_id"], "source": "shopify"})
    else:
        src = [f for f in nodes[r["copy_from"]]["filters"] if f["attribute_id"] == r["attribute_id"]]
        assert len(src) == 1, r
        n["filters"].append(dict(src[0]))
    n.setdefault("filters_added", []).append({"attribute_id": r["attribute_id"], "reason": r["reason"]})
    filters_added += 1
for r in jl("filter-drops.jsonl"):  # v0.2: inherited filters that do not apply to the node, each with its reason
    n = nodes[r["id"]]
    assert any(f["attribute_id"] == r["attribute_id"] for f in n["filters"]), r
    n["filters"] = [f for f in n["filters"] if f["attribute_id"] != r["attribute_id"]]
    n.setdefault("filters_dropped", []).append({"attribute_id": r["attribute_id"], "reason": r["reason"]})
for n in nodes.values():  # a Shopify filter names its attribute; names and values are in dist/attributes.jsonl
    used.update(f["attribute_id"] for f in n["filters"] if f["source"] == "shopify")

children = collections.defaultdict(list)
for n in nodes.values():
    if n["parent_id"]:
        assert n["parent_id"] in nodes, n["id"]
        children[n["parent_id"]].append(n["id"])


def walk(nid, depth, pen, phu):
    n = nodes[nid]
    n["depth"], n["path_en"], n["path_hu"] = depth, pen + [n["name_en"]], phu + [n["name_hu"]]
    own = sum(a["listed_products"] or 0 for a in n["arukereso"] if a["counted"])
    sub = own + sum(walk(c, depth + 1, n["path_en"], n["path_hu"]) for c in children[nid])
    n["arukereso_products_own"], n["arukereso_products_subtree"] = own, sub
    n["has_products_hu"] = None
    return sub


for root in [n["id"] for n in nodes.values() if not n["parent_id"]]:
    walk(root, 1, [], [])
assert all("depth" in n for n in nodes.values()), "a node is cut off from the tree"

KEYS = ("id", "parent_id", "depth", "name_en", "name_hu", "name_hu_reviewed", "path_en", "path_hu", "source", "renamed_hu_from",
        "renamed_en_from", "moved_from", "reason", "evidence", "links", "has_products_hu", "arukereso_products_own",
        "arukereso_products_subtree", "arukereso", "filters_from", "filters", "filters_added", "filters_dropped")
out = sorted(nodes.values(), key=lambda n: n["path_en"])
with open(T / "dist/tree.jsonl", "w", encoding="utf-8") as f:
    for n in out:
        d = {k: n[k] for k in KEYS if k in n}
        d["path_en"], d["path_hu"] = " > ".join(n["path_en"]), " > ".join(n["path_hu"])
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
with open(T / "dist/attributes.jsonl", "w", encoding="utf-8") as f:
    for h in sorted(used):
        a = A[h]
        d = {k: a[k] for k in ("attribute_id", "shopify_id", "base_attribute_id", "name_en", "name_hu", "name_hu_reviewed")}
        d["renamed_hu_from"] = a.get("renamed_hu_from")
        d["values"] = [{"id": v, **VH[v]} for v in a["vids"]]
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

# Report and checks
own_n = sum(n["source"] == "own" for n in nodes.values())
nf = sum(len(n["filters"]) for n in nodes.values())
print("nodes", len(nodes), "own", own_n, "hu renamed", renamed, "+", renamed4, "(v0.2) +", renamed5, "(v0.3) +", renamed6, "(v0.3.1) +", renamed7, "(v0.5.0)", "en renamed", sum(bool(n["renamed_en_from"]) for n in nodes.values()))
print("moved", sum(1 for n in nodes.values() if n.get("moved_from")), "filters added", filters_added)
print("links", n_links, "on", sum(bool(n["links"]) for n in nodes.values()), "nodes; filters", nf, "on",
      sum(bool(n["filters"]) for n in nodes.values()), "nodes;", len(used), "Shopify attributes used")
print("hu names reviewed", sum(n["name_hu_reviewed"] for n in nodes.values()), "of", len(nodes))
print("arukereso products counted", sum(n["arukereso_products_own"] for n in nodes.values()))
for n in out:
    if n["id"] == "own-racket-sports" or n["parent_id"] in ("own-racket-sports", "own-padel"):
        print(" > ".join(n["path_hu"]), "|", " > ".join(n["path_en"]), "|", n["arukereso_products_subtree"])
left = [" > ".join(n["path_en"]) for n in out if "paddle" in (n["name_en"] + n["name_hu"]).lower()]
assert not [x for x in left if "Padel" in x], left
padel_like = [x for x in left if not re.search(r"Boating|Swimming|Surfing|Diving|Hairbrush|Kitchen|Pickleball|Paddle Ball|Toys", x)]
print("paddle names (none is padel):", len(left), padel_like)
assert not padel_like, padel_like
# v0.3.1: an age group alone is no category name, in any suffixed form (Felnőtteknek, Gyerekeknek, Kids', Adults only)
AGE_HU = re.compile(r"^((felnőtt|gyerek|gyermek|kisgyerek|kisgyermek|bébi|tini|kamasz|újszülött|kicsi)(ek|ök|k)?(nek|nak)?|babá(k)?nak)$", re.I)
AGE_EN = re.compile(r"^(kids?'?|children'?s?|baby|babies|adults?( only)?|for adults|teens?|juniors?|toddlers?|infants?|newborns?)$", re.I)
AGE_ONLY = re.compile(AGE_HU.pattern + "|" + AGE_EN.pattern, re.I)
age_only = [n["id"] for n in out if AGE_ONLY.match(n["name_en"].strip()) or AGE_ONLY.match(n["name_hu"].strip())]
assert not age_only, age_only
soccer = [n["id"] for n in out if re.search(r"soccer", re.sub(r"football \(soccer\)", "", n["name_en"], flags=re.I), re.I)]
assert not soccer, soccer
def soccer_alone(t):  # case-insensitive: "Soccer" or "soccer" only inside "Football (Soccer)"
    return re.search(r"soccer", re.sub(r"football \(soccer\)", "", t, flags=re.I), re.I) is not None


fsoccer = [a["attribute_id"] for a in A.values() if soccer_alone(a["name_en"])] + [v for v, x in VH.items() if soccer_alone(x["en"])]
assert not fsoccer, fsoccer
fpadel = [v for v, x in VH.items() if "padel" in x["en"].lower() and "padel" not in (x["hu"] or "").lower()]
assert not fpadel, fpadel
for nid in ("sg-1-18-8", "own-running-shoes", "own-trail-running-shoes", "own-padel-shoes", "own-hiking-footwear", "own-hiking-shoes",
            "own-hiking-boots", "own-hiking-sandals"):
    n = nodes[nid]
    assert n["name_en"] and n["name_hu"], nid
    print("  ", nid, "|", " > ".join(n["path_en"]), "|", " > ".join(n["path_hu"]))
