# Sport branch (Sporting Goods) gap audit

Audited 2026-10-26. Inputs: sport-nodes.jsonl, sport-arukereso.jsonl, the Decathlon-study assortment.json and data.json (11 Hungarian sports shops, 2026-10-20), Shopify v2026-08 attributes, Google taxonomy 2021-09-21 (English and Hungarian), the whole tree.

Scope note: sport-nodes.jsonl leaves out six Sporting Goods nodes that carry another e-commerce category (Tennis Shoes 4 197, Basketball Shoes 839, Padel Shoes, Ice Baths, Shaker Bottles 616, Sim Racing 1 086). They were read from tree.jsonl and are included where relevant.

## Counts per kind (128 findings)

| kind | count |
|---|---|
| hidden_node | 57 |
| filter | 29 |
| split_placement | 17 |
| naming | 12 |
| missing_type | 7 |
| undivided_leaf | 6 |

Priority: 16 high, 55 medium, 57 low.

## The 15 most important findings

1. Visibility rule (sg): 2 715 of the branch's 3 093 nodes are hidden because Arukereso has no category, yet 88 hidden Sporting Goods nodes carry 9 093 shop listings in the study (and 17 hidden Apparel nodes 14 948); show a node when the shops' own reads have products too.
2. Running has no node (sg-1): 25 020 running shoes (Arukereso men's, women's and children's running shoe categories) sit inside the 45 464-product Athletic Shoes block; Shopify keeps running only as a value of the Activity attribute.
3. Sport shoes are spread over more than 15 places (aa-8-1): Athletic Shoes, Tennis (4 197), Basketball (839), Soccer (3 682), Cycling (7 480), Climbing (2 618), Golf, Ski and hidden Volleyball, Badminton, Rugby; propose one home under Athletic Shoes by sport with a link from each sport node (operator decides the home).
4. Hiking footwear has no home (sg-4-2): 9 892 hiking shoes sit on Athletic Shoes while the study files 10 916 products on the Camping & Hiking parent; add a Hiking Footwear node.
5. Fishing Baits & Lures holds 17 312 products on one node (sg-4-6-13-1), the largest leaf in the branch; wobblers, soft plastics, jigs, spinners, boilies and pellets exist hidden and Arukereso's own notes say its two categories span them.
6. Fishing Rods hold 5 343 products with 16 hidden rod types (sg-4-6-11), Fishing Reels 1 404 with 13 hidden types.
7. Bicycle Tires: 10 257 products and no visible child (sg-4-4-2-21); split by bike (mountain, road, city, gravel) and add the bike-type filter.
8. Bicycles: 3 774 products sit on the parent while Kids' (565 in the study), Mountain (321) and Road bikes are hidden (sg-4-4-3).
9. Sports Uniforms is one 4 376-product leaf (aa-1-24-7) although Arukereso splits football jerseys (3 347), combat wear (497) and kimonos (532); Soccer has no apparel node and sport clothing lives in three places.
10. Multi-sport knee, elbow and wrist pads (694) sit on the Sporting Goods root; add a Joint Protectors node.
11. Bicycle drivetrain: Arukereso 'Váltó' (2 286, derailleurs and shifters) sits on the parent while Derailleurs and other parts are hidden (sg-4-4-2-4).
12. Hockey Protective Gear: 765 of 768 products come from one jockstrap-named category that really holds pants, shin guards and elbow pads, which are hidden (sg-1-12-4).
13. Activewear (cross-branch): 9 296 products sit on the parent with Shorts, Leggings, Tights, Hoodies and Base Layers hidden although the study lists them in thousands (aa-1-1-1).
14. Hungarian name errors: 'Lókötők' (halters, means rogues), 'Hócipők' (snowshoes, means snow boots), 'Kerékpár-kormánycsapágyak' for stems, 'Kerékpárosfejhallgató-alkatrészek' for headset parts, literal lure names ('horgászfogók' for jigs); English Soccer becomes Football (Soccer).
15. Pickleball is hidden while 992 products sit on the Racket Sports parent in the study (13 of the 18 sampled are pickleball); padel shoes and grips show 0 products although the study has 76 padel shoes.

## Checked and fine, or already handled

- Padel, Floorball, Squash Strings, Racket Stringing Machines, Wall Bars, Pocket Knives, Equestrian jackets and body protectors, Cross-Country Ski Boots and Keepnets already have own nodes; Arukereso's remaining aru_narrower cases (Airbike, electric unicycle, golf shoes by gender, brake type, ski pole type) are attribute splits already covered by existing filters.
- No English node name in the branch uses 'paddle' for padel (Paddles & Oars, Paddleboards, Paddle Fins, Hand Paddles, Pickleball Paddles, Paddle Ball Sets are other products).
- Google's sport taxonomy is not finer than Shopify's in this branch; its Hungarian names were used as naming references (Lókötőfékek, Kerékpárkormányszárak, Hótalpak, Ágyékvédők).
- Study counts are shop listings summed over the 11 shops, not Arukereso counts. Findings marked with a knowledge line in their evidence (Hungarian angling terms, helmet and light splits, darts tip types, capacity and temperature filters) are not backed by these files.
