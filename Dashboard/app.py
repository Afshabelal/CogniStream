
from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="CogniStream Analytics",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# Dashboard Styling
# ---------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #F4F7FB;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    color: #17365D;
    font-weight: 800;
}

h2, h3 {
    color: #24527A;
}
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #FFFFFF, #EAF4FF);
    padding: 25px 20px;
    border-radius: 16px;
    border: 1px solid #C9DDF5;
    box-shadow: 0 5px 15px rgba(30, 80, 140, 0.10);
    transition: 0.3s ease;
}

[data-testid="stMetricLabel"] {
    color: #456789;
    font-size: 15px;
    font-weight: 700;
}
[data-testid="stMetricValue"] {
    color: #176B87;
    font-weight: 750;
}


[data-testid="stSidebar"] {
    background-color: #EAF0F8;
}

.chart-card {
    background: white;
    padding: 15px;
    border-radius: 14px;
    border: 1px solid #E1E8F0;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Project Paths
# ---------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR / "data" / "processed"
    / "cognitive_load_risk_analysis.csv"
)

# ---------------------------------
# Load Dataset
# ---------------------------------
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

try:
    df = load_data()
    df["date"] = pd.to_datetime(df["date"])
except FileNotFoundError:
    st.error("Cleaned dataset not found. Check data/processed folder.")
    st.stop()

# ---------------------------------
# Sidebar Filters
# ---------------------------------
st.sidebar.title("⚙️ Dashboard Controls")
st.sidebar.markdown("---")

developers = ["All"] + sorted(
    df["developer_id"].unique().tolist()
)

selected_developer = st.sidebar.selectbox(
    "Select Developer",
    developers
)

min_date = df["date"].min().date()
max_date = df["date"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
    format="YYYY-MM-DD"
)

if isinstance(date_range, (tuple, list)):
    if len(date_range) == 2:
        start_date, end_date = date_range
    elif len(date_range) == 1:
        start_date = end_date = date_range[0]
    else:
        start_date, end_date = min_date, max_date
else:
    start_date = end_date = date_range

filtered_df = df.copy()

if selected_developer != "All":
    filtered_df = filtered_df[
        filtered_df["developer_id"] == selected_developer
    ]

filtered_df = filtered_df[
    (filtered_df["date"].dt.date >= start_date)
    & (filtered_df["date"].dt.date <= end_date)
]

st.sidebar.markdown("---")
st.sidebar.caption("CogniStream | Analytics Platform")

if filtered_df.empty:
    st.warning("No data found for selected filters.")
    st.stop()

# ---------------------------------
# Dashboard Header
# ---------------------------------
st.title("🧠 CogniStream")

st.markdown(
    "### Developer Flow-State & Cognitive Load Analytics"
)

st.markdown(
    "Monitor developer productivity, focus, workload "
    "and cognitive flow patterns."
)

st.markdown("---")

# ---------------------------------
# KPI Section
# ---------------------------------
st.subheader("📊 Performance Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sessions",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Avg Productivity",
    f"{filtered_df['productivity_score'].mean():.2f}"
)

col3.metric(
    "Avg Focus Score",
    f"{filtered_df['focus_score'].mean():.2f}"
)

col4.metric(
    "Avg Workload",
    f"{filtered_df['workload_score'].mean():.2f}"
)

st.markdown("---")
chart_config = {
    "template": "plotly_white",
    "height": 400,
    "paper_bgcolor": "white",
    "plot_bgcolor": "#F8FBFF",
    "font": {
        "family": "Arial",
        "color": "#24415E",
        "size": 13
    },
    "title_font": {
        "size": 19,
        "color": "#17365D"
    },
    "margin": {
        "l": 40,
        "r": 30,
        "t": 70,
        "b": 45
    }
 }


# ---------------------------------
# Productivity Analysis
# ---------------------------------
st.subheader("📈 Productivity Analysis")

fig1 = px.histogram(
    filtered_df,
    x="productivity_score",
    nbins=20,
    title="Productivity Score Distribution",
    color_discrete_sequence=["#4285F4"]
)

fig1.update_layout(**chart_config)
fig1.update_layout(
    xaxis_title="Productivity Score",
    yaxis_title="Number of Sessions"
)
with st.container(border=True):
    st.plotly_chart(
        fig1,
        width="stretch",
        key="productivity_chart"
    )

st.markdown("---")

# ---------------------------------
# Focus and Flow Analysis
# ---------------------------------
st.subheader("🎯 Focus & Flow Analysis")

col1, col2 = st.columns(2)

with col1:
    fig2 = px.scatter(
        filtered_df,
        x="focus_score",
        y="productivity_score",
        color="flow_state",
        title="Focus vs Productivity",
        color_discrete_sequence=["#4285F4", "#20A67A"],
        hover_data=["developer_id"]
    )

    fig2.update_layout(**chart_config)

    with st.container(border=True):
        st.plotly_chart(
            fig2,
            width="stretch",
            key="focus_chart"
        )

with col2:
    flow_counts = (
        filtered_df["flow_state"]
        .value_counts()
        .reset_index()
    )

    flow_counts.columns = ["Flow State", "Count"]

    fig3 = px.pie(
        flow_counts,
        names="Flow State",
        values="Count",
        hole=0.55,
        title="Flow State Distribution",
        color_discrete_sequence=["#4285F4", "#20A67A"]
    )

    fig3.update_layout(**chart_config)
      
    with st.container(border=True):
        st.plotly_chart(
            fig3,
            width="stretch",
            key="flow_chart"
        )
st.markdown("---")

# ---------------------------------
# Workload Analysis
# ---------------------------------
st.subheader("⚖️ Workload Analysis")

fig4 = px.scatter(
    filtered_df,
    x="workload_score",
    y="productivity_score",
    color="flow_state",
    title="Workload vs Productivity",
    color_discrete_sequence=["#E89B45", "#4285F4"],
    hover_data=["developer_id"]
)

fig4.update_layout(**chart_config)

with st.container(border=True):
    st.plotly_chart(
        fig4,
        width="stretch",
        key="workload_chart"
    )

st.markdown("---")

# ---------------------------------
# Cognitive Load Risk Analysis
# ---------------------------------
st.markdown("---")

st.subheader("🧠 Cognitive Load Risk Analysis")

# Risk distribution
risk_counts = (
    filtered_df["cognitive_load_risk"]
    .value_counts()
    .reindex(
        ["Low Risk", "Medium Risk", "High Risk"],
        fill_value=0
    )
    .reset_index()
)

risk_counts.columns = ["Risk Category", "Sessions"]

risk_col1, risk_col2 = st.columns(2)

with risk_col1:
    st.metric(
        "Average Cognitive Load Risk",
        f"{filtered_df['cognitive_load_risk_score'].mean():.2f}"
    )

    st.metric(
        "High Risk Sessions",
        int(
            (filtered_df["cognitive_load_risk"] == "High Risk").sum()
        )
    )

with risk_col2:
    fig_risk = px.bar(
        risk_counts,
        x="Risk Category",
        y="Sessions",
        color="Risk Category",
        title="Cognitive Load Risk Distribution",
        text="Sessions",
        category_orders={
            "Risk Category": [
                "Low Risk",
                "Medium Risk",
                "High Risk"
            ]
        },
        color_discrete_map={
            "Low Risk": "#20A67A",
            "Medium Risk": "#E89B45",
            "High Risk": "#D9534F"
        }
    )

    fig_risk.update_layout(**chart_config)

    with st.container(border=True):
        st.plotly_chart(
            fig_risk,
            width="stretch",
            key="cognitive_risk_chart"
        )

# ---------------------------------
# Developer Data
# ---------------------------------

with st.container(border=True):
    st.markdown("### 📋 Developer Activity Records")

    st.dataframe(
        filtered_df,
        width="stretch",
        hide_index=True,
        height=400
    )
csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv_data,
    file_name="cognistream_filtered_data.csv",
    mime="text/csv"
)

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("---")

st.caption(
    "CogniStream | Developer Flow-State "
    "& Cognitive Load Analytics"
)
