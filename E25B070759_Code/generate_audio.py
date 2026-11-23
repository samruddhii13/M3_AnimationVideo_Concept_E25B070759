import os
import sys
import json
import re
import subprocess
from pathlib import Path

VOICE = "en-IN-NeerjaNeural"
RATE = "+32%"
SILENCE_GAP = 0.3  # seconds between sentences

def get_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(res.stdout.strip())

def parse_script(script_path):
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()

    scenes = {}
    current_scene = None
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^---\s*(SCENE\s*\d+|OPENING TITLE CARD).*?---", line, re.IGNORECASE)
        if m:
            tag = m.group(1).upper()
            if "TITLE" in tag:
                current_scene = "scene0"
            else:
                s_num = re.search(r"\d+", tag).group(0)
                current_scene = f"scene{s_num}"
            scenes[current_scene] = []
            continue
        if current_scene and current_scene != "scene0":
            scenes[current_scene].append(line)
    return scenes

def generate_scene_audio(scene_key, sentences, output_dir, beats_dir, voice=VOICE, rate=RATE, include_optional=True):
    beats = []
    # Filter optional sentences if requested
    filtered_sentences = []
    for s in sentences:
        is_optional = "[OPTIONAL]" in s
        clean_s = s.replace("[OPTIONAL]", "").strip()
        if not is_optional or include_optional:
            filtered_sentences.append((clean_s, is_optional))

    scene_audio_path = output_dir / f"{scene_key}_audio.mp3"
    silence_file = beats_dir / "silence_0.3.mp3"
    
    # Generate silence file if not exists
    if not silence_file.exists():
        subprocess.run([
            "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
            "-t", str(SILENCE_GAP), "-q:a", "9", "-acodec", "libmp3lame", str(silence_file)
        ], capture_output=True, check=True)

    concat_list_file = beats_dir / f"{scene_key}_concat.txt"
    concat_lines = []
    sentence_timings = []
    current_time = 0.0

    for i, (sentence, is_opt) in enumerate(filtered_sentences):
        beat_file = beats_dir / f"{scene_key}_beat_{i+1:02d}.mp3"
        # Generate TTS beat
        cmd = [
            "edge-tts",
            "--voice", voice,
            f"--rate={rate}",
            "--text", sentence,
            "--write-media", str(beat_file)
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        dur = get_duration(beat_file)
        
        start_time = round(current_time, 3)
        end_time = round(current_time + dur, 3)
        sentence_timings.append({
            "beat_index": i + 1,
            "text": sentence,
            "is_optional": is_opt,
            "start": start_time,
            "end": end_time,
            "duration": round(dur, 3),
            "file": beat_file.name
        })
        
        concat_lines.append(f"file '{beat_file.resolve()}'")
        current_time += dur
        
        # Add silence gap between sentences (except after the last sentence)
        if i < len(filtered_sentences) - 1:
            concat_lines.append(f"file '{silence_file.resolve()}'")
            current_time += SILENCE_GAP

    # Write concat list
    with open(concat_list_file, "w", encoding="utf-8") as f:
        f.write("\n".join(concat_lines) + "\n")

    # Mux into single scene audio file
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list_file),
        "-c", "copy", str(scene_audio_path)
    ], capture_output=True, check=True)

    total_dur = get_duration(scene_audio_path)
    return {
        "scene": scene_key,
        "audio_file": scene_audio_path.name,
        "total_duration": round(total_dur, 3),
        "sentences": sentence_timings
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audio_dir = root / "Audio"
    beats_dir = audio_dir / "beats"
    beats_dir.mkdir(parents=True, exist_ok=True)
    
    script_file = audio_dir / "narration_script.txt"
    scenes = parse_script(script_file)
    
    timings = {}
    total_audio_sec = 6.0  # title card silent duration estimate

    print(f"Generating audio with voice={VOICE}, rate={RATE}...")
    for s_key in sorted(scenes.keys()):
        if s_key == "scene0":
            continue
        print(f"Processing {s_key} ({len(scenes[s_key])} sentences)...")
        scene_data = generate_scene_audio(s_key, scenes[s_key], audio_dir, beats_dir, VOICE, RATE, include_optional=True)
        timings[s_key] = scene_data
        total_audio_sec += scene_data["total_duration"]
        print(f"  {s_key} duration: {scene_data['total_duration']:.2f}s")

    print(f"Total video estimated duration with title card: {total_audio_sec:.2f}s ({total_audio_sec/60:.2f} min)")

    # Check bounds: 4:45 (285s) to 5:20 (320s)
    if total_audio_sec > 320:
        print("Total duration exceeds 5:20 (320s), regenerating with [OPTIONAL] sentences dropped...")
        total_audio_sec = 6.0
        timings = {}
        for s_key in sorted(scenes.keys()):
            if s_key == "scene0":
                continue
            scene_data = generate_scene_audio(s_key, scenes[s_key], audio_dir, beats_dir, VOICE, RATE, include_optional=False)
            timings[s_key] = scene_data
            total_audio_sec += scene_data["total_duration"]
            print(f"  {s_key} duration (no optional): {scene_data['total_duration']:.2f}s")
        print(f"Revised total duration: {total_audio_sec:.2f}s")
    elif total_audio_sec < 285:
        print(f"Total duration is under 4:45 (285s) at {total_audio_sec:.2f}s. Adjusting rate to +0%...")
        total_audio_sec = 6.0
        timings = {}
        for s_key in sorted(scenes.keys()):
            if s_key == "scene0":
                continue
            scene_data = generate_scene_audio(s_key, scenes[s_key], audio_dir, beats_dir, VOICE, "+0%", include_optional=True)
            timings[s_key] = scene_data
            total_audio_sec += scene_data["total_duration"]
            print(f"  {s_key} duration (rate +0%): {scene_data['total_duration']:.2f}s")
        print(f"Revised total duration: {total_audio_sec:.2f}s")

    # Add scene0 metadata
    timings["scene0"] = {
        "scene": "scene0",
        "audio_file": None,
        "total_duration": 6.0,
        "sentences": []
    }
    timings["total_duration"] = round(total_audio_sec, 3)

    timings_path = audio_dir / "timings.json"
    with open(timings_path, "w", encoding="utf-8") as f:
        json.dump(timings, f, indent=2)
    print(f"Saved timings to {timings_path}")

if __name__ == "__main__":
    main()

