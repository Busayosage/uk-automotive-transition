# Stage 1 validation
Validation checkpoint: 15 November 2026.

## Report model
The report has three pages: Validation, UK Market Overview and BYD Performance.

| Reporting table | Rows | Grain |
|---|---:|---|
| brand_fuel_quarterly | 24,780 | Make, fuel and quarter |
| uk_quarterly | 30 | National quarter |
| dim_quarter | 30 | Quarter |

Both reporting facts have active, single-direction many-to-one relationships to dim_quarter on quarter. Automatically generated date tables are also present.

The model contains six measures: UK Total Registrations, UK BEV Registrations, UK BEV Share, BYD Total Registrations, BYD UK Market Share and BYD Registrations YoY.

## Reconciliation
The embedded model was inspected using PBIXRay. After sorting and normalising dates:
- All detailed registration records match the reporting CSV.
- All national registration counts match the reporting CSV.
- The quarter dimension matches the reporting CSV.
- The stored bev_share column differs by at most 6.9068636920910365e-09. This does not change shares displayed to two decimal places. The UK BEV Share measure calculates directly from registration totals.

These checks establish consistency between the reporting files and embedded model. They do not independently authenticate the original extraction. The model inspection did not execute a live SQL refresh or render the report in Power BI Desktop.

## Report behaviour
The quarter dropdown filters cards and breakdown charts. Both analytical pages explicitly retain full-history trend charts through the NoFilter slicer interaction.

The Power Query expressions use local SQL Server, database uk_automotive. Refresh requires the corresponding local database and tables, or an updated connection.

## Process baseline
The AS-IS map documents the earlier Google Sheets workflow: data-quality checks, quarterly pivots, share and growth calculations, findings and report-review correction loops. The later Python, SQL and Power BI implementation is described in the README.

## Baseline integrity
| File | SHA-256 |
|---|---|
| process/UK_Automotive_Reporting_AS_IS.drawio | 23af84de53fabb5a6801d2b8e46d7da133543896e81483577c17187c738e87f0 |
| powerbi/UK_Automotive_Transition_Stage1.pbix | a0d962eb09f973cd2428ba0fea1b70ffa5ed9b436a748eb77228595ea7eef3ab |

The report and process map are preserved unchanged.

## Remaining validation and delivery
Further interaction testing, professional dashboard redesign, hosted publication, automated refresh and Azure SQL deployment remain future work. Registration findings are descriptive and do not establish consumer motivations or causal effects.
