"""Extract Shopify's attribute lists into work/ (v0.2, 2026-10-26). Run once, not part of all.sh:

    python3 -I build/extract_shopify.py . <categories.json> <attributes.json>

The two inputs are Shopify's distribution files dist/en/categories.json (80 MB) and dist/en/attributes.json of
github.com/Shopify/product-taxonomy at tag v2026-08 (sha1 3ea32e7f... and 1b324910..., checked 2026-10-26). They are
too large for this repo, so only what the build needs is kept:

- work/shopify-v2026-08-category-attributes.tsv: every category id with its attribute handles, in Shopify's order.
- work/shopify-v2026-08-attributes.tsv: every attribute handle with its id, English name, the base attribute an
  extended attribute takes its values from, and its value ids. Value names (English and Hungarian) are read from
  sources/shopify-v2026-08/attribute_values.{en,hu}.txt.
"""
import json, sys
from pathlib import Path

T = Path(sys.argv[1])
cats = json.load(open(sys.argv[2], encoding="utf-8"))
attrs = json.load(open(sys.argv[3], encoding="utf-8"))["attributes"]

with open(T / "work/shopify-v2026-08-attributes.tsv", "w", encoding="utf-8") as f:
    f.write("handle\tid\tname_en\tbase_handle\tvalue_ids\n")
    for a in attrs:
        vids = ",".join(v["id"].rsplit("/", 1)[1] for v in a["values"])
        f.write(f"{a['handle']}\t{a['id'].rsplit('/', 1)[1]}\t{a['name']}\t\t{vids}\n")
        for e in a["extended_attributes"]:
            f.write(f"{e['handle']}\t\t{e['name']}\t{a['handle']}\t\n")

n = 0
with open(T / "work/shopify-v2026-08-category-attributes.tsv", "w", encoding="utf-8") as f:
    f.write("id\tattribute_handles\n")
    for v in cats["verticals"]:
        for c in v["categories"]:
            f.write(c["id"].rsplit("/", 1)[1] + "\t" + ",".join(a["handle"] for a in c["attributes"]) + "\n")
            n += 1
print("categories", n, "attributes", len(attrs))
