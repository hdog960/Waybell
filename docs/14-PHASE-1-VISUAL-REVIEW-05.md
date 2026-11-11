# WAYBELL — Phase 1 Visual Development Review 05
Date: 2026-11-11 | Starting verified main: `c868c632d0fb842d5bb2ed930d51ae3990e26440`
Status: **PHASE 1 ACTIVE — G1 OWNER APPROVAL PENDING — PHASE 2 NOT AUTHORIZED**
Canonical references: docs/00 charter, docs/02 characters, docs/06 art/audio, docs/08 roadmap, docs/13 prior review.

## Authorization and limits
User explicitly requested another **substantial Phase 1-only** visual pass following Review 04: canon-correct 3/4 exploration and combat in the same location, genuinely dry first-visit Rootbound Mill interiors and improved character directional/scale consistency. No game code, engine, deployment, real device tests or paid outside services. No Codex/Work/Vercel. The earlier separate request for an installable Pages preview has **not** been implemented by this Phase 1 visual-only slice. Do not claim an app, PWA or live website.

## Deliverables and concrete improvements
1. **New original exploration/combat diptych** (conversation art file `a_wide_cinematic_side_by_side_comparison_image.png`, preserved in review ZIP). The left and right panels keep the same village building, map of stairs, stone bridge, Waybell monument, vegetation and light direction. In the right panel, a small root/bark creature faces Tavi with a conspicuous triangular RED danger telegraph over the walkable cobbles. Tavi's signature teal cape, dark hair and lantern remain present in both. Stronger fixed-camera and scale consistency than Review 04's unrelated combat scenes. **This is a demonstration, not a canonical hostile NPC in Thimblebrook.**
2. **Two newly selected dry and stationary mill interiors** cropped from the *lower part* of generated concept board `a_detailed_high_quality_game_design_presentation.png`. They are `04_dry_lower_turbine_room_crop.png` and `05_dry_upper_spindle_room_crop.png` in the review pack: unmoving waterwheel, dry floor/channel and roots in the lower; suspended bridge/stair/rings and still machinery in the upper. Both now visually support the mandatory *first-entry before restoration* state. However, they are only ~600×320 concept crops, not fully composed or modeled final art. Any other boards that depict waterfalls in a supposed dormant mill remain **rejected**.
3. **Static phone-frame studies**: from each near-square split-panel, produced intentionally cropped 874×492 16:9 explor/combat stills plus a second version with translucent ~16% side thumb-zone annotations. This tests rough icon/character/puzzle visibility in a phone-sized bitmap and does not validate Safari, actual device size, usable space or performance. Cropping loses parts of the original art, confirming native 16:9 compositions still needed.
4. **Original editable vector cast-scale study committed directly to GitHub:** [design/phase1/cast-scale-guide-v1.svg](../design/phase1/cast-scale-guide-v1.svg) showing Tavi, Nella, Orin and Seren at a shared illustrated groundline, with clearly differentiated silhouette, age, costume colors, accessories and identity. This provides a repeatable design check for rigging, not measured canonical height or finished model. Tavi's prior eight-view sheet [design/phase1/tavi-eight-directions-v1.svg](../design/phase1/tavi-eight-directions-v1.svg) remains the directional reference, with the same costume invariants.
5. **Self-contained local image package** `WAYBELL_Phase1_Review05_Art_Studies.zip`, SHA-256 `f51f9ec4413b4d1c4229c00c9a7ef1b7fed4d7711be3a9cf02d782b3a4e3549d`, created in the current conversation/container. It contains both environment crops, source diptych, phone-scale static previews, prior Tavi 8-view illustration and a critical README. **The PNGs/ZIP are NOT stored in GitHub**. GitHub stores only original vector design source and textual critiques.

## Assessment: what passed and what is still open
| Design requirement | Evidence | Status |
|---|---|---|
| Consistent scene across exploration/combat | Same building, bridge, bell, lantern, ground plane in diptych | **Conceptually improved**; split panels almost square, not native landscape |
| Camera elevated 3/4, real depth | Layered scene composition | **Visual target demonstrated only**; true 3D camera cannot be proved by drawing |
| Tavi remains same recognizable hero | Dark tousled hair, teal cape, brass lantern in diptych | **Better**; actual eight-view anatomical/rig matching still unproven |
| Four primary character silhouettes | New original shared-floor vector and earlier individual portraits | **Guide established**, final proportions/turnarounds not approved |
| First-visit Rootbound Mill is dormant and dry | Two newly selected mill crops and existing dry-state SVG | **Improved**; missing standalone polished full-resolution interiors |
| Same-camera combat readability | Red telegraphed ground triangle, player dodge space | **Improved as concept**; 16:9 crop tight, right-thumb overlap risk untested |
| Waybell-specific motif | Bell/compass stone monument and teal/gold graphic language | **Consistent**; further distinctiveness possible |
| Mobile rendering/touch performance | No live implementation or user hardware test | **NOT TESTED** |
| Art gate G1 | Owner has approved general mood only | **NOT PASSED** |
| Phase 2 | Still locked | **NOT STARTED** |

## Explicit rejection notes
Several generated dashboards used a party RPG interface (Tavi, Nella and Orin as concurrent fighters), fabricated HP totals, invented menus or false percent-complete and GitHub commit identifiers. **These are rejected, not approved concepts or valid progress evidence.** No multiplayer/party UI is part of current WAYBELL canon. No generated image should be treated as a verified GitHub status report.
Other mill illustrations retain flowing water and are suitable **only for post-restoration** mood reference. No water or functional wheel on first entry.

## Visual implementation risks
- Illustrative asset fidelity is much greater than proven real-time 3D capability on free iPhone web delivery. There is **no evidence yet** that fully matching these illustrations at game scale is affordable.
- Native landscape world cameras need to prove correct path depth and 10–16% Tavi image height without hiding feet/doorways. Current diptych is almost square per panel, merely cropped for approximate phone check.
- Dynamic foreground fade, enemy telegraph timing, touch hitboxes, color-blind cue equivalence, rig continuity, actual lighting and optimization require an engine and must wait for owner-authorized Phase 2.
- Use the current concept images as an **aesthetic ceiling/reference**, not an asset inventory or completed visual implementation.

## Next concrete Phase 1 slice
1. Individually compose two **native 16:9** full-quality village exploration/combat images with matched lens, bearing, Tavi scale and location; ensure right thumb action areas do not overlap telegraphs.
2. Produce dedicated, high-resolution **dry Lower Turbine Hall and Upper Spindle Galleries** paintings that are not cropped from a montage. Explicitly reject spontaneous flowing water.
3. Refine Tavi eight-direction reference with body-length, clasp, satchel and lantern carry consistency; compare Nella/Orin/Seren same reference scale.
4. Add artifact accessibility/linking and produce single, concise owner review board only when art evidence is genuinely coherent; owner alone accepts G1.

## Verification plan and factual report
Connected GitHub commits, readback of review file, vector and updated ledger/README will be checked after creation; those are real evidence. The image ZIP has a local SHA-256 as given above. No browser/Chromium, WebGL, iPhone tests, Pages deployment, CI, animation or playable game were performed in this slice. No game code changed. Phase 2 remains explicitly forbidden until owner separately authorizes it following G1.
