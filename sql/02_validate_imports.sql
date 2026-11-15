USE uk_automotive;
GO

SELECT
    COUNT(*) AS quarter_count,
    MIN(quarter_start) AS first_quarter_start,
    MAX(quarter_start) AS last_quarter_start
FROM dbo.dim_quarter;