
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------
# Project Paths
# -----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "developer_flow_state_analysis.csv"
)

OUTPUT_DIR = BASE_DIR / "data" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------------
# Load Analysis Data
# -----------------------------------------
print("Starting Developer Flow-State Visualizations...")

df = pd.read_csv(INPUT_FILE)

sns.set_theme(style="whitegrid")

# -----------------------------------------
# Chart 1: High Flow Percentage by Developer
# -----------------------------------------
plt.figure(figsize=(10, 6))

sns.barplot(
    data=df,
    x="developer_id",
    y="high_flow_percentage"
)

plt.title("High Flow Percentage by Developer")
plt.xlabel("Developer")
plt.ylabel("High Flow Sessions (%)")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "developer_high_flow_percentage.png",
    dpi=300
)
plt.close()

# -----------------------------------------
# Chart 2: High Flow vs Normal Flow Productivity
# -----------------------------------------
productivity_data = df[
    [
        "developer_id",
        "high_flow_avg_productivity",
        "normal_flow_avg_productivity"
    ]
].melt(
    id_vars="developer_id",
    var_name="flow_type",
    value_name="average_productivity"
)

productivity_data["flow_type"] = productivity_data[
    "flow_type"
].map({
    "high_flow_avg_productivity": "High Flow",
    "normal_flow_avg_productivity": "Normal Flow"
})

plt.figure(figsize=(11, 6))

sns.barplot(
    data=productivity_data,
    x="developer_id",
    y="average_productivity",
    hue="flow_type"
)

plt.title("Productivity: High Flow vs Normal Flow")
plt.xlabel("Developer")
plt.ylabel("Average Productivity Score")
plt.legend(title="Flow State")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "flow_state_productivity_comparison.png",
    dpi=300
)
plt.close()

# -----------------------------------------
# Chart 3: Productivity Difference
# -----------------------------------------
plt.figure(figsize=(10, 6))

sns.barplot(
    data=df,
    x="developer_id",
    y="productivity_difference"
)

plt.title("Productivity Difference by Flow State")
plt.xlabel("Developer")
plt.ylabel("High Flow - Normal Flow Productivity")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "flow_state_productivity_difference.png",
    dpi=300
)
plt.close()

# -----------------------------------------
# Completion Summary
# -----------------------------------------
print("\nAll Flow-State Visualizations Generated Successfully!")
print(f"Developers compared: {df['developer_id'].nunique()}")
print(f"Charts generated: 3")
print(f"Charts saved in: {OUTPUT_DIR}")
