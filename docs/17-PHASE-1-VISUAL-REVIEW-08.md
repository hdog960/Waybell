# WAYBELL — Phase 1 Visual Review 08
**Date:** 2026-11-11 | **Verified starting GitHub main:** `e11ba18dee95db4cca25d2099f5031dc33854228`
**STATUS: PHASE 1 ACTIVE — G1 ART APPROVAL PENDING — PHASE 2 AND GAME CODE LOCKED**

## Authorization and governing references
User requested substantial visual development from docs/16-PHASE-1-VISUAL-REVIEW-07.md and three linked art-direction contracts: an independently painted native landscape Upper Spindle Galleries room, an exact-camera standalone painted Thimblebrook combat view, canonical Tavi/cast consistency, and iPhone-scale readability. Preserve premium aesthetic and reject collages/noncanonical mechanics. No Codex, ChatGPT Work, Vercel, outside paid services, engine, game code, Phase 2 or fabricated approvals. Core design canon remains docs/00–09.

## 1. New original Upper Spindle Galleries painting — independent and accepted as visual concept
**New original file:** `a_richly_detailed_high_quality_stylized_fantasy_g.png` — 1672 × 941 pixels, RGB, generated in this conversation as a **single full-frame 16:9-compatible landscape image**, NOT cropped from a montage. Full-size copy is in the conversation artifact `WAYBELL_Phase1_Review08_Art_Evidence.zip`; **not a GitHub-hosted image binary**. The room is visually coherent with the previously selected Lower Turbine Hall `a_highly_detailed_cinematic_game_like_fantasy_en.png`.

**What demonstrably improved:** three walkable tiers around a central open shaft, stone stair entry left, timber guardrails and visible support structure, a raised exit far right, huge immobile spindle-and-cog assembly, thick roots, teal-and-gold Waybell banners, high windows and warm atmospheric shafts of light. Three large brass Rootspool-compatible suspension rings with teal knot markings are visually identifiable. Tavi is depicted alone with dark hair, asymmetrical teal cartographer cloak and lantern. All intake channels/shafts are dry; no visible running water or spinning machinery, satisfying the first-visit state from docs/05 and the art-direction contract.

**Art-level quality assessment:** convincing handcrafted miniature-diorama aesthetic and architectural language strongly match the Lower Hall. The two spaces are distinguishable while clearly belonging to the same mill. The player can infer an entrance, a main bridge route and a higher destination.

**Unresolved:** the illustration does not prove collision, true connected geometry, vertical pathfinding or that the detailed lighting/foliage can run on mobile. Some railings obscure lower platform edges. The three Anchor rings are not yet all safely targetable in the hypothetical touch-camera composition.

## 2. Upper Galleries phone-sized assessment and framing risks
An original 874×492 downsample was created, plus a purely static translucent 16% LEFT / 16% RIGHT thumb-area overlay, with roughly 68% center remaining. These are approximations, not actual iPhone Safari screenshots, functioning controls or an approved safe-area spec.

At this small view:
- Tavi is still recognizable by teal cape but appears partly behind the proposed left movement thumb region. That is a **failure of the provisional art framing**, not proof of reliable controls.
- The middle Rootspool ring reads well, but the leftmost and far-right hanging rings risk overlap with thumb areas. Required anchor interaction will need an authored camera transition or changed art placement; this cannot be declared solved by the painting.
- A bright window dominates the upper-left view; warm sunlight looks good but may wash out nearby puzzle markers.
- The central spindle and bridge rails remain distinguishable, though the depth of the far exit benefits from a stronger shape/luminance cue.
- Lantern attachment, cloak, hand placement and facial appearance have not been tested across animation poses.

**New original editable visual artifact committed to GitHub:**
[design/phase1/upper-gallery-readability-and-traversal-v4.svg](../design/phase1/upper-gallery-readability-and-traversal-v4.svg), a 1600×900 original no-script vector staging schematic that maps first-visit route sequence, spindle, three anchor risks and left/right peripheral zones. This is NOT a 3D model or runtime implementation.

**Correction requirement before G1:** produce a revised gameplay-camera concept in which Tavi is fully central and required rings are not hidden by the two-thumb input footprint. The art may retain decorative rings at extreme edges but must ensure mandatory targets are separately legible and reachable. Later device validation remains Phase 2.

## 3. Lower Hall comparison — prior accepted art, not new
The Lower Turbine Hall original from Review 07 was included in the pack **for controlled side-by-side comparison only**. The stopped root-bound wheel, dry trough, safe foreground and elevated staircase share natural timber, mossy masonry, golden window light and Waybell banners with the new Upper Gallery. The previous illustration is not claimed as a new deliverable.

Combined first-visit state acceptance at concept level:
- **Lower Hall** — independent full-frame painting: PASS as concept direction.
- **Upper Gallery** — independent full-frame painting: PASS as concept direction.
- **Both dry and dormant** — PASS on visible image content.
- **Player movement continuity / platform collision / item puzzles** — NOT TESTED.
- **iPhone control-safe framing** — NOT PASSED; Upper player/anchors need adjustment.

## 4. Thimblebrook same-camera painted combat — STILL FAILS acceptance
Attempts this session to generate the required *standalone* painted combat companion resulted in multi-panel status collages, unrelated location changes, noncanonical cast roles or multiple enemies. All such examples have been **REJECTED AS CANONICAL ART EVIDENCE**. Some generated UI text included invented GitHub commit hashes or checkmarks, which have no relationship to actual repository state and must never be copied as factual evidence.

The unfulfilled contract [design/phase1/THIMBLEBROOK-COMBAT-MATCH-SPEC-07.md](../design/phase1/THIMBLEBROOK-COMBAT-MATCH-SPEC-07.md) remains mandatory:
- Exactly the same Thimblebrook house LEFT, distant stairs, bridge RIGHT, bell monument foreground-right, identical camera/lens/light.
- Only Tavi pose changes and ONE test Barkling appears, with a perspectively correct red ground wedge. No party members, side-scrolling camera, invented HUD or arbitrary new enemy family.
- Two native full-size paintings in isolation, not board crops, to be evaluated at phone scale.
- The prior GitHub vector camera-locked pair remains the only reliable exact-shared-geometry source. It is *not* premium painted fidelity or gameplay.

**Disposition:** Not achieved. Do not declare G1 or the combat visual gate ready.

## 5. Character art consistency
**Tavi** in the new Upper painting: dark tousled hair, teal asymmetric mapmaker cloak with gold embroidery, parchment and leather outfit, brass hand lantern. These visual tokens are consistent with the Lower Hall. At this scene scale, physical left/right gear attachments and identical underlying body proportions are not independently proven.

**Nella / Orin / Seren:** no new independently approved full-size model turnaround produced this session. The cast outline contract `design/phase1/CHARACTER-CONSISTENCY-AND-MOTION-07.md` remains active. The new collages that styled Orin as a dwarf warrior or assigned companions combat classes are rejected.

## 6. Evidence and artifact manifest
Conversation-generated ZIP: `WAYBELL_Phase1_Review08_Art_Evidence.zip`
SHA-256: `8542c115c8b57169d5aa4b7c8aaa77afddbfc7957b07ec1a77b2933d5c5fc1bd`

Contains 12 items: new Upper painting, previously accepted Lower and village painting for comparison, three 874×492 unannotated static previews, three phone-zone annotated versions, an original high-resolution two-room comparison sheet, `README.md` and `manifest.json` with provenance/hashes. The full-size images remain in the conversation/container and are **not** GitHub binary assets. The GitHub SVG/readme/review are accessible in repository.

## 7. Gate and test ledger
| Area | Evidence this session | Result |
|---|---|---|
| Premium standalone dry Upper Gallery | New independent full-res original image | **PASS as visual-direction reference** |
| Premium standalone dry Lower Hall | Previous independently painted image, compared | **PASS as prior visual-direction reference** |
| Cohesive mill architecture | Controlled new comparison at equal scale | **PROMISING, not 3D-validated** |
| Proposed phone-size clarity | 874×492 static previews and zones | **PARTIAL; Upper left player/right anchors need correction** |
| Exact-camera painted combat | Generated attempts failed contract | **OPEN / NOT PASSED** |
| Canonical characters in scene | Tavi recognizable; side/cast geometry untested | **PARTIAL** |
| True 3D visual fidelity and FPS | No engine or model work | **NOT TESTED** |
| GitHub files and continuity | Commits + independent readback in this turn | **VERIFY BEFORE REPORTING COMPLETE** |
| Final G1 owner approval | Broad art direction approved previously | **NOT GRANTED** |
| Phase 2 | Owner explicitly forbade | **LOCKED / NOT STARTED** |

## 8. Next authorized Phase 1 slice
**Priority A:** Get a true *image edit of the original Thimblebrook exploration painting* to add only Tavi combat stance, one Barkling and one red danger wedge while freezing every architectural pixel, or explicitly report failure and choose manual consistent painted workflows without introducing paid services or a game engine.
**Priority B:** Produce a revised Upper Galleries gameplay-camera concept moving Tavi/mandatory anchor interaction into the clear center while preserving the newly approved beautiful architecture.
**Priority C:** Reconcile the Tavi eight-direction physical handedness/gear continuity at matched size; improve supporting cast without inventing party systems.
**Priority D:** Owner visual reinspection once all pending pieces form a coherent packet. Only owner can approve G1; separate authorization needed for any Phase 2 implementation.

## 9. Explicit non-accomplishments
No runnable app, JavaScript/game code, engine, renderer, physical 3D scene, animation rig, functional touch controller, actual iPhone device test, measured FPS, CI game test, live GitHub Pages game/Home Screen preview, paid services, Codex, Work or Vercel. No automated G1 approval. A beautiful generated painting is an art target, not a promise that the same detail already runs on iPhone.
