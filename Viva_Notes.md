# Viva Voce Examination Notes
**Subject:** Linear Algebra and Calculus (M3)  
**Topic:** Single-Variable Functions and Graphs  
**Student:** Samruddhi Meshram | **ID:** E25B070759  
**Model Problem:** Vertical Cricket Ball Trajectory $h(t) = 20t - 5t^2$  

---

### Question 1: What is a function, and why is "exactly one output" the key?
**Answer:**  
A function $f: D \to R$ is a rule that assigns to each element $x$ in a set $D$ (the domain) **exactly one** element $f(x)$ in a set $R$ (the range).  
The condition "exactly one output" is the fundamental requirement that guarantees determinism and predictability. In physical systems, an object cannot be in two different locations at the same instant of time. For instance, at time $t = 1\text{ s}$, the cricket ball must have a single, definite height ($h = 15\text{ m}$). If a mathematical relation produced two heights for a single instant, it would fail to describe physical reality and cannot be treated as a single-variable function.

---

### Question 2: What does the Vertical Line Test check, and why does the circle fail?
**Answer:**  
The **Vertical Line Test (VLT)** states that a geometric curve in the Cartesian coordinate plane represents a single-variable function $y = f(x)$ if and only if **no vertical line intersects the curve more than once**.  
- **Why our parabola passes:** For $h(t) = 20t - 5t^2$, every vertical line $t = c$ intersects the parabola at exactly one point $(c, 20c - 5c^2)$. Therefore, $h$ is a valid function of $t$.  
- **Why the circle fails:** Consider the circle $x^2 + y^2 = 9$. The vertical line $x = 0$ intersects the circle at both $(0, 3)$ and $(0, -3)$. Because a single input $x = 0$ corresponds to two distinct outputs ($y = 3$ and $y = -3$), the circle fails the vertical line test and is a relation, not a function.

---

### Question 3: Why can two different inputs have the same output ($h(1) = h(3) = 15$), but one input cannot have two outputs?
**Answer:**  
A function is defined as a many-to-one or one-to-one mapping, but **never** a one-to-many mapping.  
- **Two inputs sharing an output (Many-to-One):** It is physically natural for a ball to reach the same height twice: once on its way up at $t = 1\text{ s}$ ($h = 15\text{ m}$), and again on its way down at $t = 3\text{ s}$ ($h = 15\text{ m}$). Each moment in time still has exactly one unambiguous height.  
- **One input having two outputs (One-to-Many):** If $t = 1\text{ s}$ gave both $h = 15\text{ m}$ and $h = 8\text{ m}$, the ball would have to exist in two places at once, violating physical reality and the mathematical definition of a function.

---

### Question 4: How do we find the intercepts of $h(t)$?
**Answer:**  
- **Vertical Intercept ($h$-intercept / initial state):**  
  Set the input $t = 0$:  
  $$h(0) = 20(0) - 5(0)^2 = 0\text{ m}$$  
  The vertical intercept is at the origin $(0, 0)$, meaning the ball is launched from ground level at $t = 0$.  
- **Horizontal Intercepts ($t$-intercepts / landing state):**  
  Set the output $h(t) = 0$ and solve for $t$:  
  $$20t - 5t^2 = 0$$  
  Factor out $5t$:  
  $$5t(4 - t) = 0 \implies t = 0\text{ or } t = 4$$  
  The horizontal intercepts are at $(0, 0)$ (the moment of release) and $(4, 0)$ (the moment of impact/landing after 4 seconds of flight).

---

### Question 5: How do we prove the maximum height is $20\text{ m}$ at $t = 2\text{ s}$?
**Answer:**  
We prove this using two distinct mathematical methods:  
1. **Completing the Square (Vertex Form):**  
   $$h(t) = -5(t^2 - 4t) = -5[(t - 2)^2 - 4] = 20 - 5(t - 2)^2$$  
   For all real numbers $t$, the squared term $(t - 2)^2 \ge 0$, which implies $-5(t - 2)^2 \le 0$. Therefore,  
   $$h(t) \le 20$$  
   The maximum possible value of $h(t)$ is $20\text{ m}$, achieved if and only if $(t - 2)^2 = 0$, which occurs at $t = 2\text{ s}$.  
2. **Symmetry of Quadratic Functions:**  
   Because the parabola is symmetric about its axis of symmetry, the vertex lies exactly halfway between the roots:  
   $$t_{\text{vertex}} = \frac{0 + 4}{2} = 2\text{ s}$$  
   Evaluating the function at this midpoint gives $h(2) = 20(2) - 5(2)^2 = 40 - 20 = 20\text{ m}$.

---

### Question 6: What is the difference between the mathematical domain and physical domain, and what is the physical range?
**Answer:**  
- **Mathematical Domain:** The formula $h(t) = 20t - 5t^2$ is an algebraic polynomial, so algebraically it accepts any real number $t \in (-\infty, \infty)$.  
- **Physical Domain:** The physical model describes the ball while it is in the air. For $t < 0$, the ball has not been thrown; for $t > 4$, the ball has struck the ground. Therefore, the physical domain is the closed interval:  
  $$D_{\text{phys}} = [0, 4]\text{ s}$$  
- **Physical Range:** On the domain $[0, 4]$, the minimum height is $0\text{ m}$ (at $t = 0$ and $t = 4$) and the maximum height is $20\text{ m}$ (at $t = 2$). Thus, the physical range is:  
  $$R_{\text{phys}} = [0, 20]\text{ m}$$

---

### Question 7: What do the average rates of change ($15, 5, -5, -15\text{ m/s}$) mean, and what does a negative value indicate?
**Answer:**  
The average rate of change over an interval $[a, b]$ is the slope of the secant line:  
$$\text{Average Rate} = \frac{\Delta h}{\Delta t} = \frac{h(b) - h(a)}{b - a}$$  
- Over $[0, 1]\text{ s}$: $\frac{15 - 0}{1} = +15\text{ m/s}$ (fast climb upward).  
- Over $[1, 2]\text{ s}$: $\frac{20 - 15}{1} = +5\text{ m/s}$ (climb slows down as gravity decelerates the ball).  
- At $t = 2\text{ s}$: instantaneous rate is $0\text{ m/s}$ (the ball momentarily halts at its peak).  
- Over $[2, 3]\text{ s}$: $\frac{15 - 20}{1} = -5\text{ m/s}$ (ball begins descending).  
- Over $[3, 4]\text{ s}$: $\frac{0 - 15}{1} = -15\text{ m/s}$ (ball accelerates downward).  
*Significance of Negative Sign:* In calculus and kinematics, sign represents direction. A positive rate of change indicates increasing height (upward motion); a negative rate of change indicates decreasing height (downward motion).

---

### Question 8: Why is the graph NOT the path of the ball in space?
**Answer:**  
The ball is thrown **straight up into the air** along a single vertical spatial axis (one-dimensional motion). Its path through physical space is a straight line segment going up from $0$ to $20\text{ m}$ and returning straight down along the same line.  
The parabola appears on the graph because the horizontal axis represents **time ($t$)**, not horizontal spatial distance ($x$). The graph displays height plotted as a function of elapsed time: $h$ vs. $t$. It is an abstract mathematical state-space representation, not a photographic trajectory.

---

### Question 9: Line-by-Line Code Architecture of Each Scene
1. **`helpers.py`**:
   - `BG = "#0F172A"`, `CURVE = "#38BDF8"`, `POINT = "#FACC15"`, `GOOD = "#4ADE80"`, `BAD = "#F87171"`, `MAXC = "#C084FC"`: Establishes accessible color hierarchy.
   - `fit(mob, margin=0.6)`: Dynamically checks bounding box against frame width/height minus margin, downscaling if necessary.
   - `boxed(*mobs, color, direction, gap, pad)`: Arranges objects in a VGroup and wraps them in a rounded `SurroundingRectangle`.
   - `check_bounds(scene, margin=0.4)`: Scans all scene mobjects at completion to assert that no geometry bleeds outside safe frame boundaries.
   - `sync_to(scene, t)`: Synchronizes Manim scene clock to narration timestamps loaded from `Audio/timings.json`.
2. **`scene0_title.py` (`Scene0Title`)**:
   - Constructs high-contrast title card with student metadata and model overview.
   - Smoothly fades in over 1.5s, holds for 3.5s, and fades out over 1.0s.
3. **`scene1_hook.py` (`Scene1Hook`)**:
   - Creates vertical meter ruler and cricket ball with white seam arc.
   - Animates ball throw using `rush_from` and `rush_into` rate functions.
   - Poses 3 key questions at heights $15\text{ m}$, $20\text{ m}$, and $0\text{ m}$.
   - Builds animated Function Machine with input arrow ($t=1\text{ s}$), processing box ($h(t)$), and output arrow ($15\text{ m}$).
   - Displays three video roadmap goals.
4. **`scene2_concept.py` (`Scene2Concept`)**:
   - Boxes core definition: "Each allowed input has exactly ONE output".
   - Shows algebraic formula with gravitational simplification note.
   - Evaluates $h(1) = 15\text{ m}$ step-by-step.
   - Constructs two-column Mapping Diagram with oval containers and animated directed arrows for each input-output pair.
   - Proves validity of many-to-one mapping ($1 \to 15$ and $3 \to 15$).
5. **`scene3_graph.py` (`Scene3Graph`)**:
   - Constructs input-output table alongside 2D Cartesian axes.
   - Drops yellow coordinate dots onto axes row-by-row.
   - Plots smooth parabola $h(t) = 20t - 5t^2$.
   - Draws dashed line connecting $(1, 15)$ and $(3, 15)$.
   - Sweeps vertical test line across parabola to demonstrate the Vertical Line Test.
   - Constructs circle $x^2 + y^2 = 9$ as a counterexample failing the test at $x = 0$.
6. **`scene4_features.py` (`Scene4Features`)**:
   - Features fixed left-half axes and four sequential right-half algebra cards.
   - Step 1: Intercepts solved via factoring $5t(4 - t) = 0$.
   - Step 2: Maximum derived via completed square form $20 - 5(t - 2)^2 \le 20$.
   - Step 3: Domain and range highlighted on respective coordinate axes.
   - Step 4: Displays increasing $[0, 2]$ and decreasing $[2, 4]$ intervals with four secant rate calculations ($+15, +5, -5, -15\text{ m/s}$).
7. **`scene5_interpretation.py` (`Scene5Interpretation`)**:
   - Implements synchronized `ValueTracker(t)` driving:
     (a) ball on vertical ruler,
     (b) dot on coordinate parabola,
     (c) dashed horizontal connector line.
   - Progressively introduces callout annotations with arrows for origin, peak, landing, and symmetry.
   - Highlights physical flight domain interval $[0, 4]$.
   - Fades out graph to present centered takeaway card.
8. **`scene6_summary.py` (`Scene6Summary`)**:
   - Presents three takeaway cards sequentially.
   - Displays held closing frame with takeaway question, student metadata, textbook reference, music credit, and AI disclosure.

