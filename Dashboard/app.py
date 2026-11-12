from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px

# Chart Styling
px.defaults.template = "plotly_white"
px.defaults.color_discrete_sequence = px.colors.qualitative.Set2

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "cognistream_cleaned_data.csv"

# Page settings
st.set_page_config(
    page_title="CogniStream Dashboard",
    page_icon="🧠",
    layout="wide"
)
# Custom Dashboard Styling
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}

h1 {
    color: #17365D;
    font-weight: 700;
}

h2, h3 {
    color: #24527A;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

[data-testid="stMetricValue"] {
    color: #176B87;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# Dashboard title
st.title("🧠 CogniStream")
st.subheader("Developer Flow-State & Cognitive Load Analytics")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

try:
    df = load_data()
    df["date"] = pd.to_datetime(df["date"])
except FileNotFoundError:
    st.error("Cleaned dataset not found. Please check the data/processed folder.")
    st.stop()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

developers = ["All"] + sorted(df["developer_id"].unique().tolist())
selected_developer = st.sidebar.selectbox(
    "Select Developer",
    developers
)

if selected_developer != "All":
    filtered_df = df[df["developer_id"] == selected_developer]
else:
    filtered_df = df.copy()
  
   # Date filter

st.sidebar.subheader("Date Filter")

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

filtered_df = filtered_df[
    (filtered_df["date"].dt.date >= start_date) &
    (filtered_df["date"].dt.date <= end_date)
]
# Empty Data Validation
if filtered_df.empty:
    st.warning("No data available for the selected filters. Please change your filters.")
    st.stop()
    
# KPI metrics
st.header("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sessions", len(filtered_df))
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

# Chart section styling
st.markdown("""
<style>
.js-plotly-plot .plotly .gtitle {
    font-size: 20px !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)
st.header("📈 Productivity Analysis")

fig1 = px.histogram(
    filtered_df,
    x="productivity_score",
    nbins=20,
    title="Productivity Score Distribution"
)
st.plotly_chart(fig1, width="stretch")

# Focus vs Productivity
st.header("🎯 Focus vs Productivity")

fig2 = px.scatter(
    filtered_df,
    x="focus_score",
    y="productivity_score",
    color="flow_state",
    title="Relationship Between Focus and Productivity"
)
st.plotly_chart(fig2, width="stretch")

# Flow state distribution
st.header("🧠 Flow State Distribution")

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
    title="Developer Flow State"
)
st.plotly_chart(fig3, width="stretch")

# Workload analysis
st.header("⚖️ Workload Analysis")

fig4 = px.scatter(
    filtered_df,
    x="workload_score",
    y="productivity_score",
    color="flow_state",
    title="Workload vs Productivity"
)
st.plotly_chart(fig4, width="stretch")

# Data table
st.header("📋 Developer Data")

st.dataframe(filtered_df, width="stretch")
# Download Filtered Data
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv_data,
    file_name="cognistream_filtered_data.csv",
    mime="text/csv"
)

st.caption("CogniStream | Developer Flow-State & Cognitive Load Analytics")