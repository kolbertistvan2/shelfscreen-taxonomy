# Electronics branch audit: summary

Branch: the e-commerce category Electronics (2,070 nodes: 497 tagged Electronics plus 1,573 untagged descendants; it covers Shopify Electronics with 248 visible nodes, Cameras & Optics with 48, and household appliances, personal care devices and baby devices that carry the Electronics category).
Sources: electronics-nodes.jsonl, electronics-arukereso.jsonl (476 categories: 320 same, 76 aru_narrower, 58 aru_broader, 22 none), arukereso-none.jsonl, shopify-attributes.jsonl, Google 2021-09-21 (English and Hungarian), tree.jsonl. Findings file: electronics-findings.jsonl (130 findings).

## Counts per kind

| Kind | Findings |
| --- | --- |
| hidden_node | 53 |
| filter | 37 |
| naming | 17 |
| split_placement | 10 |
| undivided_leaf | 8 |
| missing_type | 5 |
| Total | 130 |

By priority: 27 high, 63 medium, 40 low.

## The 15 most important findings

1. Mobile Phone Cases (el-4-8-4-2) is one block of 725,796 products; shoppers pick by phone model first, so add filters (compatible device, case type, material, MagSafe, wallet) instead of nodes, and show the hidden Battery Phone Cases.
2. Mobile Phone Replacement Parts (el-4-8-4-5) holds 82,661 products on the parent while ten Shopify children (screens, housings, charging ports, camera parts, speakers, logic boards) are hidden.
3. Mobile Phone Screen Protectors (el-4-8-4-12) is one block of 91,857 with no children; add type and compatibility filters, and give screen protectors one home (phone, tablet, camera and smartwatch protectors sit under two parents).
4. Toner & Inkjet Cartridges (el-13-3-1-7) is one block of 64,231; shops divide it into toner, ink cartridges and refill kits (Google keeps refills separate, google:7362).
5. Desktop Computers shows 421,933 and Laptops 86,850 products, but 420,036 and 82,640 of them come from the Arukereso "Egyedi ... konfiguráció" (custom configuration) categories; this looks like configurator variants, so the operator should decide whether they count as products.
6. Computers shows only Desktop and Laptops; Gaming Computers (gaming desktops and laptops), All-in-One and Barebone are hidden, and the laptop and desktop nodes have no filters (OS, processor, graphics, display, keyboard layout).
7. Audio & Video Cables (26,946; HDMI, DisplayPort, VGA, XLR, instrument all hidden) and Network Cables (28,499; Ethernet, coaxial, fiber hidden) are single blocks.
8. Headphones & Headsets holds 8,260 products on the parent; the visible In-Ear Headphones node contains only 365 in-ear monitors, while over-ear, on-ear and Gaming Headsets (551) are hidden.
9. Power Adapters & Chargers holds 11,191 phone chargers with Wall Chargers and Wireless Chargers hidden, and Remote Controls holds 10,358 with TV, universal and air-conditioner remotes hidden.
10. Computer Components holds 25,227 products from three residual buckets: USB hubs and card readers (4,256, both hidden) and laptop parts (17,066 residual, Laptop Parts shows only housings).
11. General Purpose Batteries (21,967) needs size and chemistry filters (AA, AAA, 9V, alkaline, NiMH), and Lens Filters (12,424) needs the Shopify attribute Lens filter type (UV, ND, polarizer).
12. Camera Bags & Cases (6,648; backpacks, shoulder, hard cases hidden), Digital Cameras (926; DSLR, mirrorless, compact hidden) and Optics (1,711 binoculars and monoculars on the parent; Binoculars, Monoculars, Rangefinders hidden).
13. Kitchen Appliances hides Air Fryers (1,122 products of "Olajsütő, forrólevegős sütő" sit on the parent; the visible Deep Fryers node holds only 109 commercial ones), and Humidifiers are hidden while Air Purifiers shows only 60 ozone generators (601 products on the parent).
14. Bridges & Routers holds 1,259 products with Wireless Routers, Mesh WiFi and Cellular Routers hidden; Televisions (1,239), Mobile & Smart Phones (997) and Monitors (3,234, only a POS filter) lack the filters shoppers use.
15. Eight residual Arukereso buckets ("Egyéb ...", "... kiegészítői") put about 120,000 products on parent nodes (Household Appliance Accessories 30,588, Printer accessories 24,013, Computer Components 17,066 residual, Kitchen Appliance Accessories 14,632, Audio Accessories 13,433, Electronics Accessories 11,833, Camera Parts 4,462, Mobile Phone Accessories 3,937); showing their hidden children only helps if products are read and sorted into them, because Arukereso does not divide them.

## Notes for the operator

- The tree already turned many aru_narrower rows into own nodes or filters (for example Studio Lights type, General batteries usage, HDD/SSD installation, Printer print technology, Vacuum and Fan type, Console type, Espresso automation, Smart Rings, PA Speakers, Window cleaning robots). I did not report those again; where a filter replaces hidden Shopify nodes (printers, vacuums, fans, consoles) I left the decision as it is.
- Google's taxonomy is no finer than Shopify's here: only 11 Google categories in this branch have no Shopify counterpart (CD, cassette, MP3 and MiniDisc players, contract, pre-paid and unlocked phones, CD/DVD duplicators, floppy drives, DVD recorders). Google contributed one finding (toner refills) and Hungarian name checks.
- Many Hungarian names of hidden Shopify nodes are literal machine translations (for example "Kiemelt telefonok", "Mutass és rögzíts digitális fényképezőgépek", "Lassú tűzhelyek"); the naming findings list the ones to fix before those nodes are shown.
- Electronics-type products assigned to other e-commerce categories (surveillance cameras 6,129, drone accessories 4,090, smart relays 1,897, door intercoms 2,267 and others) are listed in one split_placement finding on el for the operator to confirm.
- Findings marked "knowledge" in evidence (naming of unseen nodes) and statements marked "guess" are not backed by the files.
