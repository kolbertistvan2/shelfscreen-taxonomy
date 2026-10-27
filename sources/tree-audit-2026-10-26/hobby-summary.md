# Hobby branch audit summary (slug: hobby)

Audit date 2026-10-26. Inputs: hobby-nodes.jsonl (2532 nodes, 529 visible), hobby-arukereso.jsonl (574 rows), arukereso-none.jsonl, the full tree, shopify-attributes.jsonl, google-en.txt, google-hu.txt, shopify-to-google.txt. Nothing outside the two output files was changed.

## Counts per kind

| kind | findings |
|---|---|
| hidden_node | 73 |
| missing_type | 20 |
| split_placement | 9 |
| undivided_leaf | 8 |
| filter | 67 |
| naming | 20 |
| total | 197 |

Priority: high 48, medium 71, low 78.

## The 15 most important findings

1. Sex Toys & Erotic Games (ma-1-4) holds 43715 products with no child; Arukereso splits it into vibrators 7029, masturbators 7469, cock rings 5121, anal toys, dildos 2347, strap-ons, pumps and more, plus a bondage gear group of about 8450.
2. Pet Supplies (ap-2): collars, leashes, beds, apparel, carriers and bowls sit by product type while Arukereso splits them by animal; keep one home per type, make Animal type the first filter, and link from Dog Supplies and Cat Supplies (Google splits beds and apparel by species).
3. Dog Food (32779) and Cat Food (26073) are single blocks with only empty prescription children; add dry / wet / veterinary diet and the pet-food filters (form, age group, diet), which the tree lacks entirely.
4. Play Vehicles (tg-5-15, 18490) and Remote Control Toys (tg-5-18, 10276) show no Toy Cars, Trucks, Helicopters, Planes or Boats although Shopify has them hidden; Arukereso 'Játékautó és jármű' 13585 and Hot Wheels 4905 are toy cars.
5. Interlocking Blocks (tg-5-7-12, 26755): 22387 are LEGO spare parts and minifigures against 4368 sets; add Sets and Loose Bricks, Parts & Minifigures (the reject list used the 1016 listed products, the counter says 22387).
6. String Instrument Accessories (ae-2-7-13) keeps 14269 products on the parent: strings 10411 and cases 3858; show Guitar Strings, Orchestral Strings, Guitar Cases and Orchestral Cases; pickups 3429 also need their hidden nodes.
7. Filing & Organization (os-3) keeps 40596 products on the parent (lever arch files, ring binders, folders); Binders, File Folders, Folders & Report Covers and Portfolios are hidden.
8. Office Equipment (os-10) keeps 13485 products from 'Irodai gépek kiegészítői' with no matching node; inspect the products, then add types.
9. The Hobbies & Creative Arts root holds 12003 products ('Gyöngy, ásvány'); show Beads (ae-2-1-2-8-2) and Gemstones (ae-2-2-6-2) and split the category.
10. Art & Craft Paint (7506) divides into acrylic 4779, tempera 1139, airbrush 820, watercolor 488, glass 280; Art Brushes and Palette Knives (2640 products) are hidden deep under Craft Measuring and Color Mixing tools.
11. Erotic Clothing (ma-1-1, 25248) has no child; Arukereso divides it by garment: lingerie sets 4596, dresses 3624, panties 3078, men's underwear 2787, catsuits 2244, bodies 2187, stockings 2150.
12. Collectible Trading Cards (ae-2-2-3, 20127) hides Gaming, Sports and Non-Sports card nodes; the same Pokémon/Magic goods also fit Card Games (3080), so one home is needed.
13. Music CDs (263918) and Records & LPs (170781) have no child and no filter; add the Music genre filter first.
14. Video games: Physical Video Games (9245) splits by console in Arukereso (Switch 2188, PS5 1933, PS4 1826, Xbox One 1694) and 19722 PC titles sit on the parent while Digital Video Games stays hidden.
15. Books are missing: only Audiobooks (7423) show; Print Books and E-Books are hidden because Arukereso has no book category in these files (scope decision, shop practice is a guess).

## Notes on method

- Product counts: hobby-arukereso.jsonl 'products' differs from the counts inside hobby-nodes.jsonl for 557 of 574 rows (for example 'Kutyatáp' 7028 against 32779). Findings use the node counts and say 'Arukereso' for the category they come from.
- The nodes file also contains nodes from other branches that map into this slug (vehicles, home and garden, hardware, electronics, business): they were checked only where they belong to a hobby area (seasonal decorations, lighters, drones, aquatic plants, photo albums, signage).
- Google Shopping 2021-09-21 is finer than Shopify in this branch in only a few places: species-split beds and apparel (ids 4434, 4433, 5004, 5082), Pet Playpens (5087), Beer Pong, Wedding Favors (5453), Toy Train and Race Car Accessories (5153, 5971), Kite Accessories. Used as evidence where relevant.
- Findings marked "evidence": "knowledge" (8 of them) rest on shop practice, not on a file; the same uncertainty is written as 'guess' inside other proposals.
