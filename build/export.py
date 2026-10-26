"""Write the release files from dist/tree.jsonl and dist/attributes.jsonl (v0.2, 2026-10-26): the whole tree as CSV, the
e-commerce category summary, and the browsable page (site/index.html from site/template.html). Every node is shown."""
import collections, csv, json, sys
from pathlib import Path

T = Path(sys.argv[1])
rows = [json.loads(l) for l in open(T / "dist/tree.jsonl", encoding="utf-8")]
attrs = {a["attribute_id"]: a for a in (json.loads(l) for l in open(T / "dist/attributes.jsonl", encoding="utf-8"))}

def fname(x, k):
    return (x if x["source"] == "own" else attrs[x["attribute_id"]])[k] or ""


with open(T / "dist/tree-hu.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "parent_id", "depth", "path_hu", "path_en", "name_hu", "name_en", "name_hu_reviewed", "source",
                "links", "arukereso_products_subtree", "arukereso_products_own", "ecommerce_main", "ecommerce_sub",
                "ecommerce_main_hu", "ecommerce_sub_hu", "ecommerce_fit", "arukereso_categories", "filters_hu", "filters_en"])
    for n in rows:
        e = n["ecommerce_category"]
        w.writerow([n["id"], n["parent_id"], n["depth"], n["path_hu"], n["path_en"], n["name_hu"], n["name_en"],
                    int(n["name_hu_reviewed"]), n["source"], " ".join(n["links"]), n["arukereso_products_subtree"],
                    n["arukereso_products_own"], e["main"], e["sub"], e["main_hu"], e["sub_hu"], e["fit"], len(n["arukereso"]),
                    "; ".join(fname(x, "name_hu") for x in n["filters"]), "; ".join(fname(x, "name_en") for x in n["filters"])])

main, sub = collections.Counter(), collections.Counter()
names = {}
for n in rows:
    e = n["ecommerce_category"]
    main[e["main"]] += n["arukereso_products_own"]
    sub[(e["main"], e["sub"])] += n["arukereso_products_own"]
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

# The page: one dictionary of Shopify attributes (F), nodes refer to it by index; own filters stay inline
fidx, F = {}, []
for h in sorted(attrs):
    a = attrs[h]
    fidx[h] = len(F)
    F.append([a["name_hu"], a["name_en"], [[v["hu"], v["en"]] for v in a["values"]], 1 if a["name_hu_reviewed"] else 0])
data = []
for n in rows:
    d = {"i": n["id"], "p": n["parent_id"], "h": n["name_hu"], "e": n["name_en"], "n": n["arukereso_products_subtree"],
         "s": 1 if n["source"] == "own" else 0}
    if not n["name_hu_reviewed"]:
        d["u"] = 1
    if n["arukereso_products_own"]:
        d["o"] = n["arukereso_products_own"]
    if n.get("renamed_hu_from"):
        d["r"] = n["renamed_hu_from"]
    if n.get("reason"):
        d["why"] = n["reason"]
    if n.get("evidence"):
        d["ev"] = n["evidence"]
    if n["links"]:
        d["l"] = n["links"]
    if n.get("moved_from"):
        d["m"] = n["moved_from"]
    if n["filters"]:
        d["f"] = [fidx[x["attribute_id"]] if x["source"] == "shopify" else
                  [x["name_hu"], x["name_en"], [[v.get("hu"), v.get("en")] for v in x["values"]], 1] for x in n["filters"]]
    if n["arukereso"]:
        d["a"] = [[a["path"], a["listed_products"] if a["counted"] else 0, a["relation"]] + ([] if a["counted"] else [1]) for a in n["arukereso"]]
    e = n["ecommerce_category"]
    d["c"] = [e["main_hu"], e["sub_hu"], e["main"], e["sub"], {"clear": 0, "weak": 1}.get(e["fit"], 2),
              1 if e["inherited"] else 0, e["reason"]]
    data.append(d)
page = (T / "site/template.html").read_text(encoding="utf-8")
blob = json.dumps({"nodes": data, "filters": F}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
(T / "site/index.html").write_text(page.replace("__DATA__", blob), encoding="utf-8")
print("nodes", len(rows), "arukereso products", total, "csv and page written,", len(F), "attributes on the page")
