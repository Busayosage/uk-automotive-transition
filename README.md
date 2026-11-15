# UK Automotive Transition
## UK electrification and BYD market analysis

**Author: Seun Oseola**  
**Current milestone: Stage 1 — working analytical report and documentation**  
**Reporting coverage: 2019 Q1–2026 Q2**

### Business question

How is the UK car market shifting towards battery-electric vehicles, and how is BYD's registration presence changing?

This project combines spreadsheet exploration, Python preparation, Azure Blob Storage, local SQL Server validation and Power BI reporting. The intended cloud path also includes Azure SQL and automated refresh; those components remain in development. The first reporting milestone focuses on national BEV adoption, selected-brand registration comparisons and BYD's growth and fuel mix. Broader questions about JLR, Aston Martin, model-level comparisons and economic contribution remain outside the current dashboard's completed analysis.

### Work completed

| Area | Work carried out | Status |
|---|---|---|
| Initial exploration | Imported the make/fuel/quarter extract into Google Sheets; checked record counts, labels, numeric values, negatives, duplicates and quarter coverage; built national and brand pivots | Completed during development |
| Python | Prepared national totals, BEV share, a detailed brand/fuel table and a quarter dimension; reconciled reporting totals | Original script included |
| SQL Server | Created the local database, manually imported the three CSVs using SSMS and checked totals, duplicate keys and quarter references | Original scripts included |
| Power BI | Built the shared-quarter model, UK overview and BYD performance pages; tested quarter selection against comparison figures | Original Stage 1 PBIX included |
| Process mapping | Mapped the spreadsheet reporting workflow, including validation and review loops | Original editable map included unchanged |
| Azure Blob | Created private source/reporting containers and manually uploaded the input CSV and three reporting CSVs | Completed as a storage step |
| Azure SQL and automated refresh | Cloud database deployment encountered subscription/region restrictions; reporting continued using local SQL Server | Unfinished |
| Publication | Preserved a local Stage 1 PBIX and versioned the original scripts, map, report and project explanation | In progress |

### Azure cloud storage and delivery architecture

Azure Blob Storage is a completed part of Stage 1: two private containers hold the prepared input CSV and three reporting outputs, uploaded manually on 11 November 2026.

| Area | Completed work | Current boundary |
|---|---|---|
| Cloud storage | Private source and reporting containers; four uploaded CSVs | Manual storage step |
| Database and report | Local SQL Server validation and Power BI Import model | Local database connection |
| Azure SQL and refresh | Deployment attempts and resource-provider troubleshooting | Subscription/region blocker; not deployed or automated |

The original development screenshots record the container access settings and uploaded files. The [Azure implementation record](docs/azure-implementation.md) lists the evidence, file inventory, deployment blocker and remaining work. Screenshots are retained privately and are not yet included in this public repository.

The working report uses local SQL Server. Blob storage is a parallel cloud copy at this milestone; an automated Blob-to-Azure-SQL-to-Power-BI pipeline remains to be implemented.

### Findings: 2026 Q2 compared with 2025 Q2

The following values reconcile with the reporting CSVs and Power BI report.

| Metric | 2025 Q2 | 2026 Q2 | Change |
|---|---:|---:|---:|
| UK first registrations, all fuels | 472,763 | 538,867 | +13.98% |
| UK battery-electric registrations | 104,770 | 147,185 | +40.48% |
| UK BEV share | 22.16% | 27.31% | +5.15 percentage points |
| BYD first registrations, all fuels | 10,118 | 16,434 | +62.42% |
| BYD share of UK registrations, all fuels | 2.14% | 3.05% | +0.91 percentage points |

Battery-electric registrations grew faster than the overall registration total in this comparison. BYD also increased its share of UK registrations. These observations describe changes in registrations; they do not establish the causes of those changes or which competitors lost customers to BYD.

BYD's fuel breakdown adds context:

| Fuel category in the extract | 2025 Q2 | 2026 Q2 |
|---|---:|---:|
| Battery electric | 5,397 | 8,256 |
| Plug-in hybrid electric (petrol) | 4,721 | 7,924 |
| Hybrid electric (petrol) | 0 | 254 |
| **Total** | **10,118** | **16,434** |

BYD's total growth includes multiple fuel types. Its all-fuel registrations must not be presented as entirely battery electric.

The overview compares five selected brands. For 2026 Q2, all-fuel totals are Kia 28,164; MG 24,733; Hyundai 21,212; BYD 16,434; and Tesla 15,982. This is a selected-brand comparison, not a ranking of the entire UK market or a matched BEV-only comparison.

### Data and provenance

The current report uses the DfT/DVLA vehicle first-registration extract recorded in the original data pack, particularly `df_VEH0160_UK.csv`.

Source collection: [DfT vehicle licensing statistics data files](https://www.gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files).

The source manifest records retrieval on 29 October 2026. The current dashboard does not use a monthly SMMT sales series.

The preparation input has **24,780 rows**, at one **make × fuel × quarter** per row, over **30 quarters**. Its columns are `Make`, `Fuel`, `quarter` and `first_registrations`.

The original data-pack inventory also lists separate model, vehicle-stock, regional, charging and manufacturer-financial extracts. Those are not integrated into the three-table Power BI model described here. The original October README describes that broader pack and is not a current completion report for the dashboard.

### Preparation and validation

The original `prepare_registrations.py`:

1. Reads the prepared make/fuel/quarter input relative to the script's directory.
2. Checks missing/blank labels, missing/non-numeric counts, negatives, fractional counts and duplicate keys; stops when these checks find issues.
3. Aggregates all-make/all-fuel national totals and battery-electric totals, then calculates BEV share.
4. Checks 2025 Q2 and 2026 Q2 against the spreadsheet benchmarks.
5. Creates three reporting CSVs and reconciles detailed registrations with national totals.
6. Checks dimension-quarter uniqueness and matching reporting coverage.

| Reporting table | Rows | Grain |
|---|---:|---|
| `uk_quarterly.csv` | 30 | National quarter |
| `brand_fuel_quarterly.csv` | 24,780 | Make/fuel/quarter |
| `dim_quarter.csv` | 30 | Quarter |

The reporting CSVs contain no missing detailed fields, duplicate make/fuel/quarter keys or differences between detailed and national quarterly totals. These are internal consistency checks, not independent verification of the original extraction.

In SSMS, duplicate-key, missing-quarter and national-total mismatch queries returned no exception rows in the validation results. The checks were executed in the local SQL Server environment.

### Repository files

| File | Purpose |
|---|---|
| [prepare_registrations.py](prepare_registrations.py) | Original preparation and reconciliation code |
| [01_create_database.sql](sql/01_create_database.sql) | Creates the database if absent and selects it |
| [02_validate_imports.sql](sql/02_validate_imports.sql) | Checks quarter count and minimum/maximum quarter-start dates |
| [03_validate_brand_totals.sql](sql/03_validate_brand_totals.sql) | Counts detailed rows and returns detailed-versus-national mismatches |
| [04_validate_keys.sql](sql/04_validate_keys.sql) | Returns duplicate detailed keys and fact quarters missing from the dimension |
| [.gitignore](.gitignore) | Exclusions for credentials, environments, local data and report binaries |
| [README.md](README.md) | Project objectives, findings and setup |
| [Original AS-IS map](process/UK_Automotive_Reporting_AS_IS.drawio) | Original Google Sheets process map, preserved unchanged |
| [Stage 1 Power BI report](powerbi/UK_Automotive_Transition_Stage1.pbix) | Stage 1 report with imported aggregate data |
| [Stage 1 validation](docs/stage1-review.md) | Model checks, reconciliation and limitations |
| [Azure implementation](docs/azure-implementation.md) | Cloud storage work, upload inventory, deployment blocker and remaining architecture |

Script 01 creates the database only. Table creation/import was performed manually in SSMS; the repository does not yet supply a complete table-DDL/load pipeline.

### Running the preparation script

Development used Python 3.13 and pandas. Install pandas in your own virtual environment.

Place the existing intermediate file at:

`processed/first_registrations_all_brands_quarterly.csv`

Keep `prepare_registrations.py` at the repository root, then run:

```bash
python prepare_registrations.py
```

The script writes the three CSVs into `outputs/`. It expects the two benchmark quarters listed above. The intermediate input and the original extraction pack are not bundled here, so a clean clone alone is not sufficient to reproduce the complete raw-source-to-report process.

To reproduce the SQL checks, create/select `uk_automotive`, import the three reporting CSVs into their corresponding `dbo` tables with appropriate column types, then run scripts 02–04.

### Power BI model and report behaviour

The report connects to local SQL Server using Import mode. `dim_quarter[quarter]` filters both reporting facts through active, single-direction one-to-many relationships. There is no direct relationship between the two fact tables.

The quarter dimension contains `quarter`, `year`, `quarter_number`, `quarter_start` and `quarter_sort`. It is quarterly, not a daily calendar.

| Metric | Definition |
|---|---|
| UK total registrations | Sum of national total registrations |
| UK BEV registrations | Sum of national battery-electric registrations |
| UK BEV share | UK BEV registrations / UK total registrations |
| BYD total registrations | Sum of detailed registrations filtered to make BYD |
| BYD UK market share | BYD all-fuel registrations / UK all-fuel registrations |
| BYD YoY growth | (Selected quarter − same quarter one year earlier) / prior-year quarter |

The YoY measure uses an explicit prior-year quarter lookup and expects one selected quarter. Shares and YoY are formatted as percentages with two decimal places.

**UK Market Overview:** three national cards, BEV-share history and selected-brand all-fuel bars.

**BYD Performance:** total registrations, UK market share, YoY growth, registration history and fuel bars.

The quarter dropdown changes cards and breakdown bars. Full-history line charts deliberately retain all quarters. This behaviour was checked for 2025 Q2 and 2026 Q2. The report also retains a Validation page.

The original baseline is included at [powerbi/UK_Automotive_Transition_Stage1.pbix](powerbi/UK_Automotive_Transition_Stage1.pbix), together with the original editable map. The PBIX opens with imported data; refreshing requires a compatible local SQL Server database or changing the source. It is not a hosted interactive report. Dashboard screenshots are not yet included.

The Stage 1 PBIX was checked on 15 November 2026: its three report pages, six measures and two shared-quarter relationships match the documented build. Its 24,780 detailed records, national registration counts and 30-row quarter dimension match the reporting CSVs. The stored `bev_share` column differs by at most 6.91 × 10⁻⁹ from the CSV values; the displayed share measure calculates from registration counts. See the [review](docs/stage1-review.md) for the review boundary and file hashes.

### Process mapping

The original AS-IS map describes the earlier Google Sheets/pivot reporting workflow, including data-quality and report-review correction loops. It remains the baseline to review when documenting later Python, SQL and Power BI work.

The original map is published unchanged at [process/UK_Automotive_Reporting_AS_IS.drawio](process/UK_Automotive_Reporting_AS_IS.drawio). Its embedded progress note is historical. It describes the spreadsheet baseline, not the complete later Python/SQL/Power BI implementation. The preparation, SQL and Power BI sections above document the later implementation.

### Three-stage portfolio plan

1. **Stage 1 — working solution:** preserve and document the current preparation, SQL checks, report, original process map and findings; prepare a LinkedIn walkthrough.
2. **Stage 2 — dashboard design:** develop layout, navigation and chart clarity towards a consistent professional design, keeping accurate calculations and showing the before/after.
3. **Stage 3 — deeper analysis and delivery:** extend comparisons and business questions; implement and document refresh/deployment improvements as they are completed.

Professional redesign, broader analysis and automated cloud delivery are planned subsequent milestones.

### Limitations and publication controls

- First registrations are not identical to SMMT new-car sales and may include used imports.
- Registration counts support descriptive adoption analysis; they do not prove consumer motivations, profitability or economic impact.
- The current dashboard does not analyse individual vehicle models, despite separate model extracts appearing in the original pack inventory.
- Quarter comparisons and internal reconciliations do not independently authenticate every source observation.
- Private Azure Blob copies are a completed manual storage step, not an automated feed into the local SQL database.
- Raw downloads, local data folders, credentials, environments, SQL backups and other Power BI binaries are excluded by `.gitignore`. One exact exception permits the Stage 1 PBIX. It contains public aggregate reporting data and the local source name `localhost\\SQLEXPRESS` / `uk_automotive`. Project documentation and source code remain version-controlled.
- `.gitignore` does not remove files already tracked. Additional datasets or report binaries need their own review before publication.

Retain DfT/DVLA attribution. The original source publishers' rights and reuse terms apply to their material.
