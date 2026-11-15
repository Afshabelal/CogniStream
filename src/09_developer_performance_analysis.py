
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "processed" / "cognistream_cleaned_data.csv"
OUTPUT_FILE = PROJECT_DIR / "data" / "processed" / "developer_performance_summary.csv"


def main():
    print("Starting Developer Performance Analysis...")

    if not DATA_FILE.exists():
        print(f"ERROR: Dataset not found: {DATA_FILE}")
        return

    df = pd.read_csv(DATA_FILE)

    required_columns = [
        "developer_id",
        "productivity_score",
        "focus_score",
        "workload_score",
        "coding_hours",
        "flow_state"
    ]

    missing_columns = [
        col for col in required_columns if col not in df.columns
    ]

    if missing_columns:
        print("ERROR: Missing columns:", missing_columns)
        return

    # Calculate performance summary for each developer
    summary = df.groupby("developer_id").agg(
        total_sessions=("developer_id", "count"),
        average_productivity=("productivity_score", "mean"),
        average_focus=("focus_score", "mean"),
        average_workload=("workload_score", "mean"),
        total_coding_hours=("coding_hours", "sum"),
        high_flow_sessions=("flow_state", lambda x: (x == "High Flow").sum())
    ).reset_index()

    # Calculate high flow percentage
    summary["high_flow_percentage"] = (
        summary["high_flow_sessions"] / summary["total_sessions"] * 100
    )

    # Sort developers by average productivity
    summary = summary.sort_values(
        by="average_productivity",
        ascending=False
    )

    # Round numerical values
    numeric_columns = summary.select_dtypes(include="number").columns
    summary[numeric_columns] = summary[numeric_columns].round(2)

    # Save report
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUTPUT_FILE, index=False)

    print("\nDEVELOPER PERFORMANCE SUMMARY")
    print("--------------------------------")
    print(summary.to_string(index=False))

    print("\nTotal developers:", len(summary))
    print("Average productivity:", round(df["productivity_score"].mean(), 2))
    print("\nReport saved at:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
