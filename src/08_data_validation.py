
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "processed" / "cognistream_cleaned_data.csv"
OUTPUT_FILE = PROJECT_DIR / "data" / "processed" / "data_quality_report.csv"

# Required columns
REQUIRED_COLUMNS = [
    "developer_id",
    "date",
    "coding_hours",
    "focus_score",
    "workload_score",
    "productivity_score",
    "flow_state"
]


def main():
    print("Starting CogniStream Data Validation...")

    if not DATA_FILE.exists():
        print(f"ERROR: Dataset not found: {DATA_FILE}")
        return

    df = pd.read_csv(DATA_FILE)

    checks = []

    # Check required columns
    for column in REQUIRED_COLUMNS:
        checks.append({
            "check": f"Column exists: {column}",
            "status": "PASS" if column in df.columns else "FAIL",
            "issue_count": 0 if column in df.columns else 1
        })

    # Check missing values
    missing_count = int(df.isnull().sum().sum())
    checks.append({
        "check": "Missing values",
        "status": "PASS" if missing_count == 0 else "FAIL",
        "issue_count": missing_count
    })

    # Check duplicate records
    duplicate_count = int(df.duplicated().sum())
    checks.append({
        "check": "Duplicate records",
        "status": "PASS" if duplicate_count == 0 else "FAIL",
        "issue_count": duplicate_count
    })

    # Check score ranges
    for column in ["focus_score", "workload_score", "productivity_score"]:
        if column in df.columns:
            invalid_count = int(
                (~df[column].between(0, 100)).sum()
            )
            checks.append({
                "check": f"Valid range: {column} (0-100)",
                "status": "PASS" if invalid_count == 0 else "FAIL",
                "issue_count": invalid_count
            })

    # Save validation report
    report = pd.DataFrame(checks)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(OUTPUT_FILE, index=False)

    print("\nDATA VALIDATION SUMMARY")
    print("-----------------------")
    print(report.to_string(index=False))
    print("\nTotal records:", len(df))
    print("Passed checks:", (report["status"] == "PASS").sum())
    print("Failed checks:", (report["status"] == "FAIL").sum())
    print("\nReport saved at:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
