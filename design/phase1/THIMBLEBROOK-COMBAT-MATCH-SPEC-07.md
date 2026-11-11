# WAYBELL — Exact-Camera Painted Combat Brief 07
Authority: Phase 1 art-direction and visual QA only • 2026-11-11
Status update (Review 09, 2026-11-11): **A standalone premium painted combat candidate now exists; exact painted exploration/combat pairing still unaccepted. G1 pending.**
References: docs/04 mechanics, docs/06 art, docs/15 Review 06.

## The reproducibility issue
The original high-quality independent 16:9 Thimblebrook exploration image (`a_richly_detailed_colorful_stylized_3d_isometric.png`, previous review) depicts a cottage left, broad cobbled plaza center, steps up to rear, arched river bridge right, Waybell monument foreground-right, Tavi central-left. Later attempts to create a matching combat view repeatedly changed the camera, reconfigured the village, introduced unrelated enemy types, added multiple playable party characters or produced presentation dashboards. Decorative boards are not proof of matched-camera composition.

Existing real source-controlled concept evidence:
- `design/phase1/thimblebrook-camera-locked-exploration-v2.svg`
- `design/phase1/thimblebrook-camera-locked-combat-v2.svg`
These share the same authored **background geometry**. This validates the *layout concept*, not a full-quality painted pair, and does not indicate implemented gameplay.

## Visual target for next independent 16:9 painted combat frame
**Invariants — MUST remain pixel-composition consistent with selected exploration frame:**
- One mapmaker cottage LEFT with original teal bell banner and roofline.
- Steps leading BACK and a stone river bridge RIGHT, with unchanged bank, river and railing.
- Original brass Waybell monument foreground RIGHT, same stone base and scale.
- Same general time of day, direction of sunlight, world scale and elevated three-quarter camera.
- Tavi remains single controlled hero with dark tousled hair, asymmetric teal cape, parchment tunic, leather satchel, compact brass Echo Lantern and grounded shadow. Other core cast are NOT in the fight.
- Three-quarter camera remains elevated; no behind-the-shoulder cut, side scrolling, dynamic anime poster camera or hero 40% of frame height.

**Only changes allowed:**
- Tavi transitions from idle to guarded/attacking stance.
- ONE Barkling-like root and bark creature is introduced **as a noncanonical diagnostic encounter** (Thimblebrook normally peaceful).
- One red triangular **ground-plane** telegraph originates at creature feet, follows perspective cobblestone grid and leaves a clear dodge lane. The attack indicates shape, position and direction, not just red tint.
- Optional faint rim around creature and restrained combat movement cues; NO party HUD, level numbers, fabricated stats or button labels.

## Touch safe areas / high contrast checks
- Proposed 16% LEFT and 16% RIGHT thumb areas, with ~68% unobstructed play core; values provisional.
- Crucial target warning, enemy feet, Tavi's feet and escape route must remain in the central unobstructed area even at 874×492 static preview.
- Tavi should be visible at regular exploration zoom. Do not magnify hero to compensate for small phone viewing unless intentional camera transition is authored.
- Distinguish attack red from Restore violet, Replay cyan and Reveal amber **by shape and motion** as well as color.
- Avoid enemy attacking from behind roof/tree props or in a place obscured by right thumb area.

## Acceptance checklist
[ ] Independent standalone original 16:9 image, not a crop from montage.
[ ] Exact important cottage/bridge/bell positions match exploration reference.
[ ] Tavi silhouette/costume and camera scale match.
[ ] Enemy and telegraph read in phone-scale static review.
[ ] No HUD or characters that imply party combat.
[ ] Owner judges art quality. G1 remains pending until explicit approval.
[ ] Phase 2 is separately authorized before engine/runtime work.

## Current result
**Not complete**: a genuinely matching full-quality *painted* combat counterpart is still absent. The locked vector pair is the honest reference. Recent generated full-frame combat images changed scene identity or featured extra fighters; these are rejected, not added to canon. No game code, no 3D camera, no device test.

## Review 09 addendum — independent combat painting exists, exact match still open

A new original standalone 1672×941 painted combat image is described and reviewed in [Review 09](../../docs/18-PHASE-1-VISUAL-REVIEW-09.md): `a_richly_detailed_stylized_fantasy_isometric_3d_i.png`. It shows one canonical Tavi, one Barkling diagnostic enemy and a bold red ground-plane warning, with a cottage left, stairs at the rear, river bridge right and Waybell foreground-right. It is legible at the static 874×492 phone-like scale, including proposed left/right side zones. This satisfies the *single-scene combat composition* objective, **not** the stricter paired-match requirement.

The image's architectural details are **not exact** matches to the previously accepted standalone peaceful Thimblebrook painting, and editing attempts returned noncanonical multi-panel presentation boards. Do not retroactively describe the pair as matching at the pixel level. The project may instead seek a peaceful frame produced from the new combat painting with unchanged scenery when an editing workflow can reliably do so. The village remains peaceful in story; this enemy is a noncanonical art-level diagnostic.

The source-controlled exact-layout SVG pair remains a valid technical *art-direction constraint* only. No actual combat, renderer, camera, mobile control or game code exists. G1 remains pending; Phase 2 remains locked.
