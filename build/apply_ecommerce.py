"""Resolve every tree node's e-commerce category by inheritance from ecommerce-1..6.jsonl (4: v0.2, 2026-10-26; 5: v0.3,
2026-10-27; 6: v0.4, 2026-10-27, one row per node with its source and confidence) and write it into dist/tree.jsonl.
Every node gets one, since every node is shown. A row a later file replaces carries superseded_by and is skipped."""
import json, collections, sys
from pathlib import Path
T = Path(sys.argv[1])
HU_MAIN = {"Fashion": "Divat", "Hobby & Leisure": "Hobbi és szabadidő", "Grocery": "Élelmiszer",
           "Furniture & Homeware": "Bútor és lakberendezés", "Electronics": "Elektronika", "DIY": "Barkács",
           "Care Products": "Szépségápolás és drogéria"}
HU_SUB = {"Apparel": "Ruházat", "Bags & Accessories": "Táskák és kiegészítők", "Footwear": "Lábbeli",
          "Bullion & Precious Metal": "Nemesfém", "Camping & Adventure": "Kemping és túra", "Erotic & Adult": "Erotika",
          "Flowers & Gifts": "Virág és ajándék", "Media": "Média", "Musical Instruments": "Hangszerek",
          "Pet Supplies": "Kisállatkellékek", "Smoking Supplies": "Dohányzási kellékek", "Sports Equipment": "Sportfelszerelés",
          "Stationery, Crafts & Art Supplies": "Írószer, kreatív és művészellátó", "Toys": "Játékok",
          "Other Hobby & Leisure": "Egyéb hobbi és szabadidő", "Beverages": "Italok", "Food": "Étel",
          "Furniture": "Bútorok", "Homeware": "Lakberendezés", "Consumer Electronics": "Szórakoztató elektronika és IT",
          "Electrical Appliances": "Háztartási gépek", "Garden": "Kert", "Tools & Construction Supplies": "Szerszámok és építőanyagok",
          "Vehicle Parts": "Járműalkatrészek", "Health Care": "Egészségmegőrzés", "Household Care": "Háztartási tisztítás",
          "Personal Care": "Személyes ápolás"}
explicit = {}
for i in (1, 2, 3, 4, 5, 6):
    for line in open(T / f"work/ecommerce-{i}.jsonl", encoding="utf-8"):
        r = json.loads(line)
        if r.get("superseded_by"):  # kept for the record; a later file holds the class
            continue
        assert r["id"] not in explicit, ("e-commerce class given twice; mark the older row superseded_by", r["id"])
        main = r.get("category_main") or "none"
        sub = r.get("category_sub")
        if sub and " > " in sub:
            sub = sub.split(" > ", 1)[1]
        explicit[r["id"]] = {"main": main if main in HU_MAIN else "none", "sub": sub if main in HU_MAIN else None,
                             "fit": "none" if main not in HU_MAIN else r.get("fit", "clear"), "reason": r.get("reason"),
                             "source": r.get("source"), "confidence": r.get("confidence")}
rows = [json.loads(l) for l in open(T / "dist/tree.jsonl", encoding="utf-8")]
by = {n["id"]: n for n in rows}
def resolve(nid):
    n = by[nid]
    while n:
        if n["id"] in explicit:
            e = explicit[n["id"]]
            return e, n["id"] != nid
        n = by.get(n["parent_id"]) if n["parent_id"] else None
    return None, False
unresolved, bad_sub = [], set()
for n in rows:
    e, inherited = resolve(n["id"])
    if not e:
        unresolved.append(n["path_en"]); continue
    if e["sub"] and e["sub"] not in HU_SUB:
        bad_sub.add(e["sub"])
    other = e["main"] == "none"
    n["ecommerce_category"] = {"main": "Other" if other else e["main"], "sub": None if other else e["sub"],
                 "main_hu": "Egyéb" if other else HU_MAIN.get(e["main"]), "sub_hu": None if other else HU_SUB.get(e["sub"]),
                 "fit": e["fit"], "inherited": inherited, "reason": None if inherited else e["reason"],
                 "source": None if inherited else e["source"], "confidence": None if inherited else e["confidence"]}
print("explicit rows", len(explicit), "unresolved", len(unresolved), unresolved[:5], "unknown subs", bad_sub)
with open(T / "dist/tree.jsonl", "w", encoding="utf-8") as f:
    for n in rows:
        f.write(json.dumps(n, ensure_ascii=False) + "\n")
# Arukereso products per e-commerce category, counted on the node that holds the Arukereso category
tot = collections.Counter(); sub = collections.Counter()
for n in rows:
    if n.get("ecommerce_category") and n["arukereso_products_own"]:
        tot[n["ecommerce_category"]["main_hu"]] += n["arukereso_products_own"]
        sub[(n["ecommerce_category"]["main_hu"] or "nincs", n["ecommerce_category"]["sub_hu"] or "-")] += n["arukereso_products_own"]
allp = sum(tot.values())
for k, v in tot.most_common():
    print(f"{v:>10,} {v/allp:6.1%}  {k}")
weak = sum(1 for n in rows if n.get("ecommerce_category") and not n["ecommerce_category"]["inherited"] and n["ecommerce_category"]["fit"] != "clear")
print("weak or none explicit nodes", weak)
print("by source", collections.Counter(n["ecommerce_category"]["source"] for n in rows).most_common())
print("by fit", collections.Counter(n["ecommerce_category"]["fit"] for n in rows).most_common())
