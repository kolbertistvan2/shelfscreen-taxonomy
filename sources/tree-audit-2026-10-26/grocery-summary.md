# Grocery branch audit: summary

Branch: Food, Beverages & Tobacco (Beverages, Food Items, Cannabis) plus Baby & Toddler Food. 746 nodes, 102 visible. Sources: grocery-nodes.jsonl, grocery-arukereso.jsonl, arukereso-none.jsonl, shopify-attributes.jsonl (and the full value lists in src/shopify-v2026-08-attributes.json), Google taxonomy, shopify-to-google.txt, and (read only) the taxonomy repo's work files. Date of the Arukereso counts: 2026-10-19.

## Counts per kind (91 findings)

| kind | count |
|---|---|
| hidden_node | 29 |
| missing_type | 10 |
| split_placement | 7 |
| undivided_leaf | 4 |
| filter | 32 |
| naming | 9 |

Priority: 18 high, 31 medium, 42 low.

## The 15 most important findings

1. Tea & Infusions holds 14 848 products on one node (24 percent of all Beverages); Shopify's Black, Green, Herbal & Fruit, White, Oolong, Matcha, Rooibos and Pu-erh leaves exist but are hidden (fb-1-14-2-x).
2. Candy & Chocolate holds 5 765 products itself because Arukereso's 'Desszert' was mapped to the parent; the Candy node shows 0 own products, so Gummy, Hard Candy, Caramel, Lollipops and Hungarian szaloncukor need to be shown and the category remapped.
3. Wine has 8 042 products on one node and Pezsgő/habzóbor is a separate Arukereso category of 2 512; add a Sparkling Wine & Champagne node (Pezsgők és habzóborok) and the missing wine filters (colour, sweetness, grape, region).
4. Pálinka (1 555 products, 69 percent of Brandy) has no node and Shopify's Brandy variety list has no Pálinka value; add Pálinka & Fruit Spirits under Liquor & Spirits, and Cognac (625) under Brandy.
5. Coffee holds 6 399 products with only capsules (5 065) split out; show hidden Coffee Beans & Ground Coffee and Instant Coffee, and add the coffee filters (product form, roast, decaf).
6. Coffee capsules (5 065) have no machine-system filter; add Compatible coffee pod system (Nespresso, Dolce Gusto, Tassimo, Senseo...).
7. Condiments & Sauces keeps 2 354 products on the parent next to five small leaves; show Pasta Sauce, Soy Sauce, Hot Sauce, Marinades & Grilling, Salad Dressing, Curry and Cooking Pastes.
8. Snack Foods (2 600, Arukereso 'Chips, ropi, rágcsálnivaló') has no chips, pretzels, crackers or popcorn leaf visible; the Shopify leaves exist and are hidden.
9. Herbs & Spices is the second-largest undivided Food leaf (5 519); show Pepper and add a Paprika node (Hungarian flagship, no Shopify node); needs a product-level look.
10. Dietary preferences (gluten-free, vegan, lactose-free, sugar-free, organic), Allergen information and Storage requirements (frozen) are missing from the Food and Beverage roots (only one leaf has Dietary preferences); this is the filter Hungarian grocery shoppers use most.
11. Frozen food has no category in Shopify; Arukereso's frozen categories hold 326 products (mirelit) and 0 for frozen vegetables, fries and ice cream. Add Storage requirements on Food Items, show Prepared Meals/Appetizers under Prepared Foods, and show ice cream leaves once a shop reading finds products.
12. Cooking Oils (1 708) has no olive, sunflower, coconut or rapeseed leaf visible; also the Hungarian name of Peanut Oil is 'Dióolaj' (walnut).
13. Chocolate (2 239) and Cookies (2 410): show Bars & Tablets, Truffles & Bonbons, Gift Boxes and Wafer Cookies (nápolyi), Gingerbread (mézeskalács).
14. Protein, energy and meal-replacement bars have two homes (Snack Foods hidden nodes and Health & Beauty Nutrition Bars with 1 134 + 159 products); keep Nutrition Bars as home for those, Cereal & Granola Bars for müzli (779).
15. Water: add Mineral Water / Ásványvíz (1 331) and Medicinal Water / Gyógyvíz (70) as the Hungarian split; the carbonation-split Shopify nodes are covered by the existing Carbonation filter and should stay hidden.

## Other notes

- Beer (1 938), Whiskey (4 113), Gin, Rum, Vodka, Tequila and Liqueurs: Arukereso is flat here and so is Shopify; styles and varieties are attributes, so these are filter findings, not nodes. Beer styles are not a category.
- Alcohol-free versions have a second home in the hidden fb-1-8 subtree (Arukereso's Cider category already mixes them in); the finding asks the operator to choose one home.
- Google's 2021 taxonomy is not finer than Shopify anywhere in this branch, so it adds no missing nodes; it was used for Hungarian name checks (Google HU for Coffee Creamer, Soda, Tea).
- Food Gift Baskets (fb-2-8, 503 products) and Tobacco Products (fb-3) are children of this branch's root but are not in grocery-nodes.jsonl; they are not audited here.
- Every Étel-Ital and Baba, mama category page in the 2026-10-19 crawl (tree-cloak.jsonl) has a row in the taxonomy repo's mapping-arukereso.jsonl (checked by URL), so no category of those two roots is missing from the input.
- Findings marked 'knowledge' inside the evidence list rest on retail knowledge, not on the files; they are suggestions to be checked against shop readings. Counts that say 'about' or 'guess' are not measured.
