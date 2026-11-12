
from pathlib import Path
import pandas as pd

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load cleaned dataset
file_path = BASE_DIR / "data" / "processed" / "cognistream_cleaned_data.csv"

df = pd.read_csv(file_path)

print("\n========== COGNISTREAM DATA ANALYSIS ==========")

# 1. Overall statistics
print("\n1. Overall Performance:")
print(df[[
    "coding_hours",
    "focus_score",
    "workload_score",
    "productivity_score"
]].mean().round(2))

# 2. Developer-wise analysis
print("\n2. Developer-wise Performance:")

developer_summary = df.groupby("developer_id").agg(
    total_sessions=("developer_id", "count"),
    avg_coding_hours=("coding_hours", "mean"),
    avg_focus_score=("focus_score", "mean"),
    avg_workload_score=("workload_score", "mean"),
    avg_productivity_score=("productivity_score", "mean")
).round(2)

print(developer_summary)

# 3. Flow state analysis
print("\n3. Flow State Distribution:")
print(df["flow_state"].value_counts())

# 4. Interruption analysis
print("\n4. Average Interruptions:")
print(round(df["interruption_count"].mean(), 2))

# 5. Correlation analysis
print("\n5. Correlation with Productivity:")
print(
    df[[
        "coding_hours",
        "interruption_count",
        "task_switches",
        "focus_score",
        "workload_score",
        "productivity_score"
    ]].corr()["productivity_score"].round(2)
)

# Save developer summary
output_file = BASE_DIR / "data" / "processed" / "developer_analysis.csv"

developer_summary.to_csv(output_file)

print("\nAnalysis Completed Successfully!")
print("Summary saved at:", output_file)
