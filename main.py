# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

# Page config
st.set_page_config(page_title="Royal Palm Investment Dashboard", layout="wide")

# Load Excel Data
xls = pd.ExcelFile("ROYAL PALM RECEIPT & PORTFOLIO (2).xlsx")
df_portfolio = pd.read_excel(xls, sheet_name="PORTFOLIO")

# Data preparation
df_portfolio.columns = df_portfolio.columns.str.lower().str.replace(" ", "_")
df_portfolio["investment_year"] = pd.to_numeric(df_portfolio["investment_year"], errors="coerce")
df_portfolio["investment_month"] = df_portfolio["investment_month"].astype(str).str.upper()

# Define and format month_year
target_months = {
    "JULY": 2024, "AUGUST": 2024, "SEPTEMBER": 2024,
    "OCTOBER": 2024, "NOVEMBER": 2024, "DECEMBER": 2024, "JANUARY": 2025
}
df_portfolio["month_year"] = df_portfolio.apply(
    lambda row: f"{row['investment_month'].capitalize()} {int(row['investment_year'])}"
    if row["investment_month"] in target_months else None, axis=1
)
filtered_df = df_portfolio[df_portfolio["month_year"].notna()]
date_order = list(target_months.keys())
date_order = [month.capitalize() + f" {target_months[month]}" for month in date_order]
filtered_df["month_year"] = pd.Categorical(filtered_df["month_year"], categories=date_order, ordered=True)

# Sidebar Filters
with st.sidebar:
    st.header("📊 Filter Investment Data")
    selected_months = st.multiselect("Select Month(s)", options=date_order, default=date_order)
    selected_lands = st.multiselect("Select Land Type(s)", options=filtered_df["land"].dropna().unique(), default=filtered_df["land"].dropna().unique())

filtered = filtered_df[filtered_df["month_year"].isin(selected_months) & filtered_df["land"].isin(selected_lands)]

# Title
st.title("🌴 Royal Palm Investment Portfolio Dashboard")
st.markdown("#### _Seven-Month Investment Analysis (July 2024 - January 2025)_")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("🧑 Total Investors", value=len(filtered))
col2.metric("🌍 Land Types", value=filtered['land'].nunique())
col3.metric("🏠 Total Units", value=int(filtered['unit'].sum()))

# Bar Chart - Investment by Land Type
land_group = filtered.groupby(["month_year", "land"]).size().unstack(fill_value=0)
fig1 = px.bar(land_group, barmode="group", title="📍 Monthly Investments by Land Type", labels={"value": "No. of Investments", "month_year": "Month"})
st.plotly_chart(fig1, use_container_width=True)

# Bar Chart - Units Bought
unit_group = filtered.groupby(["month_year", "unit"]).size().unstack(fill_value=0)
fig2 = px.bar(unit_group, barmode="group", title="🏗️ Units Bought per Month")
st.plotly_chart(fig2, use_container_width=True)

# Pie Chart - Land Type Distribution
land_totals = filtered["land"].value_counts()
fig3 = px.pie(names=land_totals.index, values=land_totals.values, title="🥧 Investment Share by Land Type")
st.plotly_chart(fig3, use_container_width=True)

# Line Chart - Investment Trend
trend_data = filtered.groupby("month_year").size().reindex(date_order, fill_value=0)
fig4 = px.line(x=trend_data.index, y=trend_data.values, markers=True, title="📈 Investment Trend Over Time")
fig4.update_layout(xaxis_title="Month", yaxis_title="Number of Investments")
st.plotly_chart(fig4, use_container_width=True)

# Heatmap - Month vs Land
st.markdown("### 🔥 Heatmap of Investment Engagement (Month vs Land Type)")
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(pd.crosstab(filtered["month_year"], filtered["land"]), annot=True, fmt="d", cmap="coolwarm", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Word Report Download
st.markdown("### 📝 Download Full Portfolio Analytics Report")
with open("UMéRA Royal Palm Data Analytics Report.docx", "rb") as doc_file:
    st.download_button(
        label="📥 Download Full Word Report",
        data=doc_file,
        file_name="UMeRA_RoyalPalm_Analytics_Report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# Footer
st.markdown("---")
st.markdown("Developed by **Kajola Gbenga** | 📊 _Data Analytics Report Engine_ | 🌐 _UMéRA Business School_")
