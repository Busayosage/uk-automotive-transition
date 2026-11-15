from pathlib import Path
import pandas as pd

project_folder = Path(__file__).resolve().parent
csv_path = (
    project_folder
    / "processed"
    / "first_registrations_all_brands_quarterly.csv"
)

df = pd.read_csv(csv_path)

print(f"Rows: {len(df):,}")
print(f"Columns: {df.columns.tolist()}")
print("\nFirst five rows:")
print(df.head().to_string(index=False))
print("\nColumn data types:")
print(df.dtypes)
print("\nDATA QUALITY CHECKS")

labels = ["Make", "Fuel", "quarter"]
counts = pd.to_numeric(df["first_registrations"], errors="coerce")

missing_labels = (
    df[labels].isna()
    | df[labels].apply(lambda column: column.str.strip().eq(""))
).sum().sum()

checks = {
    "Missing or blank labels": int(missing_labels),
    "Missing or non-numeric counts": int(counts.isna().sum()),
    "Negative counts": int((counts < 0).sum()),
    "Fractional counts": int((counts.dropna() % 1 != 0).sum()),
    "Duplicate make/fuel/quarter keys": int(
        df.duplicated(subset=labels).sum()
    ),
}

for name, issues in checks.items():
    status = "PASS" if issues == 0 else "CHECK"
    print(f"{name}: {issues} — {status}")

quarters = sorted(df["quarter"].dropna().unique())
print(f"\nDistinct quarters: {len(quarters)}")
print(f"Coverage: {quarters[0]} to {quarters[-1]}")

if any(checks.values()):
    raise ValueError("Resolve the data quality issues before continuing.")
# Sum registrations across all makes and fuels.
uk_market = df.groupby("quarter")["first_registrations"].sum()

# Sum battery-electric registrations across all makes.
uk_bev = (
    df.loc[df["Fuel"].eq("Battery electric")]
    .groupby("quarter")["first_registrations"]
    .sum()
)

# Combine the totals into one reporting table.
uk_quarterly = pd.DataFrame({
    "total_registrations": uk_market,
    "bev_registrations": uk_bev,
})

uk_quarterly["bev_share"] = (
    uk_quarterly["bev_registrations"]
    / uk_quarterly["total_registrations"]
)

print("\nUK QUARTERLY COMPARISON")
print(
    uk_quarterly.loc[["2025 Q2", "2026 Q2"]]
    .to_string(formatters={"bev_share": "{:.2%}".format})
)
# Compare Python totals with our checked spreadsheet figures.
expected_counts = {
    "2025 Q2": (472763, 104770),
    "2026 Q2": (538867, 147185),
}

for quarter, expected in expected_counts.items():
    actual = (
        int(uk_quarterly.loc[quarter, "total_registrations"]),
        int(uk_quarterly.loc[quarter, "bev_registrations"]),
    )

    if actual != expected:
        raise ValueError(
            f"{quarter}: expected {expected}, got {actual}"
        )

print("\nSpreadsheet reconciliation: PASS")

# Save all 30 quarters in a separate output folder.
output_folder = project_folder / "outputs"
output_folder.mkdir(exist_ok=True)

output_path = output_folder / "uk_quarterly.csv"
uk_quarterly.reset_index().to_csv(output_path, index=False)

print(f"Reporting table saved to: {output_path}")
# Prepare registrations by quarter, brand and fuel.
brand_fuel_quarterly = (
    df.groupby(["quarter", "Make", "Fuel"], as_index=False)
    ["first_registrations"]
    .sum()
    .rename(columns={
        "Make": "make",
        "Fuel": "fuel",
        "first_registrations": "registrations",
    })
)

# Display BYD's fuel mix for the two comparison quarters.
byd_comparison = brand_fuel_quarterly.loc[
    brand_fuel_quarterly["make"].eq("BYD")
    & brand_fuel_quarterly["quarter"].isin(["2025 Q2", "2026 Q2"])
]

print("\nBYD FUEL COMPARISON")
print(byd_comparison.to_string(index=False))

# Save the full table, retaining every brand.
brand_output = output_folder / "brand_fuel_quarterly.csv"
brand_fuel_quarterly.to_csv(brand_output, index=False)

print(f"\nBrand and fuel table saved to: {brand_output}")
# Create one date record for each quarter.
dim_quarter = pd.DataFrame({
    "quarter": sorted(df["quarter"].unique())
})

dim_quarter["year"] = dim_quarter["quarter"].str[:4].astype(int)
dim_quarter["quarter_number"] = (
    dim_quarter["quarter"].str[-1].astype(int)
)

dim_quarter["quarter_start"] = pd.to_datetime({
    "year": dim_quarter["year"],
    "month": (dim_quarter["quarter_number"] - 1) * 3 + 1,
    "day": 1,
})

dim_quarter["quarter_sort"] = (
    dim_quarter["year"] * 10 + dim_quarter["quarter_number"]
)

quarter_output = output_folder / "dim_quarter.csv"
dim_quarter.to_csv(quarter_output, index=False)

print("\nQUARTER TABLE — LAST FIVE ROWS")
print(dim_quarter.tail().to_string(index=False))
print(f"\nQuarter table saved to: {quarter_output}")
# Reconcile the detailed reporting table to national totals.
prepared_totals = (
    brand_fuel_quarterly.groupby("quarter")["registrations"]
    .sum()
    .reindex(uk_quarterly.index)
)

differences = prepared_totals - uk_quarterly["total_registrations"]

if differences.isna().any() or differences.ne(0).any():
    raise ValueError(
        "Brand table does not reconcile to UK quarterly totals."
    )

if not dim_quarter["quarter"].is_unique:
    raise ValueError("Quarter table contains duplicate quarters.")

if set(dim_quarter["quarter"]) != set(uk_quarterly.index):
    raise ValueError("Quarter table does not match reporting coverage.")

print("\nReporting table checks: PASS")
print(f"UK quarterly rows: {len(uk_quarterly):,}")
print(f"Brand/fuel rows: {len(brand_fuel_quarterly):,}")
print(f"Quarter rows: {len(dim_quarter):,}")