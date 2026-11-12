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

## Review 19 addendum — genuine BACK-LEFT achieved; the only remaining Tavi painted view is FRONT-LEFT

A single full-size 1086×1448 original **BACK-LEFT three-quarter** Tavi studio painting has passed preliminary Phase 1 visual acceptance: one turned-away Tavi, dorsal compass, near physical LEFT map satchel, farther physical RIGHT-hand Echo Lantern. It is documented in [Review 19](../../docs/28-PHASE-1-VISUAL-REVIEW-19.md), [Ledger 19](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-19.md), and [the new original back-left vs front-left vector construction artwork](tavi-back-left-front-left-physical-construction-v11.svg). Total **7/8** unique individual painterly Tavi directions, NOT a production rig or owner G1 approval.

**The only eighth angle still OPEN is FRONT-LEFT 3/4.** Two actual attempted outputs became multi-character/multi-angle poster boards with invented cast roles and turnaround status graphics; both REJECTED. Do not crop a small FRONT-LEFT figure from either presentation board and call it an independent full-resolution painting. No genuine Nella, Orin or Seren original studio portrait was made this session.

**Next painting request, one clean person only:** a freckled young human Tavi facing camera from FRONT-LEFT 45°, both face and chest in view and clearly rotated away from 90° LEFT profile, left-hip map satchel near viewer, glowing right-hand brass Echo Lantern on the far side; gold Wayline embroidered asymmetric teal cloak, exact boots and physical attachment continuity. Neutral parchment setting, no letters, labels, progress bars, panels, extra figures, decorative borders or lineups. Reject subject and angle drift, including a repeated BACK-LEFT or unchanged LEFT profile. Do not generate a combined eight-view board as a substitute.

After the eighth single-view painting exists, normalize **actual character (hair-to-boot) height** and groundline before comparing costume/map motif. Use [QA contract 19](TAVI-CROSS-ANGLE-CONSTRUCTION-QA-19.md), which documents approximate foreground span differences, shared physical sides, fixed satchel/lantern and rear gold-compass topology. Mark the entire eight-view set visually coherent only when genuine differences are corrected. Then individually attempt **canonical Nella FRONT**, Orin elderly-human grandfather FRONT, Seren human High Bellkeeper FRONT; no invented class or role labels.

**No executable game, real iPhone test, engine/model, G1 owner approval or Phase 2.**

## Review 20 addendum — eight independent painted directions now exist, next focus true source-art consistency and standalone cast

NEW individual 1086×1448 full-body **FRONT-LEFT three-quarter** portrait `a_highly_detailed_fantasy_character_portrait_on_a.png` passed preliminary direction selection in [Review 20](../../docs/29-PHASE-1-VISUAL-REVIEW-20.md), completing **eight out of eight independently painted angle CONCEPT CANDIDATES**, alongside seven prior original paintings preserved byte-for-byte. This count is verified by [Angle Acceptance Ledger 20](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-20.md) and the current **17-file conversation ZIP**, but **does not** confer owner G1 approval or production asset readiness. The full-size PNGs live in the conversation packet, not the GitHub binary tree.

The new painting has correct general inventory ownership: physical LEFT-hip map satchel (closer to camera), physical RIGHT-hand brass lantern (farther side). It also has materially more gold filigree, satchel ornamental hardware, taller heavily strapped boots and a more mature/tall appearance than several earlier original images. All eight have broadly consistent silhouette/identity; none are an actual shared 3D model or perfectly matched production turn. The source-controlled [original master garment and physical inventory art v12](tavi-master-garment-and-eight-view-identity-v12.svg) defines a repeatable single compass design, one two-buckle satchel, physical right lantern, cloak asymmetry, boots and palette. It is design art, not a repaint.

**New priority, phase1 ONLY:** Refine existing individual paintings using original images as visual references, *one angle at a time*, beginning with FRONT-LEFT relative to FRONT/LEFT/FRONT-RIGHT, then rear compass and boots. Check real drawn hair/boot height, coat seam/hem, map-route branch topology, satchel strap and physical hand/grip; reject posters and count only actual modified full-size standalone paintings. The prior quick dark-foreground 8-view normalized-crop diagnostic should not be passed off as a production rig.

A genuine single-character **Nella FRONT** was requested during Review 20, but the output was a labeled Tavi turnaround board with cast snippets. Rejected; supporting-cast progress remains zero new premium originals. Try Nella again as a clean single body with youth, copper hair and practical traveling gear, no automatically assigned fantasy class or invented role; then elderly-human grandfather Orin and human last High Bellkeeper Seren as separate masters. Never crop figures from a multi-character panel. Honor [narrative canon](../../docs/02-NARRATIVE-AND-CHARACTERS.md).

**Boundary:** G1 final art approval pending; Phase 2/game code, running game, 3D engine, physical iPhone QA, PWA, Codex, Work, Vercel and outside paid services remain unstarted or prohibited.

## Review 21 addendum — new genuine front-left variant; no fake eight-way correction or cast masters

New **1024×1536 full-body standalone Tavi FRONT-LEFT** revised painting is accepted as *one alternative* to the prior 1086×1448 FRONT-LEFT. It simplifies gold wayline embroidery, satchel two-buckle closures and boot details and preserves physical LEFT hip / RIGHT hand. See [Review 21](../../docs/30-PHASE-1-VISUAL-REVIEW-21.md), [Ledger21](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-21.md) and the original [single-figure front-left garment v13 SVG](tavi-front-left-costume-registration-v13.svg). The previous eight original images remain unchanged and source-provenanced in the validated ZIP. **Do not increment direction coverage to nine or claim the seven other views have been repainted**. Exact cloth topology and body scale still differ.

An attempted standalone Nella painting again produced a **Tavi multi-angle promotional board with attached cast captions**; it is not evidence of any usable Nella master. The new [single-person supporting cast contract 21](SUPPORTING-CAST-SINGLE-PORTRAIT-CONTRACT-21.md) specifies separate Nella/Orin/Seren role- and pose-correct native-size source paintings, their rejection criteria and phone-scale illustration QA.

Next Phase 1 effort should **actually redraw and compare individual original angles**, one view at a time, prioritizing front/left/front-left garment consistency then rear compass and equipment. A diagnostic collage/height overlay is not a correction to the original paintings, and a generated board cannot overwrite narrative canon. G1 still owner-pending; Phase 2, all game code and real device testing locked.

## Review 22 addendum — real FRONT candidate, preserve younger identity, prevent multi-character image drift

The **only new accepted premium painting** is a genuine 1024×1536 individual **straight-FRONT Tavi alternative** at [Review22](../../docs/31-PHASE-1-VISUAL-REVIEW-22.md) and [Ledger22](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-22.md). New FRONT has clearer physical LEFT two-buckle satchel, physical RIGHT lantern and restrained Wayline route map; however it appears **older and more photorealistic** than the young-faced original FRONT and is NOT final canon until age/figure/costume consistency is settled. The prior original FRONT, all other seven original angles and the prior FRONT-LEFT alternative are unaltered and separately in Review22 ZIP. Do not call them corrected by the presence of a comparison board.

Three other image outputs were **rejected**: Nella request yielded labeled Tavi eight-way + cast board; independent Nella retry yielded a three-person Tavi/Nella/Orin illustration; Tavi RIGHT correction yielded a fake development-review infographic. **None is a valid native standalone corrected portrait or cast master.** Never trust on-image release versions, GitHub commits, progress checks or user-approval claims.

Original source-controlled construction art created this session:
- [Straight-FRONT Tavi body/gear registration v14](tavi-front-registration-v14.svg): one actual illustrated vector, physical-right hand and left-hip bag.
- [Single human Nella front construction v1](nella-front-construction-v1.svg): one original copper-haired olive-travel-clothed human, **vector study only**, NOT premium painterly acceptance.

For future premium individual generation, avoid mentioning “Review”, “WAYBELL visual packet”, “8 angles”, “GitHub progress”, or other characters in the image brief; place only one desired actor, native portrait, camera direction, neutral backdrop, exact physical equipment and no typography. If a board is produced, reject; do not crop/enlarge its character as a surrogate. To reconcile Tavi, prefer original FRONT + chosen youthful age standard + v12/v13/v14 physical ownership, then independently correct RIGHT, LEFT and rear; compare person-height/motif manually and **do not mark production rigged**. For cast, use [solo-character contract 21](SUPPORTING-CAST-SINGLE-PORTRAIT-CONTRACT-21.md), with Nella from the single-person SVG as a *visual proposal*, not a role-changing authority. G1 stays user-pending. Phase 2/game code stays locked.

## Review 23 addendum — real independent RIGHT profile alternative, LEFT and Nella still OPEN

One **new 1024×1536 genuine individual Tavi RIGHT-facing studio painting** passed one-figure/orientation QA, [Review 23](../../docs/32-PHASE-1-VISUAL-REVIEW-23.md), [Ledger 23](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-23.md). The eight original 1086×1448 paintings and existing FRONT / FRONT-LEFT alternates were copied byte-for-byte unchanged; the RIGHT is **a third alternative**, not a ninth direction or a final correction to the original. Compare old/new source in the review packet; its face is older-looking and **physical LEFT-hip satchel is too visible on the expected far side**. New original edited-source [right-profile physical-side registration v15](tavi-right-profile-physical-side-registration-v15.svg) shows more credible partly occluded bag placement; do not mistake this vector construction for a repainted original or functional 3D model.

**Three rejected outputs**: TWO attempted standalone LEFT profile generations yielded labeled multi-view Tavi/Nella sheets; ONE Nella request yielded another labeled Tavi/Nella group sheet. These are NOT native individual left-profile paintings, supporting cast masters, fixed costumes, photo/phone evidence, GitHub verification or visual G1 approval. Do not crop them to claim progress.

The right-profile redesign target remains right hand and lantern in near side, physical LEFT map satchel mostly on far side (partly hidden), one 8-point rear compass/map and identical boots, cloak and youthful head/face across angles. **Next one-figure premium painting request** is only left-facing Tavi alone, no project branding, no call for panels/compare, single plain studio background, near physical-left two-buckle satchel and far physical-right amber lantern. If it fails, reject, retain existing left art, and continue source-controlled garment research. For **Nella**, likewise one *human young traveler alone*, copper-red hair, olive practical clothing without a Wayline teal cloak or Echo Lantern, as in [solo cast contract](SUPPORTING-CAST-SINGLE-PORTRAIT-CONTRACT-21.md); no Tavi or labels.

Still **8 distinct original Tavi concept directions, plus 3 stand-alone alternatives** (FRONT, FRONT-LEFT, RIGHT). New accepted premium solo cast count ZERO. All actual gameplay and Phase2 remain locked. Owner G1 final approval remains pending.

## Review 24 addendum — genuinely standalone LEFT painting, now 8 originals + 4 alternatives

Review 24 produced ONE native **1086×1448 genuine standalone left-facing Tavi** studio painting with youthful brown curly hair, near physical LEFT-hip two-buckle map satchel and far physical RIGHT-hand amber lantern. No panels, captions or extra cast. See [Review 24](../../docs/33-PHASE-1-VISUAL-REVIEW-24.md), [Ledger 24](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-24.md), and the original [left-profile gear/Wayline registration v16](tavi-left-profile-gear-and-wayline-registration-v16.svg). It is a **fourth alternative** (FRONT, FRONT-LEFT, RIGHT, LEFT), not a ninth direction or an automatic correction of the previous original left pixels. All eight original direction paintings and three prior alternatives remain unchanged in the hash-verified downloadable Review24 ZIP.

The new LEFT painting is visually nearer the youthful standard and has stronger 2-buckle bag/lantern side cues than the right-profile alternative. Still reconcile the exact gold route/compass topology, asymmetric cloak hem, boots and model geometry; a 2D painting does not prove wrist/hand attachment in animation.

Two requests for a **single Nella FRONT** yielded attractive three-character Tavi/Nella boards, NOT a genuine standalone premium Nella. Both rejected; no Orin/Seren originals made. Do not crop or count board figures, project metadata or on-image claims. Next work must be a **one-person single studio canvas** without mention of other characters, release names or review status. Nella's existing standalone original SVG is a design study, NOT a premium master.

Next actual Tavi priority: independently redraw the RIGHT profile so physical LEFT map satchel is appropriately **far and partly hidden** while the physical RIGHT lantern is near, and match the chosen youthful face, route-map nodes/compass, cloak hem and boot family to the new LEFT and original FRONT. **Do not horizontally flip an entire outfit**. G1 owner final approval remains PENDING and game code/Phase2 are LOCKED.

## Review 25 addendum — TWO genuine independent RIGHT candidates, failed solo cast requests, interrupted session recovered

New original painted right-facing Tavi alternatives **A** and **B**, each genuine full-body 1024×1536 one-person source image, were created in the previously interrupted session. The archive and the prior twelve painting originals were independently reverified on 2026-11-12; see [Review25](../../docs/34-PHASE-1-VISUAL-REVIEW-25.md) and [Ledger25](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-25.md). Review25 ZIP: **23 members**, SHA-256 `dd3869ca19cdc1f9ee0d21fab0eadccfb8a02fce2896e0f2199877b59d138359`, all 22 member hashes and sizes verified; 12/12 historical PNGs identical byte-for-byte to Review24 archive. **These are TWO new candidates for RIGHT, NOT two new angles or completed production character turns**. In total, there remain EIGHT original directions, FOUR older alternatives and TWO new ones = FOURTEEN portrait sources across EIGHT directional positions.

**Physical-side finding:** In both new right-facing images, near physical-right lantern reads clearly and far physical-left satchel is **largely behind body/teal cape**, improving on Review23's excessively visible bag. Exact 3D strap attachment still not demonstrated; head looks more mature than original youthful face, and candidate A/B differ in gold compass, Wayline stitch branches, cape hem and boots. Do not choose a final production master or claim G1 without consistent individual source paintings. Original [bilateral gear illustration v17](tavi-bilateral-equipment-and-right-profile-registration-v17.svg) was authored/committed before interruption as an editable design guide, **not a substitute for the two painted images**.

Three Nella attempts yielded two-character/other composite layouts, all rejected. No independent native-resolution premium Nella, Orin or Seren painting exists from this session. Continue with exactly ONE character per canvas with a neutral background, no character lineups, project badges, title plates, task descriptions or other roles. Nella human/copper hair/olive traveler, no Echo Lantern or invented class. Do not crop marketing panels. Existing [Nella solo vector](nella-front-construction-v1.svg) remains an early design guide only.

**G1 owner final visual approval remains PENDING, Phase 2/game code LOCKED**. Static phone-like 874×492 source tile studies cannot substitute for a real hardware or in-game test.

## Review 26 addendum — FIRST genuine premium solo Nella FRONT, no fake review boards

Review26 introduced **one real independent full-size 1024×1536 Nella FRONT premium painterly concept candidate**: copper-red up-swept curls, expressive freckled human face, olive practical travel coat, mustard scarf, stitched trousers, leather utility bag and boots on plain parchment. No Tavi, no Echo Lantern and no imported fantasy class. The image is preserved as `15_NEW_NELLA_SOLO_FRONT_PAINTING.png` in the verified [Review26](../../docs/35-PHASE-1-VISUAL-REVIEW-26.md) ZIP and documented in [Ledger26](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-26.md). New original source-controlled [Nella one-person outfit registration v2](nella-solo-front-costume-registration-v2.svg) translates readable outfit/color details into editable 2D construction art, **not** a replacement native premium painting, actual 3D rig or approved game character.

**True counts:** 8 independently painted Tavi directions + 6 preserved Tavi alternatives (14 unchanged full-size source files), **one NEW Nella FRONT native painted candidate**, zero independently accepted Orin/Seren portraits, zero new accepted Tavi corrections. Attempts at Tavi RIGHT and Orin/Seren generated promotional composite review boards; rejected, not counted. On-image version/GitHub/approval labels cannot alter development truth.

**Next Nella painting must be ONE person, ONE camera, ONE neutral canvas:** Nella RIGHT first, copper messy up-do, olive long coat with restrained ochre embroidery, cream shirt, mustard scarf, side leather pouch, patched brown trousers, sturdy boots, no Tavi or glowing lantern. Follow with independent BACK and LEFT, then matching diagonals only as quality warrants. Compare full-source head/body scale to canonical youthful Tavi: actual new Nella FRONT is more realistic/adult looking, still below G1 consistency. Do not crop a poster or claim the static 874×492 whole-source portrait tile equals a 2.5D game sprite.

**Owner G1 final art acceptance PENDING; Phase 2/game code LOCKED until separate authorization.** No physical iPhone or engine work allowed in Phase 1.

## Review 27 addendum — true Nella 4-cardinal paintings and first Orin / Seren solo masters

The recovered session produced FIVE independent full-size 1024×1536 studio paintings and a verified evidence archive: [Review27](../../docs/36-PHASE-1-VISUAL-REVIEW-27.md), [Ledger27](CHARACTER-ANGLE-ACCEPTANCE-LEDGER-27.md). Nella has a true single-subject **FRONT, RIGHT, BACK, LEFT** concept set (FRONT from Review26, three NEW independently generated paintings); Orin has a NEW elderly human FRONT; Seren Vale has a NEW adult human Bellkeeper FRONT. All one-person, full length, no generated status-board crops, all **preliminary candidates** only. Tavi's fourteen earlier PNG painting sources and Nella's prior FRONT were verified 15/15 byte-identical to Review26 originals; no new Tavi correction was made.

New original editable [Nella four-angle gear and costume construction v3](nella-four-view-costume-construction-v3.svg) registers copper hair/tie, mustard scarf, olive asymmetrical coat, physical-left leather pouch, patches and boots in 2D schematic form; it is **NOT another native premium portrait, 3D rig, game sprite or gameplay camera**.

**Still-open problems:** Nella's shoulder/bag strap, coat hem and gold leaf stitching vary across angles; Orin's Wayline-green cape risks looking too similar to other travelers and he needs separate RIGHT/BACK/LEFT; Seren needs independently composed RIGHT/BACK/LEFT and coherent restrained human Bellkeeper insignia. All three supporting-cast paintings have more realistically mature head/body proportions than the original large-eyed youthful Tavi; don't claim common production scale yet.

**Next individual image direction:** Orin RIGHT or Seren RIGHT alone on neutral parchment, matching the accepted solo FRONT photo. One original person only, complete feet/hair, no review panels/title cards/extra cast. Then individually BACK and LEFT, resolve gear and body scale; match Nella's four sources before diagonals. Keep G1 final owner approval PENDING, Phase2/game code LOCKED. No actual iPhone/engine/test or paid service.
