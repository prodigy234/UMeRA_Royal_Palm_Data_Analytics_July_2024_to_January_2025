import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

# Page config
st.set_page_config(page_title="UMéRA Royal Palm Investment Dashboard", layout="wide")

# Load Excel Data
file_path = "ROYAL PALM RECEIPT & PORTFOLIO (2).xlsx"
xls = pd.ExcelFile(file_path)
df_portfolio = pd.read_excel(xls, sheet_name="PORTFOLIO")

# Data preparation
df_portfolio.columns = df_portfolio.columns.str.lower().str.replace(" ", "_")
df_portfolio["investment_year"] = pd.to_numeric(df_portfolio["investment_year"], errors="coerce")
df_portfolio["investment_month"] = df_portfolio["investment_month"].astype(str).str.upper()

# Define target months and years
date_order = ["July 2024", "August 2024", "September 2024", "October 2024", "November 2024", "December 2024", "January 2025"]
month_mapping = {month.split()[0].upper(): month for month in date_order}

df_portfolio["month_year"] = df_portfolio.apply(
    lambda row: month_mapping.get(row["investment_month"], None) if row["investment_year"] in [2024, 2025] else None, 
    axis=1
)

filtered_df = df_portfolio[df_portfolio["month_year"].notna()].copy()
filtered_df["month_year"] = pd.Categorical(filtered_df["month_year"], categories=date_order, ordered=True)

# Convert "AMOUNT" to "AMOUNT INVESTED"
if "amount" in filtered_df.columns:
    filtered_df.rename(columns={"amount": "amount_invested"}, inplace=True)

filtered_df["amount_invested"] = pd.to_numeric(filtered_df["amount_invested"], errors="coerce")

# Sidebar Filters
with st.sidebar:
    st.header("\U0001F4CA Filter UMéRA Investment Data")
    selected_months = st.multiselect("Select Month(s)", options=date_order, default=date_order)
    selected_lands = st.multiselect("Select Land Type(s)", options=filtered_df["land"].dropna().unique(), default=filtered_df["land"].dropna().unique())

filtered = filtered_df[filtered_df["month_year"].isin(selected_months) & filtered_df["land"].isin(selected_lands)]

# Title
st.title("\U0001F334 An Interactive UMéRA Royal Palm Investment Portfolio Dashboard")
st.markdown("#### _Seven-Month Investment Analysis (July 2024 - January 2025)_")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("\U0001F9D1 Total Investors", value=len(filtered))
col2.metric("\U0001F30D Land Types", value=filtered['land'].nunique())
col3.metric("\U0001F3E0 Total Units", value=int(filtered['unit'].sum()))

# Bar Chart - Investment by Land Type
land_group = filtered.groupby(["month_year", "land"]).size().unstack(fill_value=0)
fig1 = px.bar(land_group, barmode="group", title="\U0001F4CD Monthly Investments by Land Type", labels={"value": "No. of Investments", "month_year": "Month"})
st.plotly_chart(fig1, use_container_width=True)

# Bar Chart - Units Bought
unit_group = filtered.groupby(["month_year", "unit"]).size().unstack(fill_value=0)
fig2 = px.bar(unit_group, barmode="group", title="\U0001F3D7️ Units Bought per Month")
st.plotly_chart(fig2, use_container_width=True)

# Pie Chart - Land Type Distribution
land_totals = filtered["land"].value_counts()
fig3 = px.pie(names=land_totals.index, values=land_totals.values, title="\U0001F967 Investment Share by Land Type")
st.plotly_chart(fig3, use_container_width=True)

# Line Chart - Investment Trend
trend_data = filtered.groupby("month_year").size().reindex(date_order, fill_value=0)
fig4 = px.line(x=trend_data.index, y=trend_data.values, markers=True, title="\U0001F4C8 Investment Trend Over Time")
fig4.update_layout(xaxis_title="Month", yaxis_title="Number of Investments")
st.plotly_chart(fig4, use_container_width=True)

# Heatmap - Month vs Land
st.markdown("### \U0001F525 Heatmap of Investment Engagement (Month vs Land Type)")
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(pd.crosstab(filtered["month_year"], filtered["land"]), annot=True, fmt="d", cmap="coolwarm", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Additional Heatmap using amount_invested
def plot_heatmap(df):
    heatmap_data = df.pivot_table(values="amount_invested", index="month_year", columns="land", aggfunc="sum", fill_value=0)
    heatmap_data = heatmap_data.reindex(date_order)
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".0f", linewidths=0.5)
    plt.title("UMéRA Royal Palm Total Amount Generated Heatmap (July 2024 - Jan 2025)", fontsize=14, fontweight="bold")
    plt.xlabel("Land Type", fontsize=12)
    plt.ylabel("Investment Month", fontsize=12)
    plt.xticks(rotation=45)
    st.pyplot(plt)

st.markdown("### \U0001F525 Heatmap of Total Amount Invested (Month vs Land Type)")
plot_heatmap(filtered)

# Word Report Download
st.markdown("### \U0001F4DD Download Full UMéRA Portfolio Analytics Report")
with open("UMéRA Royal Palm Data Analytics Report.docx", "rb") as doc_file:
    st.download_button(
        label="\U0001F4E5 Download Full Word Report",
        data=doc_file,
        file_name="UMeRA_RoyalPalm_Analytics_Report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# Footer
st.markdown("---")
st.markdown("# About the Developer")

st.image("my_image.jpg", width=150)
st.markdown("## **Kajola Gbenga**")

st.markdown(
    """
\U0001F4C7 Certified Data Analyst | Certified Data Scientist | Certified SQL Programmer | Mobile App Developer | AI/ML Engineer

\U0001F517 [LinkedIn](https://www.linkedin.com/in/kajolagbenga)  
\U0001F4DC [View My Certifications & Licences](https://www.datacamp.com/portfolio/kgbenga234)  
\U0001F4BB [GitHub](https://github.com/prodigy234)  
\U0001F310 [Portfolio](https://kajolagbenga.netlify.app/)  
\U0001F4E7 k.gbenga234@gmail.com
"""
)

st.markdown("✅ Created using Python and Streamlit")
