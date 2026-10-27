# Care Products branch: tree gap audit (slug care-products)

Branch: 1152 nodes in the nodes file (283 visible in Hungary), 273 mapped Arukereso categories (181 same, 42 aru_narrower, 34 aru_broader, 16 none).
All Arukereso counts are the "N termék" counters listed on 2026-10-19. Parts that are my own guess about Hungarian shops (no evidence in the
files) are marked "guess" inside the proposal text of the findings.

## Counts

| kind | findings |
|---|---|
| hidden_node | 45 |
| missing_type | 5 |
| split_placement | 10 |
| undivided_leaf | 3 |
| filter | 22 |
| naming | 8 |
| total | 93 (26 high, 39 medium, 28 low) |

Findings file: care-products-findings.jsonl (same folder).

## The 15 most important findings

1. Vitamins & Supplements (hb-1-9-6) holds 32652 products on one node and Shopify's eight children (single vitamins, multivitamin, minerals, omega, collagen, digestive, sleep, CBD) are hidden; show them and add health focus and form filters.
2. Hair Color (hb-3-10-2) is a 24195-product leaf with no children and no filter; Shopify's formulation values (permanent, semi-permanent, lightener, developer, root touch-up) say how to divide it.
3. Gel nail polish has 14858 Arukereso products against 5041 for ordinary polish, but both sit on Nail Polishes (19899) with a "Gel" filter value; it needs its own node (operator decides category or filter).
4. Perfumes (hb-3-2-8, 30501 products) carry the concentration split (EDP, EDT, EDC, extrait) as an own filter while Shopify's matching categories are hidden; use one mechanism, and decide homes for samples, testers and sets.
5. Supports & Braces (hb-1-24, 10992 products) has 11 hidden body-part children (knee, ankle, wrist, back ...) and a duplicate "Body area" filter with only 7 values.
6. Hair Care (hb-3-10) holds 8609 products itself because Hair Masks, Hair Oils and Hair Serums are hidden; only Conditioners (1306) are visible.
7. Household Cleaning Supplies (hg-10-6) holds 8723 products itself; brooms, dustpans, mop heads and handles, brushes, dusters, gloves and squeegees are all hidden, only mops and buckets show.
8. Household Cleaning Products (hg-10-6-11) holds 5963 products itself; disinfectants, all-purpose, bathroom, oven, furniture and stainless steel cleaners are hidden, as are rinse aids and washing machine cleaners.
9. Medical Tape & Bandages (hb-1-8-6, 6520 products) hides plasters, gauze and dressings, compression and cohesive bandages; only kinesiology tape is split out.
10. Foundations & Concealers (hb-3-2-6-4-4) holds 7154 products while the sibling Concealers (2602) is visible and Foundations, BB and CC creams, color correctors are hidden.
11. Health Care root (hb-1) holds a 12087-product mixed bag; Incontinence Aids, Blood Pressure Monitors, Blood Glucose Meters, Oxygen Concentrators, masks and gloves are hidden.
12. Facial Cleansers (hb-3-2-9-6, 7483 products) also holds micellar water and toners per the Arukereso note; Makeup Removers and Toners & Astringents are hidden, and the node has no Cleanser type filter.
13. Gift sets and kits live in about eight places (Gift Sets 7058, Makeup Kits 321, plus hidden Cosmetic Sets, Bath & Body Gift Sets, skin care, hair care, shaving and lip kits); propose one home under hb-3-20 split by content, with links.
14. Bath & Body (hb-3-2-1) holds 6296 products where Arukereso pairs bar soap with liquid soap; Bar Soap, Liquid Hand Soap and Bath Bombs are hidden.
15. Hair Styling Products (hb-3-10-10) holds 5494 products and only Hair Mousses is split out; hair sprays, gels, pomades and waxes, creams and powders are hidden.

Also worth a decision soon: baby toiletries (1237 Arukereso products) are spread over adult nodes and a Baby & Toddler shopper finds none of them (split_placement, touches the rule that age is a filter); Personal Care root holds 2927 appliance accessory products with three competing homes; Massage & Relaxation (2658) hides Massage Creams.

## Decisions the operator has to take (they recur across findings)

- Category or filter for the same split: perfume concentration, supports by body part, bar versus liquid soap, anti-aging and acne, contact lens schedule. The tree currently often has the filter while Shopify's categories sit hidden; use one, not both.
- Shopify's Hungarian names for hidden nodes are unreliable (several wrong, see the naming finding); every node opened needs a reviewed Hungarian name. The "paddle" word appears in one hidden Shopify name (Paddle Hairbrushes).
- Google Shopping (2021-09-21) is not finer than our tree anywhere in this branch (it is a subset of Shopify); it was used only for ids and Hungarian name reference.
