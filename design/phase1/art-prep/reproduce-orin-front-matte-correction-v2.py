#!/usr/bin/env python3
"""WAYBELL Phase 1 original visual-art extraction research only.

Reproduces a *research* alpha correction of Orin FRONT from actual old alpha
and original RGB painting, both provided separately in the Review33 ZIP.
Not an image generator, game engine, production-ready transparent sprite,
physical iPhone test, or authorization to advance G1/Phase2.

Requires numpy, OpenCV, Pillow. Does not modify the original PNGs.
"""
import argparse
import hashlib
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image


def verify_bytes(path, expected):
    data = Path(path).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected:
        raise ValueError(f"Source has changed: {path.name}; {actual} != {expected}")


def render(source_path, prior_alpha_path, out_path, spec):
    verify_bytes(source_path, spec["source"]["sha256"])
    verify_bytes(prior_alpha_path, spec["prior_alpha"]["sha256"])
    source = np.asarray(Image.open(source_path).convert("RGB"))
    alpha_prior = np.asarray(Image.open(prior_alpha_path).convert("RGBA"))[:, :, 3]
    assert source.shape == (1536, 1024, 3)
    assert alpha_prior.shape == (1536, 1024)

    h, w = alpha_prior.shape
    removed_region = np.zeros((h, w), np.uint8)
    contour = np.asarray([spec["foreground_negative_polygon"]], np.int32)
    cv2.fillPoly(removed_region, contour, 255)
    removed_region = cv2.GaussianBlur(removed_region,
                                     tuple(spec["negative_blur_kernel"]),
                                     spec["negative_blur_sigma"])
    alpha = np.uint8(alpha_prior.astype(np.float32) *
                     (1.0 - removed_region.astype(np.float32) / 255.0))

    g = spec["lower_floor_color_guard"]
    red = source[:, :, 0].astype(np.float32)
    green = source[:, :, 1].astype(np.float32)
    blue = source[:, :, 2].astype(np.float32)
    floor_prob = (np.clip((red-g["red_threshold"])/g["red_divisor"], 0, 1) *
                  np.clip((green-g["green_threshold"])/g["green_divisor"], 0, 1) *
                  np.clip((blue-g["blue_threshold"])/g["blue_divisor"], 0, 1))
    vertical = np.arange(h)[:, None]
    gate = np.clip((vertical-g["min_y"])/g["ramp_pixels"], 0, 1)
    alpha = np.uint8(np.clip(alpha.astype(float) *
                   (1.0 - g["max_background_reduction"] * floor_prob * gate), 0, 255))

    ground = spec["shadow_remove"]
    for y in range(ground["start_y"], h):
        alpha[y, :] = np.uint8(alpha[y, :] *
                    max(0, (ground["finish_y"]-y)/ground["fade_pixels"]))

    boot = spec["boot_staff_shadow_exclusion"]
    keep = np.ones((h, w), np.float32)
    for y in range(boot["start_y"], min(1515, h)):
        allowed = np.zeros(w, np.uint8)
        for start, end in boot["allowed_horizontal_bands"]:
            allowed[start:end] = 255
        allowed = cv2.GaussianBlur(allowed[np.newaxis, :],
                     tuple(boot["band_blur_kernel"]),
                     boot["band_blur_sigma"])[0].astype(np.float32) / 255.0
        blend = np.clip((y-boot["start_y"])/boot["fade_pixels"], 0, 1)
        keep[y, :] = (1 - blend) + blend*allowed
    alpha = np.uint8(np.clip(alpha.astype(float)*keep, 0, 255))
    result = np.dstack((source, alpha))
    Image.fromarray(result, "RGBA").save(out_path)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--previous-alpha", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    spec_path = Path(__file__).with_name("orin-front-ground-matte-correction-v2.json")
    spec = json.loads(spec_path.read_text(encoding="utf8"))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    result = render(args.source, args.previous_alpha, args.out, spec)
    digest = hashlib.sha256(args.out.read_bytes()).hexdigest()
    print(json.dumps({
        "output": str(args.out),
        "sha256": digest,
        "matches_review33_recorded_png": digest == spec["revised_alpha_sha256"],
        "foreground_fraction": round(float((result[:, :, 3] > 127).mean()), 4),
        "production_approved": False,
        "owner_G1": "PENDING",
        "phase2_game_code": "LOCKED"
    }, indent=2))


if __name__ == "__main__":
    main()
