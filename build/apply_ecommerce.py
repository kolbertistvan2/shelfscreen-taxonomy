"""Resolve every tree node's e-commerce category by inheritance from ecommerce-1..3.jsonl and write it into dist/tree.jsonl."""
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
for i in (1, 2, 3):
    for line in open(T / f"work/ecommerce-{i}.jsonl", encoding="utf-8"):
        r = json.loads(line)
        main = r.get("category_main") or "none"
        sub = r.get("category_sub")
        if sub and " > " in sub:
            sub = sub.split(" > ", 1)[1]
        explicit[r["id"]] = {"main": main if main in HU_MAIN else "none", "sub": sub if main in HU_MAIN else None,
                             "fit": "none" if main not in HU_MAIN else r.get("fit", "clear"), "reason": r.get("reason")}
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
    if not n["visible_hu"]:
        continue
    e, inherited = resolve(n["id"])
    if not e:
        unresolved.append(n["path_en"]); continue
    if e["sub"] and e["sub"] not in HU_SUB:
        bad_sub.add(e["sub"])
    other = e["main"] == "none"
    n["ecommerce_category"] = {"main": "Other" if other else e["main"], "sub": None if other else e["sub"],
                 "main_hu": "Egyéb" if other else HU_MAIN.get(e["main"]), "sub_hu": None if other else HU_SUB.get(e["sub"]),
                 "fit": e["fit"], "inherited": inherited, "reason": None if inherited else e["reason"]}
print("explicit rows", len(explicit), "unresolved", len(unresolved), unresolved[:5], "unknown subs", bad_sub)
with open(T / "dist/tree.jsonl", "w", encoding="utf-8") as f:
    for n in rows:
        f.write(json.dumps(n, ensure_ascii=False) + "\n")
# products per e-commerce category, counted on the node that holds the Arukereso category
tot = collections.Counter(); sub = collections.Counter()
for n in rows:
    if n.get("ecommerce_category") and n["products_own"]:
        tot[n["ecommerce_category"]["main_hu"]] += n["products_own"]
        sub[(n["ecommerce_category"]["main_hu"] or "nincs", n["ecommerce_category"]["sub_hu"] or "-")] += n["products_own"]
allp = sum(tot.values())
for k, v in tot.most_common():
    print(f"{v:>10,} {v/allp:6.1%}  {k}")
weak = sum(1 for n in rows if n.get("ecommerce_category") and not n["ecommerce_category"]["inherited"] and n["ecommerce_category"]["fit"] != "clear")
print("weak or none explicit nodes", weak)
