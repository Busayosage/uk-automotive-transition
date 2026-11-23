# Stage 2 technical summary

Checkpoint: 23 November 2026.

Stage 2 extends the working UK automotive registrations report with an executive landing page, consistent page design and interactive explanations. The analytical scope remains quarterly UK car first registrations and five selected comparison brands.

## Report pages

| Page | Purpose and content |
|---|---|
| Executive Overview | National and BYD KPI rows; UK BEV-share history; selected-brand BEV comparison; BYD fuel mix; dynamic executive takeaway |
| UK Market Overview | National totals, BEV registrations and share; full-history BEV trend; prior-year comparison; selected-brand all-fuel comparison |
| BYD Performance | BYD all-fuel registrations, national market share and YoY growth; history; fuel mix and prior-year fuel comparison; selected-brand BEV comparison |
| Validation | Benchmark and model-integrity results, definitions and quarter coverage |

The Executive Overview is the default landing page. Quarter selection is synchronised across pages and updates KPIs, comparison charts and insight text. Trend charts deliberately retain the full 2019 Q1–2026 Q2 history. Navigation links connect the pages; tooltips provide metric context. Reset restores the saved default quarter, 2026 Q2. It should not be described as automatically selecting a new latest quarter after future data refreshes without further testing.

## Measures and interpretation

- UK BEV share divides national battery-electric registrations by national all-fuel car registrations.
- BYD market share divides BYD all-fuel registrations by national all-fuel car registrations.
- A brand's BEV market share divides its BEV registrations by all UK BEV registrations, not the sum of the five selected brands.
- BYD fuel-mix percentages divide each fuel category by BYD's own all-fuel total.
- Year-on-year comparisons use the same quarter in the prior year. Percentage-point changes are distinct from percentage growth.
- DAX-generated insight text responds to quarter selection and handles missing prior-year comparisons and zero-registration cases.
- Peer charts compare BYD, Tesla, MG, Kia and Hyundai. They are not a complete market ranking or proof of direct customer substitution.

For 2026 Q2, the report displays UK first registrations of **538,867**, including **147,185 BEVs (27.31%)**. BYD has **16,434** all-fuel registrations, **3.05%** of the UK total and **62.42%** growth from 10,118 in 2025 Q2. BYD BEVs are **8,256**, or **50.24%** of BYD's own total. The remaining recorded categories are petrol plug-in hybrid (7,924) and petrol hybrid (254).

## Development validation

The development validation record reports the following passing results:

| Check group | Scope | Reported result |
|---|---|---:|
| Report benchmarks | Benchmark checks on the Validation page | 34 of 34 |
| Model checks | Model-integrity checks on the Validation page | 9 of 9 |
| Quarter-level recalculation | 39 checks across 30 quarters, including values, labels and insight text | 1,170 |
| Brand-level recalculation | 11 checks across five selected brands and 30 quarters | 1,650 |
| Coverage | Coverage checks | 2 |
| Separate recalculation total | Quarter-level, brand-level and coverage checks combined | 2,822 |

The 2,822 total is a count of validation checks, not 2,822 distinct numeric figures, and does not include the 34 and 9 report-page checks as extra components. Comparisons used the prepared data files, not freshly downloaded government source data.

The development record also reports 18 interaction checks covering quarter synchronisation, navigation, reset, tooltips, chart interactions and full-history trends, followed by save-and-reopen verification. Text corrections addressed changes rounding to zero, very small shares and wording for rising or falling registrations.

The Stage 2 model definitions, export queries, comparison code and check-by-check results are not included in this repository at this checkpoint. These validation counts document the development results; they have not been rerun from a clean repository checkout. No reconstructed DAX or generated substitute test log is supplied as an original export.

## Release status

The working Stage 2 layout is visible in the report screenshots and prepared demonstration videos. Final demonstration review remains open. The repository continues to provide the original Stage 1 PBIX; it does not yet distribute a Stage 2 PBIX or PBIP project, and it is not a hosted interactive report.

The original Python preparation code, SQL checks, Stage 1 report and AS-IS process map remain the preserved baseline. The original process map describes the earlier spreadsheet workflow.

## Stage 3 work remaining

- Deeper BYD, JLR and Aston Martin research, using comparable periods, currencies, business scopes and vehicle segments.
- Model-level, regional electrification and charging analysis using appropriate datasets and definitions.
- Economic contribution and employment analysis supported by additional evidence.
- Acquisition and reconciliation of monthly SMMT data as a separate series where available.
- Azure SQL deployment and an automated loading and refresh pipeline.
- Documentation of the implemented end-to-end workflow as it develops.

Azure Blob storage currently holds manually uploaded files. The working reporting architecture uses local SQL Server and Power BI Import mode. Azure SQL deployment, automated refresh and a hosted report remain unfinished.

## Data limitations

Source: DfT/DVLA first-registration series, VEH0160; reporting coverage 2019 Q1–2026 Q2. First registrations are not identical to SMMT new-car sales and may include used imports. These results describe registration patterns; they do not establish causal effects, profitability, consumer motivations or UK economic impact.
