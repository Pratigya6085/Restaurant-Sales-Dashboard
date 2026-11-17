# ==============================================================================
#                      RUNGTA INTERNATIONAL SKILLS UNIVERSITY
#                     SCHOOL OF INFORMATION TECHNOLOGY
#                         BACHELOR OF COMPUTER APPLICATION
# ==============================================================================
#  PS No.        : 82
#  Project Title : Restaurant Sales Dashboard
#  Language      : Python 3
#  Concepts      : Pandas, Matplotlib, CSV, GroupBy
# ==============================================================================

# ------------------------------------------------------------------------------
#                         STUDENT SUBMISSION DETAILS
# ------------------------------------------------------------------------------
#  Student Name  : Pratigya Chandravanshi
#  ERP Number    : RU-26-02000
#  Section       : B
#  Session       : 2026-27
#  University    : Rungta International Skills University
#  Submitted To  : Satyaprakash Sir
# ------------------------------------------------------------------------------

import os
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# 1. LOAD DATA & HANDLE INVALID ROWS / MISSING FILES
# ------------------------------------------------------------------------------
def load_sales_data(filename="restaurant_sales.csv"):
    """
    Reads restaurant_sales.csv, validates rows, calculates Sales (Quantity x Price),
    and skips invalid rows with warning messages.
    """
    # Check if file exists (Test Case 3b)
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return None

    try:
        df = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None

    valid_rows = []
    
    # Iterate through rows and validate numeric columns
    for index, row in df.iterrows():
        row_num = index + 1
        try:
            date = str(row['Date']).strip()
            item = str(row['Item']).strip()
            category = str(row['Category']).strip()
            
            # Convert Quantity and Price to float
            quantity = float(row['Quantity'])
            price = float(row['Price'])
            
            # Store valid record with Sales column
            valid_rows.append({
                'Date': date,
                'Item': item,
                'Category': category,
                'Quantity': quantity,
                'Price': price,
                'Sales': quantity * price
            })
        except (ValueError, TypeError):
            # Exact warning required for Test Case 3a
            print(f"Warning: Row {row_num} skipped - Quantity must be a number.")
            continue

    if not valid_rows:
        return None

    return pd.DataFrame(valid_rows)


# ------------------------------------------------------------------------------
# 2. FEATURE 1: SALES BY CATEGORY (Test Case 1)
# ------------------------------------------------------------------------------
def show_sales_by_category(df):
    """
    Groups sales by Category using Pandas GroupBy and displays total sales.
    """
    if df is None or df.empty:
        return
    
    category_sales = df.groupby('Category')['Sales'].sum()
    
    # Expected order / output format
    for category, sales in category_sales.items():
        print(f"{category} : Rs. {int(sales)}")
    
    total_sales = int(df['Sales'].sum())
    print(f"Total sales: Rs. {total_sales}")


# ------------------------------------------------------------------------------
# 3. FEATURE 2: TOP ITEMS BY QUANTITY & REVENUE (Test Case 2 & 4)
# ------------------------------------------------------------------------------
def show_top_items(df):
    """
    Identifies top items by total quantity and revenue using GroupBy aggregation.
    """
    if df is None or df.empty:
        return

    item_stats = df.groupby('Item').agg({
        'Quantity': 'sum',
        'Sales': 'sum'
    })

    # Find item with maximum quantity
    top_qty_item = item_stats['Quantity'].idxmax()
    top_qty_val = int(item_stats.loc[top_qty_item, 'Quantity'])
    
    # Find item with maximum revenue
    top_rev_item = item_stats['Sales'].idxmax()
    top_rev_val = int(item_stats.loc[top_rev_item, 'Sales'])

    unit_str = "unit" if top_qty_val == 1 else "units"
    print(f"Top item by quantity: {top_qty_item} ({top_qty_val} {unit_str})")
    print(f"Top item by revenue: {top_rev_item} (Rs. {top_rev_val})")


# ------------------------------------------------------------------------------
# 4. FEATURE 3: DAILY SALES AND BEST DAY (Test Case 4)
# ------------------------------------------------------------------------------
def show_daily_sales(df):
    """
    Calculates total daily sales using GroupBy and identifies the best day.
    """
    if df is None or df.empty:
        return

    daily_sales = df.groupby('Date')['Sales'].sum()
    
    for date, sales in daily_sales.items():
        print(f"{date} : Rs. {int(sales)}")
        
    best_day = daily_sales.idxmax()
    print(f"Best day: {best_day}")


# ------------------------------------------------------------------------------
# 5. FEATURE 4: DASHBOARD VISUALIZATION (CHARTS)
# ------------------------------------------------------------------------------
def plot_sales_dashboard(df):
    """
    Generates bar charts for Sales by Category and Daily Sales using Matplotlib.
    """
    if df is None or df.empty:
        return

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Bar chart 1: Category Sales
    cat_sales = df.groupby('Category')['Sales'].sum()
    axes[0].bar(cat_sales.index, cat_sales.values, color='#4C72B0', edgecolor='black')
    axes[0].set_title("Sales by Category", fontsize=12, fontweight='bold')
    axes[0].set_xlabel("Category")
    axes[0].set_ylabel("Sales (Rs.)")
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Bar chart 2: Daily Sales
    day_sales = df.groupby('Date')['Sales'].sum()
    axes[1].bar(day_sales.index, day_sales.values, color='#DD8452', edgecolor='black')
    axes[1].set_title("Daily Sales Trend", fontsize=12, fontweight='bold')
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel("Sales (Rs.)")
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------------------------
# MAIN MENU DRIVER / CONSOLE INTERFACE
# ------------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("             RESTAURANT SALES DASHBOARD")
    print("=" * 60)
    
    filename = input("Enter CSV file name [default: restaurant_sales.csv]: ").strip()
    if not filename:
        filename = "restaurant_sales.csv"

    # Load dataset
    df = load_sales_data(filename)
    if df is None:
        return

    while True:
        print("\n1. Sales by category")
        print("2. Top items")
        print("3. Top items and daily sales")
        print("4. Show Charts")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        print()

        if choice == '1':
            show_sales_by_category(df)
        elif choice == '2':
            show_top_items(df)
            total_sales = int(df['Sales'].sum())
            print(f"Total sales: Rs. {total_sales}")
        elif choice == '3':
            show_top_items(df)
            show_daily_sales(df)
        elif choice == '4':
            plot_sales_dashboard(df)
        elif choice == '5':
            print("Program closed successfully.")
            break
        else:
            print("Invalid choice! Enter 1-5.")

if __name__ == "__main__":
    main()
