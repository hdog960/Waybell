# WAYBELL — Phase 1 Visual Review 09

**Date:** 2026-11-11  
**Starting verified main:** `889e188a21bf177b571e9897e844562f52adf6d3`  
**Status:** Phase 1 design and visual work in progress. **G1 FINAL ART APPROVAL PENDING. PHASE 2 / GAME CODE LOCKED.**

## Scope and decisions inherited
Continue visual preproduction, not playable implementation, from docs/17-PHASE-1-VISUAL-REVIEW-08.md. Maintain approved warm, rich 2.5D miniature-diorama ambition; make art testable at landscape phone scale. Need a genuinely standalone combat image, Upper Gallery control-safe correction, and consistently presented Tavi/cast. Do not treat model-generated progress percentages or collages as evidence. User forbids Codex, ChatGPT Work, Vercel and outside paid services.

## Deliverable 1 — NEW full-frame combat painting, accepted as visual direction only
**New original image**: `a_richly_detailed_stylized_fantasy_isometric_3d_i.png`, **1672×941** RGB, native landscape, produced in the originating conversation this session. It shows:
- A single Tavi with the established asymmetrical teal-and-gold cartographer cloak, dark tousled hair, practical boots and small glowing brass Echo Lantern at hip, with sword drawn.
- A single low, rooted **Barkling diagnostic enemy** with clear body/feet on the walkable courtyard. No Nella, Orin, Seren, extra party members or invented party roles.
- One broad red **ground-plane triangular attack telegraph** with a bright edge and visually intelligible orientation; a distinct clear escape area and enough visible room to dodge.
- Cottage/map-table left, center/rear stairs, river bridge right and civic Waybell in foreground-right. Original Wayline emblem and structural material vocabulary remain intact.
- No visible fake game HUD, statistics, controls, approval percentages or manufactured status labels.

**Assessment:** This is the first strong, genuinely standalone *painted* combat view produced in a continuation following earlier rejected presentation boards. At static 874×492 size Tavi and the Barkling remain identifiable and the red ground wedge reads as a danger zone. In the provisional outer 16% thumb safe-zone diagnostic the player, enemy, danger marker and available dodge area remain central, while decorative architecture extends to the right edge. The single diagnostic Barkling in normally peaceful Thimblebrook does **not** change story canon.

**Important limitation:** This painting is a fresh composition. It resembles the selected Thimblebrook exploration scene in the correct *location grammar* and angle, but architectural placement and individual pixels do **NOT** exactly match the original exploration painting. The previously required precise same-shot pair is **not finished**. No claim of a functioning real-time combat system, camera, rendered 3D materials or iPhone performance.

## Rejected image generation attempts (keep out of canon)
Two further attempts at editing/removing the Barkling or otherwise obtaining an exact matching exploration image returned multi-panel decorative boards with UI labels, simulated completion checkmarks and off-canon character roles. These were **rejected**. They do not prove matching camera, character rigging, GitHub status or game readiness. The original accepted standalone combat painting is preserved separately. **No fabricated progress from image text was entered into project records.**

## Deliverable 2 — corrected Upper Gallery camera storyboard (NEW SVG source in GitHub)
[**Upper Gallery safe keyframes v5**](../design/phase1/upper-gallery-camera-safe-keyframes-v5.svg) is a new, original editable 1600×900 SVG design document showing *two separate camera positions* along the existing dry, dormant mill gallery. It addresses the specific Review 08 shortcomings: Tavi partly inside the left proposed thumb region and rightmost Rootspool anchor at the right edge.

**Camera A: entry / lower stair.** Frame Tavi and currently reachable first anchor in the central clear area; do not demand the far anchor remain onscreen at this stage.

**Camera B: central spindle / return loop.** Follow Tavi's movement to frame the next required Rootspool anchor clear of the right controls. The far ring appears when the player moves there; no simultaneous exposure of all rings is required.

**Hard requirements:** Keep wheel and spindle stationary and dry on first arrival, path elevations coherent, railings readable, Tavi boots/shadow visible, and all **currently mandatory** targets within the unobstructed ~68% central view. Outer ~16% left/right is an illustrative assumption, not actual tested safe-area measurements. Further camera art and eventual 3D feasibility checks remain necessary.

**What this is:** a visual design storyboard with two drawn positions, not a runtime camera movement, collision model, source game code or finished environment painting.

## Deliverable 3 — original Tavi action/equipment silhouette sheet (NEW SVG source in GitHub)
[**Tavi action silhouettes v3**](../design/phase1/tavi-action-silhouettes-v3.svg) presents four normalized, original vector reference poses at a shared baseline:
- Exploration: lantern in hand, sword sheathed.
- Guard: sword in hand, lantern secured near hip.
- Wind-up: visually directional sword action while cloak and torso remain recognizable.
- Dodge: moving weight/feet and fabric trailing without hiding foot contact.

The intended physical map satchel side, teal cape hem, dark hair and boots remain part of every pose. These are **rough stylized schematics**, not final eight-direction painterly turnarounds or animations, and may have line-art/anatomy discrepancies needing further refinement. Nella, Orin and Seren are unchanged by this pass; no new party mechanics.

## Deliverable 4 — full-size and static phone diagnostic package
Created a conversation/local evidence ZIP: `WAYBELL_Phase1_Review09_Art_Evidence.zip`, **SHA-256 `b7ebbe9649edb9098d9f3aafa1ceba5e23cc06732ca24c7e85b007ffed11437b`**.

Package contains:
- NEW original combat painting source file, full size.
- PRIOR Upper Gallery full-size painting for side-by-side control comparison (not claimed as new).
- Two 874×492 scaled previews.
- Two overlaid previews with semitransparent outer 16% thumb-zone proposals and approximate landmark circles.
- Original review contact sheet with honest labels.
- README and JSON manifest with per-file SHA-256 hashes.

These PNG/ZIP files are linked through the originating conversation and **are not currently stored as binary image files in GitHub**. GitHub stores the newly authored SVG source and this text review. An 874×492 static sample is not a real iPhone test. Marker centers are approximate manually selected visual annotations, not measured collision/hitbox ground truth.

## Phase 1 acceptance matrix (truthful)
| Item | Current evidence | Determination |
|---|---|---|
| Standalone premium 16:9 Thimblebrook combat painting | NEW 1672×941 independent single-scene illustration, one Barkling, one red wedge | **Meaningful improvement; accepted as visual target** |
| Exact pixel/layout matched exploration/combat painted **pair** | Previously approved exploration and new standalone combat have architectural variance | **OPEN / not passed** |
| Combat ground-plane warning clarity | One bright red wedge, central to 874×492 review | **Conceptually readable; no dynamic timing proof** |
| Upper Gallery Tavi/anchor occlusion | Existing painting fails side-zone test; new camera 2-keyframe storyboard proposes cure | **DESIGN FIX PROPOSED; artwork still not corrected/tested** |
| Consistent Tavi action equipment | New four-pose rough SVG source | **Improved specification, not approved animation/turnaround** |
| Nella, Orin, Seren cast proportions | Prior scale reference, no new finished turnarounds | **PARTIAL / OPEN** |
| Upper and Lower mill first-entry water state | Previous full-size independent paintings remain dry/dormant | **Concept art accepted in earlier reviews; no game scene** |
| iPhone 3D real-time quality, FPS, PWA controls | No engine, code or actual device work allowed | **NOT TESTED** |
| Owner G1 final visual approval | Owner approved general aesthetic only | **NOT GRANTED** |
| Phase 2 and gameplay code | Explicitly forbidden by owner | **LOCKED / NOT STARTED** |

## Next substantive Phase 1 slice
1. Produce a **pixel- or composition-matched premium standalone peaceful exploration counterpart** using an actual in-place edit of the accepted combat painting, or demonstrate an alternative art workflow producing exact scene consistency. Keep one Tavi and remove only the diagnostic enemy/tell without changing landmark layout; reject collage attempts.
2. Render a revised **independent Upper Gallery painted camera view** implementing two-position framing: character/mandatory rings do not sit under hypothetical thumb zones.
3. Create production-quality eight-direction character art with stable handedness, cape stitch, satchel, lantern attachment, plus normalized Nella/Orin/Seren comparisons.
4. Continue phone-scale static review and clearly note discrepancies; actual on-device tests belong to separately authorized future technical work.
5. Only request G1 approval when an evidence set meets the user's art standard. **Never silently begin Phase 2**.

## Evidence and scope disclaimer
Actual GitHub file commits/readback verification follow this review update. **No game code, engine, animation rig, 3D scene, WebGL render, browser/Chromium test, iPhone touch test, real performance measurement, live Pages/Homescreen showcase, Codex, Work, Vercel or paid external service.** New illustration fidelity is an ambition, not proven runtime capability.
