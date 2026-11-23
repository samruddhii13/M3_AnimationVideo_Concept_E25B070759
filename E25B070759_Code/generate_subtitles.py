import json
from pathlib import Path

def format_timestamp(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis >= 1000:
        secs += 1
        millis -= 1000
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def main():
    root = Path(__file__).resolve().parent.parent
    timings_file = root / "Audio" / "timings.json"
    srt_file = root / "Audio" / "subtitles.srt"

    with open(timings_file, "r", encoding="utf-8") as f:
        timings = json.load(f)

    # Offset by Scene 0 title card duration
    offset = timings.get("scene0", {}).get("total_duration", 6.0)

    srt_entries = []
    idx = 1

    scene_order = ["scene1", "scene2", "scene3", "scene4", "scene5", "scene6"]
    current_scene_start = offset

    for s_key in scene_order:
        s_data = timings.get(s_key, {})
        sentences = s_data.get("sentences", [])
        for sent in sentences:
            start_time = current_scene_start + sent["start"]
            end_time = current_scene_start + sent["end"]
            text = sent["text"]

            srt_entries.append(f"{idx}\n{format_timestamp(start_time)} --> {format_timestamp(end_time)}\n{text}\n")
            idx += 1

        current_scene_start += s_data.get("total_duration", 0.0)

    with open(srt_file, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_entries))

    print(f"Generated {len(srt_entries)} subtitle entries in {srt_file}")

if __name__ == "__main__":
    main()

