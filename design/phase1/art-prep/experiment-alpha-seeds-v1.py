#!/usr/bin/env python3
"""WAYBELL Phase 1 art-only diagnostic. NOT an engine, sprite exporter or gameplay code.

Recreate rough silhouette hypotheses for Orin FRONT/RIGHT and Seren FRONT.
Requires the original 1024x1536 PNGs separately supplied in the Review32
conversation ZIP; they are deliberately NOT stored in this GitHub repository.

Dependencies: OpenCV, numpy, Pillow, scipy. Outputs are research ONLY.
Warm parchment residuals and damaged edges FAIL the production-alpha gate.
"""
import argparse
import hashlib
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from scipy.ndimage import binary_fill_holes


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def research_one(source: Path, entry: dict, destination: Path) -> dict:
    b = source.read_bytes()
    expected = entry["source_sha256"]
    if sha256(b) != expected:
        raise ValueError(f"Original source checksum mismatch: {source.name}")

    original = cv2.imread(str(source), cv2.IMREAD_COLOR)
    if original is None or original.shape[:2] != (1536, 1024):
        raise ValueError("This study only supports the verified native 1024x1536 paintings")

    scale = 0.5
    reduced = cv2.resize(original, (512, 768), interpolation=cv2.INTER_AREA)
    mh, mw = reduced.shape[:2]
    mask = np.full((mh, mw), cv2.GC_PR_BGD, np.uint8)
    poly = np.array(
        [[(int(x * scale), int(y * scale))
          for x, y in entry["probable_foreground_polygon"]]], np.int32
    )
    cv2.fillPoly(mask, poly, cv2.GC_PR_FGD)
    mask[:5, :] = cv2.GC_BGD
    mask[-5:, :] = cv2.GC_BGD
    mask[:, :5] = cv2.GC_BGD
    mask[:, -5:] = cv2.GC_BGD
    for x1, y1, x2, y2 in entry["certain_foreground_boxes"]:
        mask[round(y1*scale):round(y2*scale),
             round(x1*scale):round(x2*scale)] = cv2.GC_FGD

    bgmodel = np.zeros((1, 65), np.float64)
    fgmodel = np.zeros((1, 65), np.float64)
    cv2.grabCut(reduced, mask, None, bgmodel, fgmodel, 5, cv2.GC_INIT_WITH_MASK)
    alpha = ((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD)).astype(np.uint8) * 255
    alpha = cv2.morphologyEx(alpha, cv2.MORPH_CLOSE, np.ones((3,3), np.uint8))
    alpha = binary_fill_holes(alpha > 127).astype(np.uint8) * 255
    alpha = cv2.resize(alpha, (1024, 1536), interpolation=cv2.INTER_LINEAR)
    alpha = cv2.GaussianBlur(alpha, (3, 3), 0.6)

    rgb = np.asarray(Image.open(source).convert("RGB"))
    result = np.dstack((rgb, alpha))
    name = source.stem
    Image.fromarray(result, "RGBA").save(destination / f"{name}_UNAPPROVED_alpha.png")
    flat = np.zeros((1536, 1024, 4), np.uint8)
    flat[:, :, :3] = (30, 67, 76)
    flat[:, :, 3] = alpha
    Image.fromarray(flat, "RGBA").save(destination / f"{name}_silhouette.png")
    return {"source": source.name, "unapproved": True,
            "foreground_fraction": round(float(np.mean(alpha > 127)), 4),
            "original_sha256": expected}


def main():
    parser = argparse.ArgumentParser(description="Review32 Phase 1 art-only silhouette QA")
    parser.add_argument("--sources", type=Path, required=True,
                        help="Unmodified original PNG folder from Review32 archive")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    seed_file = Path(__file__).with_name("orin-seren-source-silhouette-seeds-v1.json")
    spec = json.loads(seed_file.read_text(encoding="utf-8"))
    report = []
    for entry in spec["subjects"].values():
        report.append(research_one(args.sources / entry["file"], entry, args.output))
    (args.output / "UNAPPROVED_MASK_QA.json").write_text(
        json.dumps({"research_only": True, "pass_production_alpha": False,
                    "results": report}, indent=2), encoding="utf-8")
    print("Research masks produced; none may be treated as production-ready sprites.")


if __name__ == "__main__":
    main()
