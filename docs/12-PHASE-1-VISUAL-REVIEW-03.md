# WAYBELL — Phase 1 Art/Readability Study 03
Date: 2026-11-11 | Status: **PHASE 1 ACTIVE, G1 PENDING; PHASE 2 FORBIDDEN**
Authority: follows docs/00, 02, 06, 08, 11. This is visual preproduction and critique, NOT an implemented game.

## Baseline verified before work
Owner-approved broad tone and style only; Phase 1 art refinement authorized. Started at latest observed main commit `648d6d418afe2f8fa30a7745e83ca610ab570d77` with docs/11 as the active last review. No game files, engine, CI build, PWA, live Pages content, or real iPhone playtest were authorized.

## What was newly created and why
### A — Hand-painted eight-direction Tavi candidate
Original concept art exists in the producing conversation as `a_detailed_polished_concept_art_character_design.png`, a parchment study with 8 labeled stances, expression portraits, detailed equipment and a coherent teal cape/lantern direction. **Visual assessment:** much better wardrobe continuity and silhouette definition than the earlier collage; back view maintains cartographer motif, key props remain visible, though limb lengths, lantern side and face shape still require true orthographic/production reference before rigging. Text and labels on illustrated concept art are not authoritative.
**Additional editable GitHub evidence:** [tavi-eight-directions-v1.svg](../design/phase1/tavi-eight-directions-v1.svg), a separate original diagram with eight normalized small silhouettes and named orientations, which makes required shape/gear consistency explicit. This SVG is schematic 2D vector work; it is neither hand-painted 3D nor a real 3D model, sprite animation or rig.

### B — Elevated three-quarter camera and matching combat composition
Generated design studies in conversation include exploratory presentation boards with camera and combat scenes. Some show the correct elevated world view; some include different costumes, incorrect side-on staging, misleading progress percentages or invented GitHub hashes and must NOT be treated as source of truth.
**New editable GitHub evidence:** [three-quarter-camera-combat-v1.svg](../design/phase1/three-quarter-camera-combat-v1.svg). Two deliberately matched static, elevated three-quarter scene diagrams: (A) village navigation with path, bridge, bellstone and small Tavi, and (B) a combat warning on a comparable ground plane. Both display a left movement touch zone and right attack/dodge/tool zone while protecting central playable visibility. They are conceptual diagrams, NOT tested controls, a true engine camera, collision geometry, an accessibility audit, or a proof of 3D feasibility. Exact perspective, FoV, zoom and UI hit regions remain subject to Phase 2 evidence.
**Candidate frame contract:** target landscape 16:9 staging; peripheral control areas around 16% on left and right (illustrative), central active scene 68%; feet/shadows read, route edges and overhead structures distinguishable, enemies cannot attack unseen behind a prop, danger red with a shape cue distinct from magic amber/cyan/violet, no critical text/icons behind thumb regions.

### C — First-visit dormant Rootbound Mill interior
The prior lush mill mood concepts often depict water and moving-looking wheels. Canonically, the dungeon starts abandoned and dry; the player later restores water flow. We corrected the level *design* by making a distinctive **lower dry turbine hall** and a **higher spindle-gallery return loop**.
**New editable GitHub evidence:** [rootbound-mill-dormant-layout-v1.svg](../design/phase1/rootbound-mill-dormant-layout-v1.svg) containing two schematic elevation studies: inactive wheel, dry or drained channels, clear low/high timber platforms, fixed ring markers (future Rootspool anchors) and a small Tavi for scale.
**Remaining gap:** no production-ready high-quality 2.5D illustration of **both interiors in their initial dormant state** has been approved; older paintovers have active water and must be labeled after-repair visual mood only. No dungeon geometry, physics, animation, or pathfinding exists.

### D — Combat readability and UI
The matched composition establishes a proof of the **design rule**, not proof of interaction. A clear enemy charge/tell area must be placed away from thumb controls and visibly reachable by a dodge; on-screen enemy, player direction, feet and hit telegraph must be distinguishable. The design should use iconic waymarks, restrained HUD and real target silhouettes, not the huge decorative dashboards seen in some automatically generated concept images.
**Remaining gap:** a clean game-scale cinematic art painting (not a vector diagram) using *exactly the same camera* for exploration and combat, plus a cast/scale comparandum for Nella, Orin and Seren, still needs review. Controls are not functional.

## Art character-identity invariants for next iteration
- **Tavi:** dark-brown tousled hair, expressive young face, layered parchment shirt, sturdy brown boots, map/compass satchel and a single asymmetrical TEAL cartographer cape with gold road stitching. Echo Lantern brass, compact and bright. No red hero scarf/cape, giant sword, or alternate hero costume.
- **Nella:** copper-red hair, lively practical traveler silhouette, no invented party role.
- **Orin:** kind elderly cartographer with white/gray beard, spectacles and rolled maps, never a generic wizard.
- **Seren Vale:** compassionate but formidable Bellkeeper, navy/burgundy robes with controlled brass details, no demonic villain form.
- **View consistency:** eight views at identical proportion and outfit schema; same lantern location when equipped and consistent clip/cape attachment. If image generation changes anatomy, record that as a *failure* rather than canon.
- **Tool familiarity:** Rootspool is a brass/vine coil with target anchors, never a fully free-form grappling mechanism. Lantern Reveal = amber path glyph, Replay = cyan parallel route, Restore = violet temporary span (distinct shape as well as color).

## Critical review of this session
| Area | Evidence | Current determination |
|---|---|---|
| Eight-direction Tavi | New illustrated turnaround candidate + normalized GitHub vector | **Improved; not production-ready or finally approved** |
| Village camera and 2.5D depth | Side-by-side design diagrams, previous village art | **Improved legibility specification; no actual 3D camera validation** |
| Rootbound Mill pre-restoration | Two new dormant-design views with fixed landmarks | **Concept grammar corrected; still needs polished first-visit interior art** |
| Combat tell visibility | Same-plane mock with danger area and edge controls | **Conceptually clearer; not live gameplay/functional test** |
| Original Waybell identity | Teal/bronze/road glyph maintained; SVG set reused | **More coherent; icon size and in-context material study still open** |
| iPhone technical performance | No engine, native device, or renderer run | **NOT TESTED / CANNOT CLAIM** |
| Owner art approval G1 | Broad mood approved earlier, final owner signoff absent | **PENDING** |
| Phase 2 | No permission | **LOCKED** |

## New technical-feasibility discipline (without doing tech work now)
Painted images are **goals**, not evidence of achievable graphics. First later playable feasibility scene must prove faithful scale, lighting and walkable-height readability on a real iPhone. If exact illustrated detail is too expensive, reduce number of props, clutter or region density rather than substituting flat visuals without owner approval. Keep this sentence in all future summaries: **No engine-based graphics fidelity or framerate has been demonstrated by these images.**

## Next authorized Phase 1 slice
1. Produce stronger clean matched-angle **painting** of village exploration vs combat, separate from vector diagrams, with Tavi consistently 10–16% image height as a starting experiment (not a confirmed standard).
2. Produce original, high-quality **dormant** mill lower/upper interior paintings without running waterfalls or rotating machinery; compare with design diagrams.
3. Character turnarounds: quality-control for real same-height/dimensions, Nella/Orin/Seren side-by-side scale chart and Tavi lantern holster/tool state.
4. Compare scene and UI marks at phone-sized static render; record any unreadable shapes before requesting G1.
5. Package only canon-respecting images in GitHub **if binary upload becomes feasible**, otherwise keep honest links to chat artifacts and editable design-source diagrams.

## Explicit non-accomplishments
No app code, 3D model, animation rig, engine test, automated browser test, deployed gameplay, verified iPhone device test, paid external services, Codex, Work or Vercel. No claim of full art acceptance or Phase 2 readiness.
