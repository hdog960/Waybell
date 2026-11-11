# WAYBELL — Rootbound Mill Art-Direction Contract 07
Authority: Phase 1 visual/art direction only • Updated 2026-11-11
Status update (Review 08, 2026-11-11): **Both Lower Hall and Upper Gallery have standalone painted direction references. Upper gameplay framing still fails proposed thumb-safe test; G1 not passed.**
Reference canon: docs/05-DUNGEON-AND-ENCOUNTER-BIBLE.md; docs/06-ART-AUDIO-AND-ACCESSIBILITY.md; docs/15-PHASE-1-VISUAL-REVIEW-06.md.

## Original new painting and provenance
Original image-generation result created in this Phase 1 session:
`a_highly_detailed_cinematic_game_like_fantasy_en.png`, standalone **1672×941** image, held in the originating ChatGPT conversation, **not in the GitHub repository**. The artwork depicts an overgrown mill interior, a huge nonmoving waterwheel jammed by thick roots, clear dry masonry and cobbles, a visible small teal-caped Tavi, light from upper windows, a route via stair/wood bridges, a floor emblem and Waybell banners. It is a high-quality *illustration*, not an in-game screenshot, render, 3D model or an environmental asset scene. Filename and visual critique are indexed here so subsequent iterations can reuse it from the user's conversation assets where accessible.

## Room A: Lower Turbine Hall — accepted visual candidate
**Emotional message:** this place once moved with water and work; now the roots hold the machinery silent. Its grandeur comes from believable mechanical mass and the feeling that a future repair will change the room.

**Essential authored landmarks and plan:**
- Monumental wood waterwheel anchored in stone on frame RIGHT, clearly not spinning, with roots entering its hub and heavy vertical supports. It must not show active spray, waterfall, white foam or moving paddles at FIRST VISIT.
- Floor-level stone path with unobstructed walking pocket for Tavi (foreground/center-left) and at least two visible routes: an ascending stone stair on the left and a rail-protected mid-height catwalk leading toward the hub.
- Empty/deactivated intake channel or blocked trough between lower walkable ground and wheel-support block. Visually distinguish a dry channel from reflective water; future restored state may introduce water.
- Wall hand-crank/sluice access with recognizably manipulable bronze lever, physically reachable via safe platform. A resonant Echo plate in a floor location cannot look identical to a decorative compass crest; icon treatment to be designed.
- Horizontal upper timber supports visibly bear the catwalk. No levitating rails, discontinuous stairs or dark void that makes depth indeterminate.
- Natural roots and moss remain environmental decoration, except selected root-constrained mechanics; do not imply every vine can be grappled.
- Warm high-angle daylight illuminates safe traversal path; use restrained dust particles and lamplight as secondary accents, not magical glow everywhere.

**Quality assessment:** clear atmosphere and surprisingly readable vertical composition, with a distinct central wheel and stageable path. Risks: visual density near the staircase, bright highlights can overwhelm puzzle markers, and the rightmost wheel/root mass partially approaches the peripheral potential action-control zone. At actual 874×492 static downsampling Tavi remains identifiable; small decorative levers become harder to distinguish. Recommend enlarged interface affordance and optional camera recenter when approaching a lever.

## Room B: Upper Spindle Galleries — partial reference, not approved standalone
Reference only: `04_upper_gallery_REFERENCE_CROP_720x405.png`, manually cropped from a lower-right panel of generated multi-panel board `a_highly_detailed_cinematic_painted_3d_illustrat.png` in the same conversation; this is explicitly NOT a separately generated 16:9 upper room at full resolution.
**Required visual composition for next standalone original painting:**
- Camera from upper diagonal toward a wood-bordered central void; at least three clearly connected walkable elevations, stairs, railings and support beams.
- A fixed Rootspool anchor ring on exposed overhead beam, distinct amber-brass ring with cyan/teal knot at center; two others visible deeper along the traversal route.
- Upper spindle, pulley and gear assembly DORMANT and visibly unpowered, with taut but stationary chains. Do not use moving lift/turbine motion cues in the first-visit shot.
- A restrained sliver of the dry wheel or channel may be visible below as a spatial link to Room A, but NOT an active waterfall.
- One Tavi of same proportions and apparent height as Lower Hall's regular gameplay camera, to establish platform scale and rail occlusion.
- Readable route from stair arrival -> mid level -> anchor traversal -> far exit, with deliberate side balcony as optional discovery.
- Keep sky or external landscape out of focus behind windows; room geometry must remain legible at phone scale.

## State transition art: BEFORE vs AFTER restoration
**Before:** dry; wheel seized; no moving chains, lift or flowing current; subdued ambient sound and dusty shafts.
**After:** repaired water channel carries water, wheel turns visibly, spindles rotate, floor/glyph lighting becomes more energetic, and shortcuts open. This deliberate contrast is a major emotional payoff and must not be spoiled in the initial paintings.
Camera anchor coordinates, room transform matrices and exact 3D topology are *not* locked by concept art; Phase 2 must test actual geometry after approval.

## Linked original editable geometry references already on main
- `design/phase1/rootbound-lower-hall-dry-fullframe-v3.svg`
- `design/phase1/rootbound-upper-spindle-dry-fullframe-v3.svg`
- `design/phase1/rootbound-first-visit-visual-contract-v2.svg`
These are authoritative **diagrammatic** source for connectivity and dry-state rules; imagery alone cannot approve a gameplay room.

## 5 explicit art tests before final G1
1. Side by side at native 16:9 without cropping from a layout board: both individual paintings must appear from the same architectural family.
2. Verify absence of flowing water / rotational motion cues in *both* first-visit images.
3. At 874×492 static phone-size, Tavi, staircase, interactable gate and Rootspool rings must be discernible.
4. Create a soft transparent edge-zone overlay (16% each edge as proposed, not final UI geometry) and reject if required puzzle objects are obscured without camera remedy.
5. Compare proposed 3D material counts and silhouettes to available free production pipeline *during later authorized phases*. Do not claim illustrated details can already run on iPhone.

## Non-negotiable honesty
No produced 3D geometry, playable room, tested shaders, collision, hitboxes, iPhone renderer, or functioning water animation. The selected Lower Hall painting is a direction reference, not an implemented result. Final G1 and Phase 2 remain explicitly locked.

## Review 08 addendum — Upper Gallery painting established (supersedes earlier 'missing standalone' status)
New independent **1672×941** original Upper Spindle Galleries illustration: `a_richly_detailed_high_quality_stylized_fantasy_g.png`. Its full-resolution image and comparable prior Lower Hall are available in the originating conversation's `WAYBELL_Phase1_Review08_Art_Evidence.zip`; they are NOT committed as image binaries in GitHub. Full factual critique: [docs/17 review 08](../../docs/17-PHASE-1-VISUAL-REVIEW-08.md).

**Now passed as visual concept:** one high-quality standalone Upper Spindle Galleries painting, dry and dormant, visually coherent with accepted Lower Hall; new routes and fixed anchor rings are illustrated. **Not passed:** Tavi and an outer anchor sit beneath provisional mobile thumb zones, so gameplay framing needs a deliberate correction; real 3D/collision and phone performance remain untested.

Original editable source-controlled art-staging schematic: [upper-gallery-readability-and-traversal-v4.svg](upper-gallery-readability-and-traversal-v4.svg), showing route, spindle, proposed anchor points and thumb-area risk. The previous section's crop is historical/older work, not the only remaining art source. Do not claim G1 or Phase 2 ready.

## Review 10 addendum — camera entry framing study, not a new painting
The accepted standalone Upper Gallery painting now has an explicit **source-pixel cropped entry-camera test** (original source crop x=0, y=76, 1200×675, upscaled solely for comparison), shown at 874×492 with provisional 16% left/right thumb areas in the Review 10 ZIP. It places Tavi around 18% of frame width, improving on the original ~13%, and centers the first two nearby Rootspool rings. This is only a **partial composition correction**: Tavi is near the left safe-area boundary and the follow-camera for the next/far ring remains unpainted and untested.

Source-controlled diagram: [upper-gallery-camera-measured-audit-v6.svg](upper-gallery-camera-measured-audit-v6.svg). Complete audit: [Review 10](../../docs/19-PHASE-1-VISUAL-REVIEW-10.md). Do not call this an independently generated full-resolution replacement, functioning camera, completed mobile-UX pass, or a G1 approval.

## Review 11 addendum — improved premium standalone Gallery painting
A new, completely standalone 1672×941 Upper Spindle Galleries painting, `a_highly_detailed_cinematic_2.5d_illustrated_gam.png`, now provides a better full-quality entry-camera visual than the prior source. Tavi stands near 42% of frame width, and both pertinent Rootspool rings are central near 50% and 63%; the outer proposed 16% thumb zones do not obscure those subjects in a new 874×492 static comparison. Wheel/gears are stationary, no flowing water appears. Full evidence and a phone-size overlay are in the conversation's Review 11 ZIP; the painting is **not** committed to GitHub as a PNG.

**Still open:** Tavi is larger than the intended wide exploration camera (roughly a quarter to a third of painting height), and no actual moving camera or 3D rendering has been tested. The source-controlled QA illustration [upper-gallery-camera-acceptance-v7.svg](upper-gallery-camera-acceptance-v7.svg) records this art-direction state. See [Review 11](../../docs/20-PHASE-1-VISUAL-REVIEW-11.md). G1 remains pending and Phase 2 locked.
