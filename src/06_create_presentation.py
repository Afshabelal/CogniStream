
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ---------------------------------
# Project Paths
# ---------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CHART_DIR = BASE_DIR / "data" / "output"
SAVE_DIR = BASE_DIR / "presentation"

SAVE_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = SAVE_DIR / "CogniStream_Presentation.pptx"

# ---------------------------------
# Presentation Setup
# ---------------------------------
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

BLUE = RGBColor(23, 54, 93)
TEAL = RGBColor(23, 107, 135)
LIGHT = RGBColor(244, 247, 251)
DARK = RGBColor(45, 60, 75)
WHITE = RGBColor(255, 255, 255)


# ---------------------------------
# Helper Functions
# ---------------------------------
def add_background(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = LIGHT


def add_title(slide, title, subtitle=None):
    box = slide.shapes.add_textbox(
        Inches(0.6), Inches(0.35),
        Inches(12), Inches(0.7)
    )
    paragraph = box.text_frame.paragraphs[0]
    paragraph.text = title
    paragraph.font.size = Pt(28)
    paragraph.font.bold = True
    paragraph.font.color.rgb = BLUE

    if subtitle:
        box2 = slide.shapes.add_textbox(
            Inches(0.65), Inches(1.05),
            Inches(12), Inches(0.45)
        )
        p = box2.text_frame.paragraphs[0]
        p.text = subtitle
        p.font.size = Pt(13)
        p.font.color.rgb = TEAL


def add_bullets(slide, items, x=0.9, y=1.8, width=11.5):
    box = slide.shapes.add_textbox(
        Inches(x), Inches(y),
        Inches(width), Inches(4.8)
    )

    frame = box.text_frame
    frame.word_wrap = True

    for i, item in enumerate(items):
        p = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
        p.text = item
        p.font.size = Pt(21)
        p.font.color.rgb = DARK
        p.space_after = Pt(22)


def add_chart(slide, filename, x=1.0, y=1.6,
              width=11.2, height=5.3):
    image_path = CHART_DIR / filename

    if image_path.exists():
        slide.shapes.add_picture(
            str(image_path),
            Inches(x), Inches(y),
            width=Inches(width),
            height=Inches(height)
        )
    else:
        box = slide.shapes.add_textbox(
            Inches(x), Inches(y),
            Inches(width), Inches(1)
        )
        box.text_frame.text = f"Chart not found: {filename}"


def new_slide(title, subtitle=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide)
    add_title(slide, title, subtitle)
    return slide


# ---------------------------------
# Slide 1: Title
# ---------------------------------
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide)

box = slide.shapes.add_textbox(
    Inches(1), Inches(2),
    Inches(11.3), Inches(1.3)
)
p = box.text_frame.paragraphs[0]
p.text = "🧠 CogniStream"
p.font.size = Pt(42)
p.font.bold = True
p.font.color.rgb = BLUE
p.alignment = PP_ALIGN.CENTER

box = slide.shapes.add_textbox(
    Inches(1), Inches(3.35),
    Inches(11.3), Inches(1)
)
p = box.text_frame.paragraphs[0]
p.text = "Developer Flow-State & Cognitive Load Analytics"
p.font.size = Pt(23)
p.font.color.rgb = TEAL
p.alignment = PP_ALIGN.CENTER

box = slide.shapes.add_textbox(
    Inches(2), Inches(5),
    Inches(9.3), Inches(0.6)
)
p = box.text_frame.paragraphs[0]
p.text = "Data Analytics Internship Project"
p.font.size = Pt(18)
p.font.color.rgb = DARK
p.alignment = PP_ALIGN.CENTER


# ---------------------------------
# Slide 2: Project Overview
# ---------------------------------
slide = new_slide(
    "Project Overview",
    "Understanding developer productivity and focus"
)

add_bullets(slide, [
    "CogniStream is a developer activity analytics project.",
    "It explores the relationship between focus, workload and productivity.",
    "It identifies patterns related to developer flow states.",
    "The project uses Python-based data analysis and an interactive dashboard."
])


# ---------------------------------
# Slide 3: Project Objectives
# ---------------------------------
slide = new_slide(
    "Project Objectives",
    "What the project aims to understand"
)

add_bullets(slide, [
    "Analyze developer productivity patterns.",
    "Understand how focus relates to productivity.",
    "Study the relationship between task switching and productivity.",
    "Explore workload and flow-state patterns.",
    "Present insights through charts and an interactive dashboard."
])


# ---------------------------------
# Slide 4: Dataset Overview
# ---------------------------------
slide = new_slide(
    "Dataset Overview",
    "A sample developer activity dataset"

)

add_bullets(slide, [
    "Total records: 500 developer activity sessions.",
    "Date range: 1 October 2026 to 21 October 2026.",
    "Data includes coding hours, workload and productivity scores.",
    "Other fields include focus score, interruptions and task switches.",
    "Data quality check: 0 missing values and 0 duplicate rows."
])


# ---------------------------------
# Slide 5: Key Performance Indicators
# ---------------------------------
slide = new_slide(
    "Performance Overview",
    "Key metrics from the analyzed dataset"
)

metrics = [
    ("Total Sessions", "500"),
    ("Avg Productivity", "51.28"),
    ("Avg Focus Score", "62.69"),
    ("Avg Workload", "68.36")
]

for i, (label, value) in enumerate(metrics):
    x = 0.8 + (i * 3.15)

    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(2.3),
        Inches(2.7), Inches(1.8)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = WHITE
    shape.line.color.rgb = TEAL

    box = slide.shapes.add_textbox(
        Inches(x + 0.1), Inches(2.65),
        Inches(2.5), Inches(0.4)
    )
    p = box.text_frame.paragraphs[0]
    p.text = label
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = DARK
    p.alignment = PP_ALIGN.CENTER

    box = slide.shapes.add_textbox(
        Inches(x + 0.1), Inches(3.15),
        Inches(2.5), Inches(0.6)
    )
    p = box.text_frame.paragraphs[0]
    p.text = value
    p.font.size = Pt(27)
    p.font.bold = True
    p.font.color.rgb = TEAL
    p.alignment = PP_ALIGN.CENTER


# ---------------------------------
# Slide 6: Analytical Findings
# ---------------------------------
slide = new_slide(
    "Key Analytical Findings",
    "Correlation with productivity score"
)

add_bullets(slide, [
    "Focus score: +0.73 — strong positive association.",
    "Task switches: -0.60 — negative association.",
    "Interruption count: -0.41 — negative association.",
    "Workload score: +0.36 — moderate positive association.",
    "Correlation indicates association, not proof of causation."
])


# ---------------------------------
# Slide 7: Flow State Distribution
# ---------------------------------
slide = new_slide(
    "Flow State Distribution",
    "Distribution of developer flow states"
)

add_chart(
    slide,
    "flow_state_distribution.png",
    x=2.0, y=1.6, width=9.3, height=5.3
)


# ---------------------------------
# Slide 8: Focus vs Productivity
# ---------------------------------
slide = new_slide(
    "Focus vs Productivity",
    "Exploring the relationship between focus and productivity"
)

add_chart(
    slide,
    "focus_vs_productivity.png"
)


# ---------------------------------
# Slide 9: Productivity by Developer
# ---------------------------------
slide = new_slide(
    "Productivity by Developer",
    "Comparing productivity patterns across developers"
)

add_chart(
    slide,
    "productivity_by_developer.png"
)


# ---------------------------------
# Slide 10: Correlation and Conclusion
# ---------------------------------
slide = new_slide(
    "Correlation Analysis & Conclusion",
    "Summary of the project's key insights"
)

add_chart(
    slide,
    "correlation_heatmap.png",
    x=0.7, y=1.5, width=6.2, height=4.8
)

box = slide.shapes.add_textbox(
    Inches(7.2), Inches(1.8),
    Inches(5.3), Inches(4.5)
)

frame = box.text_frame
frame.word_wrap = True

paragraphs = [
    "Key Takeaways",
    "Focus has the strongest positive correlation with productivity.",
    "Task switching and interruptions show negative correlations.",
    "The dashboard helps explore developer activity patterns.",
    "These findings are exploratory and do not establish causation."
]

for i, item in enumerate(paragraphs):
    p = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
    p.text = item
    p.font.size = Pt(17 if i else 22)
    p.font.bold = (i == 0)
    p.font.color.rgb = BLUE if i == 0 else DARK
    p.space_after = Pt(16)


# ---------------------------------
# Save Presentation
# ---------------------------------
prs.save(OUTPUT_FILE)

print("Presentation created successfully!")
print(f"Saved at: {OUTPUT_FILE}")
