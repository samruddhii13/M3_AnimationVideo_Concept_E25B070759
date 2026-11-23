import os
import sys
import json
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
    root = Path(__file__).resolve().parent.parent
    code_dir = root / "E25B070759_Code"
    audio_dir = root / "Audio"
    media_dir = root / "media"
    segments_dir = media_dir / "segments"
    segments_dir.mkdir(parents=True, exist_ok=True)
    output_video = root / "E25B070759_Video.mp4"

    # Step 1: Scenes configuration
    scenes = [
        ("scene0", "scene0_title.py", "Scene0Title", None),
        ("scene1", "scene1_hook.py", "Scene1Hook", "scene1_audio.mp3"),
        ("scene2", "scene2_concept.py", "Scene2Concept", "scene2_audio.mp3"),
        ("scene3", "scene3_graph.py", "Scene3Graph", "scene3_audio.mp3"),
        ("scene4", "scene4_features.py", "Scene4Features", "scene4_audio.mp3"),
        ("scene5", "scene5_interpretation.py", "Scene5Interpretation", "scene5_audio.mp3"),
        ("scene6", "scene6_summary.py", "Scene6Summary", "scene6_audio.mp3"),
    ]

    print("=== Rendering all scenes in 1080p30 ===")
    for s_key, py_file, s_class, audio_file in scenes:
        print(f"Rendering {s_class}...")
        cmd = [
            "manim", "-qh",
            "--resolution", "1920,1080",
            "--frame_rate", "30",
            str(code_dir / py_file),
            s_class
        ]
        subprocess.run(cmd, cwd=root, check=True)

    print("\n=== Muxing and encoding individual segments ===")
    segment_files = []
    total_dur = 0.0

    for s_key, py_file, s_class, audio_file in scenes:
        folder_name = py_file.replace(".py", "")
        raw_video = media_dir / "videos" / folder_name / "1080p30" / f"{s_class}.mp4"
        segment_output = segments_dir / f"segment_{s_key}.mp4"

        v_dur = get_duration(raw_video)
        print(f"{s_class} raw video duration: {v_dur:.2f}s")

        if audio_file is None:
            # Silent audio for Scene 0
            mux_cmd = [
                "ffmpeg", "-y",
                "-i", str(raw_video),
                "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
                "-c:a", "aac", "-ar", "48000", "-ac", "2",
                "-t", str(v_dur),
                str(segment_output)
            ]
        else:
            audio_path = audio_dir / audio_file
            # apad audio and clamp to video duration
            mux_cmd = [
                "ffmpeg", "-y",
                "-i", str(raw_video),
                "-i", str(audio_path),
                "-filter_complex", "[1:a]apad[a]",
                "-map", "0:v", "-map", "[a]",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
                "-c:a", "aac", "-ar", "48000", "-ac", "2",
                "-t", str(v_dur),
                str(segment_output)
            ]
        subprocess.run(mux_cmd, check=True)
        seg_dur = get_duration(segment_output)
        print(f"Segment {segment_output.name} duration: {seg_dur:.2f}s")
        segment_files.append(segment_output)
        total_dur += seg_dur

    print(f"\nTotal video duration across all segments: {total_dur:.2f}s ({total_dur/60:.2f} min)")

    # Step 2: Concatenate all segments with re-encoding
    concat_list_file = segments_dir / "concat_list.txt"
    with open(concat_list_file, "w", encoding="utf-8") as f:
        for seg in segment_files:
            f.write(f"file '{seg.resolve()}'\n")

    print("\n=== Concatenating all segments into final MP4 ===")
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list_file),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30", "-crf", "22",
        "-c:a", "aac", "-ar", "48000", "-b:a", "192k",
        "-movflags", "+faststart",
        str(output_video)
    ]
    subprocess.run(concat_cmd, check=True)

    final_dur = get_duration(output_video)
    file_size_mb = output_video.stat().st_size / (1024 * 1024)
    print(f"\nFinal Video Assembled: {output_video}")
    print(f"  Duration: {final_dur:.2f}s ({final_dur/60:.2f} min)")
    print(f"  File size: {file_size_mb:.2f} MB")

if __name__ == "__main__":
    main()

