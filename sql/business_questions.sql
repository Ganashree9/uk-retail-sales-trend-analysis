-- Latest Retail Sales Indicators
SELECT
            period,
            all_retail_ex_fuel_value_index,
            all_retail_ex_fuel_volume_index,
            internet_sales_pct,
            internet_sales_million_gbp,
            average_weekly_sales_million_gbp
        FROM retail_sales_wide
        ORDER BY date DESC
        LIMIT 12;

-- Average Sales Index by Sector and Period Group
SELECT
            sector,
            period_group,
            ROUND(AVG(sales_index), 2) AS avg_sales_index,
            ROUND(AVG(yoy_growth_pct), 2) AS avg_yoy_growth_pct
        FROM retail_sales_long
        WHERE sales_index IS NOT NULL
        GROUP BY sector, period_group
        ORDER BY sector, period_group;

-- Top 10 Sector-Months by YoY Growth
SELECT
            period,
            sector,
            ROUND(sales_index, 2) AS sales_index,
            ROUND(yoy_growth_pct, 2) AS yoy_growth_pct
        FROM retail_sales_long
        WHERE yoy_growth_pct IS NOT NULL
        ORDER BY yoy_growth_pct DESC
        LIMIT 10;

-- Recovery Ranking by Sector
WITH sector_periods AS (
            SELECT
                sector,
                AVG(CASE WHEN period_group = 'Pre-pandemic' THEN sales_index END) AS pre_pandemic_avg,
                AVG(CASE WHEN period_group = 'Post-pandemic' THEN sales_index END) AS post_pandemic_avg
            FROM retail_sales_long
            GROUP BY sector
        )
        SELECT
            sector,
            ROUND(pre_pandemic_avg, 2) AS pre_pandemic_avg,
            ROUND(post_pandemic_avg, 2) AS post_pandemic_avg,
            ROUND(((post_pandemic_avg - pre_pandemic_avg) / pre_pandemic_avg) * 100, 2) AS recovery_growth_pct,
            DENSE_RANK() OVER (
                ORDER BY ((post_pandemic_avg - pre_pandemic_avg) / pre_pandemic_avg) DESC
            ) AS recovery_rank
        FROM sector_periods
        WHERE pre_pandemic_avg IS NOT NULL
          AND post_pandemic_avg IS NOT NULL
        ORDER BY recovery_rank;

-- Online Sales Trend by Year
SELECT
            year,
            ROUND(AVG(internet_sales_pct), 2) AS avg_internet_sales_pct,
            ROUND(AVG(internet_sales_million_gbp), 2) AS avg_internet_sales_million_gbp,
            ROUND(AVG(average_weekly_sales_million_gbp), 2) AS avg_weekly_sales_million_gbp
        FROM retail_sales_wide
        GROUP BY year
        ORDER BY year;

