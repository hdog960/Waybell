# WAYBELL — Character Consistency & Motion Art Plan 07
Updated: 2026-11-11 • Phase 1 ONLY • G1 Owner Final Approval Pending • Not a 3D rig, animation or engine plan execution

## Purpose
Past multi-view generated illustrations drift in hand/lantern position, face size, cloak design and character age. A single painted hero picture is not evidence of all eight consistent directional views. This source-of-truth concept guide defines the **visual invariants** that a future production-ready eight-angle sheet must prove.

## Tavi — visual canon vs current art proposal
**Existing canon:** young apprentice mapmaker, curious expression, dark tousled hair, single asymmetric teal cartographer cloak with restrained gold road-map stitching, brass clasp and Echo Lantern, parchment shirt, sturdy brown boots, small map satchel and compass. Player is one controlled hero, not a four-member party combat RPG.
**Candidate proportions for art comparison only:** body approximately 4.2–4.8 head-heights; hair top to boot soles same measurement in all eight views; cloak hem near mid-thigh, not floor length; lantern body approximately 0.45–0.65 head heights; boots clearly separated by empty space at idle. Final numeric rig proportions require owner G1 visual approval and later model validation.
**Strong identity anchors:** teal from shoulder to angled hem; warm brass crescent clasp by upper chest; embroidery of road topology rather than random spells; asymmetrical satchel strap that stays on same physical side; recognizable directional fringe; lantern with distinctive Wayline route trapped in its glass.

## Eight-direction view contract
Draw and label all at same canvas scale, foot baseline and camera inclination:
0 South/front: symmetrical face landmarks but asymmetric cape hem visible.
1 South-East/front three-quarter: chest clasp + satchel strap still on physically correct side.
2 East/right profile: one eye, nose depth, lantern arm silhouette, no shifted accessory placement.
3 North-East/back three-quarter: map embroidery becomes legible on rear cloak, same shoulder fold.
4 North/back: rear hem and map-route line, satchel should not teleport or mirror.
5 North-West/back three-quarter: inverse facing direction while physical ownership of accessories stays constant.
6 West/left profile: alternate nose silhouette and mirrored *view*, but NOT mirrored physical costume details.
7 South-West/front three-quarter: same proportions as South-East without changing hairline or face age.
**Mirror rule:** viewing direction is not a license to flip the complete character sprite and move the clasp/lantern/satchel to the other hand. Future runtime might use a 3D rig with camera orbit; the art sheet must remain physically coherent.

## Canonical inventory poses (art planning, not equipped gameplay)
- Idle: lantern in preferred right hand; sheathed sword and map satchel visible, shoulders relaxed.
- Movement: lantern sways, but its light source remains anchored; clear boot contact and shadow.
- Combat: lantern shielded near hip, sword drawn with readable attack direction; cape does not cover attack windup.
- Rootspool equipped: brass vine spool remains physically attached to belt with visible cord/anchor motif.
- Echo Replay: cyan trailing mark follows original footfalls; does not imply a second playable party hero.
- Restore: violet bridge/stair phenomenon, separate from the hero silhouette and red danger warnings.

These are **candidate staging rules** to evaluate with owner, not new locked game mechanics. They must reconcile later with touch-input affordances and 3D collision.

## Supporting cast comparison
| Character | Silhouette traits | Distinct palette and visual story | Avoid |
|---|---|---|---|
| Nella | More active/forward-weighted stance, copper-red hair, compact explorer clothing | Copper + leaf green; quick open gestures; independent explorer | Mage party slot, healer, invented role, identical Tavi cape |
| Orin | Older rounded posture, gray-white hair/beard, spectacles, map tube or folio | Warm wool/brown, parchment; gentle but capable | Dwarf warrior or armored party tank |
| Seren Vale | Taller reserved upright silhouette, restrained formal coat/dress and Bellkeeper brass | Navy/burgundy + muted gold; stern compassionate expression | Villain demon spikes, bright cyan wizard combat-party class |
| Tavi | Compact adventurer, teal asymmetric cape, map satchel, lantern | Teal + amber brass; recognizable from phone-height camera | Red scarf alternative hero, hulking armor, duplicate NPC |

## Art QC before G1
- Display front/back/side/diagonal on same baseline and neutral background.
- Crop all eight views to equivalent rendered head height and boot-to-head height; compare in an overlay with alpha blending.
- Flag any angle where lantern, satchel, compass clasp, map stitching, hairline, boots, or proportions change unnaturally.
- Add four expressions for Tavi (curious, determined, surprised, subdued), one key story reaction each for Nella/Orin/Seren.
- Shrink each to approx. 100–140 px full-body height for *static* preview. Faces may become indistinct; silhouette and cloak color must remain readable. This is NOT an in-engine or physical iPhone assessment.
- Check that the player never looks like a generic supporting NPC under scene color and lighting.

## Current assessment
Previous original vectors are helpful (design/phase1/tavi-eight-directions-v1.svg, design/phase1/tavi-cast-directional-audit-v2.svg, design/phase1/cast-scale-guide-v1.svg). They are schematic consistency aids, NOT a completed professional rig turnaround. This session's independent lower mill painting maintains a small identifiable teal-cloaked Tavi, but adds no new full multi-angle character source. Character G1 remains incomplete; do not infer signoff from the detailed diagrams or generated boards.

## Phase 2 boundary
When and ONLY when separately authorized after G1, feasibility work may check actual model topology, skin weighting, cloth behavior and real camera occlusion. None of that is implemented by this document.
