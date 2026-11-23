# From Input to Output: Reading the Graph of a Function
**M3 Linear Algebra & Calculus — Animated Video Project**

- **Student Name:** Samruddhi Meshram
- **Student ID:** E25B070759
- **Course:** Linear Algebra and Calculus (M3)
- **Deadline:** 25 November 2026
- **Video File:** [E25B070759_Video.mp4](file:///Users/samruddhi1306/animation_video_M3/E25B070759_Video.mp4) (1080p, 30 fps, 317.33 s / 5:17)
- **Subtitles:** [Audio/subtitles.srt](file:///Users/samruddhi1306/animation_video_M3/Audio/subtitles.srt) (Separate SRT file; FFmpeg build lacks libass)
- **Storyboard:** [Storyboard/Functions_Graphs_Storyboard.pdf](file:///Users/samruddhi1306/animation_video_M3/Storyboard/Functions_Graphs_Storyboard.pdf)
- **Contact Sheets:** [verification_frames/final_contact.png](file:///Users/samruddhi1306/animation_video_M3/verification_frames/final_contact.png)

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

## 2. Visual Design & Split-Screen Architecture
The entire video is built around a **real red cricket ball** (with curved white seam arcs and specular shine) to ground mathematical abstraction in tangible physics:
- **Ball-and-Graph Split Screen (`ball_and_graph_stage`):**
  - **Left:** Vertical height ruler ($0$ to $25\text{ m}$) on which the red cricket ball climbs and falls.
  - **Right:** Coordinate axes ($t \in [0,5]$, $h \in [0,25]$) matching the ruler's height ($4.4\text{ units}$) and vertical position to machine precision.
  - **Dashed Connector:** A live horizontal line directly connects the center of the cricket ball to the corresponding point on the graph dot at all times: $\text{ball height} = \text{graph height}$.
  - **ValueTracker Integration:** A single unified `ValueTracker(t)` drives the cricket ball, graph marker, traced trajectory, dashed connector line, and live readout card simultaneously.
- **Strict Layout Standards:**
  - Standardized margin protection (`SAFE = 0.6`).
  - Strict player controls avoidance (all visual content kept above $y = -3.00$, leaving the bottom $1.0\text{ unit}$ completely clear).
  - Clean card wrappers (`card()`), rounded pills (`pill()`), and halo glow shaders (`glow()`).
  - Zero bounding-box collisions or text overlaps across all scenes verified by automated layout assertions.

---

## 3. Mathematical Model & Verified Results
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

## 4. Verification Evidence & Quality Assurance

### 4.1 FFprobe Stream Conformance
```json
{
  "streams": [
    {
      "codec_name": "h264",
      "codec_type": "video",
      "width": 1920,
      "height": 1080,
      "r_frame_rate": "30/1",
      "duration": "317.333333"
    },
    {
      "codec_name": "aac",
      "codec_type": "audio",
      "sample_rate": "48000",
      "channels": 2,
      "duration": "317.321333"
    }
  ],
  "format": {
    "duration": "317.333333",
    "size": "12798839"
  }
}
```
- Resolution: $1920 \times 1080$ progressive.
- Frame Rate: $30\text{ fps}$.
- Duration: $317.33\text{ s}$ ($5\text{ min } 17.33\text{ s}$), well within the $4:45$ to $5:20$ requirement.
- Audio-Video Sync Difference: $\Delta = 0.012\text{ s} \ll 0.5\text{ s}$.

### 4.2 Audio Volume Measurements
All five required test windows were checked using `ffmpeg volumedetect`:
| Time Window | Segment Description | Mean Volume | Max Volume | Status |
| :--- | :--- | :--- | :--- | :--- |
| **0 – 30 s** | Scene 0 Title & Scene 1 Hook | `-26.5 dB` | `-8.1 dB` | Audible, No Clipping |
| **60 – 80 s** | Scene 2 Mapping Diagram | `-26.0 dB` | `-8.0 dB` | Audible, No Clipping |
| **150 – 170 s** | Scene 3 Graph & VLT | `-25.3 dB` | `-8.0 dB` | Audible, No Clipping |
| **240 – 260 s** | Scene 4 Behaviour & Rates | `-25.4 dB` | `-7.6 dB` | Audible, No Clipping |
| **Last 20 s** | Scene 6 Closing Credits | `-25.7 dB` | `-7.8 dB` | Audible, No Clipping |
*Result: Zero instances of `-inf`, zero dropped audio, consistent vocal presence throughout.*

---

## 5. Voice Narration & Audio Specifications
- **Voice Model:** Microsoft Edge TTS `en-IN-NeerjaNeural` (Indian English Female).
- **Speech Rate:** `+32%` (precisely calibrated to ensure the total video lands between 4:45 and 5:20).
- **Silence Gaps:** Standard 0.3 s silence inserted between consecutive sentences.
- **Audio Stream:** AAC, 48,000 Hz, Stereo, 128-192 kbps.
- **Subtitles:** Provided as a standalone file `Audio/subtitles.srt` (this FFmpeg build does not include `libass`, ensuring zero video compression artifacts from burning).

---

## 6. References & Credits
- **Primary Textbook Reference:** *course textbook and class notes*
- **Music Credit:** No background music (clean, high-intelligibility voice narration only).

---

## 7. AI Disclosure
- **Assisted Tools:** Code generation, script timing orchestration, and speech synthesis assisted by Google DeepMind Antigravity AI and Microsoft Edge TTS (`en-IN-NeerjaNeural`).
- **Student Verification:** All physical calculations, mathematical equations, domain/range limits, algebraic factorizations, and pedagogical layouts were independently formulated and verified by the student (Samruddhi Meshram).
