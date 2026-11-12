# WAYBELL — Tavi Eight-Direction Art Construction QA 19

**2026-11-11 | PHASE 1 ORIGINAL DESIGN only | G1 owner acceptance pending | Phase 2/code locked.**

## Evidence baseline and provenance
Starting GitHub main independently verified as `51ea0eb71d526a1385afcd3cd4e9a08841ae6312`. Following `docs/27-PHASE-1-VISUAL-REVIEW-18.md` and `design/phase1/CHARACTER-ANGLE-ACCEPTANCE-LEDGER-18.md`, seven independently generated Tavi studio paintings now exist as **preliminary painterly direction candidates**. The seventh is NEW BACK-LEFT 3/4 `a_highly_detailed_painterly_fantasy_character_ill.png` (1086×1448). The six PRIOR full-resolution paintings were copied byte-for-byte from prior evidence/individual source. Two FRONT-LEFT generation attempts were multi-character, multiple-angle promotional images with invented cast labels: **REJECTED**, not counted as independent art.

For the new source-controlled original two-view vector construction see [back-left vs front-left physical inventory art v11](tavi-back-left-front-left-physical-construction-v11.svg). Its right panel is a design schematic; it does not satisfy the missing eighth premium painting.

## True portrait-direction evidence
| Angle | Visual state | Physical-side QA |
|---|---|---|
| FRONT | PRIOR individual 1086×1448 concept | Right lantern picture-left, left satchel picture-right |
| RIGHT PROFILE | PRIOR individual concept | Right lantern near; left satchel partly occluded |
| BACK | PRIOR individual concept | Right lantern picture-right; left bag picture-left |
| LEFT PROFILE | PRIOR individual concept | Left satchel near; right lantern far |
| FRONT-RIGHT 3/4 | PRIOR individual concept | Right lantern near/front, left satchel on opposite hip |
| BACK-RIGHT 3/4 | PRIOR individual concept | Rear compass, right lantern near, left satchel far |
| **BACK-LEFT 3/4** | **NEW independent individual concept** | Rear compass, **left satchel near and picture-left**, **right lantern farther and picture-right** |
| FRONT-LEFT 3/4 | **OPEN, no independent premium painting** | Target: chest and face turned 45° left, left satchel nearer, right lantern farther |

**Actual count: 7/8 unique premium standalone painted concepts. Owner G1 approval count: 0.** Prior individual candidates are not production-ready rigs, and none of the generated composite images are accepted as individual standalone source.

## Observed cross-angle differences requiring correction before G1
1. **Compass topology:** FRONT/BACK and new BACK-LEFT vary in radius, star-spoke lengths, line density and how the Wayline roads branch from the compass. Canonical motif should be one 8-point compass on the rear garment with consistent star orientation and **recognizably the same route junctions**; do not invent a new map every angle.
2. **Cape cut:** The lower hem drops to different lengths and sides in independently painted views. Artist should register shoulder/collar seam, dominant long side of asymmetrical hem and cape fold breakpoints to the SAME physical body side through front/side/back/three-quarter turns.
3. **Map satchel:** Use one leather flap, two functional buckles, the same map-roll count/placement if visible, and one diagonal attachment strap. Keep the bag at physical LEFT hip without doubling or swapping attachments on east/west rotation.
4. **Echo Lantern:** One brass hanging lantern with one handle and amber glass core, in physical RIGHT hand. The hand/handle may be occluded by correct camera perspective, but not magically relocated to physical left or duplicated.
5. **Figure morphology:** Tousled brown hair and a youthful human face, one consistent head-to-torso ratio, same sleeve/cuff structure, belt-line and practical boot family. Some independently generated portraits have visibly different buckle counts and leg heights.
6. **Camera scale:** All original canvas sizes are **1086×1448**, but the *painted figure height* is not identical. Same source dimensions are NOT matched anatomical scale. Must normalize actual crown-to-sole height and ground contact before final eight-way assembly and mark any remaining deviations rather than hiding them by crop.
7. **Phone legibility:** Prior and new 874×492 static mockups show teal cloak, dark hair and lantern glow most clearly. Gold embroidery, map latch, eyes and smaller belt details generally disappear at 96–160px source **rectangle** heights. These are art-level source-image studies, not actual rendered hero pixel heights or iPhone hardware validation.

### Image-mask diagnostic, NOT a skeletal measurement
A simple dark-foreground mask `R<160, G<153, B<150` across central columns `120–965` of each 1086×1448 original measured approximate dark-feature vertical spans (includes clothing and hair; excludes light sleeves, accessories and floor shadow, and is **not a reliable full-body bounding box**):

| Angle | Dark-feature vertical span (source pixels) |
|---|---:|
| FRONT | 1300 |
| RIGHT PROFILE | 1382 |
| BACK | 1369 |
| LEFT PROFILE | 1385 |
| FRONT-RIGHT | 1408 |
| BACK-RIGHT | 1377 |
| BACK-LEFT | 1374 |

These are deliberately **diagnostic** rather than accepted production proportions, but flag up to ~8% image-scale variation across the independent paintings. The next artist should align the actual visible crown and boot-groundline manually before G1.

## Next individual premium painting specification — FRONT-LEFT ONLY
One studio full-body Tavi on **plain warm parchment without borders, lettering, panels, checklists, maps, companions or secondary poses**, native portrait format similar to 1086×1448. Face and chest turned about 45 degrees **toward picture-left**, both eyes plausible and shoulders clearly rotated, not a repeated left 90-degree profile. Satchel clearly anchored to physical LEFT, near viewer; glowing brass Echo Lantern carried in physical RIGHT hand on farther side; same tall collar clasp, hem, rear road-map embroidery, youthful human face, satchel flap and boots as existing six prior paintings and NEW back-left. Treat separately composed source art as required; **do not crop a character out of a review board**. If the generated image contains extra figures or fake status labels, reject and retain 7/8.

After one good FRONT-LEFT, make an actual person-height-aligned eight-way assembly and fix motif/hem and gear discrepancies rather than inferring that matching source dimensions prove perfect continuity. Give G1 packet to owner for inspection only when paint quality and physical consistency are genuinely mature; never auto-pass it.

## Cast remains open
**Nella:** impulsive quick-witted childhood friend; independent fate, not an invented healer/archivist/tinkerer class. **Orin:** elderly human grandfather, former surveyor. **Seren Vale:** human last High Bellkeeper with a credible but damaging Quieting plan. **No premium individual Nella/Orin/Seren portrait passed Review 19.**

## Provenance and excluded scope
`WAYBELL_Phase1_Review19_Visual_Evidence.zip` (SHA-256 `7e01a9a5043fa56182294eb2b90381546c407c2db4406d423d4dfdbd755a7b1c`) contains 14 files: seven ORIGINAL full-resolution portraits (six PRIOR, one NEW), comparison, rear-angle registration, new detail audit, 874×492 static portraits/16% thumb-band hypotheses, README, and SHA-256 JSON manifest. ZIP integrity verified. Raster evidence is in the conversation, **not committed as GitHub binary PNGs** through the text-write connector.

No game code, 3D model, rig, animation, actual hardware or PWA/Pages deployment, paid external service, Codex, Work or Vercel. G1 PENDING, Phase 2 LOCKED.
