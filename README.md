
# 🌴 UMéRA Royal Palm Investment Dashboard

This interactive Streamlit dashboard visualizes and analyzes investment data from the **Royal Palm Estate Project** across a 7-month period (July 2024 – January 2025). It is designed to provide real-time insights to stakeholders, investors, and decision-makers by exploring trends, performance, and portfolio metrics.

---

## 📊 Project Summary

The Royal Palm Investment Dashboard imports, cleans, and transforms the Excel-based investment portfolio data, then presents it in a visually intuitive format using interactive charts, heatmaps, KPIs, and filters.

The dashboard helps answer questions such as:
- How much investment was received monthly?
- Which land types attracted the most interest?
- What is the monthly trend in unit purchases?
- Which months and land types generated the most revenue?

---

## 🧩 Features

- ✅ **Dynamic Filtering**: Filter investment data by month and land type.
- 📈 **Interactive Charts**: View bar charts, line graphs, pie charts, and two types of heatmaps.
- 🧮 **KPI Summary**: Key performance indicators show total investors, land types, and units purchased.
- 📊 **Heatmaps**:
  - Engagement (number of investors)
  - Revenue (total amount invested)
- 📄 **Word Report Download**: Export a pre-written full analytical report.
- 🧑‍💼 **Developer Profile**: Information about the developer and contact links.

---

## 🚀 How to Run the Project

### 🛠️ Prerequisites

- Python 3.8+
- `pip` (Python package manager)
- Install required packages:

```bash
pip install -r requirements.txt
```

> `requirements.txt` contents:

```txt
streamlit
pandas
matplotlib
seaborn
plotly
openpyxl
Pillow
```

### 🧪 Running the App

1. Clone the repository or download the project.
2. Place the Excel file: `ROYAL PALM RECEIPT & PORTFOLIO (2).xlsx` in the project root.
3. Place your profile image as `my_image.jpg` in the same directory.
4. Add the Word report file: `UMéRA Royal Palm Data Analytics Report.docx`.
5. Launch the Streamlit app:

```bash
streamlit run main.py
```

---

## 🧱 Project Structure

```bash
royal-palm-dashboard/
│
├── main.py                         # Main Streamlit app
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
├── ROYAL PALM RECEIPT & PORTFOLIO (2).xlsx   # Excel investment data
├── UMéRA Royal Palm Data Analytics Report.docx  # Downloadable Word report
└── my_image.jpg                    # Developer's profile image
```

---

## 🧠 Technologies Used

| Tool/Library      | Purpose                        |
|------------------|--------------------------------|
| **Python**        | Programming Language            |
| **Streamlit**     | Web App Framework               |
| **Pandas**        | Data Manipulation               |
| **Matplotlib**    | Static Plotting (heatmaps)      |
| **Seaborn**       | Statistical Visualization       |
| **Plotly**        | Interactive Charts              |
| **Pillow (PIL)**  | Image handling in Streamlit     |
| **Openpyxl**      | Excel file support              |

---

## 📸 Screenshots

> Add screenshots of your dashboard in use to better illustrate functionality.

---

## 📥 Report Download Feature

The dashboard includes a button to download a full Word-format analytics report summarizing findings. Make sure to include a file named:
```
UMéRA Royal Palm Data Analytics Report.docx
```

---

## 👤 About the Developer

**Kajola Gbenga**

📇 Certified Data Analyst | Certified Data Scientist | SQL Programmer  
📧 k.gbenga234@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kajolagbenga)  
💻 [GitHub](https://github.com/prodigy234)  
🌐 [Portfolio](https://kajolagbenga.netlify.app/)

---

## ✅ License

This project is licensed under the MIT License. You are free to use, modify, and distribute it with proper attribution.

---

## 📌 Note

- Ensure all external files (Excel, image, Word doc) are in the correct format and properly named.
- If deploying to Streamlit Cloud, remember to upload these supporting files as part of the repository.
