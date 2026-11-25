# From Input to Output: Reading the Graph of a Function
**M3 Linear Algebra & Calculus — Animated Video Project**

### 📹 Video Link
- **Video Link:** [Watch the Animation Video](https://drive.google.com/file/d/1I-UgU4pVGD8MRemJ7KyCdi25bA8A7B4P/view?usp=sharing)
- **Video File (Repository):** [E25B070759_Video.mp4](./E25B070759_Video.mp4)
- **Specifications:** 1080p Full HD, 16:9, 30 fps, Progressive H.264 / AAC, Duration: 5 min 17.33 s (317.33 s)
- **Subtitles:** [Audio/subtitles.srt](./Audio/subtitles.srt) (Separate synchronized SRT file)
- **Storyboard Document:** [Storyboard/Functions_Graphs_Storyboard.pdf](./Storyboard/Functions_Graphs_Storyboard.pdf)
- **Visual Contact Sheets:** [verification_frames/final_contact.png](./verification_frames/final_contact.png)

---

## 1. Project Overview & Learning Objectives
- **Course:** Linear Algebra and Calculus (M3)
- **Topic:** Single-variable functions and graphs: input-output mapping, coordinate graph reading, and key graphical features explained through a single real-world physical model.

### Learning Objectives
By the end of this animated video, the viewer will be able to:
1. **Explain the Function Definition:** Explain how a single-variable function maps every allowed input $t$ to exactly one output $h(t)$, and why multiple inputs yielding the same output is valid while a single input yielding multiple outputs violates the definition.
2. **Read and Plot Coordinates:** Interpret every point on a coordinate graph as an ordered pair $(t, h(t))$ representing physical state (elapsed time vs. vertical altitude).
3. **Analyze Key Graphical Features:**
   - **Horizontal Intercepts ($t$-intercepts):** Identify launch ($t = 0\text{ s}$) and landing ($t = 4\text{ s}$) where $h(t) = 0$.
   - **Vertex and Global Maximum:** Locate the apex ($t = 2\text{ s}, h = 20\text{ m}$) using symmetry and algebraic completion of the square.
   - **Domain & Range:** Distinguish between the algebraic domain ($\mathbb{R}$) and the physically meaningful domain ($[0, 4]\text{ s}$) and range ($[0, 20]\text{ m}$).
   - **Increasing & Decreasing Behaviour:** Understand where the function rises ($t \in [0, 2]$) and falls ($t \in [2, 4]$).
   - **Average Rate of Change:** Calculate secant slopes $\frac{\Delta h}{\Delta t}$ across unit intervals ($+15, +5, -5, -15\text{ m/s}$) and interpret the physical meaning of a negative rate as downward motion.
   - **Vertical Line Test (VLT):** Verify graphical function validity and contrast with relations that fail (e.g., a circle).

---

## 2. Visual Architecture: Split-Screen Real-World Model
To make mathematical abstractions tangible and visually intuitive, the animation employs a synchronized split-screen architecture built around a **realistic cricket ball** (featuring dual curved seam stitching and light reflection):

- **Left Panel (Physical Space — $x = -5.2$):**
  A vertical height ruler ($0$ to $25\text{ m}$) on which the red cricket ball climbs and falls in real-time kinematics.
- **Middle Panel (Mathematical Space — $x = -1.4$):**
  Coordinate axes ($t \in [0, 5]\text{ s}$, $h \in [0, 25]\text{ m}$) matching the ruler's vertical height ($4.4\text{ units}$) and baseline elevation to machine precision ($10^{-16}$).
- **Dynamic Horizontal Connector:**
  A faint dashed cyan line joins the center of the physical cricket ball to the tracking point on the coordinate curve at every frame. This visually demonstrates the core concept:
  $$\text{Height of physical ball} \equiv \text{Height coordinate on graph}$$
- **Right Panel (Concept & Analysis Cards — $x = 3.8$):**
  A dedicated $5.4\text{-unit}$ wide zone for clear explanatory cards, data tables, and calculus feature pills, preventing any visual overlap with the graph or trajectory.
- **Unified ValueTracker:**
  A single continuous tracker variable $t$ drives the ball, trajectory trace, connector line, coordinate dot, and live readout card (`t = 1.0 s | h = 15 m`) in exact synchronization.
- **Player Controls Safety:**
  All visual elements are strictly maintained above $y = -3.00$, leaving the bottom $1.0\text{ unit}$ completely unobstructed for media player interfaces.

---

## 3. Mathematical Formulation & Verified Properties

### Physical Model
- A cricket ball is projected straight upward from ground level ($h = 0\text{ m}$) with an initial vertical velocity of $v_0 = 20\text{ m/s}$.
- Air resistance is neglected, and gravitational acceleration is taken as $g = 10\text{ m/s}^2$ (an explicitly stated simplification of $9.8\text{ m/s}^2$).

### Mathematical Rule in Three Equivalent Forms
$$h(t) = 20t - 5t^2 = 5t(4 - t) = 20 - 5(t - 2)^2$$

- **Standard Form:** $h(t) = 20t - 5t^2$ highlights initial velocity ($20\text{ m/s}$) and gravitational deceleration ($-5t^2 = -\frac{1}{2}gt^2$).
- **Factored Form:** $h(t) = 5t(4 - t)$ immediately reveals the roots (launch at $t = 0\text{ s}$, landing at $t = 4\text{ s}$).
- **Vertex Form:** $h(t) = 20 - 5(t - 2)^2$ proves the maximum height of $20\text{ m}$ occurs at $t = 2\text{ s}$, because $(t - 2)^2 \ge 0$ for all real $t$.

### Tabulated Values
| Time $t$ (seconds) | Height $h(t)$ (metres) | Physical Interpretation |
| :---: | :---: | :--- |
| **$0\text{ s}$** | $0\text{ m}$ | Launch from ground level |
| **$1\text{ s}$** | $15\text{ m}$ | Upward flight |
| **$2\text{ s}$** | $20\text{ m}$ | Maximum height (apex, instantaneous velocity = 0) |
| **$3\text{ s}$** | $15\text{ m}$ | Downward flight (symmetric to $t = 1\text{ s}$) |
| **$4\text{ s}$** | $0\text{ m}$ | Ground impact / landing |

### Key Calculus & Function Properties
1. **Domain and Range:**
   - Physical Flight Domain: $t \in [0, 4]\text{ s}$
   - Physical Flight Range: $h \in [0, 20]\text{ m}$
2. **Symmetry:**
   The parabolic trajectory is symmetric about the vertical axis $t = 2\text{ s}$. Equal heights occur at equal time offsets: $h(2 - \Delta t) = h(2 + \Delta t)$. For example, $h(1) = h(3) = 15\text{ m}$.
3. **Average Rates of Change:**
   - Interval $[0, 1]\text{ s}$: $\frac{15 - 0}{1} = +15\text{ m/s}$ (Rapid climb)
   - Interval $[1, 2]\text{ s}$: $\frac{20 - 15}{1} = +5\text{ m/s}$ (Climb decelerates)
   - Interval $[2, 3]\text{ s}$: $\frac{15 - 20}{1} = -5\text{ m/s}$ (Descent begins; negative indicates downward direction)
   - Interval $[3, 4]\text{ s}$: $\frac{0 - 15}{1} = -15\text{ m/s}$ (Descent accelerates)
4. **Trajectory vs. Graph:**
   The graph is an abstraction plotting height against time; it is **not** the spatial curve of the ball. The actual ball travels strictly in a one-dimensional vertical line up and down.

---

## 4. Technical Specifications & Verification

### 4.1 Video Stream Conformance (FFprobe Verified)
- **Container:** MP4 (ISO/IEC 14496-14)
- **Video Codec:** H.264 / AVC (High Profile, progressive)
- **Dimensions:** $1920 \times 1080$ (16:9 widescreen)
- **Frame Rate:** $30.0\text{ fps}$ constant
- **Audio Codec:** AAC (LC), 48,000 Hz, Stereo, 192 kbps
- **Exact Duration:**
  - Video stream: $317.333333\text{ s}$ ($5\text{ min } 17.33\text{ s}$)
  - Audio stream: $317.321333\text{ s}$
  - Sync drift: $\Delta = 0.012\text{ s} \ll 0.5\text{ s}$
- **Total File Size:** $12.21\text{ MB}$ (comfortably within standard GitHub limits)

### 4.2 Audio Volume Verification (`ffmpeg volumedetect`)
Measured across 5 benchmark windows throughout the video:
| Window | Segment Description | Mean Volume | Max Volume | Status |
| :---: | :---: | :---: | :---: | :---: |
| **0 – 30 s** | Title & Physical Hook | `-26.5 dB` | `-8.1 dB` | Audible, No Clipping |
| **60 – 80 s** | Input-Output Mapping | `-26.0 dB` | `-8.0 dB` | Audible, No Clipping |
| **150 – 170 s** | Graph Construction & VLT | `-25.3 dB` | `-8.0 dB` | Audible, No Clipping |
| **240 – 260 s** | Key Features & Average Rates | `-25.4 dB` | `-7.6 dB` | Audible, No Clipping |
| **Last 20 s** | Summary & Acknowledgements | `-25.7 dB` | `-7.8 dB` | Audible, No Clipping |

*Summary: Audio is loud, crisp, and consistent with no silent or dropped sections.*

---

## 5. Animation Code Structure

```
├── E25B070759_Video.mp4           # Final assembled 1080p MP4 animation
├── README.md                      # Project documentation and specifications
├── Viva_Notes.md                  # Comprehensive viva preparation notes
├── Storyboard/
│   └── Functions_Graphs_Storyboard.pdf  # PDF storyboard documentation
├── Audio/
│   ├── narration_script.txt       # Master narration script by scene & beat
│   ├── subtitles.srt              # 79 timed subtitle entries
│   ├── timings.json               # Word-level sync timings for animation
│   └── scene[1-6]_audio.mp3       # Rendered audio stems
├── E25B070759_Code/
│   ├── design.py                  # Colors, fonts, layout constants, 3-zone stage
│   ├── helpers.py                 # Math utilities, cricket ball generator, sync helpers
│   ├── scene0_title.py            # Opening title card with topic banner
│   ├── scene1_hook.py             # Physical real-world cricket ball hook
│   ├── scene2_concept.py          # Input-output mapping & function definition
│   ├── scene3_graph.py            # Split-screen coordinate plot & Vertical Line Test
│   ├── scene4_features.py         # Intercepts, vertex, domain, range, rate secants
│   ├── scene5_interpretation.py   # Narrative curve reading & physical motion recap
│   ├── scene6_summary.py          # Recap card, references, and AI disclosure
│   ├── generate_audio.py          # Edge-TTS voice generation script
│   ├── generate_subtitles.py      # Subtitle (.srt) synchronizer
│   ├── assemble_video.py          # FFmpeg multi-scene stitcher and audio mixer
│   └── requirements.txt           # Python dependencies (manim, edge-tts, etc.)
└── verification_frames/           # Rendered QA frames and contact sheets
```

---

## 6. How to Build & Render from Source

1. **Set Up Python Environment:**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   pip install -r E25B070759_Code/requirements.txt
   ```

2. **Generate Audio & Timings:**
   ```bash
   python E25B070759_Code/generate_audio.py
   python E25B070759_Code/generate_subtitles.py
   ```

3. **Render Scenes (Manim Community):**
   ```bash
   manim -qh --disable_caching E25B070759_Code/scene0_title.py Scene0Title
   manim -qh --disable_caching E25B070759_Code/scene1_hook.py Scene1Hook
   manim -qh --disable_caching E25B070759_Code/scene2_concept.py Scene2Concept
   manim -qh --disable_caching E25B070759_Code/scene3_graph.py Scene3Graph
   manim -qh --disable_caching E25B070759_Code/scene4_features.py Scene4Features
   manim -qh --disable_caching E25B070759_Code/scene5_interpretation.py Scene5Interpretation
   manim -qh --disable_caching E25B070759_Code/scene6_summary.py Scene6Summary
   ```

4. **Assemble Final Video:**
   ```bash
   python E25B070759_Code/assemble_video.py
   ```

---

## 7. References & AI Disclosure
- **Course Reference:** Standard Linear Algebra and Calculus (M3) course syllabus and textbook.
- **Audio Credit:** Microsoft Edge TTS (`en-IN-NeerjaNeural`, Indian English Female, calibrated at `+32%` rate).
- **AI Tooling Disclosure:** Animation code generation, script sync calculations, and voice synthesis aided by Google DeepMind Antigravity AI and Edge TTS. All mathematical derivations, physics equations, pedagogical structuring, and visual layout assertions were independently designed and verified.
