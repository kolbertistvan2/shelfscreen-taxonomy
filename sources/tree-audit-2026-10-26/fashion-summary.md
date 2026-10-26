# Fashion branch audit: summary

Branch: Apparel & Accessories (aa) plus Luggage & Bags (lb) and the fashion nodes pulled in from other branches (695 nodes). Sources: Arukereso counters of 2026-10-19, the Decathlon study assortment.json, Shopify v2026-08 attributes, Google taxonomy 2021-09-21. 105 findings in fashion-findings.jsonl.

## Counts per kind

| kind | findings |
|---|---|
| hidden_node | 32 |
| missing_type | 18 |
| split_placement | 17 |
| undivided_leaf | 6 |
| filter | 19 |
| naming | 13 |
| total | 105 (22 high, 47 medium, 36 low) |

The leading pattern: one broad Arukereso category (a "pulóver", "nadrág", "cipő", "dzseki", "csizma", "papucs" bucket) sits on a parent node, and Shopify's finer children stay hidden. The own counts add up exactly to the Arukereso categories (for example Athletic Shoes 45464, Boots 33878, Shoes root 43333, Clothing Tops 326897).

## The 15 most important findings

1. Clothing Tops holds 326897 products, all from the Arukereso "pulóver" and "felső" categories; Hoodies, Sweatshirts, Sweaters and Polos are hidden. Baby & Children's Tops has the same problem (86090).
2. Athletic Shoes holds 45464 products in one block: running 24536, general sport 10966, hiking 9892, boxing 70. Add Running, Hiking and Training leaves.
3. Sport shoes are split: Soccer (3682), Tennis (4197), Basketball (839), Golf (103) and Padel Shoes (0, Decathlon 76) sit under Sporting Goods. Propose one home, Shoes > Athletic Shoes > sport, with links from the sport nodes.
4. The Shoes root holds 43333 products; Sneakers is hidden although the Decathlon study has 4974 sneaker products in 8 shops. The same root holds 21322 slides, clogs and slippers from the "papucs" categories, which need Slides & Flip-Flops and Clogs nodes.
5. Boots holds 33878 products with no child: ankle boots 7497, motorcycle 5625, snow 3673, rain 3245, plus hiking boots that are split with Athletic Shoes (hiking total 9892).
6. Pants (24118) hides Cargo, Chinos, Joggers, Trousers; Shorts (17877) hides Bermudas, Denim, Cargo (the operator's example, confirmed and extended).
7. Coats & Jackets (45796): Arukereso divides dzseki (25778) from kabát (17917) and ski jackets (2101); 17 Shopify types are hidden, including Blazers, Puffer and Parka. Women's blazers (2593) sit on the Clothing root.
8. Uniforms & Workwear holds 345242 products from the single Arukereso category "Munkaruha", with 11 hidden children; work shoes (130211), hi-vis (5037) and safety gloves (24425) sit in Business & Industrial.
9. Activewear has hidden nodes the Decathlon study uses: shorts 3891 (9 shops), hoodies and sweatshirts 3339 (9 shops), base layer tops 992 (6 shops); base layers (9296) sit on the Activewear root.
10. Baby & Children's Shoes (29244): Sneakers (22595) are hidden and children's slippers (6005) have no node.
11. Men's Underwear (18475) and Women's Underpants (8702) hide boxer, brief, trunk, thong and similar types; Socks (13886) hide ankle, footie, knee and sport socks.
12. Smartwatch and fitness tracker accessories (41800) fill Watch Accessories next to 6307 classic watch bands; no node for them.
13. Team jerseys have three homes (Sports Uniforms 4376 in the Hobby category, Basketball Apparel 452, Cycling Jerseys 8343); motorcycle clothing has four (Outerwear 15212, gloves, helmets, boots); gloves have ten.
14. Filters: Activewear and its leaves carry only gender, so sport clothing needs the Activity filter; Jewelry (rings, earrings, necklaces, bracelets) and Watches have no filter at all; Bras (20014) have none.
15. Baby & Children's One-Pieces (39106) divides into bodysuits 37968, rompers 937 and overalls 201; children's shorts (2405) have no leaf at all.

## Notes for the operator

- Split-placement proposals for shoes are a decision: Option A (my proposal) is one home under Shoes with sport links; Option B keeps sport homes and links from Shoes. Equipment-bound footwear (cycling, climbing, ski, snowboard) is listed separately as a lower-priority choice.
- The taxonomy repo rejected hiking shoes, loafers, espadrilles and boxing shoes as "attribute: activity or style" (work/own-nodes-rejected.jsonl). The brief treats activity as a category, so they are proposed here.
- Product counts are the "N termék" counters (products_listed_2026_10_19); the crawled `products` field is capped by sitemaps (about 24 for many categories) and was not used.
- A few proposals rest partly on retail knowledge, marked as a "knowledge:" line inside the evidence list (men's dress shoes, men's underwear types, rings). No finding rests on knowledge alone.
