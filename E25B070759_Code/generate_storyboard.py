import os
import json
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether

def main():
    root = Path(__file__).resolve().parent.parent
    timings_path = root / "Audio" / "timings.json"
    pdf_path = root / "Storyboard" / "Functions_Graphs_Storyboard.pdf"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    with open(timings_path, "r", encoding="utf-8") as f:
        timings = json.load(f)

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=6,
        fontName="Helvetica-Bold"
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0284C7"),
        spaceAfter=12,
        fontName="Helvetica-Bold"
    )
    meta_style = ParagraphStyle(
        "MetaText",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#334155")
    )
    h2_style = ParagraphStyle(
        "SectionHeader",
        parent=styles["Heading2"],
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=10,
        spaceAfter=4,
        fontName="Helvetica-Bold"
    )
    cell_bold = ParagraphStyle(
        "CellBold",
        parent=styles["Normal"],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#0F172A"),
        fontName="Helvetica-Bold"
    )
    cell_text = ParagraphStyle(
        "CellText",
        parent=styles["Normal"],
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#1E293B")
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("From Input to Output: Reading the Graph of a Function", title_style))
    story.append(Paragraph("M3 Linear Algebra & Calculus — Animation Video Storyboard", subtitle_style))
    story.append(Paragraph("<b>Student:</b> Samruddhi Meshram &nbsp;|&nbsp; <b>Student ID:</b> E25B070759 &nbsp;|&nbsp; <b>Course:</b> Calculus (M3)", meta_style))
    story.append(Paragraph("<b>Model:</b> Real-life vertical cricket ball trajectory: <i>h(t) = 20t - 5t²</i> (g = 10 m/s², no air resistance)", meta_style))
    story.append(Spacer(1, 8))

    # Objective Box
    obj_html = (
        "<b>Learning Objective:</b> By the end of this video, the viewer will be able to explain how a function "
        "maps each input to exactly one output, plot and read its graph, and identify and interpret its key features "
        "(intercepts, maximum/vertex, physical domain and range, increasing/decreasing behaviour, and average rate of change)."
    )
    obj_table = Table([[Paragraph(obj_html, meta_style)]], colWidths=[532])
    obj_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F0F9FF")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#0284C7")),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(obj_table)
    story.append(Spacer(1, 12))

    # Scene Data
    scenes_info = [
        {
            "num": "Scene 0",
            "title": "Opening Title Card",
            "key": "scene0",
            "visual": "Navy slate canvas (#0F172A). Centered glowing card with main title, course, example description, student name and ID.",
            "math": "Topic statement: Single-variable functions and graphs. Model: h(t) = 20t - 5t².",
            "anim": "Soft fade in of card, hold for 3.5s, soft fade out.",
            "narr": "Silent opening title card (held for 6.0 seconds)."
        },
        {
            "num": "Scene 1",
            "title": "Hook & The Real-Life Problem",
            "key": "scene1",
            "visual": "Vertical ruler (0 to 20 m) on left with red cricket ball. Right side displays three key questions, followed by a Function Machine diagram.",
            "math": "t = 1 s -> h = 15 m; t = 2 s -> h = 20 m; t = 4 s -> h = 0 m. Machine rule: h(t) = 20t - 5t².",
            "anim": "Ball thrown straight up and down. Questions appear at specific altitudes. Function machine demonstrates input t=1 passing through rule box to output 15m.",
            "narr": "Introduces the cricket ball throw, poses questions on height and landing, defines a function as an exact rule mapping time to height, outlines 3 video goals."
        },
        {
            "num": "Scene 2",
            "title": "Concept & Mapping Diagram",
            "key": "scene2",
            "visual": "Boxed core definition. Formula card with physical assumptions. Full two-column Mapping Diagram (Domain on left, Range on right) with directed arrows.",
            "math": "Definition: exactly ONE output per input. Physics rule h(t) = 20t - 5t². Evaluation: h(1) = 15 m. Domain {0, 1, 2, 3, 4}, Range {0, 15, 20}.",
            "anim": "Definition card enters. Formula evaluated step-by-step. Directed arrows grow sequentially from each input to output; highlight that 1 and 3 share output 15.",
            "narr": "Clarifies input and output definitions, explains the physics formula and g=10 simplification, walks through mapping diagram, defines Domain and Range."
        },
        {
            "num": "Scene 3",
            "title": "Plotting the Graph & Vertical Line Test",
            "key": "scene3",
            "visual": "Input-output table on left, 2D Cartesian axes (Time t vs Height h) on right. Sweeping vertical test line. Circle counterexample (x² + y² = 9).",
            "math": "Points: (0,0), (1,15), (2,20), (3,15), (4,0). Parabola curve. Circle x² + y² = 9 has x=0 -> y=±3.",
            "anim": "Table rows drop yellow dots on axes. Parabola smoothly drawn. Dashed horizontal line connects (1,15) and (3,15). Vertical line sweeps across graph. Circle appears and fails test.",
            "narr": "Constructs the parabola from table points, clarifies that graph is height vs time and not spatial path, explains two inputs sharing output, demonstrates vertical line test."
        },
        {
            "num": "Scene 4",
            "title": "Key Features: Worked Analysis",
            "key": "scene4",
            "visual": "Split layout: permanently visible parabola on left half, structured algebra cards on right half presented sequentially in four steps.",
            "math": "1. Intercepts: h(0)=0, 5t(4-t)=0 -> t=0,4. 2. Max: h(t)=20-5(t-2)² <= 20 at t=2. 3. Domain [0,4], Range [0,20]. 4. Secants: +15, +5, -5, -15 m/s.",
            "anim": "Step 1 marks origin and landing with green dots. Step 2 identifies vertex with purple dot and symmetry line. Step 3 highlights axis intervals. Step 4 draws secant lines.",
            "narr": "Thoroughly calculates intercepts by factoring, derives maximum height via completing the square, defines physical domain and range, analyzes increasing/decreasing rates."
        },
        {
            "num": "Scene 5",
            "title": "Physical Interpretation & Story",
            "key": "scene5",
            "visual": "Synchronized ValueTracker animation: vertical ruler on left, axes in center with parabola. Value-driven connecting dashed line. Callouts with arrows.",
            "math": "Continuous tracking of h(t) = 20t - 5t² for t in [0, 4]. Symmetry: rise time = fall time = 2 s.",
            "anim": "ValueTracker moves ball on ruler and dot on parabola in perfect lockstep. Callouts appear at origin, peak, landing, and symmetry line. Takeaway card centers at finish.",
            "narr": "Interprets each mathematical feature as a chapter of the real-world flight, emphasizing the power of a graph to communicate an entire physical relationship at a glance."
        },
        {
            "num": "Scene 6",
            "title": "Summary & Closing Frame",
            "key": "scene6",
            "visual": "Three sequential takeaway cards with clean bullet points. Closing frame with core reflection question, student metadata, references, and AI disclosure.",
            "math": "Recap: (1) Single output per input (VLT), (2) Coordinate pairs (t, h(t)), (3) Real-world interpretation of intercepts, peak, and rates.",
            "anim": "Cards 1, 2, 3 appear sequentially. Closing frame softly fades in and holds.",
            "narr": "Recaps the three core principles, poses the concluding takeaway question, references credits and AI disclosure."
        }
    ]

    for sc in scenes_info:
        dur = timings.get(sc["key"], {}).get("total_duration", 0.0)
        dur_str = f"{dur:.2f} s ({dur/60:.2f} min)" if dur > 0 else "6.00 s"

        scene_table_data = [
            [Paragraph(f"<b>{sc['num']}: {sc['title']}</b>", cell_bold), Paragraph(f"<b>Measured Duration:</b> {dur_str}", cell_bold)],
            [Paragraph("<b>Visual Layout</b>", cell_bold), Paragraph(sc["visual"], cell_text)],
            [Paragraph("<b>Mathematical Content</b>", cell_bold), Paragraph(sc["math"], cell_text)],
            [Paragraph("<b>Animation Description</b>", cell_bold), Paragraph(sc["anim"], cell_text)],
            [Paragraph("<b>Narration Summary</b>", cell_bold), Paragraph(sc["narr"], cell_text)]
        ]

        t = Table(scene_table_data, colWidths=[130, 402])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E2E8F0")),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#94A3B8")),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))

        story.append(KeepTogether([t, Spacer(1, 10)]))

    doc.build(story)
    print(f"Generated storyboard PDF: {pdf_path}")

if __name__ == "__main__":
    main()

