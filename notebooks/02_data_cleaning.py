from pathlib import Path
import pandas as pd
import re

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "drsi.csv"
CLEANED_DIR = PROJECT_ROOT / "data" / "cleaned"
CLEANED_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_WIDE = CLEANED_DIR / "cleaned_retail_sales_wide.csv"
OUTPUT_LONG = CLEANED_DIR / "cleaned_retail_sales_long.csv"

df = pd.read_csv(RAW_FILE)

# Rename first column
df = df.rename(columns={"Title": "period"})

# Remove metadata rows
metadata_rows = ["CDID", "PreUnit", "Unit", "Release Date", "Next release", "Important Notes"]
df = df[~df["period"].astype(str).isin(metadata_rows)].copy()

# Keep only monthly rows, e.g. 2020 JAN, 2020 FEB, 2020 MAR
month_pattern = r"^\d{4}\s[A-Z]{3}$"
df = df[df["period"].astype(str).str.upper().str.match(month_pattern, na=False)].copy()

# Convert period to date
df["period_clean"] = df["period"].astype(str).str.title()
df["date"] = pd.to_datetime(df["period_clean"], format="%Y %b", errors="coerce")
df = df.dropna(subset=["date"]).copy()

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["month_name"] = df["date"].dt.month_name()

# Select useful columns for this portfolio project
selected_columns = {
    "RSI:Value Seasonally Adjusted:All Retailers ex fuel:All Business Index": "all_retail_ex_fuel_value_index",
    "RSI:Volume Seasonally Adjusted:All Retailers ex fuel:All Business Index": "all_retail_ex_fuel_volume_index",
    "RSI:Value Seasonally Adjusted:All Retailers inc fuel:All Business Index": "all_retail_inc_fuel_value_index",
    "RSI:Volume Seasonally Adjusted:All Retailers inc fuel:All Business Index": "all_retail_inc_fuel_volume_index",
    "RSI:Predominantly food stores (val sa):All Business Index": "food_stores_value_index",
    "RSI:Predominantly food stores (vol sa):All Business Index": "food_stores_volume_index",
    "RSI:Predominantly non-food stores (valsa):All Business Index": "non_food_stores_value_index",
    "RSI:Predominantly non-food stores (vol sa):All Business Index": "non_food_stores_volume_index",
    "RSI:Textiles, clothing & footwear (val sa):All Business Index": "clothing_footwear_value_index",
    "RSI:textiles:clothing:footwear (vol sa):All Business Index": "clothing_footwear_volume_index",
    "RSI:Household goods stores (val sa):All Business Index": "household_goods_value_index",
    "RSI:Household goods stores (vol sa):All Business Index": "household_goods_volume_index",
    "RSI:Value Seasonally Adjusted:Non-store Retailing:All Business Index": "non_store_retail_value_index",
    "RSI:Volume Seasonally Adjusted:Non-store Retailing:All Business Index": "non_store_retail_volume_index",
    "Internet sales as a percentage of total retail sales (ratio) (%)": "internet_sales_pct",
    "Internet retail sales, £ millions. All retailing": "internet_sales_million_gbp",
    "Average weekly value for all retailing (£ million)": "average_weekly_sales_million_gbp"
}

available_columns = {
    original: clean
    for original, clean in selected_columns.items()
    if original in df.columns
}

missing_columns = [
    original
    for original in selected_columns
    if original not in df.columns
]

if missing_columns:
    print("Warning: Some expected columns were not found:")
    for col in missing_columns:
        print(f"- {col}")

keep_cols = ["period", "date", "year", "month", "month_name"] + list(available_columns.keys())
cleaned = df[keep_cols].rename(columns=available_columns).copy()

# Convert selected values to numeric
value_cols = [col for col in cleaned.columns if col not in ["period", "date", "year", "month", "month_name"]]

for col in value_cols:
    cleaned[col] = pd.to_numeric(cleaned[col], errors="coerce")

# Filter to post-2015 for a cleaner dashboard
cleaned = cleaned[cleaned["year"] >= 2015].copy()

# Create long-format table for sector comparison
sector_columns = {
    "food_stores_value_index": "Food Stores",
    "non_food_stores_value_index": "Non-Food Stores",
    "clothing_footwear_value_index": "Clothing & Footwear",
    "household_goods_value_index": "Household Goods",
    "non_store_retail_value_index": "Non-Store Retailing"
}

available_sector_columns = {
    col: sector
    for col, sector in sector_columns.items()
    if col in cleaned.columns
}

long_df = cleaned.melt(
    id_vars=["period", "date", "year", "month", "month_name"],
    value_vars=list(available_sector_columns.keys()),
    var_name="metric",
    value_name="sales_index"
)

long_df["sector"] = long_df["metric"].map(available_sector_columns)

# Calculate YoY growth by sector
long_df = long_df.sort_values(["sector", "date"])
long_df["yoy_growth_pct"] = long_df.groupby("sector")["sales_index"].pct_change(periods=12) * 100
long_df["yoy_growth_pct"] = long_df["yoy_growth_pct"].round(2)

# Pandemic comparison flag
long_df["period_group"] = long_df["year"].apply(
    lambda y: "Pre-pandemic" if y < 2020 else ("Pandemic period" if y in [2020, 2021] else "Post-pandemic")
)

# Save outputs
cleaned.to_csv(OUTPUT_WIDE, index=False)
long_df.to_csv(OUTPUT_LONG, index=False)

print("Cleaning complete.")
print(f"Wide rows: {cleaned.shape[0]}")
print(f"Wide columns: {cleaned.shape[1]}")
print(f"Long rows: {long_df.shape[0]}")
print(f"Long columns: {long_df.shape[1]}")
print(f"Saved wide file to: {OUTPUT_WIDE}")
print(f"Saved long file to: {OUTPUT_LONG}")

print("\nWide preview:")
print(cleaned.head())

print("\nLong preview:")
print(long_df.head(10))