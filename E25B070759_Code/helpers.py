import os
import json
from pathlib import Path
from manim import *

BG = "#0F172A"; CURVE = "#38BDF8"; POINT = "#FACC15"; GOOD = "#4ADE80"; BAD = "#F87171"; MAXC = "#C084FC"

# Set default font
Text.set_default(font="Helvetica Neue")

def fit(mob, margin=0.6):
    """Scale a mobject down so it stays inside the frame with a margin."""
    max_w = config.frame_width - 2 * margin
    max_h = config.frame_height - 2 * margin
    if mob.width > max_w: mob.scale_to_fit_width(max_w)
    if mob.height > max_h: mob.scale_to_fit_height(max_h)
    return mob

def boxed(*mobs, color=YELLOW, direction=DOWN, gap=0.35, pad=0.35):
    """Stack mobjects, centre them, and draw a box sized to the stack."""
    group = VGroup(*mobs).arrange(direction, buff=gap)
    box = SurroundingRectangle(group, color=color, buff=pad, corner_radius=0.15)
    return VGroup(box, group)

def check_bounds(scene, margin=0.4):
    """Print a warning for any top-level mobject outside the safe area."""
    xmax = config.frame_width / 2 - margin
    ymax = config.frame_height / 2 - margin
    for m in scene.mobjects:
        if (m.get_right()[0] > xmax or m.get_left()[0] < -xmax or
                m.get_top()[1] > ymax or m.get_bottom()[1] < -ymax):
            print("OUT OF FRAME:", type(m).__name__, m.get_center())

def sync_to(scene, t):
    """Wait until the scene clock reaches t seconds (never negative)."""
    remaining = t - scene.renderer.time
    if remaining > 0.01:
        scene.wait(remaining)
    elif remaining < -0.05:
        print(f"LATE by {-remaining:.2f}s at target {t}")

def configure_scene(scene):
    """Configure standard scene settings: background color."""
    scene.camera.background_color = BG

def load_timings(scene_key=None):
    """Load Audio/timings.json and optionally return a specific scene's timings."""
    candidates = [
        Path("Audio/timings.json"),
        Path("../Audio/timings.json"),
        Path(__file__).resolve().parent.parent / "Audio" / "timings.json"
    ]
    for p in candidates:
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
                if scene_key:
                    return data.get(scene_key, {})
                return data
    print("WARNING: Audio/timings.json not found!")
    return {}

