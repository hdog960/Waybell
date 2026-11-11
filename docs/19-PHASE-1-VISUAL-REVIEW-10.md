# WAYBELL — Phase 1 Visual Review 10

**Date:** 2026-11-11  
**Verified starting `main`:** `85e6a7c4f556e8e91e20fa8a09018373d2cd32f0`  
**Status:** **PHASE 1 ACTIVE • G1 FINAL ART APPROVAL PENDING • PHASE 2 LOCKED**

## User authorization and non-negotiable limits
User asked to continue meaningful Phase 1-only visual development from Review 09, preserving the premium handcrafted 2.5D diorama aesthetic. Highest priorities: a peaceful standalone Thimblebrook exploration picture compositionally matching the accepted combat picture; a corrected full-quality Upper Spindle Galleries camera composition with Tavi and mandatory anchors away from thumb areas; and better eight-direction Tavi/cast consistency. Reject noncanonical party roles, fake status claims, collages and first-visit flowing water. Commit and read back actual GitHub source, provide a downloadable evidence packet, keep G1 owner approval pending. **No game code, Phase 2, Codex, Work, Vercel or outside paid services.**

## 1. MAJOR IMPROVEMENT — peaceful Thimblebrook companion art

**New original standalone illustration:** `a_richly_detailed_high_detail_fantasy_game_style.png`, native image **1671 × 941**, generated using the earlier independently accepted 1672 × 941 combat painting as visual context; preserved as the original image in the new conversation ZIP.

It depicts the **same recognizable Thimblebrook courtyard composition** in peaceful exploration mode:
- timber/stone mapmaker cottage and teal banner at left;
- wood cart and flower planters at cottage entrance;
- broad cobbled plaza and circular navigation mosaic in the foreground;
- lantern-lit stair flight rising at the rear;
- stone bridge and stream at right;
- civic Waybell monument at right front;
- the **same single dark-haired, teal-map-cloaked Tavi** now idle and carrying the warm brass Echo Lantern.

The diagnostic Barkling and its red warning wedge are gone; nobody else was introduced. The village remains peaceful in story canon. Image-generation altered subtle surface/textural details and Tavi's pose, so the result is a **strong composition/camera match**, not a claim of source-pixel-perfect inpainting or an engine-locked camera.

**Objective static comparison performed:** both the accepted combat and new peaceful paintings were resized to 1600×900 for same-size coordinate comparison. Mean absolute per-pixel RGB channel difference (0–255) and fraction of pixels with mean difference below 25 are:
| Region | Mean abs difference | Fraction below 25 |
|---|---:|---:|
| Upper architecture, top 380 px | 13.55 | 86.3% |
| Upper-left cottage | 12.61 | 88.0% |
| Right bridge | 12.63 | 87.4% |
| Lower-right bell | 10.84 | 92.0% |
| Central combat floor (intentional scene difference) | 22.03 | 70.7% |

These values are a concrete **visual-similarity diagnostic**, not a formal gameplay camera calibration. Architectural composition is sufficiently coherent for a Phase 1 *paired-scene visual target*. Strict pixel identity remains unattested; exact real-time camera requires separately authorized later technical work.

**Acceptance:** scene and camera *art direction* improved substantially and can be shown together to the owner. Full G1 still pending.

## 2. Upper Spindle Galleries — PARTIAL camera fix, not a new premium painting
The two attempts to regenerate or edit a full-quality Upper Gallery image returned decorative montage/marketing boards that included fake update checkmarks, invented companion roles and alleged commit identifiers. **Both were rejected.** Neither is a new standalone Upper Gallery art source or a verified GitHub record.

A useful alternative was created from the **already accepted** full-size original Upper Gallery image `a_richly_detailed_high_quality_stylized_fantasy_g.png`:

- A manually planned **entry-focused camera crop** of its actual pixels at original source coordinates `x=0, y=76, width=1200, height=675` was resized to 1600×900 solely for visual comparison. File `06_UpperGallery_ENTRY_CAMERA_REFRAME_FROM_ORIGINAL.png`.
- At this narrower framing, Tavi is approximately 18% of the screen width rather than ~13%; the nearer two Rootspool targets fall inside the central field of view. The far ring is intentionally off-camera, not required at the entry position.
- A new 874×492 static view plus approximate outer 16% thumb-zone overlay was created. This is a **camera composition study**; upscaling adds no genuine detail, and it is NOT a separate fully rendered high-resolution premium painting or tested responsive camera.
- The Gallery first-visit state remains dry and unpowered. Static earlier painting still carries warm window light, connected wooden bridges and stationary machinery. No new water or animated machinery was introduced.

**Original GitHub design artifact added:** [Upper Gallery measured camera audit v6](../design/phase1/upper-gallery-camera-measured-audit-v6.svg), comparing the original broad composition with the entry crop and identifying ongoing interaction risks.

**Critical remaining failure:** an interactive follow camera or actual revised full-quality painted view at the second anchor position is still missing. Tavi is only just outside the left 16% region in the entry crop, so movement may reintroduce occlusion. G1 mobile readability **cannot** pass from this crop alone.

## 3. Tavi and cast — normalized visual analysis, no false animation claim
Using the existing painted eight-view Tavi reference `a_detailed_polished_concept_art_character_design.png`, we extracted eight directional crops into **one newly normalized comparison plate**: `08_Tavi_8view_NORMALIZED_reference.png`. The artwork inside the crops is **not newly painted**; normalization improves QC comparison only.

New source-controlled contract: [Tavi & Cast Physical Continuity Audit 10](../design/phase1/TAVI-AND-CAST-VISUAL-CONTINUITY-10.md), establishing:
- Physical RIGHT lantern carry and hip-retention rules; physical LEFT map satchel, never flip both sides by mirroring east/west frames.
- Identical teal-and-gold asymmetrical cape hem, brass clasp, Wayline embroidery, tousled brown hair, trouser cuffs and boots in all eight directions.
- Distinct Nella (copper-red agile explorer), Orin (elderly bespectacled cartographer, human proportions) and Seren (navy/burgundy dignified Bellkeeper) visual language.
- Character pose sequence: exploration lantern carry, guard with lantern secured, sword wind-up and grounded dodge.
- Explicitly reject fake party combat roles and invented class names.

**Still open:** a genuinely final hand-matched eight-angle orthographic sheet with consistent anatomy, exact equipment-side visibility and professional cast turnarounds. A cropped prior illustration is not that new final artwork.

## 4. Downloadable evidence and QA
New downloadable current-conversation package:

`WAYBELL_Phase1_Review10_Visual_Evidence.zip`  
**SHA-256:** `f7b18ade2abedd74fd81f705f36c5212e786d4cec5f9c3d8a2108dc9314aae66`  
**15 files** including original new peaceful full-size painting, earlier combat full-size comparison, prior accepted Upper Gallery painting, annotated and unannotated 874×492 static phone previews, entry-camera crop and diagnostics, previous character-sheet crops re-aligned to eight orientations, a controlled four-image comparison board, README and JSON file/hash manifest.

The full-resolution **PNG images are conversation artifacts and are NOT committed to GitHub as binary files** by this GitHub text-only connector workflow. Only original author-written SVG and documentation are committed and subsequently read back.

**Real tests performed:**
- Existing GitHub Review 09 and ledger independently read from latest main at start.
- Two original full-size relevant paintings available for review, checked at phone-like bitmap size.
- Static contact-sheet and 16% edge-zone overlays were generated.
- Measured approximate RGB visual similarity in named architectural regions.
- Image-generation montage attempts rejected.

**NOT performed:** real Safari/iPhone hardware test, 3D camera, controller input, animation, renderer, WebGL, FPS/memory/battery, playable website, PWA install, engine code, browser regression test or Pages deployment. All remain outside authorized Phase 1 work.

## 5. G1 assessment and next development slice

| Art requirement | Result | Decision |
|---|---|---|
| Standalone peaceful Thimblebrook painting | New genuine landscape counterpart to accepted combat | **Strong improvement; composition-matched direction** |
| Exact pixel-level match | Similar architecture/geometry with residual differences | **Not certified exact** |
| Combat warning readability | Earlier accepted one-Barkling view; paired side-by-side tested visually | **Good concept target; no runtime proof** |
| Both dry dormant mill interiors | Earlier full-resolution paintings remain selected | **Established as concept references** |
| Upper Gallery entry thumb framing | New calculated crop and phone overlay | **Partially improved, still at edge** |
| Full Upper Gallery tracked reframe | Only conceptual storyboard, no genuine new full-quality painting | **OPEN** |
| Tavi eight-direction plus cast | New normalized existing-art comparison and original physical inventory QA | **Improved audit; production turnaround OPEN** |
| Final owner art gate G1 | Not requested/received for full packet | **PENDING** |
| Phase 2/game code | Not authorized | **LOCKED** |

### Next authorized Phase 1 slice
1. Produce a new **full-detail independent Upper Gallery painted frame** using the accepted painting's architecture but positioning Tavi and currently actionable anchors comfortably central, for both entry and next-traversal positions; check physical iPhone-like viewing size before owner reinspection.
2. Refine production-ready character turnarounds: eight truly matched physical orientations with lantern/satchel sides stable, plus principal cast uniform-proportion turnarounds.
3. Package a final owner-inspection set without manufactured progress percentages, invented roles or code/engine claims; do **not** auto-pass G1.

**The artistic target remains high and realistic 3D fidelity is not yet demonstrated.** The owner must explicitly accept the G1 art package and separately authorize Phase 2 before anything playable is built.
