# WAYBELL — Detailed Phased Development Roadmap
Version: Phase 0 / 1.0 | Authority: task order, phase deliverables, evidence, release gates.
**NO PHASE 1 OR GAME DEVELOPMENT IS AUTHORIZED BY THIS DOCUMENT.** It is a plan, not a schedule promise. Each phase requires explicit direction and gates must never be self-approved when owner approval is specified.

## Development operating model
Unit of progress is a **verified coherent slice**, not a minimum run time or arbitrary version number. For each slice: inspect latest main -> state objective -> implement only authorized scope -> run appropriate tests -> inspect rendered result -> commit/reconcile -> verify deployed Pages if applicable -> report SHA, actual files and test evidence, remaining defects. No "done" for sketches, empty scaffolds or failed browser checks. Stop on owner approval checkpoints.

## Project gates and prerequisites
G0 Docs gate: all /docs/00–09 and README are authored, consistent, committed and fetched from GitHub. No gameplay assets or code. Gate can be verified without owner style judgment.
G1 Visual approval: owner approves actual original 2.5D character/environment/camera/style samples. No coding may substitute for this.
G2 Feasibility approval: iPhone web prototype proves real geometry, controls and acceptable mobile behavior; owner approves feel.
G3 Vertical-slice approval: player genuinely completes 45–60 min opening, enjoyable and aesthetic is acceptable.
G4 Dungeon benchmark approval: first complete dungeon meets puzzle, combat, art and boss standard; other dungeons reuse quality bar.
G5 Act I narrative and world gate: first two dungeons and rescue complete with persistent state.
G6 Full main story feature complete: all 6 major dungeons, main character arcs, connectivity and ending playable.
G7 Final release acceptance: optional content quality, visual/audio polish, performance, accessibility, saves and end-to-end tests pass; owner approves.

## Phase 0 — Authoritative preproduction documentation (NOW)
Dependency: repo created and available.
Deliverables: docs/00 Charter; 01 Design Bible; 02 Story; 03 World/Side Content; 04 Mechanics/UX; 05 Dungeons; 06 Art/Audio; 07 Tech/Test; 08 Roadmap; 09 Decisions/Traceability; root README. Cross-check naming, region graph, branch-order invariants, non-monetization, no paid services. Commit and fetch files. Record known uncertainties. Avoid game code, Phase 1 concept assets, engine packages or CI setup.
Exit G0 evidence: file list, repository links, stable commit SHA, content verification and contradictions checked. G0 completion does NOT authorize Phase 1.

## Phase 1 — Original visual language (ONLY IF OWNER AUTHORIZES)
P1.1 Select consistent environment/character material principles and color grammar (samples must be original or licensed).
P1.2 Draw/prototype 3D diorama orthographic perspectives for Thimblebrook, the panoramic Long Reach, Rootbound Mill.
P1.3 Design Tavi front/back/side/diagonal views, lantern and Rootspool, NPC silhouette comparisons.
P1.4 Establish lighting, layered height, target camera, UI-safe area, prop affordance sheet.
P1.5 Build art quality review packet with side-by-side detail and rejection notes. These are concept/proof visuals, not playable code.
Exit G1: explicit owner art acceptance. Do not advance merely because packet exists.

## Phase 2 — Engine and on-device feasibility
Depends G1 + authorization.
P2.1 Evaluate two no-cost WebGL stacks on actual iPhone, choose evidence-based engine.
P2.2 Create minimal multi-height walkable area, correct shadows, collisions and touch navigation.
P2.3 Add camera occlusion behavior, player idle/walk/turn, first landmark framing.
P2.4 Deploy minimal build to GitHub Pages under /Waybell/ and validate via public URL.
P2.5 Test Home Screen PWA experience, suspend/resume, save prototype, orientation, touch safe areas, iPhone overheating/perf.
P2.6 Record selected engine and measured scope constraints in decisions register.
Exit G2: real playable scene, no major mobile visual or input flaw, explicit owner go/no-go.

## Phase 3 — Premium opening vertical slice (45–60 min target)
Depends G2.
P3.1 Construct Thimblebrook residential loop, water crossing, scenic ridge and early ruins with authored NPC routines.
P3.2 Implement Tavi readable rig/animation, Orin and Nella key dialogue, opening story triggers.
P3.3 Add early enemies, shield/sword/dodge, checkpoint, accessible settings.
P3.4 Implement Echo Lantern Reveal and Replay tutorials; prototype Restore only if sufficient context.
P3.5 Build first small puzzle dungeon with fair hint/softlock handling and one encounter.
P3.6 Stage first road disappearance and the dramatic Long Reach scenic reveal/music handoff.
P3.7 Add Roadbook minimal map and manual/auto save; test load/reload and installable experience.
P3.8 Run at least one complete independent opening-session audit and fix most severe problems.
Exit G3: genuinely enjoyable and stable slice, verified on iPhone; owner approval required.

## Phase 4 — System infrastructure (reusable game backbone)
Depends G3.
P4.1 Region/portal graph and door/scene transition states; tile/mesh collision constraints.
P4.2 Event/quest flag framework with dependency checks and backtracking behavior.
P4.3 Complete Lantern modes, one active Echo/6 sec default and restore expiry safety.
P4.4 Tool framework for dedicated target behaviors, camera/auto aim and switch interactions.
P4.5 Enemy/boss state machines with visible telegraph audit.
P4.6 Save schema versioning, settings/accessibility, chapter/routine data, Roadposts.
P4.7 Deterministic test fixtures and basic reliable build checks.
Exit: reusable end-to-end systems proven in at least two distinctly themed test areas; no regressions in slice.

## Phase 5 — Long Reach and Wilderbloom / first dungeon benchmark
Depends Phase 4.
P5.1 Complete overworld first-visit route + gated discoveries and recognizable skyline.
P5.2 Develop Fernrest, forest routes and 3 forest enemy families.
P5.3 Rootbound Mill R01–R10 authored puzzles with item tutorial and shortcuts.
P5.4 Rootspool traversal/combat; Briarbell phases, forest bell reward, world state updates.
P5.5 Implement first region side stories/Waymaking where they reinforce progression.
P5.6 Full regression: no puzzle softlocks, robust iPhone camera and boss readability.
Exit G4: owner approves full dungeon benchmark before replicating dungeon pipeline.

## Phase 6 — Brasshollow and Act I completion
Depends G4.
P6.1 City layers, market routines, bridges/lifts and city state.
P6.2 Bellfound Choir B01–B10; Sunlens physics with wide aiming tolerance and chime/mirror clue UX.
P6.3 Cantor encounter, Nella reunion and Seren story scenes, regional repair.
P6.4 Implement first 4 chapters seamlessly and test full Act I save/reload.
Exit G5: complete Act I, no missing rescue or unexplained plot states.

## Phase 7 — Middle-game branch: Tidemarrow / Ashglass
Depends G5; independent substreams can be produced in either order but both must be integrated.
P7.T1 Reedhaven/wetlands, camera and water surfaces.
P7.T2 Drowned Archive T01–T10, Tideweights and Silt Librarian.
P7.T3 Blueprint half A, Yaselle [correction: canonical spelling **Yselle**], ferry/world states.
P7.A1 Emberhold/cinder passes, machinery and heat/contrast cues.
P7.A2 Hearth Forge A01–A10, Ironhand and Cinder Regent.
P7.A3 Blueprint half B, Dorrik arc and cooling tram.
P7.X1 Test both quest/dungeon orders, start/finish, side quest prerequisites, player item availability and Act II return states.
Exit: both permutations playable with no wrong dialogue or item dependencies. Note: canonical name always **Yselle**.

## Phase 8 — Snowglass and convergence
Depends Phase 7 plus chapter 8 return.
P8.1 Snowglass authored landscape/outpost and wind visibility.
P8.2 Sleeping Orrery S01–S10; tool interplay without arbitrary gating.
P8.3 Galecloak movement/landing and Asterion boss.
P8.4 Iven's decentralized model exposition and Nella/Orin subplot convergence.
P8.5 Validate cross-region tool backtracking, late player movement and story readiness.
Exit: final equipment unlocked; all story conditions for finale reachable.

## Phase 9 — Broken Horizon, climax and complete main story
Depends Phase 8.
P9.1 Construct disconnected but visually coherent final region and authored U01–U10 path.
P9.2 Implement multi-tool sequence and clear revisitable mechanism checkpoints.
P9.3 Stage ethical Seren confrontation; final network puzzle + battle.
P9.4 Create ending and epilogue variation flags plus postgame accessible memorial mode.
P9.5 Full main-story playthrough two middle-region orders; fix blockers.
Exit G6: finished story with six playable main dungeons and final credits; owner checks story pacing.

## Phase 10 — Optional depth and world transformation
Depends G6.
P10.1 Forgotten Tollhouse, Hollowglass Theater and Reedcrypt, each unique puzzle/boss/upgrades.
P10.2 Implement all 18 side quests with state fallback and coherent epilogue outcomes.
P10.3 Add all eight Waymaking restoration projects and route shortcuts.
P10.4 Add meaningful region revisits, secrets and Roadbook pages; reject filler.
P10.5 Optional-content playthrough and main-story-only regression.
Exit: completionist content enhances world but never breaks mandatory quest graph.

## Phase 11 — Art/audio, controls and accessibility completion
Can polish earlier, but final pass follows integrated content.
P11.1 Character animation consistency across all directions, shadow/foot contact, NPC gestures.
P11.2 Final region lighting/material identity; eliminate pop-in, broken meshes, depth-occlusion defects.
P11.3 Original music motifs and adaptive states, spatial/ambient sound and caption equivalence.
P11.4 Touch adjustment/landscape UX across supported iPhones; menus and Roadbook.
P11.5 Accessibility test matrix: reduced effects, text size, hints, aim, audio, color.
P11.6 Polish boss readability, combat timing, discovery pace and cinematic comfort.
Exit: no unacceptable visual/audio/UI defects on supported test hardware; comparative aesthetic owner review.

## Phase 12 — Release hardening and public verification
Depends Phase 11.
P12.1 Verify all quest flags, tool cross-interactions and puzzles from new save through credits in both branch orders.
P12.2 Regression matrix across browsers/iPhone hardware, save corruption, device pause/resume, PWA cache, Pages base path.
P12.3 Performance profiling and memory budget, loading progress and offline behavior.
P12.4 Documentation update, attribution/licenses, build reproducibility, release ledger.
P12.5 Verify deployed public Pages build *separately* from git commit/CI outcome, collect screenshot/observation evidence.
P12.6 Owner final review/acceptance; only then declare playable release ready.
Exit G7: green meaningful tests + authentic device and owner signoff + Pages proof. No fabricated version or tests.

## Quality decisions and stop/go
- Phase gates are conjunctive: failure in art, gameplay, mobile, test, or content means the phase remains open.
- Time/number of AI sessions is not a valid measure of delivered work.
- If full scope threatens quality, first cut optional content breadth and reduce geographic footprints; preserve core story, tool teaching, dungeon individuality and iPhone usability.
- Never solve Phase 2 feasibility failure by substituting a flat 2D game without owner permission.
- Every significant phase-gate change requires updating docs/09 with explicit owner approval.

## Definition-of-done checklist for each future development slice
[ ] Correct starting main commit verified
[ ] Work belongs to currently authorized phase
[ ] Implemented behavior evidenced by actual code/scene diff (when implementation authorized)
[ ] Automated tests run with outputs recorded, or transparently NOT RUN
[ ] Manual visual and device tests recorded, or NOT RUN
[ ] No new severe collision, depth sorting, camera/UX, control or progression defects
[ ] Commit and deployment state correctly reported
[ ] Owner checkpoint respected
[ ] Next slice concretely defined without claiming background work
