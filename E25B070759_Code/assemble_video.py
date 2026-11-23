"""assemble_video.py
Mux pre-rendered 1080p60 scene videos with their audio tracks,
then concatenate into the final E25B070759_Video.mp4.

Pre-conditions (run before this script):
  manim -qh --disable_caching E25B070759_Code/sceneN_*.py SceneNClass
  for every scene 0-6.
"""
import os
import subprocess
from pathlib import Path

def get_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(res.stdout.strip())

def main():
    root       = Path(__file__).resolve().parent.parent
    audio_dir  = root / "Audio"
    media_dir  = root / "media"
    segs_dir   = media_dir / "segments"
    segs_dir.mkdir(parents=True, exist_ok=True)
    output_video = root / "E25B070759_Video.mp4"

    # (folder_stem, class_name, audio_file or None)
    scenes = [
        ("scene0_title",         "Scene0Title",        None),
        ("scene1_hook",          "Scene1Hook",          "scene1_audio.mp3"),
        ("scene2_concept",       "Scene2Concept",       "scene2_audio.mp3"),
        ("scene3_graph",         "Scene3Graph",         "scene3_audio.mp3"),
        ("scene4_features",      "Scene4Features",      "scene4_audio.mp3"),
        ("scene5_interpretation","Scene5Interpretation","scene5_audio.mp3"),
        ("scene6_summary",       "Scene6Summary",       "scene6_audio.mp3"),
    ]

    # Manim produces 1080p30 or 1080p60
    def find_video(folder, cls):
        for quality in ("1080p30", "1080p60"):
            p = media_dir / "videos" / folder / quality / f"{cls}.mp4"
            if p.exists():
                return p
        raise FileNotFoundError(f"Cannot find rendered video for {cls}")

    print("=== Muxing & encoding segments ===")
    segment_files = []

    for folder, cls, audio_file in scenes:
        raw = find_video(folder, cls)
        seg = segs_dir / f"segment_{folder}.mp4"
        v_dur = get_duration(raw)
        print(f"{cls}: raw={v_dur:.2f}s  → {seg.name}")

        if audio_file is None:
            mux_cmd = [
                "ffmpeg", "-y",
                "-i", str(raw),
                "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
                "-c:a", "aac", "-ar", "48000", "-ac", "2",
                "-t", str(v_dur),
                str(seg)
            ]
        else:
            audio_path = audio_dir / audio_file
            mux_cmd = [
                "ffmpeg", "-y",
                "-i", str(raw),
                "-i", str(audio_path),
                "-filter_complex", "[1:a]apad[a]",
                "-map", "0:v", "-map", "[a]",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
                "-c:a", "aac", "-ar", "48000", "-ac", "2",
                "-t", str(v_dur),
                str(seg)
            ]
        subprocess.run(mux_cmd, check=True, capture_output=False)
        print(f"  → segment duration: {get_duration(seg):.2f}s")
        segment_files.append(seg)

    # Concat list
    concat_txt = segs_dir / "concat_list.txt"
    with open(concat_txt, "w") as f:
        for s in segment_files:
            f.write(f"file '{s.resolve()}'\n")

    print("\n=== Concatenating into final video ===")
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_txt),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30", "-crf", "22",
        "-c:a", "aac", "-ar", "48000", "-b:a", "192k",
        "-movflags", "+faststart",
        str(output_video)
    ]
    subprocess.run(concat_cmd, check=True)

    final_dur = get_duration(output_video)
    size_mb   = output_video.stat().st_size / (1024*1024)
    print(f"\n✓ Final video: {output_video}")
    print(f"  Duration: {final_dur:.2f}s  ({final_dur/60:.2f} min)")
    print(f"  Size: {size_mb:.2f} MB")

if __name__ == "__main__":
    main()
