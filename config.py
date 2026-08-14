from pathlib import Path

INPUT_PATTERN = "sales_*.xlsx"
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

EXPECTED_COLS = ["order_id", "date", "region", "product", "quantity", "unit_price"]
CONTROL_TOTAL_REVENUE = 154200.0 