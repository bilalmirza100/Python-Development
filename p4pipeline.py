import argparse
import logging
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path
import config

logging.basicConfig(
    filename="pipeline_audit.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def run_pipeline(start_date=None, end_date=None):
    files = list(Path("data").glob(config.INPUT_PATTERN))
    if not files:
        logging.warning("No input workbooks found.")
        return 0.0

    cleaned_dfs = []
    for f in files:
        try:
            df = pd.read_excel(f)
            # Schema Validation
            if not all(col in df.columns for col in config.EXPECTED_COLS):
                logging.error(f"Missing columns in {f.name}. Skipped.")
                continue
            
            # Cleaning & Filtering Invalid Rows
            df = df.dropna(subset=["order_id", "date"]).copy()
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
            df["revenue"] = df["quantity"] * df["unit_price"]
            cleaned_dfs.append(df)
        except Exception as e:
            logging.error(f"Error processing {f.name}: {e}")

    if not cleaned_dfs:
        return 0.0

    master = pd.concat(cleaned_dfs, ignore_index=True)

    # Command-Line Date Range Filtering
    if start_date:
        master = master[master["date"] >= pd.to_datetime(start_date)]
    if end_date:
        master = master[master["date"] <= pd.to_datetime(end_date)]

    # Calculate KPIs
    region_kpi = master.groupby("region").agg(total_revenue=("revenue", "sum"), orders=("order_id", "count")).reset_index()
    product_kpi = master.groupby("product").agg(total_revenue=("revenue", "sum"), units=("quantity", "sum")).reset_index()
    total_revenue = master["revenue"].sum()

    # Generate Chart
    plt.figure(figsize=(6, 4))
    plt.bar(region_kpi["region"], region_kpi["total_revenue"] / 1e3, color="#1f77b4")
    plt.title("Revenue by Region ($K)")
    plt.tight_layout()
    chart_path = config.OUTPUT_DIR / "region_chart.png"
    plt.savefig(chart_path, dpi=200)
    plt.close()

    # Export Excel Report with OpenPyXL
    excel_path = config.OUTPUT_DIR / "Executive_Sales_Report.xlsx"
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        master.to_excel(writer, sheet_name="Transactions", index=False)
        region_kpi.to_excel(writer, sheet_name="Region KPIs", index=False)
        product_kpi.to_excel(writer, sheet_name="Product KPIs", index=False)

    # Export PDF Summary
    pdf_path = config.OUTPUT_DIR / "Executive_Sales_Summary.pdf"
    with PdfPages(pdf_path) as pdf:
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.axis('off')
        ax.text(0.1, 0.9, "Executive Sales Summary", fontsize=18, fontweight='bold', color="#1F4E78")
        ax.text(0.1, 0.82, f"Total Revenue: ${total_revenue:,.2f}", fontsize=14, fontweight='bold')
        pdf.savefig(fig)
        plt.close(fig)

    logging.info(f"Pipeline executed successfully. Total Revenue: {total_revenue}")
    return total_revenue

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", help="YYYY-MM-DD")
    parser.add_argument("--end-date", help="YYYY-MM-DD")
    args = parser.parse_args()
    run_pipeline(args.start_date, args.end_date)