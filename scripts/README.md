# Synthetic data generation

`generate_synthetic_data.py` creates fully artificial data for demonstrating
the Power BI dashboard. It does not read confidential source records or copy
distributions from the original datasets.

The column contracts and categorical domains come from:

- `data/graduates_schema.md`
- `data/survey_schema.md`
- `data/data_dictionary.md`

All generation probabilities are fictional, explicit, and intentionally
simple. Therefore, generated metrics do not represent actual employment,
education, program performance, or survey results.

## Run

From the repository root, generate the default datasets with:

```powershell
python scripts/generate_synthetic_data.py
```

Defaults:

- 3,000 graduates
- 900 survey responses
- random seed `42`

Optional parameters:

```powershell
python scripts/generate_synthetic_data.py `
  --graduates-count 3000 `
  --survey-count 900 `
  --seed 42
```

| Parameter | Description | Default |
| --- | --- | ---: |
| `--graduates-count` | Number of synthetic graduates | `3000` |
| `--survey-count` | Number of unique synthetic responses | `900` |
| `--seed` | Seed used for reproducible generation | `42` |

Both counts must be greater than zero, and the survey count cannot exceed the
graduate count. Running the same parameters and seed produces the same content.

## Outputs

The script overwrites these generated files on each successful run:

- `data/synthetic/graduates_synthetic.csv`
- `data/synthetic/survey_synthetic.csv`

Before writing, it validates expected row counts, identifier uniqueness,
referential integrity, documented categorical domains, 4.0-only survey scope,
course and cohort consistency, IT/programmer employment rules, and continuing
education fields. A validation failure stops execution with an error.
