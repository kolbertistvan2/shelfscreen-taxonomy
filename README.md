# shelfscreen-taxonomy

A product category tree for webshop catalogues: one modern, market-wide tree with English and Hungarian names,
built on Shopify's Standard Product Taxonomy v2026-08. Hungary first; other markets add their languages later.

Version 0.5.0 (2026-10-27: the tree gaps, 57 own nodes for product types no node and no kind filter value held). Version 0.4.1 was 2026-10-27 (ruling II, ECDB first), version 0.4.0 was 2026-10-27 (e-commerce categories decided by rule, the Jev, review and the controller's rulings), version 0.3.1 was 2026-10-27 (fix round 1 of the v0.3.0 review), version 0.2 was 2026-10-26 (two fix rounds on 2026-10-27), version 0.1 was 2026-10-20.

## What is in it

| | v0.1 (2026-10-20) | v0.2 (2026-10-26) | v0.3.1 (2026-10-27) | v0.4.0 (2026-10-27) | v0.5.0 (2026-10-27) | v0.5.1 (2026-10-27) |
|---|---|---|---|---|---|---|
| Nodes | 14 865: Shopify's 14 606 plus 259 own | 14 901: Shopify's 14 606 plus 295 own | 15 055: Shopify's 14 606 plus 449 own | the same | 15 112: Shopify's 14 606 plus 506 own (57 new, see "Tree gaps") | 15 115: Shopify's 14 606 plus 509 own (3 new, see "Aliases and tree gaps (v0.5.1)") |
| Shown | 3 095 (only nodes with Hungarian products under them) | every node | every node | the same | the same | the same |
| Hungarian names | every node; 1 512 Shopify translations corrected | every node; 1 512 + 847 corrected; 6 212 marked reviewed | every node; 1 512 + 847 + 3 283 + 105 corrected; 14 297 marked reviewed (758 not: the reviewer was unsure) | the same | every node; 2 more Shopify names corrected (`hu-renames-7.jsonl`); 14 354 marked reviewed (the 57 new own nodes named when made) | 1 more corrected (`hu-renames-8.jsonl`, Elektromos csónakmotorok); 14 358 marked reviewed; 30 aliases on 16 nodes (`aliases_hu`, `aliases_en`) |
| English names | Shopify's | 39 renamed to "Football (Soccer)" | the same, plus Drills (own node) | the same | the same | the same |
| Links | none | 114 on 13 nodes (Shoes and Clothing to the sport nodes) | 271 on 114 nodes | the same | 300 on 125 nodes (the new sport clothing, Beer to the radlers) | the same |
| Node moves | none | 15 Shopify nodes moved under own nodes | 49 (34 more: the motorcycle, heating and gift-set homes and others) | the same | the same | the same |
| Filters | 300 on 267 nodes | 95 058 on 14 742 nodes, from 8 501 Shopify attributes with all their values; 20 inherited filters dropped with a reason | 95 969 on 14 888 nodes; 16 filters added with a reason; 21 dropped (the 20 and the garment type on Erotic Clothing) | the same | 96 447 on 14 945 nodes; 18 added (beer kinds on alcohol-free beer); 13 kind values and 2 filter names corrected in Hungarian | 96 474 on 14 948 nodes; 22 added (boot-type on Chaps, seafood-cut, bag-style on Padel Bags); 2 own kind filters (dish of a ready meal, kind of a vegetable mix); 3 own values (Ale, Flavoured beer, Hake); 1 value renamed (Half chaps: Hopilett) |
| Arukereso | all 2 988 categories placed; 10 234 765 products | all 2 988 placed; 9 732 089 products counted (two custom configuration categories not counted) | the same; 21 categories moved to a better existing node and 142 placed on new own nodes | the same | the same | the same |
| E-commerce categories | every node classed into seven e-commerce categories | the same, with the new nodes classed | the same; Fireplaces reclassed to DIY (heating), Paper Hand Towels to Care Products > Personal Care, Practice Heads to Other | every node classed on its own, with a source (rule, jev, review, review-pending, ruling) and the Jev's confidence; see "E-commerce categories" below; v0.4.1: ruling II (ECDB first) moves 9 ruled nodes to their reviewed class | the new own nodes inherit their parent's class; 6 sport clothing nodes carry their own (`ecommerce-7.jsonl`) | the 3 new own nodes inherit their parent's class |

Counts from `sh build/all.sh` on 2026-10-27 (v0.5.1, v0.5.0, v0.4.1, v0.4.0 and v0.3.1) and from the v0.1 and v0.2 release files.

## Rules

- Backbone: Shopify Standard Product Taxonomy v2026-08 (MIT, see `NOTICE.md`). Google's product taxonomy
  (2021-09-21) is only a mapping target, through Shopify's own mapping file.
- Every node has an English and a Hungarian name. Shopify's Hungarian translation is not taken as it is: v0.2
  reviewed the sport, shoes and clothing branches, v0.3 every other node. `name_hu_reviewed` is true where the
  reviewer was sure (changed or kept); 758 names the reviewer was unsure of stay `false`, changed or not. An own
  node counts as reviewed only through its line in `work/hu-review-scope.tsv` (since v0.3.1; the 154 v0.3 own
  nodes were checked one by one in fix round 1).
- No category is named only by an age group ("Gyerek", "Felnőtteknek", "Kids"), in any suffixed form; a children's category names its product type
  (the operator, 2026-10-27). The children's branches (Baby & Children's Clothing and Shoes) stay (the operator,
  2026-10-27). The build stops on an age-only name. Mature is "Korhatáros termékek (18+)" in Hungarian.
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
- A new own node enters only with its evidence written next to it in `work/own-nodes.jsonl`: an Arukereso
  category with its listed products, an Arukereso category whose name lists the type (counted on the parent when
  Arukereso does not divide it), a mapper sample note, the Decathlon study's product names, or (since v0.5.0) the
  studies' product databases and the name gold set, read on a stated date. A finding that rests
  on knowledge alone, on Shopify attribute values alone or on Google 2021 alone is not added
  (`work/audit-v03-decisions.jsonl` says why, finding by finding).
- Controller rulings of 2026-10-27 (the operator left these to the controller: "nem tudom"; they are not his
  words, see `work/controller-rulings.jsonl`): motorcycle parts have their own group (Vehicle Parts & Accessories >
  Motorcycle Parts & Accessories) beside the car parts; tyre season is a filter (Vehicle tire type), not a node;
  heating goes under DIY (Hardware > Heating, Ventilation & Air Conditioning > Heating, with boilers, radiators,
  water heaters, indoor fireplaces and their accessories; heat pumps stay under Climate Control Appliances with a
  link from Heating, firewood and fuel stay with the fireplace accessories, outdoor fireplaces go to Outdoor
  Living: the heating ruling covers heating devices, not fuel or garden fire pits, fix round 1); workwear goes under Fashion (Safety Boots under
  Shoes, High-Visibility Safety Apparel under Uniforms & Workwear; protective equipment stays in Work Safety
  Protective Gear).
- A console platform (PlayStation, Xbox, Nintendo) is brand-named, so it stays a filter (Video game platform);
  occasions (wedding, christening, Christmas) are the Celebration type filter.
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

## E-commerce categories (v0.4.0)

The operator, 2026-10-27, quoted in the controller's brief: "nézd meg az ecdb kategorizálását is a biztonság kedvéért
meg a shopify-t és a google shopping-ot. és erre építünk szabályt, a jev meg eldönti", then "oke mehet". The run is
`bench/ecommerce_classify/` in the fast-browse-jev repo (commits b6e7be5f, a339026f and ef5a35f3); its full evidence is in
`shelfscreen-data/2026-10-27/ecommerce-classify/`. `work/ecommerce-6.jsonl` holds one row per node: `category_main`,
`category_sub`, `fit`, `source`, `confidence` (the Jev's, where it answered), `reason`, `jev` (its choice and
confidence).

1. Evidence per node: the ECDB definitions (`ecdb-categories.jsonl`, 7 main and 27 subcategories, and 208 deeper
   ECDB nodes; equal to the v3 document) matched word by word on the node's English path, excludes as vetoes; the
   Shopify vertical and the Google top category (`sources/google-2021-09-21/`, reached through Shopify's own mapping),
   each mapped to ECDB main categories by a table with a reason per row; the v0.3.1 class.
2. Rule (source `rule`): where the ECDB match and the v0.3.1 class name the same main and subcategory and each table
   that decides holds that main, the node is clear. 5 379 nodes; the other 9 676 are open.
3. The Jev (TypeSafe jev-1.13.0) picks one of the 27 subcategories ("Main > Sub") or Other on every open node, with
   each option's ECDB definition, includes, excludes, its main category's includes and excludes, and ECDB's deeper
   nodes. Calibration first, on 300 rule-clear nodes stratified over the seven categories (agreement with the rule
   94.3%); the bound is the lowest confidence at which agreement is at least 99%:

   | Confidence at or above | Answered | Agreed | Agreement |
   |---|---|---|---|
   | 0.00 | 300 | 283 | 94.3% |
   | 0.50 | 291 | 279 | 95.9% |
   | 0.70 | 267 | 261 | 97.8% |
   | 0.79 (bound) | 258 | 256 | 99.2% |
   | 0.90 | 239 | 237 | 99.2% |
   | 0.95 | 208 | 207 | 99.5% |
   | 1.00 | 89 | 89 | 100% |

   The calibration had no node whose true class is Other: 13 of its 17 misses were the Jev choosing Other.
4. Controller rulings for v0.4.0 (2026-10-27, not the operator's words): a Jev answer at or above the bound that
   keeps the v0.3.1 class is clear (source `jev`). The Jev's 1 193 changes to Other or to another main category were
   reviewed by three reviewers against the ECDB definitions; the reviewed class applies where the reviewer was sure
   (source `review`, the reviewer's reason kept), the v0.3.1 class with fit `weak` where not. A node below the bound,
   or a Jev change within the same main category that no reviewer saw, keeps its v0.3.1 class with fit `weak`
   (source `review-pending`, the Jev's choice and confidence kept). The controller's rulings
   (`work/controller-rulings.jsonl`: heating, heating scope, workwear; fix round 1: Practice Heads Other, Paper Hand
   Towels Personal Care) override all of these (source `ruling`, 103 nodes); 73 nodes where the Jev or a reviewer chose
   otherwise are listed in `shelfscreen-data/2026-10-27/ecommerce-classify/v040/ruling-conflicts.jsonl`.
5. Ruling II (v0.4.1, controller, 2026-10-27, not the operator's words): ECDB first. The categories are built on
   ECDB's definitions, so a controller ruling holds only where ECDB's definitions do not name the item. Where a
   reviewer was sure and quoted an ECDB definition that names the item, the reviewed class stands: Hardhats and
   Welding Helmets (Workwear excludes "Helmets", Headwear "Safety helmets"), Protective Eyewear, Goggles and Safety
   Glasses (Workwear and Sunglasses exclude "Safety glasses and goggles"), Hearing Protection Earmuffs (Headphones
   exclude "Hearing protection") go to Other; Medical Masks to Care Products > Health Care (Other Medical Products
   includes "Personal protection equipment (e.g. gloves, masks)"); Water Heaters and Heat Pump Water Heaters to
   Electronics > Electrical Appliances (Household Appliances includes "Heating and cooling appliances"). The other
   sure reviews in the ruled subtrees quote no ECDB line naming the item (Face Shields, Safety Knee Pads, the work
   safety harnesses and tethers, 10 nodes) and keep the ruling.

Counts (`sh build/all.sh`, 2026-10-27):

| | v0.3.1 | v0.4.0 | v0.4.1 | v0.5.0 |
|---|---|---|---|---|
| Hobby & Leisure | 5 688 | 5 687 | 5 687 | 5 711 |
| DIY | 2 644 | 2 591 | 2 582 | 2 582 |
| Electronics | 2 068 | 1 924 | 1 926 | 1 926 |
| Furniture & Homeware | 1 521 | 1 490 | 1 490 | 1 490 |
| Care Products | 1 157 | 1 116 | 1 117 | 1 118 |
| Grocery | 753 | 749 | 749 | 758 |
| Fashion | 732 | 746 | 746 | 769 |
| Other | 492 | 752 | 758 | 758 |
| fit clear / weak / none | 13 759 / 804 / 492 | 10 603 / 3 700 / 752 | 10 597 / 3 700 / 758 | 10 602 / 3 701 / 758 explicit; the other 51 inherit |
| source | 289 explicit, 14 766 inherited | rule 5 377, jev 5 013, review 1 157, review-pending 3 405, ruling 103 | rule 5 377, jev 5 013, review 1 166, review-pending 3 405, ruling 94 | rule 5 383, jev 5 013, review 1 166, review-pending 3 405, ruling 94, inherited 51 |

By source and fit in v0.4.1: rule clear 5 377; jev clear 5 013; review clear 114, weak 354, none 698 (reviewed to
Other); review-pending weak 3 346, none 59; ruling clear 93, none 1 (Practice Heads). In v0.4.0, review had clear
111 and none 692, ruling clear 102. A `weak` fit now also means the
class waits for review.

## Tree gaps (v0.5.0)

The operator, 2026-10-27 19:24, handing the open tree gaps to the controller: "oldd ezeket meg okosan"
(`work/operator-decisions.jsonl`). Controller ruling ZZ (2026-10-27, not the operator's words): a product type is
covered when a node exists for it or when the deepest fitting node carries a kind filter (a Shopify `*-variety` or
`*-type` attribute) whose value names it, for example Beer with beer-variety Pale lager. Only a type that neither
covers is a gap, and a gap becomes an own node by the area-structure rule of 2026-10-27.

Candidates came from real data, read on 2026-10-27: the name gold set's product words whose node is missing or only
a parent (`shelfscreen-data/2026-10-27/name-gold/gold.jsonl`, 360 rows, and the tree gaps of the name loop); the
breadcrumb leaves of the Decathlon study's 17 201 products (1 782 distinct paths; `studies/decathlon/exports/decathlon/
builder-input-decathlon.hu.jsonl`); and the product groups and names of the beer (528 products), FRoSTA (356),
perfume (17 583) and padel (9 877) studies' databases. Each candidate was checked against the node names and the kind
values of the tree before it became a node.

| Outcome | What |
|---|---|
| own node (57, `own-nodes.jsonl`, `added: v0.5.0`) | padel clothing by garment (tops, shorts, skirts, dresses, pants, jackets, sweatshirts) and padel equipment (racket accessories with frame protectors, dampeners and covers, ball pressurizers, nets); running and hiking clothing by garment; Football (Soccer) Clothing with shorts, pants, training tops and socks (sportszár); Golf, Hunting, Handball, Table Tennis and Sailing Clothing (Sailing as a sport); Orienteering with its control flags; mountaineering boots; freeze-dried outdoor meals; Basque pelota and frontenis; petanque; kite parts; fishing particle baits, feeder baskets and pre-tied rigs; dive marker buoys; camping cupboards; kick scooter wheels, brakes, handlebars and grip tape; table tennis table parts; trampoline frame parts and springs; breaded fish with fish fingers, breaded cheese, breaded vegetables and onion rings; dill, parsley, chives and basil; refillable perfume atomizers |
| covered by a kind value | lager, dark beer, IPA (beer-variety); radler and the flavoured beer mixes (Beer-Based Cocktails, beer-based-cocktail-variety Radler); alcohol-free lager and radler (the two beer kind filters added to Low Alcohol & Alcohol-Free Beer); wax beans; spray and stick deodorants (dispenser-type); half chaps; air gun pellets (BBs, projectile-type Pellet); fish by species (seafood-type) |
| covered by a node | ready meals by dish, vegetable mixes by use, plant-based burgers, dive computers, golf trolleys (Golf Bag Carts), shaker bottles, pedometers (Activity Monitors), grip gel, peteca (Shuttlecocks), fencing underarm protectors (Plastrons), tent parts, bicycle parts, most fishing, riding and winter items |
| filter, not a node | the cut of a fish or a vegetable (fillet, florets), a beer gift pack, the sport of a sock, cap or wristband |
| not made | a generic "ale" (Shopify names the ale kinds one by one; a beer named only ale takes Other), figure skating dresses and tennis garments (too few), items with one to four products |

Every candidate that did not become a node is in `own-nodes-rejected.jsonl` with its outcome, the node or value that
covers it and the reason (47 rows, `added: v0.5.0`).

Thresholds (controller, 2026-10-27, not the operator's words): a sport clothing node needs 20 products in the sources
above, and a garment node under it (shorts under Padel Clothing) 25 products of that garment; socks, caps and
wristbands stay on the general accessory nodes with the sport as a filter, except football socks (sportszár), which
Hungarian shops sell as their own product. A product type of its own (feeder baskets, dill) needs no threshold.

Placement: sport goods sit under their sport, and Activewear, its Tops, Pants, Shorts, Vests & Jackets and
Sweatshirts & Hoodies, Skirts, Dresses, Athletic Socks and Boots link to the new sport nodes (`links.jsonl`). Beer and
Low Alcohol & Alcohol-Free Beer link to Beer-Based Cocktails, whose Hungarian name is now "Radlerek és sörkoktélok".
Freeze-dried meals live under Prepared Foods with a link from Camping & Hiking; perfume atomizers under Perfumes &
Colognes with a link from Travel Bottles & Containers.

E-commerce category: a new node inherits its parent's class. Where that would break the rule above, the node has its
own row in `ecommerce-7.jsonl`: Football (Soccer), Golf, Handball and Table Tennis Clothing are Fashion > Apparel
(activewear and team kits), Hunting Clothing Fashion > Apparel with fit `weak` (the definitions do not name it), Sailing
Clothing Hobby & Leisure > Sports Equipment (water sport apparel).

Hungarian labels of kind values that Hungarian shops say otherwise (`filter-renames.jsonl`, `added` in `source`):
beer-variety Pale lager "Világos sör", Dark lager "Barna sör", Lager "Láger", India pale ale (IPA) "IPA", Wheat beer
"Búzasör", Amber/Red ale "Vörös sör"; aftershave-product-form Lotion "Arcvíz"; seafood-type Pollock "Alaszkai
tőkehal", Scallop "Fésűkagyló", Squid "Kalmár", Crab "Tarisznyarák", Calamari "Tintahalkarika"; projectile-type
Pellet "Légfegyver-lövedék"; and the filter names seafood-type "Hal vagy tenger gyümölcse fajtája" and
artificial-bait-form "Csali formája".

## Aliases and tree gaps (v0.5.1)

The second pass on the tree gaps, from the name builder's measured misses on tree v0.5.0 (the catalogue branch's
`bench/name_gold/loop.md`, "Tree gaps for the next taxonomy pass"), under the same hand-over (the operator,
2026-10-27 19:24: "oldd ezeket meg okosan") and controller ruling ZZ.

Aliases: `work/aliases.jsonl` holds one row per word (`id`, `lang`, `alias`, `relation`, `source`, `added`), and the
build writes them on the node as `aliases_hu` and `aliases_en` (empty lists elsewhere). An alias is a word shops use
for the node that its names lack, with its source (the shop wording or product it was read from); never a brand,
never a filter value alone. `relation` is `synonym`, or `compound` for a shop word that joins the node's word and
one of its filter values (`deostick`: Deodorants + dispenser-type Stick; `karfiolrózsa`: Cauliflower +
vegetable-preparation-style Florets). 30 aliases on 16 nodes, for example `komputer` and `búvárszámítógép` (Dive
Computers), `fogaskoszorú` (Bicycle Cassettes), `sícipő` (Ski Boots), `lövedék` (BBs), `markolat` (Padel Grips &
Overgrips), `pressurizer` and `labdanyomás-megőrző` (Padel Ball Pressurizers), `deo` and `deostick` (Deodorants),
`futóóra` (Sports Watches), `zöldségburger` (Plant-Based Burgers), `sörital` and `beer mix` (Beer-Based Cocktails),
`kormánybandázs` (Handlebar Tape & Wraps).

| Outcome | What |
|---|---|
| own node (3) | Fish Bites & Shapes (Halfalatkák és halfigurák, 6 products: halfalatka, halfigura, fish nuggets), Protein Water (Fehérjevizek, 2), Peteca (1, a game of its own beside Basque pelota) |
| own value (3, `value-adds.jsonl`) | beer-variety Ale (7 beers say only "ale") and Flavoured beer (Ízesített sör, 5 beers flavoured in brewing; a beer mixed with a flavoured drink stays Beer-Based Cocktails); seafood-type Hake (Hekk, 2) |
| own kind filter (2, `node-attributes.jsonl`) | Prepared Meals & Entrées: dish (lasagne, tepsis halfilé, rák rizzsel, paella, risotto, gnocchi, curry, pasta dish, rice dish); Vegetable Mixes: kind (serpenyős, wok, tepsis, krémleves, leveszöldség, franciasaláta-alap, rizses) |
| filter added (4) | boot-type on Chaps (v0.5.0 recorded hopilett as Chaps + Half chaps without the filter on the node); seafood-cut on Fresh & Frozen Seafood and Breaded Fish & Seafood (tilápiafilé, lazacsteak, hekkfilé); bag-style on Padel Bags (padel hátizsák) |
| renamed | Trolling Motors: Elektromos csónakmotorok (was Villanymotorok); boot-type Half chaps: Hopilett |
| covered by a node | etetőpellet-szett (Fishing Pellets), hátsó gyerekülés (Bicycle Child Seats + placement Rear), kormányszalag-rögzítő ragasztószalag (Handlebar Tape & Wraps, one product), hajpánt (Hair Bands; the gold row's Headbands is in doubt), izomstimulátor and testpermet (their nodes' names hold the word) |

Every candidate has a row in `own-nodes-rejected.jsonl` with `added: v0.5.1` (22 rows), counts read on 2026-10-27
from the Decathlon builder input, the beer, FRoSTA, perfume and padel databases and the name gold set. A product type
of its own needs real products in that data, not a threshold.

## Filters

A node's filters are Shopify's attribute list for its category, with all values. An own node takes the list of
the Shopify category named in its `filters_from`, else of its nearest Shopify ancestor. In `dist/tree.jsonl` a
Shopify filter is a reference (`{"attribute_id", "source": "shopify"}`); its English and Hungarian names and
values are in `dist/attributes.jsonl`, keyed by `attribute_id`. Own filters (for example fragrance
concentration) carry their names and values inline. An inherited filter that does not describe the node is
dropped and recorded with its reason (`work/filter-drops.jsonl`, `filters_dropped` on the node). A Shopify
attribute a node lacks but needs is added with its reason (`work/filter-adds.jsonl`, `filters_added` on the node;
16 in v0.3, for example the frame filters on Eyeglass Frames and Celebration type on Gift Giving).

Review of the Hungarian filter names: the names of the 1 874 Shopify attributes used in the sport, shoes and
clothing branches (`work/filter-hu-review-scope.txt`, 1 940 attributes marked reviewed with the v0.1 ones) were
checked, and their 16 010 distinct values were checked one by one; 15 969 are listed in
`work/filter-values-checked.txt`, the other 41 (mostly fragments of corrupt Shopify values) were not confirmed
and stay unreviewed. In all, 16 093 of the 73 133 distinct values in the dictionary are marked `hu_reviewed`.
`work/filter-renames.jsonl` holds 1 131 rows: 340 attribute names and 769 values corrected in Hungarian, 15
attribute names and 9 values in English (a row may carry both), each with the name it replaced (`old_hu` or `old_en`); the build checks that name before it applies a
correction.

## Changes from v0.5.0

| v0.5.0 | v0.5.1 |
|---|---|
| no aliases | `aliases_hu`, `aliases_en` on every node (`work/aliases.jsonl`) |
| Shopify's attribute values only | plus own values (`work/value-adds.jsonl`, id `own-...`), kept before Other |
| `hu-renames-1..7.jsonl` | plus `hu-renames-8.jsonl` |
| 506 own nodes | 509 |

## Changes from v0.4.1

| v0.4.1 | v0.5.0 |
|---|---|
| 449 own nodes | 506: 57 for the tree gaps, each with its evidence and `products_2026_10_27` |
| `hu-renames-1..6.jsonl` | plus `hu-renames-7.jsonl` (Búvárkomputerek, Radlerek és sörkoktélok) |
| `ecommerce-1..6.jsonl` | plus `ecommerce-7.jsonl` (6 sport clothing nodes) |
| `own-nodes-rejected.jsonl` rows on Arukereso categories | plus rows on gap candidates: `candidate`, `source`, `products`, `outcome`, `covered_by`, `reason` |

## Changes from v0.3.1

| v0.3.1 | v0.4.0 and v0.4.1 |
|---|---|
| e-commerce classes in `ecommerce-1..5.jsonl`, inherited down the tree from 289 explicit rows | `ecommerce-6.jsonl` classes every node; every older row carries `superseded_by` |
| `ecommerce_category`: `main`, `sub`, `main_hu`, `sub_hu`, `fit`, `inherited`, `reason` | plus `source` and `confidence`; `dist/tree-hu.csv` has `ecommerce_source` and `ecommerce_confidence` |
| controller rulings over every other source | v0.4.1, ruling II: ECDB first; a ruling holds only where ECDB's definitions do not name the item |
| Google's taxonomy used only through Shopify's mapping file | the Google taxonomy 2021-09-21 itself (English, Hungarian) in `sources/google-2021-09-21/` |

## Changes from v0.2

| v0.2 | v0.3.1 |
|---|---|
| Hungarian names reviewed in the sport, shoes and clothing branches (6 212) | every branch reviewed (14 297 marked reviewed); `work/hu-renames-5.jsonl` holds 3 283 corrections and `work/hu-renames-6.jsonl` the 105 of fix round 1, each with the name it replaced (`old_hu`), the reviewer's certainty (`sure`) and its source (review, consistency check or audit naming finding) |
| own nodes in sport and fashion | 154 more own nodes in DIY, Electronics, Furniture & Homeware, Care Products, Grocery and Hobby & Leisure, each with its evidence and the audit finding it answers |
| Arukereso categories placed by the v0.1 mapping or an own node | `work/arukereso-remaps.jsonl` moves 21 categories to a better existing node (the build checks the old node) |
| filters from Shopify's list, minus the dropped ones | plus `filters_added` (`work/filter-adds.jsonl`) |
| `moved_from` on moved Shopify nodes | also on moved own nodes (`old_parent_id` in `work/node-moves.jsonl`; the build checks it) |
| e-commerce classes in `ecommerce-1..4.jsonl` | plus `ecommerce-5.jsonl` (Fireplaces to DIY under the heating ruling, Paper Hand Towels, Practice Heads; the older rows carry `superseded_by`) |
| no record of the audit decisions | `work/audit-v03-decisions.jsonl`: one row per finding of the seven audits (1 120), with the decision and the nodes it made |

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
| `moved_from` | the parent before the node was moved (only on moved nodes) |
| `reason`, `evidence` | own nodes only: why the node exists, and the measured evidence |
| `aliases_hu`, `aliases_en` | words shops use for the node that its names lack (since v0.5.1; empty lists where none) |
| `links` | ids of nodes this node points to (Apparel > Shoes and Clothing to the sport nodes) |
| `has_products_hu` | null for now |
| `arukereso_products_own`, `arukereso_products_subtree` | Arukereso "N termék" counts (2026-10-19) on the node and under it, counted categories only |
| `arukereso[]` | placed Arukereso categories: `path`, `url`, `relation`, `listed_products`, `counted` |
| `filters_from` | the Shopify category whose attribute list the node takes, when not its own |
| `filters[]` | `{"attribute_id", "source": "shopify"}`, or an own filter with `attribute_id`, `source: "own"`, `name_en`, `name_hu`, `name_hu_reviewed`, `values[]` (`en`, `hu`) |
| `filters_added[]` | filters added to the node's list: `attribute_id`, `reason` (only where any) |
| `filters_dropped[]` | inherited filters left out: `attribute_id`, `reason` (only where any) |
| `ecommerce_category` | `main`, `sub`, `main_hu`, `sub_hu`, `fit` (clear, weak, none), `inherited`, `reason`, `source` (rule, jev, review, review-pending, ruling), `confidence` (the Jev's, or null) |

### `dist/attributes.jsonl`, one Shopify attribute per line

| Field | What |
|---|---|
| `attribute_id` | Shopify handle, the key a node filter refers to |
| `shopify_id`, `base_attribute_id` | Shopify's numeric id; for an extended attribute, the attribute it takes its values from |
| `name_en`, `name_hu`, `name_hu_reviewed`, `renamed_hu_from` | names, review flag, the Hungarian name before a correction |
| `values[]` | `id`, `en`, `hu`, `hu_reviewed`, `renamed_hu_from`; an own value (v0.5.1) has an id starting `own-` |

## Layout

| Path | What |
|---|---|
| `dist/tree.jsonl` | every node: id, parent, names, paths, source, rename and move history, evidence, aliases, links, Arukereso categories and counts, filters, e-commerce category |
| `dist/attributes.jsonl` | the filter dictionary: every Shopify attribute in use with its English and Hungarian names and values |
| `dist/tree-hu.csv` | every node, flat, with Hungarian names and filter names |
| `dist/ecommerce-summary.csv` | Arukereso products per e-commerce category and subcategory |
| `site/index.html` | the browsable page: grouped by e-commerce category or as the full tree, search, links, filters, HU/EN |
| `sources/google-2021-09-21/` | Google's product taxonomy 2021-09-21 with ids, English and Hungarian (`SOURCE.txt`) |
| `sources/shopify-v2026-08/` | Shopify's categories, attributes and attribute values (English, Hungarian) and its mapping to Google 2021-09-21 |
| `sources/arukereso-2026-10-19/category-pages.jsonl` | Arukereso's 3 002 category pages: breadcrumb and heading |
| `sources/tree-audit-2026-10-26/` | the tree audit findings of 2026-10-26 (sport, fashion, DIY, electronics, furniture and homeware, care products, grocery, hobby, other) that the own nodes and decisions cite (`finding` field), with their summaries |
| `work/` | the build's input: Shopify's tree and attribute lists as tables, and the decisions applied to them (see below) |
| `build/` | `sh build/all.sh` rebuilds `dist/` and `site/` from `work/` (Python 3, standard library only); `build/extract_shopify.py` made the two Shopify attribute tables once |

The decisions in `work/`:

| File | What |
|---|---|
| `operator-decisions.jsonl` | the operator's decisions, with his words where they were passed on |
| `controller-rulings.jsonl` | the controller's rulings of 2026-10-27 on the DIY questions the operator left open (not his words) |
| `audit-v03-decisions.jsonl` | the decision on every finding of the seven v0.3 audits |
| `mapping-arukereso.jsonl`, `arukereso-not-counted.jsonl` | Arukereso categories on the tree; the ones not counted |
| `hu-renames-1..8.jsonl`, `hu-review-scope.tsv` | Hungarian node renames; which node names were reviewed and in which round |
| `en-renames.jsonl` | English node renames (Football (Soccer), Drills) |
| `own-nodes.jsonl`, `own-nodes-rejected.jsonl` | own nodes with their evidence; proposals rejected, with reasons |
| `aliases.jsonl`, `value-adds.jsonl` | node aliases with their sources; own values of Shopify attributes, with reasons (v0.5.1) |
| `node-moves.jsonl`, `links.jsonl` | moved nodes; links between nodes |
| `arukereso-remaps.jsonl` | Arukereso categories moved to another existing node, with the old node and the reason |
| `node-attributes.jsonl`, `filter-adds.jsonl`, `filter-drops.jsonl` | own filters; filters added; inherited filters dropped, with reasons |
| `filter-renames.jsonl`, `filter-hu-review-scope.txt`, `filter-values-checked.txt` | filter name fixes with the old names; which attributes and which values were reviewed |
| `ecommerce-1..7.jsonl` | e-commerce classes; 6 (v0.4.0) holds every node with its source and confidence, the older rows are superseded; 7 (v0.5.0) the new sport clothing nodes |

## How the decisions were made

Each Arukereso category was mapped onto Shopify, the Hungarian names were reviewed, own nodes and filters
proposed, and every node classed into the e-commerce categories. In v0.2 the sport, shoes and clothing branches
were checked against the product names of the Decathlon study (`shelfscreen-data/2026-10-20/decathlon`,
dashboard files of 2026-10-24): a new node is added only where those products, or Arukereso categories, show
it. In v0.3 seven reviewers checked the Hungarian names of the remaining 8 689 nodes (3 257 changed, 758 marked
unsure); the controller checked every parent and child pair and every renamed term across the tree for
consistency and fixed 36 names (for example camera lenses are objektív throughout, Taps & Dies is Menetfúrók és
menetmetszők, the Rivet Guns children say szegecshúzó), and applied 9 audit naming findings on names reviewed
earlier. Fix round 1 of the v0.3.0 review (v0.3.1) applied the review's name table, checked the 154 new own
node names one by one and every renamed name against its parent, and reverted four remaps that contradicted their
evidence. The structure of DIY, Electronics, Furniture & Homeware, Care Products, Grocery, Hobby & Leisure and Other
follows the 2026-10-26 audit findings: 154 own nodes, 34 moves, 157 links and 21 remapped Arukereso categories, each
tied to its finding. Each decision sits in `work/` with its reason; a change is made there and the tree rebuilt.
