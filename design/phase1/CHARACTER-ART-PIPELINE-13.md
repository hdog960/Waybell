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
