
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    PROJECT_DIR / "data" / "processed"
    / "developer_performance_summary.csv"
)

OUTPUT_DIR = PROJECT_DIR / "data" / "output"


def main():
    print("Starting Developer Performance Visualization...")

    if not DATA_FILE.exists():
        print("ERROR: Performance summary file not found.")
        return

    df = pd.read_csv(DATA_FILE)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Chart 1: Average Productivity
    df_productivity = df.sort_values(
        "average_productivity", ascending=False
    )

    plt.figure(figsize=(10, 6))
    plt.bar(
        df_productivity["developer_id"],
        df_productivity["average_productivity"]
    )
    plt.title("Average Productivity by Developer")
    plt.xlabel("Developer")
    plt.ylabel("Average Productivity Score")
    plt.ylim(0, 100)
    plt.tight_layout()

    productivity_path = OUTPUT_DIR / "developer_productivity_comparison.png"
    plt.savefig(productivity_path, dpi=300)
    plt.close()

    # Chart 2: High Flow Sessions
    df_flow = df.sort_values(
        "high_flow_sessions", ascending=False
    )

    plt.figure(figsize=(10, 6))
    plt.bar(
        df_flow["developer_id"],
        df_flow["high_flow_sessions"]
    )
    plt.title("High Flow Sessions by Developer")
    plt.xlabel("Developer")
    plt.ylabel("Number of High Flow Sessions")
    plt.tight_layout()

    flow_path = OUTPUT_DIR / "developer_high_flow_comparison.png"
    plt.savefig(flow_path, dpi=300)
    plt.close()

    # Chart 3: Average Focus Score
    df_focus = df.sort_values(
        "average_focus", ascending=False
    )

    plt.figure(figsize=(10, 6))
    plt.bar(
        df_focus["developer_id"],
        df_focus["average_focus"]
    )
    plt.title("Average Focus Score by Developer")
    plt.xlabel("Developer")
    plt.ylabel("Average Focus Score")
    plt.ylim(0, 100)
    plt.tight_layout()

    focus_path = OUTPUT_DIR / "developer_focus_comparison.png"
    plt.savefig(focus_path, dpi=300)
    plt.close()

    print("\nAll visualizations generated successfully!")
    print("Charts saved in:", OUTPUT_DIR)
    print("1.", productivity_path.name)
    print("2.", flow_path.name)
    print("3.", focus_path.name)


if __name__ == "__main__":
    main()
