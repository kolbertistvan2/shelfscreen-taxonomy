"""Write the release files from dist/tree.jsonl: the visible Hungarian tree as CSV, the e-commerce category
summary, and the browsable page (site/index.html from site/template.html)."""
import collections, csv, json, sys
from pathlib import Path

T = Path(sys.argv[1])
rows = [json.loads(l) for l in open(T / "dist/tree.jsonl", encoding="utf-8")]
vis = [n for n in rows if n["visible_hu"]]

with open(T / "dist/tree-hu-visible.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "parent_id", "depth", "path_hu", "path_en", "name_hu", "name_en", "source", "products_subtree",
                "products_own", "ecommerce_main", "ecommerce_sub", "ecommerce_main_hu", "ecommerce_sub_hu",
                "ecommerce_fit", "arukereso_categories", "filters_hu", "filters_en"])
    for n in vis:
        e = n["ecommerce_category"]
        w.writerow([n["id"], n["parent_id"], n["depth"], n["path_hu"], n["path_en"], n["name_hu"], n["name_en"],
                    n["source"], n["products_subtree"], n["products_own"], e["main"], e["sub"], e["main_hu"],
                    e["sub_hu"], e["fit"], len(n["arukereso"]), "; ".join(x["name_hu"] for x in n["filters"]),
                    "; ".join(x["name_en"] for x in n["filters"])])

main, sub = collections.Counter(), collections.Counter()
names = {}
for n in vis:
    e = n["ecommerce_category"]
    main[e["main"]] += n["products_own"]
    sub[(e["main"], e["sub"])] += n["products_own"]
    names[e["main"]] = e["main_hu"]
    names[(e["main"], e["sub"])] = e["sub_hu"]
total = sum(main.values())
with open(T / "dist/ecommerce-summary.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["ecommerce_main", "ecommerce_main_hu", "ecommerce_sub", "ecommerce_sub_hu", "arukereso_products", "share"])
    for m, v in main.most_common():
        w.writerow([m, names[m], "", "", v, f"{v / total:.4f}"])
        for (mm, s), sv in sorted(sub.items(), key=lambda kv: -kv[1]):
            if mm == m and s:
                w.writerow([m, names[m], s, names[(mm, s)], sv, f"{sv / total:.4f}"])

data = []
ids = {n["id"] for n in vis}
for n in vis:
    d = {"i": n["id"], "p": n["parent_id"] if n["parent_id"] in ids else None, "h": n["name_hu"], "e": n["name_en"],
         "n": n["products_subtree"], "s": 1 if n["source"] == "own" else 0}
    if n["products_own"]:
        d["o"] = n["products_own"]
    if n.get("renamed_hu_from"):
        d["r"] = n["renamed_hu_from"]
    if n.get("reason"):
        d["why"] = n["reason"]
    if n["filters"]:
        d["f"] = [[x["name_hu"], x["name_en"], [[v.get("hu"), v.get("en")] for v in x["values"]], x["source"]] for x in n["filters"]]
    if n["arukereso"]:
        d["a"] = [[a["path"], a["listed_products"], a["relation"]] for a in n["arukereso"]]
    e = n["ecommerce_category"]
    d["c"] = [e["main_hu"], e["sub_hu"], e["main"], e["sub"], {"clear": 0, "weak": 1}.get(e["fit"], 2),
              1 if e["inherited"] else 0, e["reason"]]
    data.append(d)
page = (T / "site/template.html").read_text(encoding="utf-8")
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
(T / "site/index.html").write_text(page.replace("__DATA__", blob), encoding="utf-8")
print("visible", len(vis), "products", total, "csv and page written")
