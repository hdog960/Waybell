# WAYBELL — Project Charter and Source-of-Truth Rules
Version: Phase 0 / 1.0 | Status: AUTHORITATIVE DESIGN, NOT IMPLEMENTATION | Updated: 2026-11-10

## One-sentence vision
An original, richly crafted iPhone-first 2.5D action-adventure in which a young mapmaker uses echoes of forgotten roads to reconnect communities, explores interconnected regions and handcrafted dungeons, and learns that love and connection survive change.

## Fundamental product constraints (locked by owner)
- Project: **WAYBELL: The Roads We Leave**. Repository: https://github.com/hdog960/Waybell . Default branch: main. Intended public Pages URL: https://hdog960.github.io/Waybell/ (deployment unverified).
- No Codex, ChatGPT Work, Vercel, or external paid services. Use ordinary ChatGPT, the connected GitHub repository, free GitHub Pages and zero-cost locally/bundled libraries and assets with legally compatible licenses.
- Initial delivery: iPhone-first landscape browser/PWA; no native App Store promises, subscriptions, external backend, or multiplayer. Browser compatibility and offline behavior are acceptance-tested, not presumed.
- Original IP only: no Zelda characters, names, sprites, songs, dungeon copies, derivative textures, or reproductions. Ocarina of Time is a reference for emotional design principles only.
- Premium stylized diorama aesthetic: *true* 3D geometry and height in three-quarter perspective (not a flat sidescroller), expressive characters, strong lighting and art coherence.
- Touch controls must NOT obscure central play, puzzles, boss tells or HUD; prioritize safe-area support and two-thumb ergonomics.
- No game code, art-production phase, or Phase 1 until Phase 0 docs are verified. No automatic phase escalation at approval gates.
- Player's final approval controls art direction, vertical slice, and full-game acceptance.
- The design of a 18–25h main journey is a **goal, not an implementation estimate or completion promise**. Cut content quantity before sacrificing quality.

## Design pillars in priority order
1. Wonder before instruction: distinctive vistas, landmarks, curiosity.
2. Knowledge over numbers: ability-based traversal and rewarding recall.
3. Places become personal: authored character arcs and visible world changes.
4. Dungeons teach a language: observe, experiment, understand, combine, master.
5. Music and atmosphere carry memory.
6. Mobile clarity: every important interaction is readable and comfortable.

## Source-of-truth hierarchy
1. The user's latest explicit direction in the relevant chat.
2. This charter for locked constraints, approval rights, and project status.
3. docs/01 through docs/08 for their named subjects; cross-reference rather than duplicate detailed requirements.
4. docs/09-DECISIONS-AND-TRACEABILITY.md for decision status, scope and conflict tracking.
5. README for navigation only.
When material conflict occurs, log it in docs/09 and seek owner approval before changing a locked premise. Future releases must record versions and actual test evidence; a document declaring success is not test evidence.

## Authority / scope boundaries
- PHASE 0: documentation only. No gameplay implementation, asset generation, staging prototype, CI workflow, or public marketing screenshots as if playable.
- PHASE 1: art direction only after owner explicitly authorizes next phase; concepts are not final game assets.
- PHASE 2+: coding only after owner's approval; each phase has objective exit criteria in docs/08.
- Repository modifications: explicit requested documentation is allowed now. Never overwrite unrelated content.
- This is single-player and hand-authored. No procedural main dungeons, grind economy, gacha, consumable energy, loot-color treadmill, or mandatory online account.

## Definition of a complete Phase 0
- README links every authoritative document.
- Consistent cast, story ending, Wayline rules, ability mechanics, seven regions, six main dungeons and three optional dungeons.
- Detailed production roadmap includes gates, verifiable deliverables, dependencies, test criteria, risks and fallback scope.
- All documents committed to main; fetched/read back and cross-checked. Phase 0 signoff only pertains to *documentation*. It does not imply game/playable readiness or grant automatic Phase 1 approval.

## Change control
Use versioned updates in future; add decision records for scope-changing choices. Critical changes (story ending, rendering format, tools, region count, quality gates, service costs, monetization) require owner approval. Minor clarifications may be documented with explanation and date.

## Status at creation
Repository exists with a minimal README. Pages enabled per owner; no verified build. Phase 0 document package in progress. No game code or art-production assets.
