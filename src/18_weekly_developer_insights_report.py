
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    BASE_DIR / "data" / "processed"
    / "weekly_developer_performance.csv"
)

REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

REPORT_FILE = REPORT_DIR / "Weekly_Developer_Insights_Report.md"

print("Generating Weekly Developer Insights Report...")

# Load weekly developer performance data
df = pd.read_csv(DATA_FILE)
df["week_start"] = pd.to_datetime(df["week_start"])

# Overall developer performance
developer_summary = (
    df.groupby("developer_id")
    .agg(
        average_productivity=("average_productivity", "mean"),
        average_focus=("average_focus", "mean"),
        average_workload=("average_workload", "mean"),
        total_sessions=("total_sessions", "sum"),
        total_high_flow_sessions=("high_flow_sessions", "sum")
    )
    .round(2)
    .reset_index()
)

# Rank developers by productivity
developer_summary = developer_summary.sort_values(
    "average_productivity",
    ascending=False
)

# Weekly productivity leader
weekly_leaders = (
    df.loc[
        df.groupby("week_start")["average_productivity"].idxmax()
    ]
    .sort_values("week_start")
)

# Overall insights
top_productivity = developer_summary.iloc[0]
top_focus = developer_summary.sort_values(
    "average_focus", ascending=False
).iloc[0]

top_high_flow = developer_summary.sort_values(
    "total_high_flow_sessions", ascending=False
).iloc[0]

overall_productivity = df["average_productivity"].mean()
overall_focus = df["average_focus"].mean()
overall_workload = df["average_workload"].mean()

# Generate Markdown report
report = f"""# Weekly Developer Insights Report

## 1. Executive Summary

This report analyzes weekly developer performance using productivity,
focus, workload, coding sessions, and high-flow session indicators.

- **Total Developers:** {df["developer_id"].nunique()}
- **Total Weeks Analyzed:** {df["week_start"].nunique()}
- **Total Sessions:** {df["total_sessions"].sum()}
- **Overall Average Productivity:** {overall_productivity:.2f}
- **Overall Average Focus:** {overall_focus:.2f}
- **Overall Average Workload:** {overall_workload:.2f}

## 2. Top Performers

### Highest Average Productivity
- Developer: **{top_productivity["developer_id"]}**
- Average Productivity: **{top_productivity["average_productivity"]:.2f}**

### Highest Average Focus
- Developer: **{top_focus["developer_id"]}**
- Average Focus: **{top_focus["average_focus"]:.2f}**

### Most High-Flow Sessions
- Developer: **{top_high_flow["developer_id"]}**
- High-Flow Sessions: **{int(top_high_flow["total_high_flow_sessions"])}**

## 3. Developer Performance Comparison

| Developer | Avg Productivity | Avg Focus | Avg Workload | Sessions | High-Flow Sessions |
|---|---:|---:|---:|---:|---:|
"""

for _, row in developer_summary.iterrows():
    report += (
        f"| {row['developer_id']} "
        f"| {row['average_productivity']:.2f} "
        f"| {row['average_focus']:.2f} "
        f"| {row['average_workload']:.2f} "
        f"| {int(row['total_sessions'])} "
        f"| {int(row['total_high_flow_sessions'])} |\\n"
    )

report += """
## 4. Weekly Productivity Leaders

| Week Starting | Developer | Productivity | Focus | Workload |
|---|---|---:|---:|---:|
"""

for _, row in weekly_leaders.iterrows():
    report += (
        f"| {row['week_start'].strftime('%Y-%m-%d')} "
        f"| {row['developer_id']} "
        f"| {row['average_productivity']:.2f} "
        f"| {row['average_focus']:.2f} "
        f"| {row['average_workload']:.2f} |\\n"
    )

report += f"""
## 5. Key Findings

- **Productivity Leader:** {top_productivity["developer_id"]} achieved
  the highest average productivity score.
- **Focus Leader:** {top_focus["developer_id"]} recorded the highest
  average focus score.
- **High-Flow Leader:** {top_high_flow["developer_id"]} recorded the
  greatest number of high-flow sessions.
- The overall average productivity across analyzed developers was
  {overall_productivity:.2f}.
- The overall average focus score was {overall_focus:.2f}.
- The overall average workload score was {overall_workload:.2f}.

## 6. Recommendations

1. Review practices associated with high productivity and focus scores.
2. Encourage balanced workloads and regular breaks.
3. Identify weeks with lower productivity for further investigation.
4. Monitor focus and workload together instead of evaluating productivity
   using a single metric.
5. Use weekly performance trends to support team planning and workload
   management.

## 7. Limitations

- The dataset is synthetic and intended for analytical demonstration.
- Scores represent exploratory performance indicators.
- Correlations and rankings do not establish causal relationships.
- High-flow session counts should not be interpreted as psychological
  or clinical measurements.

---

*Generated automatically by the CogniStream Weekly Developer Insights
Analysis.*
"""

# Save report
REPORT_FILE.write_text(report, encoding="utf-8")

print("Weekly Developer Insights Report generated successfully!")
print("Developers analyzed:", df["developer_id"].nunique())
print("Weeks analyzed:", df["week_start"].nunique())
print("Top productivity developer:", top_productivity["developer_id"])
print("Report saved at:", REPORT_FILE)
