# WAYBELL — Technical Feasibility, Architecture, Build, and Test Strategy
Version: Phase 0 / 1.0 | Authority: technical constraints and future verification criteria. NO ENGINE OR CODE IS SELECTED YET.

## Locked deployment and cost constraints
Official repo: https://github.com/hdog960/Waybell ; target GitHub Pages https://hdog960.github.io/Waybell/ ; owner says Pages enabled. Static GitHub Pages only for initial prototype, hosted free subject to GitHub's published use limits. No Codex, ChatGPT Work, Vercel, third-party paid hosting/API/asset library, backend account, DRM, in-app checkout, multiplayer server, AI inference service or other recurring expense. Repository created; current docs-only setup is NOT a deployed game.

## Engine evaluation (Phase 2 decision)
Select a browser-friendly GPU 3D engine capable of stylized true 3D diorama environments, WebGL fallback, light/mobile hardware, PWA delivery, and manageable self-hosted bundle. Candidates for a small technical spike (not predetermined): Three.js, Babylon.js or comparable no-cost permissively licensed option. Evaluate real iPhone safari: scene stability, input latency, geometry+lighting, occlusion/collision, animation, load/memory, asset export workflow, license. Favor the simplest proven stack; avoid adding dependencies for novelty. No engine lock in Phase 0 and no package installations yet.

## Proposed architecture (concept)
- Static site SPA / web asset bundles served at Pages project subpath `/Waybell/`; root-relative URLs need caution.
- Scene module: region chunk loading, scene switch state and camera framing.
- Simulation module: movement, collision, elevation, actions, combat, Echo object restrictions and puzzle events.
- Content module: authored scene metadata, puzzle rules, region graph, NPC schedules, quest flags and dialogue.
- Presentation module: render materials/lighting, animations, audio zones, menus, touch input, subtitles and accessibility.
- Persistence module: versioned local save schema, checkpoints, graceful data fallback, PWA asset caching strategy.
- Validation module: deterministic puzzle unit scenarios, integration checks, browser smoke tests and human device audits.
- No network play or mandatory online persistent server.

## Mobile performance and delivery targets
Target 60 fps on validated supported recent iPhones if sustainable; stable 30 fps fallback if required. Frame pacing, total JS and asset download sizes, battery/thermal behavior, orientation change and long-sessions must be measured, not claimed. Scene contents must fit memory constraints: texture atlases, LOD or authored occlusion, compressed assets when platform support verified, only needed chunks active. Prefer original low-to-medium poly sculpted geometry with strong silhouettes over heavy effects.
Load startup should show meaningful progress and error fallback. Use responsive viewport, device pixel ratio scaling, safe area, loss/restoration of WebGL context, pause on background, resumption after lock/unlock and refresh.
Avoid glitched geometry, transparent wall sorting, banding, clipping, walls popping out, character feet floating or hidden touch UI. Document target phone models upon testing.

## Camera/render and interaction policy
Three-quarter 3D, actual traversable raised platforms and multi-level geometry; no fake flat world that merely looks isometric in concept art. Collision separated from decorative meshes. Visibility management with tested fading/roof culling plus safe ray checks; never let enemies strike invisibly behind a camera occluder. Map world-space targeting into finger-friendly interaction zones; snap to valid target when visually nearby, otherwise make target affordance explicit.

## Browser and PWA constraints
- GitHub Pages static deployment can deliver assets and installable PWA; test manifest, icons, service worker caching and HTTPS when implementation begins.
- Offline support is an aspiration to validate on iOS Home Screen, not an assured capability. Service worker update logic must not mismatch save schema and asset manifests; support clear reload/recovery affordance.
- Browser local storage/IndexedDB is not a guaranteed backup. Evaluate optional manual save export/import with user gesture if no backend; do not promise multi-device cloud sync.
- No paid or user-data services; minimal necessary telemetry only if user explicitly consents (default none).

## Save schema concept (no schema implemented yet)
Fields: `schemaVersion`, `profileId`, `chapter`, `region`, `safeSpawnId`, `healthMax`, `healthCurrent`, `toolUnlocks`, `lanternUpgrades`, `roadpostFlags`, `waymakingFlags`, `questFlags`, `npcMilestones`, `roadbookDiscoveries`, `currency`, `preferences`, `lastSavedAt`. The team must define checksum/backup strategy, migration fixtures and guardrails in Phase 2. Do not save transient Echo recordings or mid-animation positions if unsafe; resume at safe spawn after interruptions.

## Git workflow policy
Owner-approved next phase only. Keep docs under /docs; later code under tested structure. Feature work through traceable commits/PRs, no misleading "deployed" claims, no destructive overwrites of owner changes. Before merge check branch freshness and integration tests; avoid bypassing a failing test solely to report progress. Log exact commit SHA, changes, tests, known defects, mobile acceptance and Pages checks. GitHub Actions may assist if within the owner's free plan/quota; not an autonomous AI developer. No requirement to add Actions during Phase 0. Manual inspect public Pages separately from GitHub commit status.

## Automated test plan (for future implementation)
1. Unit/rules: inventory unlock ordering, world graph reachability, chapter branch permutations, Echo replay boundaries, Restore expiry safety, currency not blocking required progress.
2. Puzzle fixtures: each mandatory puzzle has preconditions, hints, solution path, failure/reset state; build deterministic scenarios for boundary conditions and tool absence.
3. Combat: telegraph lead times, damage, stun, dodge, shield, boss phase transitions and defeated checkpoint persistence.
4. Save/version: clean start, reload at chapter transitions, mid-dungeon checkpoint, storage unavailable/full, interrupted writes, invalid schema, migration to new schema.
5. Browser: hosted project path, asset requests, menu responsive layout, keyboard controls for dev, iPhone touch, landscape, viewport safe areas, page scroll disabled.
6. Accessibility: high-contrast text and cues, accessible subtitle layout, reduced motion, difficulty, hint options and color-independent puzzles.
7. End-to-end: full main quest in BOTH permutations (Archive before Forge, Forge before Archive), all side content and zero side content, all 9 dungeons, credits/postgame.
8. Deployment: verify exact public Pages URL in remote browser after publish, confirm correct content version, all assets accessible, PWA manifest and save reload.
No automated test replaces actual human assessment of camera, art, emotional pacing, mobile ergonomics and music.

## Verification evidence format (future releases)
Release ledger entry: version + date + branch head + commit URLs + changed files + actual features exercised + test commands AND outputs + browser/device session observations + Pages URL + open bugs + phase gate status. Clearly distinguish NOT RUN, PASS, FAIL and NOT APPLICABLE. An unexecuted tool call or a file edit is not a confirmed deployment.

## Risk register and mitigations
R1 Browser 3D performance insufficient -> reduce area density/effects, limit render distance by authored framing, prefer bounded scenes before lowering character quality.
R2 iOS Safari PWA storage quirks -> explicit save backups/export if feasible, checkpoints and schema tests.
R3 Giant scope 18–25h unrealistic -> preserve polished 45–60 min slice, reduce optional areas or compress region footprints, retain narrative/dungeon quality.
R4 Multi-tool puzzles arbitrary -> mechanic tutorials, readable icons and hint tiers.
R5 Art asset inconsistency -> approve style packet before volume production; maintain style sheets and reference scene.
R6 Height and camera prevent clear control -> increase projection/landing guides, camera occlusion, simplify jumps, touch tests.
R7 GitHub Pages base path mismatch or stale caches -> build/deploy smoke tests and versioned cache policy.
R8 External assets/copyright -> original work or explicit license inventory.
R9 Free tool quotas change -> remain within usable free tier or simplify workflow without charging the owner.
R10 Story contradiction -> chapter/quest state graph, docs source hierarchy and owner-controlled change log.

## Technical decision gates
Phase 2 begins ONLY after visual gate and explicit authorization. It cannot pass until user can play an actual touch-controlled *true 3D* scene at project Pages URL with stable persistence and no blockers. Exact engine, input treatment, PWA offline strategy and performance target selected on measured evidence, recorded in docs/09.
