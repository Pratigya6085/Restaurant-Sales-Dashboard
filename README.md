# Restaurant Sales Dashboard (PS No. 82)

An interactive Python-based analytics dashboard designed to process restaurant sales data from CSV files, compute critical financial metrics, and display insights through console reports and visual charts using **Pandas** and **Matplotlib**.

---

## 📌 Project Details

- **PS No.:** 82
- **Project Title:** Restaurant Sales Dashboard
- **Student Name:** Pratigya Chandravanshi
- **ERP Number:** RU-26-02000
- **University:** Rungta International Skills University
- **Section:** B
- **Submitted To:** [Satyaprakash Sir (@SATYAPRAKASHSETHY)](https://github.com/SATYAPRAKASHSETHY)

---

## 🚀 Key Features

1. **Robust Data Loading & Validation:**
   - Dynamically loads CSV files (`restaurant_sales.csv` by default).
   - Validates numerical columns (`Quantity` and `Price`) and skips invalid rows with precise warning messages.
   - Computes dynamic `Sales` for each valid item (`Quantity × Price`).

2. **Category Sales Analysis:**
   - Summarizes aggregate sales partitioned by product categories using Pandas `groupby`.
   - Computes total cumulative revenue across all menu categories.

3. **Item & Performance Insights:**
   - Identifies top-performing menu items based on **Quantity Sold** and **Revenue Generated**.
   - Handles singular/plural unit labeling gracefully.

4. **Daily Sales & Best Day Metrics:**
   - Aggregates sales figures by date to identify overall daily performance.
   - Pinpoints the single best revenue-generating day.

5. **Visual Dashboard (Matplotlib):**
   - Renders side-by-side bar charts for **Sales by Category** and **Daily Sales Trend**.
   - Features gridlines and customized plot aesthetics.

---

## 📁 File Structure

```text
.
├── main.py                 # Main Python source code
├── restaurant_sales.csv    # Default sales dataset
└── README.md               # Project documentation
```

---

## 📋 CSV Format Requirements

The input file `restaurant_sales.csv` must contain the following schema:

| Column Header | Data Type | Description |
| :--- | :--- | :--- |
| `Date` | String | Transaction date (e.g., `YYYY-MM-DD` or `DD-MM-YYYY`) |
| `Item` | String | Name of the food/drink item |
| `Category` | String | Category (e.g., `Beverages`, `Main Course`, `Desserts`) |
| `Quantity` | Numeric | Units ordered (must be numeric) |
| `Price` | Numeric | Price per unit in currency units |

---

## 💻 How to Run

1. **Install Prerequisites:**
   Ensure Python 3.8+ is installed along with the required dependencies:
   ```bash
   pip install pandas matplotlib
   ```

2. **Execute the Script:**
   ```bash
   python main.py
   ```

3. **Menu Options:**
   - `1` : View total sales grouped by Category.
   - `2` : View top items by unit sales and revenue.
   - `3` : View top items alongside complete daily sales performance.
   - `4` : Render interactive Matplotlib charts.
   - `5` : Exit the dashboard.
