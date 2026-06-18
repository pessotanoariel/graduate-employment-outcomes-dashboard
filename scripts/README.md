# Synthetic data generation

This directory contains the scaffold for replacing confidential source data
with fully synthetic datasets.

## Documented inputs

The generator specification is limited to the repository documentation:

- `data/graduates_schema.md`
- `data/survey_schema.md`
- `data/data_dictionary.md`

The files under `data/raw/` are reserved for source inputs when an approved
workflow requires them. Confidential records must not be committed to the
repository or used as rows to transform into synthetic output.

## Planned flow

1. Read the documented schemas, types, categorical domains, and relationship.
2. Define generation parameters only after volumes, distributions, field
   dependencies, and missing-value rules have been documented and approved.
3. Generate artificial graduate records with new synthetic identifiers.
4. Generate artificial survey responses linked only to those synthetic
   graduate identifiers.
5. Validate column order, types, allowed values, identifier uniqueness, and
   referential integrity against the documented contracts.
6. Write `graduates_synthetic.csv` and `survey_synthetic.csv` to
   `data/synthetic/`.

The current `generate_synthetic_data.py` intentionally stops before generation.
It records output paths and column contracts without creating CSV files or
introducing undocumented business rules.

## Future execution

Once generation rules are approved, the intended entry point will be:

```powershell
python scripts/generate_synthetic_data.py
```

Run it from the repository root. Generated CSV files should remain separate
from any raw inputs.
