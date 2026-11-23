# From Input to Output: Reading the Graph of a Function
**M3 Linear Algebra & Calculus — Animated Video Project**

- **Student Name:** Samruddhi Meshram
- **Student ID:** E25B070759
- **Course:** Linear Algebra and Calculus (M3)
- **Deadline:** 25 November 2026
- **Video File:** [E25B070759_Video.mp4](file:///Users/samruddhi1306/animation_video_M3/E25B070759_Video.mp4) (1080p, 30 fps)
- **Subtitles:** [Audio/subtitles.srt](file:///Users/samruddhi1306/animation_video_M3/Audio/subtitles.srt) (Separate SRT file; FFmpeg build lacks libass)
- **Storyboard:** [Storyboard/Functions_Graphs_Storyboard.pdf](file:///Users/samruddhi1306/animation_video_M3/Storyboard/Functions_Graphs_Storyboard.pdf)

---

## 1. Learning Objective & Topic Overview
**Topic:** Single-variable functions and graphs: input-output mapping, graph behaviour, and key features explained through ONE real-life physical model.

**Learning Objective:**
By the end of this video, the viewer will be able to:
1. Explain how a single-variable function maps each allowed input to exactly one output.
2. Read and construct a coordinate graph where each point represents an input-output pair $(t, h(t))$.
3. Identify and interpret all key graphical and calculus features:
   - Initial altitude and landing time (horizontal intercepts),
   - Maximum height and axis of symmetry (vertex),
   - Physical domain and range versus algebraic domain,
   - Increasing and decreasing intervals, and
   - Average rate of change (secants) and the physical meaning of a negative rate.

---

## 2. Mathematical Model & Verified Results
- **Physical Context:** A cricket ball thrown vertically upward from hand height ($h=0$) at an initial velocity of $20\text{ m/s}$. Air resistance is neglected, and gravitational acceleration is simplified to $g = 10\text{ m/s}^2$ (an intentional simplification of $9.8\text{ m/s}^2$, explicitly stated on-screen).
- **Function Rule:**
  $$h(t) = 20t - 5t^2 = 5t(4 - t) = 20 - 5(t - 2)^2$$
- **Consistency of Forms:**
  $$20 - 5(t - 2)^2 = 20 - 5(t^2 - 4t + 4) = 20 - 5t^2 + 20t - 20 = 20t - 5t^2$$
- **Input-Output Data:**
  - $t = 0\text{ s} \implies h(0) = 0\text{ m}$ (Launch origin)
  - $t = 1\text{ s} \implies h(1) = 20(1) - 5(1)^2 = 15\text{ m}$
  - $t = 2\text{ s} \implies h(2) = 20(2) - 5(2)^2 = 20\text{ m}$ (Apex)
  - $t = 3\text{ s} \implies h(3) = 20(3) - 5(3)^2 = 15\text{ m}$
  - $t = 4\text{ s} \implies h(4) = 20(4) - 5(4)^2 = 0\text{ m}$ (Landing)
- **Intercepts:**
  $h(t) = 0 \iff 5t(4 - t) = 0 \iff t = 0\text{ s}$ or $t = 4\text{ s}$.
- **Vertex / Maximum:**
  Since $(t - 2)^2 \ge 0$ for all real $t$, $-5(t - 2)^2 \le 0$. Hence $h(t) \le 20$, with equality strictly at $t = 2\text{ s}$. The parabola is symmetric about the vertical line $t = 2$.
- **Domain & Range:**
  - Algebraic Domain: $\mathbb{R}$
  - Physical Flight Domain: $[0, 4]\text{ s}$
  - Physical Range: $[0, 20]\text{ m}$
- **Average Rate of Change ($\Delta h / \Delta t$):**
  - $[0, 1]\text{ s}$: $(15 - 0) / 1 = +15\text{ m/s}$ (Upward climb)
  - $[1, 2]\text{ s}$: $(20 - 15) / 1 = +5\text{ m/s}$ (Climb slows)
  - $[2, 3]\text{ s}$: $(15 - 20) / 1 = -5\text{ m/s}$ (Downward fall)
  - $[3, 4]\text{ s}$: $(0 - 15) / 1 = -15\text{ m/s}$ (Fall accelerates)
  *A negative average rate signifies downward velocity.*
- **Vertical Line Test:**
  The parabola passes the Vertical Line Test because every vertical line $t = c$ intersects the curve at at most one point. The circle $x^2 + y^2 = 9$ fails at $x = 0$, yielding two outputs ($y = 3$ and $y = -3$).
- **Crucial Distinction:**
  The graph depicts height against elapsed time. It is **not** the physical path of the ball through space, which is a straight vertical line up and down.

---

## 3. Project File Structure
```
Maths-Animation-Video/
├── E25B070759_Code/
│   ├── helpers.py               # Shared constants, fit(), boxed(), check_bounds(), sync_to()
│   ├── scene0_title.py          # Scene 0: Opening title card
│   ├── scene1_hook.py           # Scene 1: Real-life ball throw and function machine
│   ├── scene2_concept.py        # Scene 2: Function definition and mapping diagram
│   ├── scene3_graph.py          # Scene 3: Graph construction and Vertical Line Test
│   ├── scene4_features.py       # Scene 4: Intercepts, maximum, domain/range, behaviour
│   ├── scene5_interpretation.py # Scene 5: Physical story and synchronized ValueTracker
│   ├── scene6_summary.py        # Scene 6: Three takeaways and closing credits frame
│   ├── generate_audio.py        # Edge TTS beat generator and timing calculator
│   ├── generate_subtitles.py    # Subtitle generator (Audio/subtitles.srt)
│   ├── generate_storyboard.py   # ReportLab PDF storyboard generator
│   ├── assemble_video.py        # Complete rendering, muxing, and concatenation pipeline
│   └── requirements.txt         # Project dependencies
├── Audio/
│   ├── narration_script.txt     # Complete verbatim narration text
│   ├── timings.json             # Precise sentence and scene timing measurements
│   ├── beats/                   # Per-sentence MP3 audio beats and silence segments
│   ├── scene1_audio.mp3 ... scene6_audio.mp3 # Per-scene assembled audio tracks
│   └── subtitles.srt            # External subtitle file
├── Storyboard/
│   └── Functions_Graphs_Storyboard.pdf # Comprehensive PDF storyboard
├── verification_frames/
│   ├── scene0.png ... scene6.png       # Quality-control contact sheets per scene
│   └── final_checks.png                # Final video spot-check frames
├── E25B070759_Video.mp4         # Final 1080p30 release video (under 100 MB)
├── README.md                    # Project documentation
├── Viva_Notes.md                # In-depth viva voce examination prep notes
└── .gitignore                   # Excludes .venv/, media/, __pycache__/
```

---

## 4. Installation & Reproduction Instructions

### 4.1 Prerequisites
- Python 3.11
- FFmpeg (macOS: `brew install ffmpeg`)
- LaTeX (BasicTeX / MacTeX with `pdfTeX` and `dvipng`/`dvisvgm`)

### 4.2 Virtual Environment & Dependencies
```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r E25B070759_Code/requirements.txt
```

### 4.3 Rendering Individual Scenes
To render any scene at high quality (1080p, 30 fps):
```bash
source .venv/bin/activate
manim -qh --resolution 1920,1080 --frame_rate 30 E25B070759_Code/scene0_title.py Scene0Title
manim -qh --resolution 1920,1080 --frame_rate 30 E25B070759_Code/scene1_hook.py Scene1Hook
manim -qh --resolution 1920,1080 --frame_rate 30 E25B070759_Code/scene2_concept.py Scene2Concept
manim -qh --resolution 1920,1080 --frame_rate 30 E25B070759_Code/scene3_graph.py Scene3Graph
manim -qh --resolution 1920,1080 --frame_rate 30 E25B070759_Code/scene4_features.py Scene4Features
manim -qh --resolution 1920,1080 --frame_rate 30 E25B070759_Code/scene5_interpretation.py Scene5Interpretation
manim -qh --resolution 1920,1080 --frame_rate 30 E25B070759_Code/scene6_summary.py Scene6Summary
```

### 4.4 Automated End-to-End Pipeline
To re-generate audio, subtitles, storyboard, and the full video from scratch:
```bash
source .venv/bin/activate
python E25B070759_Code/generate_audio.py
python E25B070759_Code/generate_subtitles.py
python E25B070759_Code/generate_storyboard.py
python E25B070759_Code/assemble_video.py
```

---

## 5. Voice Narration & Audio Engineering
- **Voice Model:** Microsoft Edge TTS `en-IN-NeerjaNeural` (Indian English Female, natural pacing).
- **Speech Rate:** `+32%` (precisely calibrated to ensure the total video lands between 4:45 and 5:20).
- **Silence Gaps:** Standard 0.3 s silence inserted between consecutive sentences.
- **Audio Specifications:** AAC, 48,000 Hz, Stereo, 192 kbps.
- **Subtitles:** Provided as a standalone file `Audio/subtitles.srt` (time-offset from the opening title card).

---

## 6. References & Credits
- **Primary Textbook Reference:** *Thomas' Calculus* (14th Edition), George B. Thomas, Maurice D. Weir, and Joel Hass. Pearson Education.
- **Music Credit:** No background music (clean, high-intelligibility voice narration only).

---

## 7. AI Disclosure
- **Assisted Tools:** Code generation, script timing orchestration, and speech synthesis assisted by Google DeepMind Antigravity AI and Microsoft Edge TTS (`en-IN-NeerjaNeural`).
- **Student Verification:** All physical calculations, mathematical equations, domain/range limits, algebraic factorizations, and pedagogical layouts were independently formulated and verified by the student (Samruddhi Meshram).
