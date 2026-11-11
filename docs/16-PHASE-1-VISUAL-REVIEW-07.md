# WAYBELL — Phase 1 Visual Review 07
Updated 2026-11-11 • Started from verified GitHub main `117059b4bacd9ff5d8d7dbe85b559b76cedc3e3c`.
**STATUS: PHASE 1 ACTIVE — G1 OWNER ART APPROVAL PENDING — PHASE 2 AND GAME CODE LOCKED.**

## Owner's request and scope
Continue a substantial premium Phase 1 art pass following docs/15: independently composed native 16:9 painted combat and dormant mill interiors, camera consistency, Tavi and cast coherence, static iPhone-scale readability. Reject noncanonical images and log actual improvements in GitHub. **Do not begin Phase 2, 3D implementation, app code, Codex, Work, Vercel or paid external services.** No previous Home Screen preview is claimed or touched here.

## Actual NEW generated artwork
### Accepted **as a strong visual target, not final assets**
**Original standalone Lower Turbine Hall painted illustration:** `a_highly_detailed_cinematic_game_like_fantasy_en.png` created this session in the originating conversation. 1672×941 pixels, approximately 16:9 (landscape). A solitary canon-consistent teal-caped Tavi stands on the cobbled lower mill floor, next to an antique bronze Echo/Wayline marker and rail-protected paths. A monumental wooden waterwheel sits frozen at right, immobilized by large roots crossing the hub; no activated waterwheel, spray or flowing waterfall. Architecture uses warm morning sun shafts, timber railings, glazed upper windows, mossy masonry and original Waybell banners. Visibly distinct low and elevated walkways.
**Assessment:** Meets the *first-visit dry/dormant* art direction, warm premium quality and a clearly legible centerpiece. Does not prove that all detailing translates to free-hosted 3D on iPhone; the stairs at far left and some control-side props become tight near the proposed thumb reserve. Tavi reads in static 874×492 preview, but small levers/markers need more defined silhouettes.

### Partial visual references — **not approved as complete**
**Upper Spindle Gallery:** Generated multi-panel artwork `a_highly_detailed_cinematic_painted_3d_illustrat.png` showed a promising dry gallery with rails, stairs, gears and an unpowered wheel, but its panel is **not** an independently generated 16:9 painting. A crop `04_upper_gallery_REFERENCE_CROP_720x405.png` and upscaled phone comparison `05_upper_gallery_REFERENCE_upscaled_for_phone.png` are provided in the review packet, explicitly marked a low-resolution source panel. Upscaling adds no missing detail. Full-resolution independent upper gallery is STILL REQUIRED.

**Painted combat counterpart:** Multiple original image-generation attempts yielded collages or changed scene identity. Several invented party members, extra hostile characters or alternate perspective. These are **rejected**, not merged into canon or used to claim the exact-camera combat requirement passed. The reliable canon camera pair remains the exact-shared-geometry original SVG art already on main: `design/phase1/thimblebrook-camera-locked-exploration-v2.svg` and `design/phase1/thimblebrook-camera-locked-combat-v2.svg`. They verify authored composition consistency, not painted 3D fidelity or actual combat.

## Phone-scale static quality inspection
Session packet `WAYBELL_Phase1_Review07_Art_Packet.zip` SHA-256 `cafaadd87d7f59352bb4b63caa0d7fccbe141b8cacabdf6acb206f3b631d77be`. Includes:
- `01_lower_turbine_hall_STANDALONE_painted.png`: entire original 1672×941 accepted direction image.
- `02_lower_hall_874x492_static.png`: downsampled readability sample.
- `03_lower_hall_thumb_zones_STATIC.png`: overlay of approx. 16% each side for left/right control study, leaving ~68% center.
- `04_upper_gallery_REFERENCE_CROP_720x405.png`: source gallery panel crop; NOT independent artwork.
- `05_upper_gallery_REFERENCE_upscaled_for_phone.png`: phone study only (no added detail).
- `00_review07_visual_comparison.png`: honest, labeled art comparison.
- `README.md`: provenance and rejection log.
The packet's JPG/PNG assets live in the conversation/container only, **NOT in GitHub**, because no authenticated binary upload was available in this workflow. The full original painted room is an illustration, not a 3D scene asset or screenshot.

Static inspection passed at a coarse level: center path and hero remain recognizable, the wheel is a distinctive hero feature, and upper/lower architecture have different silhouettes. **Unresolved:** leftmost approach stair partly intersects a thumb-zone concept overlay; smaller gates/markers are not reliably readable without contextual enlargement. Static downsampling is NOT an actual iPhone test.

## NEW independently committed GitHub design documentation
- [Rootbound Mill visual-state and room art contract](../design/phase1/ROOTBOUND-MILL-ART-DIRECTION-CONTRACT-07.md): detailed before/after wheel and sluice rules, scene landmarks, camera and route composition, upper-gallery independent painting brief.
- [Thimblebrook combat exact-camera match specification](../design/phase1/THIMBLEBROOK-COMBAT-MATCH-SPEC-07.md): precise architectural invariants, single diagnostic Barkling and red ground telegraph, protected thumb/center zones, rejection and acceptance checklist.
- [Tavi eight-angle character/cast consistency and motion art plan](../design/phase1/CHARACTER-CONSISTENCY-AND-MOTION-07.md): handedness, physical outfit/lantern continuity, proportions, equivalent baselines, Nella/Orin/Seren design distinctions and new QC criteria.
These are legitimate Phase 1 original *design specifications*, not implementation, game code, animation or final character assets.

## Explicit acceptance matrix
| Feature | Evidence | Current state |
|---|---|---|
| Premium, independent Lower Hall illustration | New 1672×941 single-image concept | **STRONG VISUAL REFERENCE**; first-visit dry rule visually passes |
| Premium, independent Upper Gallery illustration | Only attractive collage crop; previous full-frame vector layout exists | **FAIL / OPEN** |
| Premium, independent matched-camera painted exploration + combat | Existing first landscape painted exploration and exact-layout SVG pair; imagegen attempts changed scene | **FAIL / OPEN** |
| Canonical Tavi eight-direction model | Existing schematic sheets + newly detailed per-angle art plan | **SPECIFICATION IMPROVED; finished painterly matching angles missing** |
| Nella, Orin and Seren consistent model language | New cast audit checklist + prior shared-scale schematic | **PARTIAL** |
| 16:9 phone-size static composition | Original Lower Hall at 874×492 and safe-zone overlay | **PERFORMED AS STATIC REVIEW ONLY** |
| Real iPhone 3D quality, camera, touch/FPS | No engine or application code | **NOT TESTED / NOT DEMONSTRATED** |
| G1 owner visual approval | Owner previously approved overall aesthetic only | **PENDING / NOT PASSED** |
| Phase 2 engineering | Prohibited | **NOT STARTED** |

## What should happen on next Continue Development (Phase 1 ONLY)
1. Get ONE high-quality independently composed 16:9 **Upper Spindle Galleries** painting at full source detail. Same root-locked architecture as Lower Hall, deep layered catwalk and fixed Rootspool anchor. No running water.
2. Produce full-quality standalone *combat* painting of EXACT same Thimblebrook scene/camera as a selected exploration original. Reject all decorative multi-panel boards, extra heroes, unrelated enemies and fabricated HUD stats.
3. Reconcile Tavi body/head, cloak embroidery, right-hand lantern and satchel side on genuine eight-view art, with a similar non-party cast scale comparison.
4. Side-by-side owner review of both proper mill paintings and matching combat/exploration pair. G1 decision only through explicit owner action; no automatic phase change.
5. When publishing a future Home Screen preview is explicitly requested in a separate task, treat that as static Phase 1 showcase (not gameplay), independently verify the public Pages URL. It was not published in this slice.

## Verification / non-accomplishments
GitHub source files and README/ledger updates are to be verified by readback in this session; publication of an actual rendered game, 3D assets, animation, browser or iPhone gameplay, functional controls, CI tests and PWA installation were not performed. No paid services, Codex, Work or Vercel. No unsupported assertion that all requested artwork is finished.
