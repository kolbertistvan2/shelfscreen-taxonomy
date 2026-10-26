"""Assemble the category tree (v0.1, 2026-10-20): Shopify v2026-08 backbone, Hungarian renames, own nodes,
the Racket Sports group, attribute filters, and Arukereso categories with their listed product counts."""
import collections, csv, json, sys
from pathlib import Path

T = Path(sys.argv[1])
nodes = {}
for line in open(T / "work/shopify-v2026-08.tsv", encoding="utf-8"):
    p = line.rstrip("\n").split("\t")
    if p[0] == "id":
        continue
    nid, en, hu = p
    parent = nid.rsplit("-", 1)[0] if "-" in nid else None
    nodes[nid] = {"id": nid, "parent_id": parent, "name_en": en.split(" > ")[-1], "name_hu": hu.split(" > ")[-1],
                  "source": "shopify-v2026-08", "renamed_hu_from": None, "arukereso": [], "filters": []}

renamed = 0
for i in (1, 2, 3):
    for line in open(T / f"work/hu-renames-{i}.jsonl", encoding="utf-8"):
        r = json.loads(line)
        n = nodes[r["id"]]
        n["renamed_hu_from"], n["name_hu"] = n["name_hu"], r["new_hu"]
        renamed += 1

for line in open(T / "work/own-nodes.jsonl", encoding="utf-8"):
    r = json.loads(line)
    nodes[r["id"]] = {"id": r["id"], "parent_id": r["parent_id"], "name_en": r["name_en"], "name_hu": r["name_hu"],
                      "source": "own", "renamed_hu_from": None, "arukereso": [], "filters": [], "reason": r["reason"]}

# Racket Sports: one family under Sporting Goods > Athletics
nodes["own-racket-sports"] = {"id": "own-racket-sports", "parent_id": "sg-1", "name_en": "Racket Sports",
                              "name_hu": "Ütős sportok", "source": "own", "renamed_hu_from": None, "arukereso": [],
                              "filters": [], "reason": "Tennis, padel, pickleball, squash, badminton and table tennis as one family."}
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

# Arukereso categories: own node when the own-nodes step placed them, else the mapped Shopify node
own_of = {}
for line in open(T / "work/own-nodes.jsonl", encoding="utf-8"):
    r = json.loads(line)
    for p in r["arukereso_paths"]:
        own_of[p] = r["id"]
mapping = [json.loads(l) for l in open(T / "work/mapping-arukereso.jsonl", encoding="utf-8")]
for m in mapping:
    nid = own_of.get(m["arukereso_path"], m["shopify_id"])
    nodes[nid]["arukereso"].append({"path": m["arukereso_path"], "url": m["url"], "relation": m["relation"],
                                    "listed_products": m.get("products_listed_2026_10_19")})

for line in open(T / "work/node-attributes.jsonl", encoding="utf-8"):
    a = json.loads(line)
    nodes[a["shopify_id"]]["filters"].append({k: a[k] for k in ("attribute_id", "source", "name_en", "name_hu", "values")})

children = collections.defaultdict(list)
for n in nodes.values():
    if n["parent_id"]:
        children[n["parent_id"]].append(n["id"])


def walk(nid, depth, pen, phu):
    n = nodes[nid]
    n["depth"], n["path_en"], n["path_hu"] = depth, pen + [n["name_en"]], phu + [n["name_hu"]]
    own = sum(a["listed_products"] or 0 for a in n["arukereso"])
    sub = own + sum(walk(c, depth + 1, n["path_en"], n["path_hu"]) for c in children[nid])
    n["products_own"], n["products_subtree"] = own, sub
    n["visible_hu"] = sub > 0 or n["id"].startswith("own-padel") or n["id"] == "own-racket-sports"
    return sub


for root in [n["id"] for n in nodes.values() if not n["parent_id"]]:
    walk(root, 1, [], [])

out = sorted(nodes.values(), key=lambda n: n["path_en"])
with open(T / "dist/tree.jsonl", "w", encoding="utf-8") as f:
    for n in out:
        f.write(json.dumps({**n, "path_en": " > ".join(n["path_en"]), "path_hu": " > ".join(n["path_hu"])}, ensure_ascii=False) + "\n")
vis = [n for n in out if n["visible_hu"]]
print("nodes", len(nodes), "visible in HU", len(vis), "own", sum(n["source"] == "own" for n in nodes.values()),
      "hu renamed", renamed, "with filters", sum(bool(n["filters"]) for n in nodes.values()))
print("depths visible", dict(sorted(collections.Counter(n["depth"] for n in vis).items())))
print("products placed", sum(n["products_own"] for n in nodes.values()))
for n in out:
    if n["id"] in ("own-racket-sports",) or n["parent_id"] == "own-racket-sports" or n["parent_id"] == "own-padel":
        print(" > ".join(n["path_hu"]), "|", " > ".join(n["path_en"]), "|", n["products_subtree"])
left = [" > ".join(n["path_en"]) for n in vis if "paddle" in (n["name_en"] + n["name_hu"]).lower()]
print("paddle left (boating oars only expected):", left)
assert all("Boating" in x for x in left)
