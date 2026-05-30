# Great Britain Retail Sales Trend Analysis

## Project Overview

This project analyses Great Britain retail sales trends using the official Office for National Statistics (ONS) Retail Sales Index dataset.

The aim of the project is to understand how retail sales, online sales, and sector performance changed before, during, and after the pandemic period.

The project uses Python for data inspection and cleaning, SQL for business analysis, and Power BI for dashboard reporting.

## Business Questions

This project answers the following business questions:

1. How has online retail sales share changed over time?
2. Which retail sectors performed strongest after the pandemic?
3. How did sector performance differ before, during, and after the pandemic?
4. Which sectors experienced the sharpest disruption and recovery?
5. What are the latest retail sales indicators for Great Britain?

## Dataset

The dataset used in this project is the official ONS Retail Sales Index time series dataset.

The raw dataset included retail sales value indexes, volume indexes, online sales percentage, average weekly retail sales, and sector-level retail indicators.

The original raw file contained:

- 657 rows
- 622 columns
- Metadata rows
- Monthly retail sales records
- Multiple retail sector indicators

For this project, selected indicators were cleaned and transformed into dashboard-ready datasets.

## Tools Used

- Python
- Pandas
- SQLite
- SQL
- Power BI
- GitHub

## Project Structure

```text
uk-retail-sales-trend-analysis/
├── dashboard/
│   └── retail_sales_dashboard.pbix
├── data/
│   ├── raw/
│   │   └── drsi.csv
│   └── cleaned/
│       ├── cleaned_retail_sales_wide.csv
│       ├── cleaned_retail_sales_long.csv
│       └── retail_sales.db
├── notebooks/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   └── 03_sql_analysis.py
├── reports/
│   └── sql_analysis_results.md
├── screenshots/
│   └── dashboard_overview.png
├── sql/
│   └── business_questions.sql
└── README.md
```

## Data Cleaning Process

The raw ONS dataset was wide and contained many indicators, so a focused cleaning process was required before analysis.

The cleaning process included:

- Inspecting the raw dataset structure
- Removing metadata rows such as CDID, Unit, Release Date, and Next Release
- Filtering the dataset to monthly time periods
- Converting period values into date format
- Selecting relevant retail sales indicators
- Creating a wide dataset for KPI and trend analysis
- Creating a long dataset for sector comparison
- Calculating year-on-year growth by retail sector
- Grouping records into pre-pandemic, pandemic, and post-pandemic periods

## Cleaned Datasets

Two cleaned datasets were created:

### 1. Wide Dataset

File:

```text
data/cleaned/cleaned_retail_sales_wide.csv
```

Purpose:

- KPI analysis
- Online sales trend analysis
- Latest retail indicator reporting
- Power BI cards and time-series charts

### 2. Long Dataset

File:

```text
data/cleaned/cleaned_retail_sales_long.csv
```

Purpose:

- Sector comparison
- Pre-pandemic, pandemic, and post-pandemic analysis
- Year-on-year growth analysis
- Power BI sector charts

## SQL Analysis

SQL was used to answer business questions and create an analysis report.

The SQL analysis includes:

- Latest retail sales indicators
- Average sales index by sector and period group
- Top sector-months by year-on-year growth
- Post-pandemic recovery ranking by sector
- Online sales trend by year

SQL outputs were saved in:

```text
reports/sql_analysis_results.md
sql/business_questions.sql
data/cleaned/retail_sales.db
```

## Key Insights

- Online retail sales share increased from 12.48% in 2015 to 27.83% in 2026.
- Non-store retailing showed the strongest post-pandemic recovery, with 74.79% growth compared with the pre-pandemic average.
- Clothing and footwear experienced the sharpest pandemic disruption, followed by strong recovery later.
- Online sales peaked during the pandemic period and remained much higher than pre-pandemic levels.
- Retail sector performance shows clear structural change after 2020.

## Power BI Dashboard

![Dashboard Overview](screenshots/dashboard_overview.png)

The Power BI dashboard includes:

- Online sales share over time
- Sales index by retail sector
- Average sector performance before, during, and after the pandemic
- Latest internet sales share KPI
- Latest average weekly retail sales KPI
- Key business insights

## Skills Demonstrated

- Public dataset analysis
- Data inspection with Python
- Data cleaning with Pandas
- Time-series data preparation
- SQL business analysis
- SQLite database creation
- Power BI dashboard design
- KPI reporting
- Retail and e-commerce analytics
- GitHub project documentation

## Portfolio Value

This project is relevant for entry-level data analyst roles because it demonstrates the full analytics workflow:

1. Finding and using an official public dataset
2. Inspecting and cleaning raw data
3. Transforming data for analysis
4. Writing SQL queries to answer business questions
5. Building a Power BI dashboard
6. Communicating insights clearly through GitHub documentation

## Conclusion

This project demonstrates how official public retail data can be transformed into clear business insights.

It highlights the growth of online retail, sector-level recovery trends, and post-pandemic changes in Great Britain retail sales.
