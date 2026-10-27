# DIY branch audit: summary

Branch: the e-commerce category DIY (2 571 nodes, 740 visible). Output file: diy-findings.jsonl (251 findings).
Priority split: 38 high, 106 medium, 107 low.

## Counts per kind

| kind | findings |
| --- | --- |
| hidden_node | 118 |
| filter | 54 |
| missing_type | 32 |
| naming | 21 |
| split_placement | 15 |
| undivided_leaf | 11 |
| total | 251 |

## The 15 most important findings

1. Tiles are missing: Building Materials itself holds 18 970 products from one Arukereso category "Csempe, padlólap", and only the hidden Wall Tiles node exists; add Tiles with Wall Tiles and a new Floor Tiles node.
2. Motorcycle parts are spread over car-part nodes: 30 Arukereso categories with about 125 000 products are told apart only by a Vehicle type filter; propose one Motorcycle Parts & Accessories group (operator decision, it is a vehicle-type split).
3. Automotive Tires holds 251 457 products in one block, the largest node of the branch; divide by season and vehicle class (or make them filters) and add rim bolt pattern and size filters to Rims (38 104).
4. Paint (10 433) is one block while Arukereso splits it into interior wall (5 065), enamel (2 333), spray (1 906), floor and concrete (490), plinth (389) and facade (250) paint.
5. Circuit protection is wrong: Circuit Breakers (5 492) holds only RCDs ("Fi relé"), while 16 176 products (miniature breakers, fuses, energy meters) sit on Power & Electrical Supplies itself; rebuild with MCB, RCD, fuses and meters.
6. Hardware Fasteners holds 42 127 products on the parent; show the hidden Screws, Nuts & Bolts, Rivets and Threaded Rods (the HU name of Rivets is wrong, "Szegek").
7. Faucets holds 37 163 products and only Kitchen Faucets is split out; show Bathroom Sink Faucets and Bathtub & Shower Faucets, which Arukereso's "Fürdőszobai csaptelep" mixes.
8. Drill bits (34 175) need Masonry, Twist and Screwdriver Bits, and Tool Sockets (hidden, with 27 744 "Bitfej készlet, Dugókulcsfej" products on Tool Accessories) should have one home with Socket Wrenches.
9. Plumbing itself holds 32 295 products ("Fűtés szerelvény": valves, pipes and fittings mixed); show Pipes, Hoses, Pipe Connectors, Adapters and Ball Valves, which are hidden. Also the HU name "Vízszerelés" hides the bathroom (299 320 products in the subtree).
10. Bearings (13 483) are one block although Arukereso lists five bearing types (deep groove ball 7 725, tapered roller 2 170, spherical roller 1 282, cylindrical roller 1 187, needle roller 1 119).
11. Wrenches (12 499) lacks Open-End, Ring and Combination Wrenches as a type, and Pliers (11 625) and Measuring Tools (15 929) hide most of what shops sell (moisture meters, infrared thermometers, cutting pliers, locking pliers).
12. Car body parts (18 060) hide Fenders, Hoods, Doors, Trunks, Spoilers and Door Handles; Vehicle Cleaning (15 626) hides car shampoo, wax, glass and upholstery cleaners.
13. Workwear and PPE sit in three places: gloves, helmets and masks are DIY, while Workwear (345 242), Safety Boots (130 211) and hi-vis vests are Fashion; propose one home with links.
14. Heating is split between DIY (radiators 9 715, valves, thermostats) and Electronics (boilers 1 231, water heaters 943, stoves 2 059, heat pumps 2 263); a boiler and its radiators are not found together.
15. Fixture hardware (16 474, "Fürdőszoba szerelvény") hides aerators, click-clack drain plugs and sink drains; Pumps (12 442) hide well, sewage, utility and pool pumps; Seeds (7 908) have no home for vegetable and flower seed because the Seeds node holds only grass seed (353).

## Notes on evidence

- Evidence strings name the Arukereso category with its listed count (2026-10-19), the hidden Shopify node id with the tree's Hungarian name, Google ids or Shopify attributes.
- 95 findings carry at least one item marked "knowledge:" (a guess about what Hungarian shops sell, mostly for hidden Shopify types that no Arukereso category feeds); none is knowledge-only. Where Arukereso has no category for a type (cable, conduit, gutters, hinges, gates, fuel pumps, alternators), the node shows 0 products for Arukereso reasons; the count should come from shop crawls.
- Several "own-" nodes already added by the taxonomy build cover the Arukereso narrower and none categories of this branch (padlocks, lock cylinders, contactors, fairings, snow chains, roof windows, bearings; 117 own nodes in the branch), so those are not repeated here.
- Operator decisions flagged in the file: motorcycle parts as a group (vehicle-type split), tire season as node or filter, paint use as node or filter, one home for heating and for workwear across e-commerce categories.
