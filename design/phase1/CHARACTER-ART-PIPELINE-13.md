# WAYBELL — Character Art Production & Consistency Protocol 13
**Date:** 2026-11-11 | **Status:** Phase 1 concept-only. G1 pending. Phase 2 locked.
Authority: docs/02 narrative canon, docs/06 art direction, design/phase1/TAVI-AND-CAST-VISUAL-CONTINUITY-10.md and docs/21 Review 12.

## The production problem discovered across Reviews 11–13
Requesting an entire cast's multiple directions in one image repeatedly yielded decorative, auto-labeled **promotional boards**, with off-canon invented roles (Orin as a warrior/forger, Seren as an elf mage, Nella as a party healer, etc.), unsupported checkmarks/commits and body/prop inconsistencies. Such generated boards must be REJECTED, not regarded as proof of production-ready turnarounds.

## New master — successful original standalone Tavi front painting
A true isolated high-quality painterly front-view Tavi was created in Review 13 as `a_richly_detailed_stylized_2.5d_3d_looking_painte.png` (1086 × 1448). It is included in the **conversation** Review 13 ZIP, not GitHub image bytes. Accepted *as a costume and style master*, NOT a finished model or G1 acceptance.

Observed invariants in the new master:
- Dark-brown tousled hair, warm curious face with freckles; eyes remain expressive but facial details will not read at wide camera scale.
- Unique unequal teal cloak with gold embroidered way/compass marks, one warm-brass collar clasp, parchment sleeves, layered leather vest and practical trouser/boot construction.
- Brass Echo Lantern in Tavi's *physical right hand* (screen LEFT in front view). One light source and one carry attachment.
- Leather satchel at Tavi's *physical left hip* (screen RIGHT in front view), diagonal strap, map tubes and hanging brass compass.
- The master is artistically polished but head-to-body ratio, exact cloak geometry, lantern/holster mechanics and handedness across other angles are **unproven**.

Source-controlled separate original **SVG** art matching master appearance and body-side logic: [Tavi costume master construction v5](tavi-costume-master-construction-v5.svg). It is an editable annotated vector **construction illustration**, not an exact re-render of the painted image or a 3D rig.

## Revised visual workflow — single-character, single-angle first
Do **not** request a four-character board or 'progress review' as the actual generation subject. For each new view:
1. Treat accepted Tavi FRONT portrait as reference image, not just its text description. Generate one clean full-body **RIGHT PROFILE** on neutral background, no typography, border, labels, scenes, party, or second person. Keep face, cloak fabric, satchel physical location and boots identical. Check perspective-specific hand placement and proportions against master.
2. Generate **BACK** as independent view using master + approved right profile; keep cape map pattern, clasp/shoulder seam, bag side, boot silhouette. An unseen lantern may be allowed if blocked by the body; it must not change physical hands.
3. Generate **LEFT PROFILE** (not a horizontal mirror of right-profile art); compare actual left hip satchel visibility and lantern on opposite image side.
4. Only after front/right/back/left match, create the four three-quarter views individually. Use the same subject body and clothing references, and reject each view with anatomical or handedness drift.
5. Crop and normalize all 8 artworks to a consistent baseline and apparent height; align torso, clavicle, boot top, facial age, head and hands before assembling a sheet. **The assembled sheet itself is a derivative, not a generation target.**
6. Evaluate both painterly 1:1 detail and phone-scale silhouette at 874×492, plus any wide-camera model height near 10–16% of frame as an exploratory standard, not a locked approval threshold.

## Cast: three individually controlled model pipelines
Create one FRONT master each first, compare its actual costume to docs/02, and generate right/back/left views only after accepting the master:
- **Nella:** copper-red hair, youthful energetic human explorer, leaf/olive green practical travel garments, quick body posture, compact pack. Avoid mage/healer/archivist/party-class inventions.
- **Orin:** visibly **elderly** human cartographer, grey-white beard/hair, spectacles, rolled maps/map tubes, warm brown wool layers. Avoid muscular armored warrior, smith, warden or fantasy dwarf proportions.
- **Seren Vale:** human dignified Bellkeeper, upright composed expression with compassionate sternness, navy and burgundy robes with restrained brass/bell accents. Avoid elf pointed ears, demonic armor, archmage, party fighter or extra invented attributes.

No final costume, physical height or race reinterpretation may be silently inferred from a generated board; the *narrative canon* has priority.

## Objective art QC gate for each view
| Check | What to inspect | Pass only if |
|---|---|---|
| Physical hand/side | Lantern and satchel across front/back/side | Same bodily side in every angle |
| Silhouette | Teal cloak and lower hem across angles | Same garment, recognizably unequal hem |
| Form | Head width, torso length, boots, hand reach | Changes consistent with rotation, not new proportions |
| Surface | Wayline embroidery, clasp, leather and stitching | Same marks, not arbitrary symbols replacing each other |
| Emotion/role | Neutral expression and known story role | No invented backstory, titles, party class or gear |
| Camera readability | 95, 125, 155 px hero-height static tests | Teal player identity visible and lantern/satchel reasonable at expected scale |
| Mobile | 874×492 static samples | No critical character/enemy cue depends on tiny text or face details |
| Honest status | Source record, resolution and user G1 | No pretend app screenshot, verified engine fidelity, or self-approval |

A failed view must be retaken individually. Artistic quality alone is not evidence of consistency. **Never mark eight-view, cast, iPhone tests or G1 complete unless independently verified.**

## Evidence generated in Review 13
- One original full-size Tavi painted front master and its detail crops.
- Three static shrink tests (95/125/155 px portrait height) in a 874×492 canvas; color/silhouette read best, tiny equipment/details degrade.
- The previously selected Thimblebrook pair and Rootbound Mill wide painting were copied as **PRIOR** references in ZIP, not newly generated this session.
- Multiple generated composite promotional sheets rejected and deliberately excluded.
- The master PNG is not a committed GitHub binary; the original SVG construction source and this protocol are committed and verifiable.

## G1 boundary
Tavi's seven additional premium painted angles, the twelve key supporting-cast views, action animation, physics, models and real device behavior **remain unfinished**. Final visual signoff belongs to the owner, and Phase 2 requires explicit separate authorization. No game code, Codex, Work, Vercel or outside paid service was used.

## Review 14 practical addendum — new RIGHT PROFILE candidate, back/left paintings remain open

The individual-angle method produced a genuinely new clean, standalone **1086×1448 right-profile Tavi painting** (`a_highly_detailed_stylized_illustration_on_a_warm.png`) with consistent costume and a right-hand lantern. This is **candidate view 2 of 8**, alongside the previous accepted front master. Full review: [Review 14](../../docs/23-PHASE-1-VISUAL-REVIEW-14.md).

Attempts to create independent back and left paintings still yielded promotional boards with invented character roles and false progress labels, which are rejected. Two new original, isolated **vector construction reference** files clarify the geometry without being misrepresented as finished painterly views:
- [Back orientation physical-sidedness v6](tavi-back-physical-side-construction-v6.svg)
- [Left-side physical-sidedness v6](tavi-left-profile-physical-side-construction-v6.svg)

Keep the next request scoped to **one image, one rear-facing full-body Tavi**. Use real front/right painted sources as images rather than describing a marketing review; require the same rear cloak embroidery and physical left bag/right lantern, neutral studio background, and no labels or decorative board. If the image becomes an infographic or model/cast chart, reject it even if individual figures are attractive. Do not use cropping from a poster as a surrogate for a standalone generated painting.

The complete [angle acceptance ledger 14](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-14.md) maintains truthful original-painted counts. No G1, Phase 2, actual animation, playable app or physical device test was achieved.

## Review 16 addendum — single-image LEFT PROFILE achieved; cardinal art references now complete as candidates

Using the earlier three painted sources as the fixed design intent, a **new genuine independent 1086×1448 Tavi LEFT PROFILE** was selected in Review 16. Its physical LEFT map satchel is nearer the viewer and physical RIGHT-hand Echo Lantern remains on the far side. There are now **four individual painted cardinal candidates (front, right, back, left)**, not a final eight-way production rig or G1 signoff. See [Review 16](../../docs/25-PHASE-1-VISUAL-REVIEW-16.md) and [Ledger 16](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-16.md).

**New original source-controlled cardinals QA art:** [Tavi four-cardinal gear and seam reference v8](tavi-four-cardinal-gear-and-seam-reference-v8.svg). Study physical bag/lantern placement and left/right screen mapping before producing diagonals. The actual painted gold route embroidery and proportions are broadly similar but not identical. Do not interpret this SVG as a photorealistic source painting or a game model.

Further attempts at a diagonal and at Nella returned additional LEFT Tavi paintings instead. Only the **first independently accepted left profile** counts in this release. Do not count alternative poses as diagonal/cast art. The next generated artwork must be one 45-degree **front-right diagonal**, not a profile, montage, or cast lineup; reject subject/facing failure with no ledger advancement. Maintain narrative canon for Nella, Orin and Seren.

No game code, runtime camera, physical iPhone tests or Phase 2 were conducted. G1 remains pending owner approval.

## Review 17 addendum — actual FRONT-RIGHT 45° painting exists; next attempt must be BACK-RIGHT

The one-at-a-time generation method produced a real single-image **1086×1448 premium FRONT-RIGHT 3/4** Tavi candidate, visually distinct from both FRONT and RIGHT cardinal paintings. See [Review 17](../../docs/26-PHASE-1-VISUAL-REVIEW-17.md), [Ledger 17](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-17.md) and [new original four-diagonal gear source](tavi-diagonal-physical-gear-visual-contract-v9.svg). There are now **5/8** preliminary individual painted Tavi views. This count does not grant G1 approval and does not prove a real rig.

A subsequent BACK-RIGHT request produced a multi-character promotional board containing small angle panels and cast members; a Nella request produced a Tavi report board. **Both rejected.** Their role labels, extra character artwork and on-image status are not verified source.

**Next standalone direction contract — BACK-RIGHT / NE:**
- Single Tavi only, neutral warm studio parchment; entirely full-body visible, one uninterrupted native portrait; absolutely no decorative board, collage, text, inset, cast lineup or UI.
- Figure rotates **away** from viewer approximately 45 degrees, showing clearly the dorsal teal cape compass map, the back of the head and a partial physical-right facial cheek/profile. Do not show both eyes or a front chest panel prominently.
- Physical RIGHT hand holds brass Echo Lantern on the nearer right side; physical LEFT hip map satchel stays left, possibly more occluded. Head/body, boots and clasp all match previous independent source portraits.
- Reject any right-profile, front-right, or generic rear pose. Require a distinct three-quarter back silhouette.
- Once independently accepted, proceed to BACK-LEFT (bag nearer, lantern farther) and then FRONT-LEFT (chest + physical left nearer), each separate call and full-size source.
- Inspect normalized *painted person height*, braid/compass embroidery and gold road-node topology before assemblage. Never infer true 3D geometric continuity from image similarity.

**Supporting cast:** Nella must be her own one-person studio FRONT portrait: Tavi's quick-witted human childhood friend with copper-red hair and a practical explorer wardrobe, not an automatically equipped party-class. Orin must appear as Tavi's elderly human grandfather, and Seren as the human last High Bellkeeper. Never let an image generator override docs/02.

No game code, animation, tested PWA or iPhone hardware work is authorized. G1 stays owner-pending and Phase 2 locked.

## Review 18 addendum — real BACK-RIGHT painting completed; reject fake eight-view claims

NEW independent full-size `a_highly_detailed_fantasy_character_illustration_o.png` from Review 18 is **Tavi BACK-RIGHT 3/4**, one person only: rear Wayline compass, partial RIGHT cheek, near physical RIGHT-hand lantern, far physical LEFT satchel. It is a preliminary *painted concept candidate*, not an animated character or G1-approved asset. Total verified independent premium Tavi paintings: **6 of 8**. See [Review 18](../../docs/27-PHASE-1-VISUAL-REVIEW-18.md), [Ledger 18](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-18.md) and [new original rear-right gear registration illustration](tavi-back-right-cloak-and-gear-registration-v10.svg).

BACK-LEFT generations during this slice returned two multi-character/multi-angle artwork boards; one even claimed “8-direction complete,” though **BACK-LEFT and FRONT-LEFT remain OPEN**. Do NOT crop these figures, copy generated checkmarks, assert new Nella/Orin/Seren portraits, or retroactively lock costume seams. The only new standalone painted picture accepted this slice is BACK-RIGHT.

### Next two studio requests (one per call, no shared board)
- **BACK-LEFT**: Tavi turned AWAY ~45° toward picture-left. Character's back and the physical LEFT cheek/shoulder contour visible. Compass embroidered on back; near-side physical-LEFT map satchel; far-side RIGHT-hand brass Echo Lantern. No front chest or both eyes, no text/frames/labels/multiple angles. Maintain identical hair, right/left shoulder height, cape hem and boots.
- **FRONT-LEFT**: Tavi turned TOWARD camera ~45° to picture-left, showing face and chest, near physical-LEFT satchel and far physical-RIGHT lantern. One full-body human on neutral warm parchment only. Never horizontally mirror the existing front-right portrait and thereby invert actual equipment sides.
- Both must be original full-resolution individual images, subject to close-up and 874×492 static legibility QA. At completion compare the **actual figure** height/groundline plus gold route-map topology across all eight; same canvas dimensions alone do not prove a rig.

No game code, physical iPhone validation, 3D engine or owner G1 approval. Phase 2 remains locked.
