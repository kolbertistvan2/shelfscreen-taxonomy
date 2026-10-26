# Notice

This tree is built on the Shopify Standard Product Taxonomy, release v2026-08
(https://github.com/Shopify/product-taxonomy), used under the MIT License. The license text is in
`sources/shopify-v2026-08/LICENSE`. The files under `sources/shopify-v2026-08/` are Shopify's distribution files,
unchanged (v0.2 adds `attribute_values.en.txt` and `attribute_values.hu.txt`). The two tables
`work/shopify-v2026-08-attributes.tsv` and `work/shopify-v2026-08-category-attributes.tsv` are derived from
Shopify's `dist/en/attributes.json` and `dist/en/categories.json` of the same release by
`build/extract_shopify.py`.

The Arukereso category names and breadcrumbs under `sources/arukereso-2026-10-19/`, and the product counts in
`work/mapping-arukereso.jsonl`, were read from Arukereso's public category pages on 2026-10-19.
