from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

files = sorted(RAW_DIR.glob("*.csv"))

print(f"Found {len(files)} CSV file(s):\n")

for file in files:
    print("=" * 80)
    print(f"File: {file.name}")

    try:
        df = pd.read_csv(file)
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")
        print("\nColumn names:")
        print(list(df.columns))
        print("\nFirst 10 rows:")
        print(df.head(10))
    except Exception as e:
        print(f"Error reading file: {e}")