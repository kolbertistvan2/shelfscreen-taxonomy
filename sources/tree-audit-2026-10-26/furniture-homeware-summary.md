# Furniture & Homeware branch audit

Branch slug: furniture-homeware (1 518 nodes, 321 visible). Sources: Arukereso counts (2026-10-19), Shopify v2026-08 hidden nodes and attributes, Google taxonomy 2021-09-21. Findings are in furniture-homeware-findings.jsonl (138 lines).

## Counts per kind

| kind | findings | high | medium | low |
|---|---|---|---|---|
| hidden_node | 53 | 15 | 21 | 17 |
| missing_type | 12 | 2 | 3 | 7 |
| split_placement | 15 | 0 | 5 | 10 |
| undivided_leaf | 13 | 1 | 4 | 8 |
| filter | 32 | 8 | 17 | 7 |
| naming | 13 | 0 | 4 | 9 |
| total | 138 | 26 | 54 | 58 |

## The 15 most important findings

1. Lighting Fixtures (hg-13-9) holds 91 272 products on one node; show the hidden Ceiling Lights, Chandeliers, Pendant Lights (hg-13-9-2, -3, -5). Evidence: Arukereso Fali- és mennyezeti lámpa, csillár.
2. Drinkware (hg-11-10-5) holds 57 864 products (Bögre, csésze 51 816, Pohár 6 048); show Mugs, Cups and Saucers, Tumblers, Beer and Shot Glasses, Wine Glasses.
3. Bathroom Vanities (fr-4-14-1) holds 42 941 products (Fürdőszoba bútor 38 884); turn it into Bathroom Furniture with Bathroom Cabinets (fr-4-14-1-1) and Vanity Units, rename it.
4. Posters, Prints & Visual Artwork (hg-3-4-2) holds 61 828 products on the parent (Grafika, falikép 51 310, Festmény 10 518); show hidden Paintings (hg-3-4-2-4) and Prints (hg-3-4-2-2).
5. Light Bulbs (hg-13-7) holds 25 999 products; show LED, Halogen, Incandescent, Compact Fluorescent and add filters Bulb cap type (E27, E14, GU10), Bulb shape, Light temperature.
6. Mattresses (fr-2-6) holds 21 236 products in one Arukereso category; show Memory Foam, Latex, Innerspring, Hybrid, Foam; filters Firmness, Coil system type, Bedding size.
7. Duvet Covers (hg-15-1-5) holds 16 631 products that Arukereso calls Ágyneműhuzat (bed linen); show Bedding Sets (hg-15-1-11) and Pillowcases (hg-15-1-8), rename the HU name from Paplanhuzatok.
8. Lamps (hg-13-5) holds 15 484 products (Asztali lámpa); show Table Lamps (hg-13-5-5) and Bedside Lamps; Desk Lamps today holds only 40 nail-salon lamps.
9. Lighting (hg-13) holds 29 803 products on the parent (Kültéri lámpa 29 671); show Flood & Spot Lights, Landscape Pathway Lighting, In-Ground Lights, Track Lighting.
10. Cookware (hg-11-2-3) holds 10 714 products; show Frying Pans, Saucepans, Stock Pots, Pressure Cookers, Woks, Dutch Ovens, Cookware Sets; filters Compatible stove top type, Coating.
11. Beds & Bed Frames (fr-2-2) holds 10 603 products; show Bunk, Loft, Divan (boxspring), Trundle, Wall Beds; filters Bedding size, Bed storage type, Headboard style.
12. Towels (hg-15-4) holds 8 473 products on the parent while Bath Towels holds only 685 baby towels; show Hand Towels and Beach Towels, fix the mapping.
13. Window Blinds & Shades (hg-3-74-3) holds 7 881 products; Shopify keeps Roller, Day & Night, Roman, Venetian, Vertical, Pleated only as the attribute Blind/Shade style, so make them nodes (rolók, reluxák, plisszé, szalagfüggöny).
14. Kitchen Tools & Utensils (hg-11-8) holds 8 143 products on the parent with 57 hidden children; show Graters, Spatulas, Ladles, Whisks, Tongs, Cookie Cutters, Mixing Bowls and add Serving Utensils (Tálalóeszköz 1 583).
15. Shelving (fr-19) holds 5 783 products (Polc) on the parent; show Wall Shelves & Ledges (fr-19-2) and Heavy Duty & Utility Shelving (fr-19-3).

Also high: Conference & Visitor Chairs under Office Chairs (Tárgyalószék 3 743, missing_type), Disposable Cups and Plates (5 689), Rugs filters (12 234).

## Notes on the evidence

- Google's taxonomy adds nothing finer than Shopify in this branch: every Google category except 4 is already a target of Shopify's own mapping. The 4 not covered are Poker & Game Tables (google:2693), Sewing Machine Tables (google:5121), Coffee Filter Baskets and Food Grinder Accessories (the last two are appliance accessories, not in this audit). Google's Hungarian names are partly unnatural (for example Rögzített fényforrások for Lighting Fixtures), so they were not copied.
- Hungarian names given for hidden nodes are proposals; Shopify's Hungarian for hidden nodes is unreliable (hg-3-65 Trunks is "Csomagtartók", the car boot).
- Findings marked "knowledge" in the evidence are guesses from retail practice, not measured: boxspring, sliding-door wardrobes, sofa beds, puffs, headboards, table runners, LED panels and similar.
- Counters to check on the live page before use: Aprons 39 273 and Posters 39 084 are listed counts but only 24 and 26 products were sampled; the listed figures look high for one category each.
- The Arukereso mapping file is partly older than the own nodes: for example Műfenyő points to the hidden Artificial Trees (hg-3-2-4) although own-artificial-christmas-trees now exists; such categories were not reported as gaps.
