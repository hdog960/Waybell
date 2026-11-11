# WAYBELL — Gameplay Systems, Progression, and Interface
Version: Phase 0 / 1.0 | Authority: player-facing rules, equipment mechanics, controls and persistence behavior.

## Player-state core
A single controllable hero, Tavi. 3D traversal primarily on readable walkable surfaces with hand-authored changes in height. Persistent health upgrades, major equipment, optional lantern enhancements, flags for milestones, routes, side quests, Roadbook discoveries, settlement changes, and preferences. No XP levels or power-by-grind.

## Standard actions
Walk in any horizontal direction; sprint (no punishing stamina meter for ordinary exploration); context action; limited contextual ledge climb; swim in approved water; block with shield; light strike; charged strike; dodge with clear recovery; activate equipped tool or lantern. Contextual jumps occur with obvious geometry; do not demand blind diagonal jumping or persistent camera rotation. Ground shadows/landing silhouettes must accurately match feet and elevation.

## Echo Lantern interaction specification
Three modes, explicit feedback, highly constrained:
- **Reveal:** Show only authored Wayline marks, recorded impressions, or hidden glyphs in range; intensity/sound rises toward nearby echo features. No full detective-vision wallhack or revealing arbitrary invisible rewards.
- **Replay:** Record up to SIX seconds of player locomotion and designated resonant interactions, then spawn ONE Echo that repeats exactly once. Echo cannot carry inventory, deal direct weapon damage, permanently operate ordinary physical switches, solve anything without a predefined resonant interface, or independently navigate on its own. It may draw attention from enemies for a short period when enemy archetype permits; no infinite aggro abuse. New recording replaces prior Echo. Failure/abort returns control immediately and restores puzzle to safe retry state.
- **Restore:** Temporarily solidify only specially marked lost bridges, stairs, or mechanisms. Clear expiry warning/visual and forgiving grace period so a platform does not disappear under a player with no recovery. Permanently repaired road segments are triggered by story/Waymaking flags, not lantern spam.
- Optional upgrades: stronger clue reception (Tollhouse), +2 sec recording to 8 sec (Theater), expanded restore range at compatible fixtures (Reedcrypt). These do not gate main story.
- Resonant objects visually distinguishable from normal objects even with color-blind support. Every Echo puzzle has an authored simple baseline plus advanced combinations later.

## Major exploration tools
**Rootspool (Wilderbloom):** Target designated organic anchors at visible range; zip/swing over gaps and pull loose handles/armor. Cannot grapple anywhere arbitrarily or collide through walls.
**Sunlens (Brasshollow):** Redirect light from authored sources via oriented reflective surfaces; reveal glyphs and dazzle specific enemies. Do not require subpixel joystick precision.
**Tideweights (Tidemarrow):** Toggle buoyancy modes in buoyancy-marked water volumes; sink, float, resist directed currents. Never mandate long breath-holding or hard-to-read underwater depth.
**Ironhand (Ashglass):** Push/pull polarity-marked metal pieces on constrained tracks; redirect mechanisms and expose armor. Must not drag mission-critical objects out of puzzle bounds.
**Galecloak (Snowglass):** Glide from safe-height launch and ride authored visible wind lanes. Clear landing zones and automatic camera adjustment; no endless unrestricted flight.

**Three-job rule:** Each major item must have at least one substantial traversal use, one environmental puzzle use and one combat or encounter use outside its acquisition tutorial.

## Combat model
Lock-on is optional/soft on touch: nearest intentional facing/aim target in a short cone, with manual correction and prominent target feedback. Basic sword/shield combat plus dodge and charged move. Player attack must cause visible contact/impact feedback and sound. Enemies broadcast attack with wind-up animation, distinct audio and ground indicator if AoE. No offscreen instant rush, behind-foreground attacks, or undodgeable sequences. Use brief invulnerability after taking damage. Damage values provisional; balance with tests rather than document false final numbers.

### Enemy behavioral roster (target 20 base types)
Wilderbloom: Barkling charger, Thornhopper leaper, Mossback tank.
Brasshollow: Brass Sentinel shielder, Mirror Wisp teleport, Watcher ranged.
Tidemarrow: Mireling ambusher, Reed Stalker dart user, Siltbound Guardian heavy.
Ashglass: Ember Crawler swarm, Ironbound Soldier armored, Furnace Wraith cone flame.
Snowglass: Rimehound flank, Gale Wraith wind zone, Crystal Guardian reflect.
Long Reach: Field Nibbler nuisance, Roadbound Shade melee, Bellscar Scout ranged.
Broken Horizon: Echo Phantom mimic, Fractured Custodian mixed-system elite.
These are **20 distinct mechanics to prototype and validate**, not a promise of 20 completely different rig families. Boss designs in docs/05. Enemy variations must materially change behavior, not just recolor.

## Boss readability
Major bosses: 3 primary phases maximum unless extremely short, clear transitions, readable weak points, and one explicitly taught equipment-based counter. Checkpoints immediately outside bosses, skippable return dialogue and no mandatory redoing puzzles on defeat. No HP inflation to extend length.

## Health, difficulty, failure
Start 6 health segments, maximum planned 12, awarded from story and optional exploration. Normal attacks cause discrete predictable damage; upgrades increase health or combat options, not 200 stat multipliers. Three presets: Story (less damage + forgiving timing), Adventure (default), Legend (stronger pressure + tighter timing, no grind). Difficulty changeable in settings, never locked behind restart. Death respawns near checkpoint, retains collected progress, resets only local encounter and transient puzzle interaction state.

## Economy
Waymarks are a single basic currency used for standard consumables, map supplies, cosmetic outfits and small nonessential equipment improvements. Currency acquired by ordinary exploration and quests, without repetitive farming. No paid purchase integration in the prototype; no randomized scarcity or premium pay-to-advance. Money must never gate mandatory keys or chapter progression. Item inventory limited curated set; tools not consumable. No durability loss.

## Roadbook and quests
Roadbook combines local map, discovered features, player markers, quest clues, character notes, bestiary and echoes. The map is hand-authored and progressively revealed, but retains every known location. Quests have readable log state: undiscovered, available, active, completed, changed due to world state. Clear optional/must-do differentiation. No roaming minimap clutter or incessant popups.

## NPC interactions and temporal presentation
Authored daily routines with schedule fallback (critical NPC interaction availability always guaranteed). Weather and day/night provide atmosphere and few targeted interactions, never forced waiting to progress. Wait-to-morning at inns/safe areas. Relationship consequences tracked via finite quest states; not simulated autonomous agent population.

## Two-thumb iPhone contract
Landscape orientation; left area devoted to directional movement, right to contextual action, attack/defend/dodge, and active tool. Central 2.5D playfield must stay clear; HUD takes minimal corner/peripheral territory and never masks boss telegraphs. Safe areas, viewport shifts, device proportions, large touch targets, and adjustable controls must be evaluated on actual devices. No page scrolling, pinch-to-zoom causing browser navigation, or accidental long-press text selection. Navigation and combat visible at standard iPhone brightness. Settings available before first battle.

## Accessibility contract
Separated settings for difficulty, puzzle hints (nudge -> clue -> direct), damage intensity, text size, subtitle/audio-cue captions, high contrast interaction glyphs, reduced shake/flash, adjustable button placement, haptics toggle, simplified aiming options, and tap/hold alternatives where possible. No vital clue carried exclusively by color or sound. Avoid making the accessibility options punish rewards or story.

## Save behavior and compatibility
Autosave at region transitions, completed quests, equipment pickup and checkpoints; manual safe-area save. Versioned serialization; safe handling of corrupted/incomplete local storage; backup or export strategy to be explored in Phase 2. Clear notice that browser storage can be deleted by user or OS: promise reliable practical persistence but not guaranteed cloud sync without backend. Save slot model: at least one robust profile, more only if testing supports. PWA caching must not serve mismatched content versions after deploy. Every significant milestone can be reloaded with flags consistent.

## System acceptance tests
- Replay six-second sequence and swap recording during it; no more than one Echo; controls immediately return on abort.
- Every action on a doorway, one-way ledge, water border, moving lift, wind zone, and road-restoration tile.
- Player cannot get stranded due to temporary platform expiry; retry loops have no lost items.
- Branch order Tideweights->Ironhand and reverse; all required content reachable.
- Boss controls remain accessible even with larger text/high contrast mode.
- New saves, existing saves across updates, interrupted writes and offline-to-online PWA version changes.
- Persistent item, quest and route states agree after restart.
