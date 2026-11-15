USE uk_automotive;
GO

-- Duplicate quarter/make/fuel combinations
SELECT quarter, make, fuel, COUNT(*) AS copies
FROM dbo.brand_fuel_quarterly
GROUP BY quarter, make, fuel
HAVING COUNT(*) > 1;

-- Quarters missing from the quarter dimension
SELECT DISTINCT quarter
FROM dbo.brand_fuel_quarterly
EXCEPT
SELECT quarter FROM dbo.dim_quarter;

SELECT quarter
FROM dbo.uk_quarterly
EXCEPT
SELECT quarter FROM dbo.dim_quarter;