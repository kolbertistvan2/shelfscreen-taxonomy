# shelfscreen-taxonomy

A product category tree for webshop catalogues: one modern, market-wide tree with English and Hungarian names,
built on Shopify's Standard Product Taxonomy v2026-08. Hungary first; other markets add their languages and their
own visible nodes later.

Version 0.1 (2026-10-20).

## What is in it

| | |
|---|---|
| Nodes | 14 865: Shopify's 14 606 plus 259 own nodes |
| Visible in Hungary | 3 095 (a node shows only where Hungarian products sit under it) |
| Hungarian names | every node; 1 512 Shopify translations corrected (for example Athletics: "Sportágak", not "Atlétika") |
| Filters | 300 on 267 nodes (gender, age group, animal type, power source...), English and Hungarian |
| Arukereso | all 2 988 categories placed, with their product counts |
| E-commerce categories | every node classed into seven top-level e-commerce categories, at subcategory level |

## Rules

- Backbone: Shopify Standard Product Taxonomy v2026-08 (MIT, see `NOTICE.md`). Google's product taxonomy
  (2021-09-21) is only a mapping target, through Shopify's own mapping file.
- Every node has an English and a Hungarian name. Shopify's Hungarian translation is not taken as it is.
- A split by an attribute (gender, age group, material...) is a filter, not a category.
- Padel is its own node under Racket Sports (Sportszerek > Sportágak > Ütős sportok > Padel), next to Tennis,
  Pickleball, Squash, Badminton and Table Tennis. The word "paddle" names no padel node.
- The seven e-commerce categories ("e-kereskedelmi kategória") are Fashion / Divat, Hobby & Leisure / Hobbi és
  szabadidő, DIY / Barkács, Electronics / Elektronika, Care Products / Szépségápolás és drogéria, Furniture &
  Homeware / Bútor és lakberendezés, Grocery / Élelmiszer. A node with none of them is Other / Egyéb. Each category
  has in-scope and out-of-scope lists that cut across the tree: tennis and padel shoes are Fashion > Footwear, hair
  dryers Electronics > Electrical Appliances, car electronics DIY > Vehicle Parts.
- Product counts are the "N termék" counters of Arukereso's category pages, read on 2026-10-19. They count
  products listed on Arukereso, not offers and not shops. Arukereso's sitemaps are not used for counts: many of
  their category files stop at 24 products.

## Layout

| Path | What |
|---|---|
| `dist/tree.jsonl` | every node: id, parent, names, paths, source, Hungarian rename history, filters, Arukereso categories, product counts, e-commerce category |
| `dist/tree-hu-visible.csv` | the 3 095 nodes visible in Hungary, flat |
| `dist/ecommerce-summary.csv` | Arukereso products per e-commerce category and subcategory |
| `site/index.html` | the browsable page: grouped by e-commerce category or as the full tree, search, filters, HU/EN |
| `sources/shopify-v2026-08/` | Shopify's categories and attributes (English, Hungarian) and its mapping to Google 2021-09-21 |
| `sources/arukereso-2026-10-19/category-pages.jsonl` | Arukereso's 3 002 category pages: breadcrumb and heading |
| `work/` | the build's input: Shopify's tree as one table, and the decisions applied to it: Arukereso mapping, Hungarian renames, own nodes (and the rejected ones with reasons), filters, e-commerce classes |
| `build/` | `sh build/all.sh` rebuilds `dist/` and `site/` from `work/` (Python 3, standard library only) |

## How the decisions were made

Each Arukereso category was mapped onto Shopify, the Hungarian names were reviewed, own
nodes and filters proposed, and every node classed into the e-commerce categories. Each decision sits in `work/`
with its reason; a change is made there and the tree rebuilt.
