# Investment Analysis & Visualization

## Overview
This project processes and visualizes investment data from an Excel file named `ROYAL PALM RECEIPT & PORTFOLIO (1).xlsx`. The script loads investment portfolio data, filters relevant months, and generates various charts and visualizations to analyze investment trends.

## Features
- **Data Cleaning & Preparation:**
  - Standardizes column names.
  - Converts `investment_year` to numeric format.
  - Filters data for specific target months (September 2024 - January 2025).
  - Creates a `month_year` column for analysis.
- **Data Grouping & Cross-tabulation:**
  - Groups data by `land` and `unit` types.
  - Computes cross-tabulations for investment month vs. land and unit types.
- **Data Visualization:**
  - Heatmaps for investment trends across land and unit types.
  - Bar charts showing investments per land and unit type.
  - Pie charts displaying investment distribution.
  - Monthly investment bar plots.
  - Line charts for investment trends over time.

## Dependencies
The script requires the following Python libraries:
- `pandas` for data manipulation
- `matplotlib` for plotting
- `seaborn` for statistical visualizations
- `numpy` for numerical operations

Install dependencies using:
```bash
pip install pandas matplotlib seaborn numpy
```

## Usage
### 1. Load and Clean Data
- Reads the `PORTFOLIO` sheet from the Excel file.
- Converts column names to lowercase and replaces spaces with underscores.
- Ensures `investment_year` is numeric.
- Filters for specific investment months.

### 2. Group & Transform Data
- Creates a `month_year` column to store formatted month-year values.
- Groups investments by land and unit type.
- Uses `pd.crosstab` to generate cross-tabulation tables.

### 3. Generate Visualizations
- **Heatmaps** (`plot_heatmap`):
  - Visualizes investments across different land and unit types.
- **Bar Charts** (`plot_bar_chart`):
  - Shows investment distribution by land and unit types.
- **Pie Charts** (`plot_pie_chart`):
  - Displays percentage distribution of investments.
- **Monthly Investment Bar Plot** (`plot_monthly_investment`):
  - Plots the number of investments per month.
- **Investment Trend Line Chart** (`plot_trend_line`):
  - Shows the trend of investments over time.

## Error Handling & Fixes
### Warning: `SettingWithCopyWarning`
- The warning occurs due to modifying a slice of the original DataFrame.
- **Fix:** Use `.loc[]` to explicitly modify the filtered DataFrame:
  ```python
  filtered_df.loc[:, "month_year"] = pd.Categorical(
      filtered_df["month_year"], categories=date_order, ordered=True
  )
  ```

### Error: `ValueError: No numeric data to plot`
- The error occurs when attempting to plot a pie chart with an empty dataset.
- **Fix:** Add a condition to check if data sum is zero before plotting:
  ```python
  def plot_pie_chart(data, title):
      total_sum = data.sum()
      if total_sum.sum() == 0:
          print(f"No data available for {title}. Skipping pie chart.")
          return
      total_sum.plot(kind="pie", autopct="%1.1f%%", figsize=(8, 8), colormap="Set3",
                     startangle=140, wedgeprops={'edgecolor': 'black'})
      plt.title(title, fontsize=14, fontweight="bold")
      plt.ylabel("")
      plt.show()
  ```

## File Structure
```
📂 Project Directory
│-- 📄 script.py (Main Python script for analysis and visualization)
│-- 📄 ROYAL PALM RECEIPT & PORTFOLIO (1).xlsx (Input Excel file)
│-- 📄 README.md (This documentation)
```

## Author
- **Kajola Gbenga**

