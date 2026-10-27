# Category tree audit: branch "other" (Other / Egyéb)

Inputs read: other-nodes.jsonl (488 nodes: Baby Transport, Business & Industrial parts, Software, Services, Religious & Ceremonial, Vehicles, Gift Cards, Firewood & Fuel, Product Add-Ons, Bundles), other-arukereso.jsonl (59 categories), arukereso-none.jsonl (162 categories, every branch), tree.jsonl, shopify-attributes, Google taxonomy. Output: other-findings.jsonl (220 rows). Each row has the brief's fields plus `branch` and `source`; none-list rows also have `status`.

The branch is small in Arukereso evidence: 72 of its 488 nodes are visible in Hungary, and Software (8942 products), Services (2360) and Baby Transport (3518) hold most of the products. Most other hidden Business & Industrial, Services and Vehicles nodes have no Arukereso category at all, so findings there are marked knowledge.

## Counts per kind

Branch findings (source "branch", 58 rows):

| kind | rows |
|---|---|
| hidden_node | 17 |
| filter | 14 |
| naming | 14 |
| split_placement | 8 |
| missing_type | 4 |
| undivided_leaf | 1 |

By priority: 5 high, 24 medium, 29 low. Of the 17 hidden_node rows, 13 cite an Arukereso, Shopify or Google source and 4 are knowledge only (bt-7-3, bt-7-1, rc-2, bi-21).

Arukereso "none" list (source "arukereso-none row N", 162 rows, every branch):

| status | rows | meaning |
|---|---|---|
| own_node_exists | 122 | tree v0.1.0 already has an own node for the category, no action |
| no_action | 24 | empty, mislabeled, mixed bag or covered by an existing node |
| open | 16 | a real gap or a wrong mapping, see the list at the end |

By kind: missing_type 151, split_placement 6, filter 2, undivided_leaf 2, hidden_node 1. By recommended branch (all 162): diy 74, hobby 33, electronics 20, furniture-homeware 15, care-products 12, sport 5, fashion 1, grocery 1, other 1. Open rows by branch: hobby 7, furniture-homeware 4, diy 2, sport 1, care-products 1, grocery 1.

One discrepancy worth knowing: arukereso-none.jsonl was written before the own nodes were created. Its `shopify_id` is the nearest old node, while tree.jsonl already maps 122 of the 162 URLs to own-* nodes (the relation stays "none" in the tree).

## The 15 most important findings

1. bt-6-3 Baby Strollers: 752 products sit on the parent while six stroller types (jogging, double, umbrella, convertible, travel system, full-sized) are hidden. Show them; Shopify uses the same five values for stroller accessories. Hungarian names need a fix (Sportbabakocsik, not Esernyős).
2. so-1-10 Multimedia & Design Software: 2563 products (Arukereso Zeneszerkesztő program) sit on the parent; Music Composition and Sound Editing are hidden children. Show and move.
3. Experience vouchers live in three places: Gift Cards (802), Entertainment & Recreation Services (1317), Accommodation (1028). Pick one home (Services, with type nodes) and link from Gift Cards.
4. se-4 Entertainment & Recreation Services: 1317 experience vouchers on the parent; add own nodes for spa, dining, driving and flying, tours, and show the hidden Outdoor, Indoor and Children Activities.
5. Photo albums (none list, furniture-homeware branch): 2508 products sit on Gift Giving (71 percent of its 3546) although Photo Albums (hg-10-16-8-1) exists, hidden. Re-map and show.
6. Office Equipment (none list, hobby branch): 13485 of its 13494 products come from one catch-all Arukereso category (machine accessories). Largest undivided block in the none list.
7. Packing Materials (none list, hobby branch): 4981 of 6077 products are Zacskó, tasak (food bags, vacuum bags, courier bags) in one block; split by use.
8. Baby Transport and its accessories (3518 products) are labelled Other, while Baby & Toddler is Care Products and Baby Toys is Hobby. Decide the home.
9. bt-7-3-2 Stroller Footmuffs: 854 of 1062 come from "Babakabát, overál, bundazsák", which mixes baby coats and overalls (apparel) with sleeping sacks. Split to Liners & Sacks and Outerwear.
10. Software filters: License type, Operating system, User type (and VPN, firewall features on Antivirus) on Antivirus (1921), Office (1388), Operating Systems (660). None of the visible software nodes carries a filter.
11. so-1-2 and so-4: the Office and Operating Systems categories carry cloud suites and server licences (Microsoft 365, Dynamics, Power BI); the hidden CRM, ERP, Data Analysis, Cloud Services and Network Software nodes should be shown.
12. bi-22-4 Money Handling: 591 products (banknote verifiers and counters) on the parent; Banknote Verifiers, Coin & Bill Counters, Cash Drawers are hidden. Rename Bankjegy-hitelesítők to Bankjegyvizsgálók.
13. bt-6-1 Car Seats: 468 products on the parent; show Convertible Car Seats and add filters for installation (ISOFIX or belt), orientation and weight group.
14. Naming that would mislead: POS-terminálok holds the cash register computers (368), but a Hungarian POS terminál is a card reader; Fóliahordozók (Wrap Carriers) is a mistranslation; babahordozó means both infant car seat and soft carrier; two sibling nodes are both called Kotrógépek.
15. so-2 Digital Goods: 424 game subscriptions and top-up cards need their own node (game cards also overlap Gift Cards and Video Game Software); bi-17-1 strapping bands (355) are missing next to strapping machines; hg-5-7 Firewood & Fuel (237) hides its pellet, firewood and briquette children and needs the fuel-form filter.

Short of the top 15: Scooters (72 on Motorcycles & Scooters) need an own node or the Motorcycle/Scooter type filter; practice heads (244, hairdressing) are filed as retail mannequin heads; the Drones path runs through the literal "Levegőnél nehezebb légi járművek".

## Naming checks that found nothing

No "paddle", "soccer" or "football" appears in this branch. No Hungarian name is duplicated across the branch except Kotrógépek (bi-11-1 and bi-11-6) and the hidden Pénzügy és biztosítás (bi-7 and se-7-2). Google's taxonomy is not finer than Shopify's anywhere in this branch; its Hungarian names were used only as a naming reference.

## Open rows from the none list (16), with the branch that should hold each

- hobby: Ajándékozás > Vicces ajándék (1023, novelty gifts, own node or leave); Keresztelő ajándék (15) and Esküvői dekoráció (829) as an Occasion filter; Irodai gépek kiegészítői (13485) and Zacskó, tasak (4981) to split; Tanulói munkalap (2438) rename decision; Timpani (132) check.
- furniture-homeware: Fényképalbum (2508) re-map to Photo Albums; Tálalóeszköz (1583) re-map to Flatware serving; Okos világítás szett (132) and Fagylaltkehely (15) re-map.
- diy: Távfelügyeleti rendszer (1429) unclear mix, split cameras and alarms; Talajcsavar (126) re-map to Ground Spikes.
- sport: Bokszcipő (70) belongs under Boxing & Martial Arts with a link from Athletic Shoes.
- care-products: Műkörmös lámpa (40) belongs with Nail Tools.
- grocery: Protein étel (229) is food, link from sports nutrition.

Of the 122 resolved rows, 5 carry a check note about a path and label that disagree (own-brochure-holders, own-tagging-guns, own-dash-cam-accessories, own-fruit-mills, own-nail-dust-collectors).

## Method note

Counts are from the 2026-10-19 listing in the input files. Hungarian trade terms I propose without an Arukereso or Google source are marked knowledge in the evidence field and should be checked on three Hungarian shops before use. No file outside the two outputs was changed; my helper scripts are in the scratchpad folder other-work.
