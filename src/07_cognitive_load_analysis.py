
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "cognistream_cleaned_data.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "cognitive_load_risk_analysis.csv"

# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)

# Required columns
required_columns = [
    "workload_score",
    "focus_score",
    "interruption_count",
    "task_switches"
]

# Validate dataset
missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

# Calculate normalized risk components
df["workload_risk"] = df["workload_score"].clip(0, 100)

df["low_focus_risk"] = 100 - df["focus_score"].clip(0, 100)

df["interruption_risk"] = (
    df["interruption_count"].clip(0, 15) / 15
) * 100

df["task_switching_risk"] = (
    df["task_switches"].clip(0, 20) / 20
) * 100

# Calculate overall cognitive load risk score
df["cognitive_load_risk_score"] = (
    df["workload_risk"] * 0.35
    + df["low_focus_risk"] * 0.30
    + df["interruption_risk"] * 0.20
    + df["task_switching_risk"] * 0.15
).round(2)

# Classify risk levels
def classify_risk(score):
    if score >= 65:
        return "High Risk"
    elif score >= 35:
        return "Medium Risk"
    else:
        return "Low Risk"

df["cognitive_load_risk"] = (
    df["cognitive_load_risk_score"].apply(classify_risk)
)

# Save results
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

# Display summary
print("Cognitive Load Risk Analysis Completed!")
print("\nRisk Distribution:")
print(df["cognitive_load_risk"].value_counts())

print(
    "\nAverage Cognitive Load Risk Score:",
    df["cognitive_load_risk_score"].mean().round(2)
)

print(f"\nFile saved at: {OUTPUT_FILE}")
