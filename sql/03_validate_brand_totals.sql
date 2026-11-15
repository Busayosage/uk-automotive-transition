USE uk_automotive;
GO

SELECT COUNT(*) AS row_count
FROM dbo.brand_fuel_quarterly;

WITH brand_totals AS (
    SELECT quarter, SUM(registrations) AS total_registrations
    FROM dbo.brand_fuel_quarterly
    GROUP BY quarter
)
SELECT
    COALESCE(b.quarter, u.quarter) AS quarter,
    b.total_registrations AS brand_total,
    u.total_registrations AS uk_total
FROM brand_totals AS b
FULL OUTER JOIN dbo.uk_quarterly AS u
    ON b.quarter = u.quarter
WHERE b.quarter IS NULL
   OR u.quarter IS NULL
   OR b.total_registrations <> u.total_registrations;