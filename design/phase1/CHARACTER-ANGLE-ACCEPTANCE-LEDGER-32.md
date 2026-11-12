# WAYBELL — Phase 1 Character Art Acceptance Ledger 32

**Date:** 2026-11-12 (America/Indiana/Indianapolis)  
**Starting independently verified `main`:** `3331be737da98e56350a9e3a5f763e9e9bbec6fa`  
**Authority:** Phase 1 art research only. **Owner G1 final visual signoff PENDING. Phase 2/game code LOCKED.**

## Result, stated without inflated painting counts

Two new image-generation attempts intended to produce ONE genuine full-size **Orin BACK**:
1. A WAYBELL “Review 32” board with multiple Orin figures, fake GitHub SHA, progress labels and a fake Continue button.
2. An **Orin BACK/LEFT/FRONT triptych**, with embedded captions and an altered older-looking outfit.

**BOTH rejected completely.** Neither is an independently composed single-person native full-body premium portrait. No crop, stretch or recolored panel was substituted. The invented release/verification/approval claims displayed in the generated image are **NOT** real work evidence.

**NEW PREMIUM PORTRAITS ACCEPTED = ZERO.** No qualifying Orin BACK/LEFT or Seren RIGHT/BACK/LEFT painting. No repaired Orin right-profile PNG. Tavi/Nella art unchanged.

## Actual preserved original independent painterly source inventory

| Character | True original full-size painting files | Unique preliminary view coverage |
|---|---:|---|
| Tavi | 14 (eight original directional paintings + six alternatives) | Eight unique directions, still not physically matched |
| Nella | 4 | FRONT, RIGHT, BACK, LEFT |
| Orin | 2 | FRONT, RIGHT only; BACK and LEFT **MISSING** |
| Seren Vale | 1 | FRONT only; RIGHT, BACK, LEFT **MISSING** |
| **Total** | **21 existing, zero new** | Preliminary concepts, not 3D/game characters |

Verified all **21/21** original raster files were included in Review32 ZIP byte-for-byte from Review31. Existing Thimblebrook peaceful/combat and dry-first-visit Rootbound Mill world reference paintings remain unchanged; no executable source or Pages modification.

## Substantial authentic art-development work: figure-focused source alpha research

Rather than falsely accept another promotional character board, made a **manual-seeded source-portrait silhouette study** for:
- Orin genuine FRONT (`19_NEW_ORIN_FRONT_INDEPENDENT.png`), exact original SHA `6dc40ca712ff17b2758d809416e55267954a76b07e05b8ddbc77c49071867fa4`
- Orin genuine RIGHT (`21_NEW_ORIN_RIGHT_PRELIMINARY.png`), SHA `4667e38208de608b6fb21e62c0b204111be0e03ffc57baa6a0602d8b8041eb38`
- Seren genuine FRONT (`20_NEW_SEREN_FRONT_INDEPENDENT.png`), SHA `660cffb56a51c1bb6845f70843508146c712aaf10bc97f7c8b9469534dd22967`.

Author-created polygon foreground regions and targeted garment/staff seed boxes were run through OpenCV GrabCut, hole-fill and modest feathering. This yields **three technical source-derived 1024×1536 RGBA alpha probes** and **three flat dark silhouettes**. The latter demonstrate better **character silhouette shape readability** at a static 874×492 composition, not an actual player sprite or game camera.

**Production-alpha acceptance: FAIL.** In the genuine source-backed alpha comparison, orange parchment halo/filled areas remain prominent around Orin RIGHT's head/rod and under boots; fine curly hair, pale facial skin and cream fabric blend with background. Flat silhouettes are readable but some contours are artificially boxy/over-inclusive, notably the right-hand staff. No accepted fully transparent layered premium character asset resulted. Previous Review31 unaccepted auto-matte status unchanged.

## New source-controlled original art-preparation assets

- [**Orin/Seren silhouette seed polygons v1**](art-prep/orin-seren-source-silhouette-seeds-v1.json): original exact **1024×1536** manually authored foreground shape coordinates for three specific original images, hard foreground garment/rod boxes, expected SHA hashes and explicit failure observations. This is a real editable art-prep shape source rather than a decorative vector turnaround.
- [**Experimental art-only silhouette reproduction script v1**](art-prep/experiment-alpha-seeds-v1.py): original local-source image QA/reproduction script, does not alter any native input PNG, does not implement a game, creates research-only masks with verified SHA input checks. Original source PNGs are **not hosted on GitHub**; running requires the local source images from the conversation evidence archive. Its output must **never** be treated as an approved production sprite.

The actual research PNGs are bundled in the downloadable conversation packet, not uploaded to GitHub binary art. Existing Orin garment v4 and prior costume sources remain preserved.

## Actual static art size and source-quality QA

`33_STATIC_874x492_MASK_SILHOUETTE_RESEARCH.png` displays three flat figure masks in a phone-sized **static** visual rectangle; `34_MASK_RESEARCH_SIDE_BY_SIDE.png` shows original Orin/Seren source pixels behind technically flawed checkerboard alpha; `35_STATIC_874x492_PAINTERLY_ALPHA_PROBE.png` shows the flawed image-backed matte at nominal small figure scale; `36_REAL_ALPHA_EDGE_DEFECT_AUDIT.png` exposes the source-derived color contamination. The studies do **not** test actual iPhone Safari, finger interaction, FPS, real cutout character scale, 2.5D model rotation, runtime lighting or animation.

**Observed foreground fractions** under current *experimental*, inaccurate masks: Orin FRONT 0.4288, Orin RIGHT 0.4102, Seren FRONT 0.3374. These are research mask coverage ratios, **not reliable measurements of actual silhouette occupancy or production fit**.

## Review32 verified downloadable packet

**`WAYBELL_Phase1_Review32_Visual_Evidence.zip`** — **39 files / 69,820,393 bytes**.  
**Full archive SHA-256:** `5825ebbb84d1be0f296882952b238984c9039fc296f1fb4fa2f7bfdac76c725f`.  
**ZIP CRC PASS; 38/38 manifest exact-byte and SHA-256 entries PASS; 21/21 prior native painting originals byte-identical against verified Review31.**

Contains: 21 unchanged actual full-resolution painterly portraits; actual earlier source-based Orin FRONT/RIGHT, Seren FRONT and four-character FRONT comparisons; three new alpha research PNGs; three new flat alpha silhouette PNGs; several authentic static phone-size and edge audit images; QA JSON, README and SHA manifest. **Rejected promotional/triptych images are excluded**, and no analytical crop/silhouette is counted as a new premium character painting.

## G1 and next work

- **Orin premium BACK and LEFT:** still OPEN. Existing two unique Orin painterly directions disagree on spectacles, short/full mantel, chart satchel and rod grip. v4 broad teal/moss mantle, no spectacles, two-chart left bag, right measuring staff is *provisional* art direction only.
- **Seren premium RIGHT/BACK/LEFT:** still OPEN; human Bellkeeper story/role must be preserved.
- **Manual alpha/layer feasibility:** research masks FAIL; if Phase 1 continues, attempt source-layer redraw/semantic matte repair as dedicated individual visual assets rather than simply resizing whole portrait paintings.
- **Owner final G1:** PENDING explicit owner approval. **Phase 2/game code:** LOCKED until separate explicit instruction (even if G1 is eventually passed).

**No paid services, Codex, ChatGPT Work, Vercel, gameplay/engine code, physical iPhone testing, Pages/PWA deployment or 3D rigging.** The source-controlled Python file is **art QA tooling only**, not playable game code.
