# WAYBELL — Phase 1 Visual Refinement Packet 02

Status: P1.1–P1.5 IN PROGRESS; **G1 NOT PASSED**.
Date: 2026-11-11. Authority: art-direction candidate and critical review; docs/00, 02, 06 and 08 remain binding.
No engine, gameplay code, actual 3D environment, browser app, or Phase 2.

## Authorization boundary
The owner approved the **overall visual direction** of Phase 1 board 01, then specifically requested further character, Thimblebrook, gameplay-camera, dungeon and combat/UI refinement. This does NOT mean the complete G1 art standard is approved. No Phase 2 authorization. Only original conceptual art, design-source vector graphics, static mobile-layout studies and written reviews are within scope.

## Deliverables produced and examined
- Character concept: tavi_s_waybell_character_design_sheet.png, with multi-view Tavi and supporting cast; not a precise final matched rig turnaround.
- Wayline/material concept: lanterns_bells_and_waylines.png; world symbols and antique materials; may be too detailed for actual iPhone UI.
- Village identity: golden_hour_in_thimblebrook.png; newly visible Wayline path inlays, civic bell markers, terrace paths and Orin at a map table.
- Dungeon layout concepts: rootbound_mill_dungeon_concept_board.png; mill interior, waterwheel and platform levels; not a completed first-visit architecture plan.
- New camera/location study: a_highly_detailed_cinematic_bright_fantasy_villa.png; 16:9 art, distinct Tavi, central road, stone bridge, bell stone.
- New static camera-touch annotation: waybell_phase1_touch_safe_zone_study.png. A 1600x900 art study with roughly 16% reserved on each edge for thumb controls and ~68% central playfield. **This is a drawn overlay, not a functioning control layout.**
- New phone-size review: waybell_phase1_phone_scale_review.png, a static 874x492 downsizing; no real hardware test.
- Original editable SVG source **in GitHub**: design/waybell-iconography-v1.svg — six concept glyphs for Reveal, Replay, Restore, Roadpost, Great Bell and Rootspool with deliberate amber, cyan and violet semantic roles.
- Separate seven-image conversation ZIP: WAYBELL_Phase1_Visual_Refinement_02.zip, SHA-256 c03e0a57a5cef2fbaa09ff056310061a09c95a5d5381ba9b5a82dcf9af62a05d. The ZIP and PNG illustrations are NOT committed to GitHub; only SVG source and written critique are committed.

Reject other generated presentation/dashboard variants that gave Tavi a red scarf/red cape, introduced an unsupported "Lira" ally, switched to sidescroller camera, or printed fake 90% completion/approval ratings. These are NOT canonical WAYBELL designs and must not leak into implementation.

## A. Canonical character visual proposal
**Tavi:** dark tousled brown hair, open curious face, teal-blue asymmetrical mapmaker cloak with thin embroidered map/road patterns, brass clasp, parchment shirt, practical brown boots, map satchel, compass, small brass Echo Lantern whose glowing core contains a geometric route. Tavi's teal cape is the strongest at-a-glance player marker. Small bell-and-road motifs must support rather than overpower the silhouette. Maintain cape edge, clasp, satchel, hairline, boot tops and lantern design across angles; no sudden alternate costume from individual generated frames.

**Nella:** energetic red-haired explorer with compact practical travel kit, distinct more athletic/expressive posture; not a bard or invented extra party member.
**Orin:** elderly bespectacled cartographer with gray-white beard, map tubes and a soft warm posture, not a wizard archetype.
**Seren Vale:** dignified navy/burgundy Bellkeeper with restrained brass, compassionate but stern expression; no demonic armor or conspicuously evil visual shorthand.

Current illustration offers front/side/back/three-quarter suggestions, but *not* eight clean matched directional views of uniform scale or proven game animations. **Next art requirement:** explicit 8-direction Tavi turnout and 6 emotions, lantern carry/holster and Rootspool attachment, plus Nella/Orin/Seren silhouette height comparison. Full final cast approval outstanding.

## B. Unique Waybell world architecture and icons
Storybook warmth is approved as broad artistic tone, but generic medieval fantasy alone is not enough. Every important travel node should carry an original Wayline/bell identity:
- **Reveal:** amber route on compass-like ring or embedded path glyph; the signature shape is a way with endpoints.
- **Replay:** two offset traversed tracks, cyan memory following amber original, not a summoner's copy.
- **Restore:** violet temporary translucent bridge/stair shape with obvious expiry; use different geometry/shape from red danger.
- **Roadpost:** navigational miniature bell integrated with a waystone; point of travel and social reconnection, not merely a lamp.
- **Great Bell:** major load-bearing civic architectural feature with distinct local shape; not repeatedly pasted onto every roof.
- **Rootspool:** brass vine reel that anchors to authored rings/vines; recognizable attachment carried by Tavi.
- **Roadbook/compass:** cartographic paper, stitched map lines, and inset waymarks as a consistent motif.

Visual colors: TEAL identifies Tavi/cartography; AMBER marks historical imprint and interactable wayline; CYAN Replay/motion; VIOLET temporary Restore; RED danger telegraphs. Back every color with distinctive silhouette and movement. Do not overdecorate ordinary village houses with magic signs. **The original vector icon sheet is a proposal, not final in-game pixel-size art.**

## C. Thimblebrook spatial-identity approval targets
Four memorable gameplay zones: Orin's home/map table, cozy cobbled main crossroads, stone bridge and river market, lookout ridge framing Long Reach. Elevated cottages, carved stone, oak, vines, flowers and paper lanterns are the material vocabulary. Village social routines/landmarks must remain recognizable when Act II refugees and shops arrive. The bellstone and map inlay should tell players something about the road system.

Visual no-go: a castle or giant cathedral replacing this small village; thick flowering plants blocking character feet or bridge rails; a painting with no plausible traversable route. Proposed village art has legible connecting lanes and good scale cues, but actual room-by-room navigation is not implemented.

## D. Three-quarter camera and iPhone safe zones
The new village scene is an excellent **location/material reference**, but it is still too cinematic: perspective closer to a third-person postcard than a fixed/elevated three-quarter gameplay camera. Tavi appears roughly one-quarter to one-third of image height, larger than an initial exploratory target (~10–16%, provisional) and does not demonstrate rotation/occlusion/depth sorting. **Do not pass it off as an actual in-game screenshot or approved camera.**

Safe zone exploration: reserve approximate outer 16% left and right for thumb interaction, protect central 68% for player, enemies, boss telegraphs, and puzzle objects. In a full-screen game, the actual clear view may require dynamic framing and UI flexibility. Left movement and right interaction/attack/dodge/tool, never control buttons over active targets. Verify with safe areas for notches and alternate aspect ratios later; no CSS/JS has been made.

Concept-level camera gate checks: Tavi's boots and shadow remain grounded; path edges and stair connections are obvious; bridge water and upper level separated spatially; foreground roof/tree can fade; small important characters stay recognizable; UI doesn't cover crossings, weak points, or controls. 874x492 static downsampling is only a **mock phone-size** check, not measured device performance.

## E. Rootbound Mill art review and consistency
**Lower turbine hall** = dormant vast wooden wheel, dry channel, stone gate controls, root-wrapped masonry, low bridge and vertical stairs; first-timer learns water-flow controls and Echo plate.
**Upper spindle galleries** = multiple timber balconies with readable elevations, fixed Rootspool anchor rings and moving-platform route; forms a return shortcut when the water flow is restored.
Character and anchors have clear contrast from foliage and hanging ropes; bridge rails must not hide the player.

Critical canon check: existing concept images show running water and wheels. These are **post-restoration references only**. The initial dungeon must appear dormant until the player repairs it. A lower panel of the mixed interior concept includes an ornate stained-glass hall reminiscent of Bellfound Choir; this must not be adopted as a Rootbound Mill room. Still missing two coherent, clearly labeled first-visit interior gameplay views (not just scenic paintings).

## F. Combat / UI readability
Aim at three-quarter view, not side-scrolling. Tavi body, feet and attack direction must be visible; enemies telegraph with distinguishable wind-up pose plus floor danger shape. No enemy attack may be obscured by tree, wall, bloom or right-thumb buttons. For touchscreen, low-button-count adaptive action scheme with generous size and feedback is the intended direction; not yet implemented. Red AoE warning must be legible in motion and distinct from amber path magic and violet restoration.

A prior side-on duel and decorative dashboard mockups **fail** the intended camera and canonical-character constraints; they are not proof of combat design. A new true-camera combat proof remains an open Phase 1 task.

## G. Honest technical feasibility limit
Illustrations are MUCH easier to perfect than actual dynamically rendered, animated 3D worlds. These visual references are a target, not proof that all detail can ship at 60 FPS on iPhone. Later phases may use authored bounded scenes, reusable meshes/materials, stylized lighting and asset reuse to achieve the same mood within zero paid services. No engine selection or device FPS claims now; all require separately authorized Phase 2 and actual iPhone testing.

## Current Phase 1 assessment
| Work item | Status | Evidence / remaining work |
|---|---|---|
| P1.1 palette/material/symbol grammar | DRAFT ADVANCED | New original editable SVG; needs icon-size checks |
| P1.2 village and dungeon visual style | PARTIAL | Selected village and mill concepts; first-visit dormant mill and true camera pending |
| P1.3 canonical cast and Tavi | PARTIAL | Good candidate character sheet; uniform 8-direction + consistent props pending |
| P1.4 camera/touch/combat | PARTIAL | New static annotated 16:9 illustration; true high-angle combat mock pending |
| P1.5 review and critique | DONE FOR PACKET 02 | This honest work log, acceptance/rejection notes, conversation ZIP |
| G1 owner visual approval | NOT PASSED | Broad mood approved, final coherent package not signed off |
| Phase 2 | NOT AUTHORIZED | No engine or game code |

## Next Continue Development slice — remain strictly Phase 1
1. Create a consistent eight-direction Tavi design and Nella/Orin/Seren scale sheet.
2. Produce a correct elevated three-quarter village **gameplay framing** illustration (less heroic postcard), with Tavi smaller and one clear destination.
3. Produce dormant Rootbound Mill lower/upper rooms with clearly marked usable Rootspool hooks.
4. Produce a matching-perspective enemy warning/combat concept inside safe zones.
5. Evaluate phone-scale legibility; request final owner signoff only after missing samples are actually convincing.

## Verification and limitations
The SVG and review text have been submitted to GitHub using connected repository tools; their readback is required to confirm persistence. Other images are preserved as conversation files and ZIP, not GitHub binaries. No external paid service, Vercel, Codex or Work. No real browser run, native iPhone test, game code, assets built into engine, or public playable site. **G1 and Phase 2 remain locked.**
