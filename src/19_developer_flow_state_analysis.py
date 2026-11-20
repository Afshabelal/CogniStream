
from pathlib import Path
import pandas as pd

# -----------------------------------------
# Project Paths
# -----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "cognistream_cleaned_data.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "developer_flow_state_analysis.csv"

# -----------------------------------------
# Load Dataset
# -----------------------------------------
print("Starting Developer Flow-State Analysis...")

df = pd.read_csv(INPUT_FILE)

# -----------------------------------------
# Developer-wise Flow State Analysis
# -----------------------------------------
flow_analysis = df.groupby("developer_id").agg(
    total_sessions=("developer_id", "count"),
    high_flow_sessions=("flow_state", lambda x: (x == "High Flow").sum()),
    normal_flow_sessions=("flow_state", lambda x: (x == "Normal Flow").sum()),
    avg_productivity=("productivity_score", "mean"),
    avg_focus_score=("focus_score", "mean"),
    avg_workload_score=("workload_score", "mean"),
    avg_coding_hours=("coding_hours", "mean")
).reset_index()

# -----------------------------------------
# Calculate High Flow Percentage
# -----------------------------------------
flow_analysis["high_flow_percentage"] = (
    flow_analysis["high_flow_sessions"]
    / flow_analysis["total_sessions"]
) * 100

# -----------------------------------------
# Productivity Comparison by Flow State
# -----------------------------------------
high_flow_productivity = (
    df[df["flow_state"] == "High Flow"]
    .groupby("developer_id")["productivity_score"]
    .mean()
    .reset_index()
    .rename(columns={
        "productivity_score": "high_flow_avg_productivity"
    })
)

normal_flow_productivity = (
    df[df["flow_state"] == "Normal Flow"]
    .groupby("developer_id")["productivity_score"]
    .mean()
    .reset_index()
    .rename(columns={
        "productivity_score": "normal_flow_avg_productivity"
    })
)

# -----------------------------------------
# Merge Productivity Comparisons
# -----------------------------------------
flow_analysis = flow_analysis.merge(
    high_flow_productivity,
    on="developer_id",
    how="left"
)

flow_analysis = flow_analysis.merge(
    normal_flow_productivity,
    on="developer_id",
    how="left"
)

# -----------------------------------------
# Calculate Productivity Difference
# -----------------------------------------
flow_analysis["productivity_difference"] = (
    flow_analysis["high_flow_avg_productivity"]
    - flow_analysis["normal_flow_avg_productivity"]
)

# -----------------------------------------
# Round Numerical Values
# -----------------------------------------
numeric_columns = flow_analysis.select_dtypes(
    include="number"
).columns

flow_analysis[numeric_columns] = flow_analysis[numeric_columns].round(2)

# -----------------------------------------
# Sort by High Flow Percentage
# -----------------------------------------
flow_analysis = flow_analysis.sort_values(
    by="high_flow_percentage",
    ascending=False
)

# -----------------------------------------
# Save Results
# -----------------------------------------
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

flow_analysis.to_csv(OUTPUT_FILE, index=False)

# -----------------------------------------
# Display Results
# -----------------------------------------
print("\nDeveloper Flow-State Analysis:")
print(flow_analysis.to_string(index=False))

print("\nAnalysis Summary:")
print(f"Total Developers: {flow_analysis['developer_id'].nunique()}")
print(f"Total Sessions: {flow_analysis['total_sessions'].sum()}")
print(
    "Average High Flow Percentage:",
    round(flow_analysis["high_flow_percentage"].mean(), 2),
    "%"
)

print("\nDeveloper Flow-State Analysis completed successfully!")
print(f"Output saved at: {OUTPUT_FILE}")
