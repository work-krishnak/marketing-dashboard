import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Marketing Analytics Dashboard", layout="wide")

# Load data
df = pd.read_csv("campaign_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Derived KPIs
df["ctr"] = (df["clicks"] / df["impressions"]) * 100
df["cpc"] = df["spend"] / df["clicks"]
df["cpa"] = df["spend"] / df["conversions"]

st.title("Marketing Analytics Dashboard")
st.caption("Campaign performance overview — sample data")

# --- Sidebar filters ---
st.sidebar.header("Filters")
campaigns = st.sidebar.multiselect(
    "Campaign", options=sorted(df["campaign"].unique()), default=sorted(df["campaign"].unique())
)
channels = st.sidebar.multiselect(
    "Channel", options=sorted(df["channel"].unique()), default=sorted(df["channel"].unique())
)

filtered = df[df["campaign"].isin(campaigns) & df["channel"].isin(channels)]

if filtered.empty:
    st.warning("No data matches the selected filters. Adjust filters in the sidebar.")
    st.stop()

# --- KPI row ---
total_spend = filtered["spend"].sum()
total_clicks = filtered["clicks"].sum()
total_conversions = filtered["conversions"].sum()
avg_ctr = (filtered["clicks"].sum() / filtered["impressions"].sum()) * 100
avg_cpc = filtered["spend"].sum() / filtered["clicks"].sum()
avg_cpa = filtered["spend"].sum() / filtered["conversions"].sum()

col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Total Spend", f"${total_spend:,.0f}")
col2.metric("Total Clicks", f"{total_clicks:,.0f}")
col3.metric("Conversions", f"{total_conversions:,.0f}")
col4.metric("Avg CTR", f"{avg_ctr:.2f}%")
col5.metric("Avg CPC", f"${avg_cpc:.2f}")
col6.metric("Avg CPA", f"${avg_cpa:.2f}")

st.divider()

# --- Trend chart ---
st.subheader("Spend & Conversions Over Time")
trend = filtered.groupby("date")[["spend", "conversions"]].sum().reset_index()
fig_trend = px.line(trend, x="date", y=["spend", "conversions"], markers=True)
st.plotly_chart(fig_trend, use_container_width=True)

# --- Channel comparison ---
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Spend by Channel")
    channel_spend = filtered.groupby("channel")["spend"].sum().reset_index()
    fig_channel = px.pie(channel_spend, names="channel", values="spend", hole=0.4)
    st.plotly_chart(fig_channel, use_container_width=True)

with col_b:
    st.subheader("Conversions by Campaign")
    campaign_conv = filtered.groupby("campaign")["conversions"].sum().reset_index()
    fig_campaign = px.bar(campaign_conv, x="campaign", y="conversions")
    st.plotly_chart(fig_campaign, use_container_width=True)

# --- Raw data table ---
st.subheader("Raw Campaign Data")
st.dataframe(filtered.sort_values("date"), use_container_width=True)