# shelfscreen-taxonomy

A product category tree for webshop catalogues: one modern, market-wide tree with English and Hungarian names,
built on Shopify's Standard Product Taxonomy v2026-08. Hungary first; other markets add their languages later.

Version 0.2 (2026-10-26, fix round 1 on 2026-10-27). Version 0.1 was 2026-10-20.

## What is in it

| | v0.1 (2026-10-20) | v0.2 (2026-10-26) |
|---|---|---|
| Nodes | 14 865: Shopify's 14 606 plus 259 own | 14 901: Shopify's 14 606 plus 295 own |
| Shown | 3 095 (only nodes with Hungarian products under them) | every node |
| Hungarian names | every node; 1 512 Shopify translations corrected | every node; 1 512 + 847 corrected; 6 212 marked reviewed |
| English names | Shopify's | 39 renamed to "Football (Soccer)" |
| Links | none | 114 on 13 nodes (Shoes and Clothing to the sport nodes) |
| Node moves | none | 15 Shopify nodes moved under own nodes |
| Filters | 300 on 267 nodes | 95 058 on 14 742 nodes, from 8 501 Shopify attributes with all their values; 20 inherited filters dropped with a reason |
| Arukereso | all 2 988 categories placed; 10 234 765 products | all 2 988 placed; 9 732 089 products counted (two custom configuration categories not counted) |
| E-commerce categories | every node classed into seven e-commerce categories | the same, with the new nodes classed |

Counts from `sh build/all.sh` on 2026-10-27 (v0.2 after fix round 1) and from the v0.1 release files.

## Rules

- Backbone: Shopify Standard Product Taxonomy v2026-08 (MIT, see `NOTICE.md`). Google's product taxonomy
  (2021-09-21) is only a mapping target, through Shopify's own mapping file.
- Every node has an English and a Hungarian name. Shopify's Hungarian translation is not taken as it is: the
  sport, shoes and clothing branches were reviewed, and `name_hu_reviewed` says which names were. Elsewhere a
  name may still be Shopify's own translation (`name_hu_reviewed: false`).
- Every node is shown (the operator, 2026-10-26). `has_products_hu` stays empty (null) until the product
  database fills it; the Arukereso counts are their own fields (`arukereso_products_own`,
  `arukereso_products_subtree`) and do not decide what is shown.
- Product type and sport are categories; gender, age group, material, colour, size and perfume concentration
  are filters (the operator, 2026-10-26).
- Sport shoes and clothing sit in the tree by sport: football boots under Football (Soccer), running shoes
  under Running, padel shoes under Padel, hiking shoes under Hiking Footwear. Apparel > Shoes and Apparel >
  Clothing link to them through `links` (the operator, 2026-10-26).
- English names say "Football (Soccer)" where Shopify says "Soccer"; American Football keeps its name.
- Padel is its own node under Racket Sports (Sportszerek > Sportágak > Ütős sportok > Padel), next to Tennis,
  Pickleball, Squash, Badminton and Table Tennis. The word "paddle" names no padel node and no padel filter value.
- A new own node enters only with its evidence written next to it in `work/own-nodes.jsonl`.
- The seven e-commerce categories ("e-kereskedelmi kategória") are Fashion / Divat, Hobby & Leisure / Hobbi és
  szabadidő, DIY / Barkács, Electronics / Elektronika, Care Products / Szépségápolás és drogéria, Furniture &
  Homeware / Bútor és lakberendezés, Grocery / Élelmiszer. A node with none of them is Other / Egyéb. They follow
  `v3 Ecommerce Product category definitions`: running, tennis and basketball shoes are Fashion > Footwear;
  football, climbing and bike shoes are Sports Equipment; activewear, team jerseys and kits (football,
  basketball, rugby, Sports Uniforms) are Fashion > Apparel, cricket clothing too with fit `weak`; sport-specific
  apparel (ski and snowboard clothing, wetsuits and water sport apparel, martial arts and fencing wear,
  goalkeeper gloves) is Sports Equipment, cheerleading uniforms too with fit `weak`. Cycling and riding apparel
  stay Sports Equipment with fit `weak`. A `weak` fit means the definitions do not name the product. A class
  is given once: an older row that a later file replaces carries `superseded_by` and is skipped.
- Product counts are the "N termék" counters of Arukereso's category pages, read on 2026-10-19. They count
  products listed on Arukereso, not offers and not shops. Arukereso's sitemaps are not used for counts: many of
  their category files stop at 24 products. The custom PC and laptop configuration categories ("Egyedi ...
  konfiguráció") are placed but not counted (the operator, 2026-10-26; `counted: false`).

## Filters

A node's filters are Shopify's attribute list for its category, with all values. An own node takes the list of
the Shopify category named in its `filters_from`, else of its nearest Shopify ancestor. In `dist/tree.jsonl` a
Shopify filter is a reference (`{"attribute_id", "source": "shopify"}`); its English and Hungarian names and
values are in `dist/attributes.jsonl`, keyed by `attribute_id`. Own filters (for example fragrance
concentration) carry their names and values inline. An inherited filter that does not describe the node is
dropped and recorded with its reason (`work/filter-drops.jsonl`, `filters_dropped` on the node).

Review of the Hungarian filter names: the names of the 1 874 Shopify attributes used in the sport, shoes and
clothing branches (`work/filter-hu-review-scope.txt`, 1 940 attributes marked reviewed with the v0.1 ones) were
checked, and their 16 010 distinct values were checked one by one; 15 969 are listed in
`work/filter-values-checked.txt`, the other 41 (mostly fragments of corrupt Shopify values) were not confirmed
and stay unreviewed. In all, 16 093 of the 73 133 distinct values in the dictionary are marked `hu_reviewed`.
`work/filter-renames.jsonl` holds 1 131 rows: 340 attribute names and 769 values corrected in Hungarian, 15
attribute names and 9 values in English (a row may carry both), each with the name it replaced (`old_hu` or `old_en`); the build checks that name before it applies a
correction.

## Changes from v0.1

| v0.1 | v0.2 |
|---|---|
| `products_own`, `products_subtree` | `arukereso_products_own`, `arukereso_products_subtree` |
| `visible_hu` (true or false) | removed; every node is shown, and `has_products_hu` is null until the product database fills it |
| `dist/tree-hu-visible.csv` (visible nodes) | `dist/tree-hu.csv` (every node) |
| filters inline with names and values | a Shopify filter is a reference `{"attribute_id", "source": "shopify"}` to `dist/attributes.jsonl`; own filters stay inline (`source: "own"`, names and values) |
| no links, evidence, moves or English renames | `links`, `evidence`, `moved_from`, `renamed_en_from`, `name_hu_reviewed`, `filters_from`, `filters_dropped`, `arukereso[].counted` |

### `dist/tree.jsonl`, one node per line

| Field | What |
|---|---|
| `id`, `parent_id`, `depth` | Shopify id (`aa-8-1`) or own id (`own-running-shoes`); parent; depth (a root is 1) |
| `name_en`, `name_hu`, `path_en`, `path_hu` | names and full paths (` > ` between levels) |
| `name_hu_reviewed` | true when the Hungarian name was reviewed (v0.1 or v0.2 scope, or an own node) |
| `source` | `shopify-v2026-08` or `own` |
| `renamed_hu_from`, `renamed_en_from` | Shopify's name before a rename, else null |
| `moved_from` | the Shopify parent before the node was moved under an own node (only on moved nodes) |
| `reason`, `evidence` | own nodes only: why the node exists, and the measured evidence |
| `links` | ids of nodes this node points to (Apparel > Shoes and Clothing to the sport nodes) |
| `has_products_hu` | null for now |
| `arukereso_products_own`, `arukereso_products_subtree` | Arukereso "N termék" counts (2026-10-19) on the node and under it, counted categories only |
| `arukereso[]` | placed Arukereso categories: `path`, `url`, `relation`, `listed_products`, `counted` |
| `filters_from` | the Shopify category whose attribute list the node takes, when not its own |
| `filters[]` | `{"attribute_id", "source": "shopify"}`, or an own filter with `attribute_id`, `source: "own"`, `name_en`, `name_hu`, `name_hu_reviewed`, `values[]` (`en`, `hu`) |
| `filters_dropped[]` | inherited filters left out: `attribute_id`, `reason` (only where any) |
| `ecommerce_category` | `main`, `sub`, `main_hu`, `sub_hu`, `fit` (clear, weak, none), `inherited`, `reason` |

### `dist/attributes.jsonl`, one Shopify attribute per line

| Field | What |
|---|---|
| `attribute_id` | Shopify handle, the key a node filter refers to |
| `shopify_id`, `base_attribute_id` | Shopify's numeric id; for an extended attribute, the attribute it takes its values from |
| `name_en`, `name_hu`, `name_hu_reviewed`, `renamed_hu_from` | names, review flag, the Hungarian name before a correction |
| `values[]` | `id`, `en`, `hu`, `hu_reviewed`, `renamed_hu_from` |

## Layout

| Path | What |
|---|---|
| `dist/tree.jsonl` | every node: id, parent, names, paths, source, rename and move history, evidence, links, Arukereso categories and counts, filters, e-commerce category |
| `dist/attributes.jsonl` | the filter dictionary: every Shopify attribute in use with its English and Hungarian names and values |
| `dist/tree-hu.csv` | every node, flat, with Hungarian names and filter names |
| `dist/ecommerce-summary.csv` | Arukereso products per e-commerce category and subcategory |
| `site/index.html` | the browsable page: grouped by e-commerce category or as the full tree, search, links, filters, HU/EN |
| `sources/shopify-v2026-08/` | Shopify's categories, attributes and attribute values (English, Hungarian) and its mapping to Google 2021-09-21 |
| `sources/arukereso-2026-10-19/category-pages.jsonl` | Arukereso's 3 002 category pages: breadcrumb and heading |
| `sources/tree-audit-2026-10-26/` | the sport and fashion audit findings of 2026-10-26 that the own nodes cite (`finding` field), with their summaries |
| `work/` | the build's input: Shopify's tree and attribute lists as tables, and the decisions applied to them (see below) |
| `build/` | `sh build/all.sh` rebuilds `dist/` and `site/` from `work/` (Python 3, standard library only); `build/extract_shopify.py` made the two Shopify attribute tables once |

The decisions in `work/`:

| File | What |
|---|---|
| `operator-decisions.jsonl` | the operator's decisions of 2026-10-26, with his words |
| `mapping-arukereso.jsonl`, `arukereso-not-counted.jsonl` | Arukereso categories on the tree; the ones not counted |
| `hu-renames-1..4.jsonl`, `hu-review-scope.tsv` | Hungarian node renames; which node names were reviewed |
| `en-renames.jsonl` | English node renames (Football (Soccer)) |
| `own-nodes.jsonl`, `own-nodes-rejected.jsonl` | own nodes with their evidence; proposals rejected, with reasons |
| `node-moves.jsonl`, `links.jsonl` | Shopify nodes moved under own nodes; links between nodes |
| `node-attributes.jsonl`, `filter-drops.jsonl` | own filters; inherited filters dropped, with reasons |
| `filter-renames.jsonl`, `filter-hu-review-scope.txt`, `filter-values-checked.txt` | filter name fixes with the old names; which attributes and which values were reviewed |
| `ecommerce-1..4.jsonl` | e-commerce classes |

## How the decisions were made

Each Arukereso category was mapped onto Shopify, the Hungarian names were reviewed, own nodes and filters
proposed, and every node classed into the e-commerce categories. In v0.2 the sport, shoes and clothing branches
were checked against the product names of the Decathlon study (`shelfscreen-data/2026-10-20/decathlon`,
dashboard files of 2026-10-24): a new node is added only where those products, or Arukereso categories, show
it. Each decision sits in `work/` with its reason; a change is made there and the tree rebuilt.
