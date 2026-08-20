#!/usr/bin/env python3
"""Extract measured palette candidates from an image for visual review."""

from __future__ import annotations

import argparse
import colorsys
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract approximate dominant colors; visual interpretation is still required."
    )
    parser.add_argument("image", type=Path)
    parser.add_argument("--colors", type=int, default=8, choices=range(3, 17))
    parser.add_argument(
        "--crop-percent",
        type=float,
        default=0.0,
        help="Crop this percentage from every edge before analysis (0-20).",
    )
    parser.add_argument("--output", type=Path, help="Optional Markdown output path")
    return parser.parse_args()


def hue_name(hue: float, saturation: float, value: float) -> str:
    if value < 0.16:
        return "near-black"
    if saturation < 0.08 and value > 0.9:
        return "near-white"
    if saturation < 0.12:
        return "gray-neutral"
    degrees = hue * 360
    bands = [
        (15, "red"),
        (45, "orange"),
        (70, "yellow"),
        (165, "green"),
        (195, "cyan"),
        (255, "blue"),
        (290, "violet"),
        (335, "magenta"),
        (360, "red"),
    ]
    return next(name for edge, name in bands if degrees < edge)


def role_hint(rank: int, saturation: float, value: float) -> str:
    if value < 0.22:
        return "dark-anchor candidate"
    if value > 0.9 and saturation < 0.15:
        return "highlight/negative-space candidate"
    if rank == 1:
        return "dominant-field candidate"
    if rank <= 3:
        return "secondary-mass candidate"
    if saturation > 0.6:
        return "accent candidate"
    return "supporting-tone candidate"


def median_rgb(pixels: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    channels = [sorted(pixel[channel] for pixel in pixels) for channel in range(3)]
    middle = len(pixels) // 2
    return tuple(channel[middle] for channel in channels)


def extract(
    image_path: Path, color_count: int, crop_percent: float
) -> tuple[list[tuple[int, tuple[int, int, int]]], tuple[tuple[int, int, int], tuple[int, int, int]]]:
    if not 0 <= crop_percent <= 20:
        raise ValueError("--crop-percent must be between 0 and 20")
    with Image.open(image_path) as opened:
        rgba = opened.convert("RGBA")
        background = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        rgb = Image.alpha_composite(background, rgba).convert("RGB")
    if crop_percent:
        dx = round(rgb.width * crop_percent / 100)
        dy = round(rgb.height * crop_percent / 100)
        rgb = rgb.crop((dx, dy, rgb.width - dx, rgb.height - dy))
    rgb.thumbnail((640, 640))
    if hasattr(rgb, "get_flattened_data"):
        pixels = list(rgb.get_flattened_data())
    else:
        pixels = list(rgb.getdata())
    by_luminance = sorted(
        pixels, key=lambda pixel: 0.2126 * pixel[0] + 0.7152 * pixel[1] + 0.0722 * pixel[2]
    )
    tail_size = max(1, len(by_luminance) // 20)
    anchors = (median_rgb(by_luminance[:tail_size]), median_rgb(by_luminance[-tail_size:]))

    quantized = rgb.quantize(colors=color_count, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette()
    counts = quantized.getcolors() or []
    result: list[tuple[int, tuple[int, int, int]]] = []
    for count, index in sorted(counts, reverse=True):
        base = index * 3
        result.append((count, tuple(palette[base : base + 3])))
    return result, anchors


def render_markdown(
    image_path: Path,
    colors: list[tuple[int, tuple[int, int, int]]],
    anchors: tuple[tuple[int, int, int], tuple[int, int, int]],
) -> str:
    total = sum(count for count, _ in colors)
    lines = [
        "# Measured palette candidates",
        "",
        f"- Source: `{image_path}`",
        "- Note: pixel frequency is not visual importance; inspect the image and correct for borders, text, skin, shadows, transparency, and compression.",
        "",
        "| Rank | Hex | Share | Hue family | H / S / V | Suggested review role |",
        "|---:|---|---:|---|---|---|",
    ]
    for rank, (count, rgb) in enumerate(colors, start=1):
        r, g, b = rgb
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        lines.append(
            f"| {rank} | `#{r:02X}{g:02X}{b:02X}` | {count / total:.1%} | "
            f"{hue_name(h, s, v)} | {h * 360:.0f}° / {s:.0%} / {v:.0%} | {role_hint(rank, s, v)} |"
        )
    dark, light = anchors
    lines.extend(
        [
            "",
            "## Contrast anchors",
            "",
            f"- Darkest-region median (bottom 5% luminance): `#{dark[0]:02X}{dark[1]:02X}{dark[2]:02X}`",
            f"- Brightest-region median (top 5% luminance): `#{light[0]:02X}{light[1]:02X}{light[2]:02X}`",
            "- These anchors help preserve a dark skeleton or pale highlight that broad quantization may blend away; small semantic accents still require visual inspection.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    colors, anchors = extract(args.image, args.colors, args.crop_percent)
    markdown = render_markdown(args.image, colors, anchors)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown, end="")


if __name__ == "__main__":
    main()
