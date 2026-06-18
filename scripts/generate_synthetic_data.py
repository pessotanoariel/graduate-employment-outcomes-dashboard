"""Scaffold for the synthetic data generation pipeline.

The future implementation must generate these datasets in ``data/synthetic``:

* ``graduates_synthetic.csv``: synthetic graduate reference population.
* ``survey_synthetic.csv``: synthetic survey responses linked to graduates by
  ``graduate_id``.

The schemas and allowed categorical values must come exclusively from:

* ``data/graduates_schema.md``
* ``data/survey_schema.md``
* ``data/data_dictionary.md``

No source records or transformations of confidential records should be used.
The implementation will preserve the documented conceptual structure (column
names, data types, categorical domains, and table relationship) while creating
new, artificial records. Volumes, distributions, dependencies between fields,
and missing-value rules must not be implemented until they are explicitly
documented and approved.

This module intentionally does not create any dataset yet.
"""

from pathlib import Path
from typing import Final


PROJECT_ROOT: Final = Path(__file__).resolve().parents[1]
SYNTHETIC_DATA_DIR: Final = PROJECT_ROOT / "data" / "synthetic"

GRADUATES_OUTPUT: Final = SYNTHETIC_DATA_DIR / "graduates_synthetic.csv"
SURVEY_OUTPUT: Final = SYNTHETIC_DATA_DIR / "survey_synthetic.csv"

# Column order follows graduates_schema.md. These constants define structure
# only; they do not encode record counts, distributions, or new business rules.
GRADUATES_COLUMNS: Final = (
    "graduate_id",
    "gender",
    "jurisdiction",
    "course",
    "course_type",
    "cohort",
)

# Column order follows survey_schema.md. A future implementation must select
# graduate_id values from the synthetic graduates dataset to preserve the
# documented relationship without copying identifiers from real data.
SURVEY_COLUMNS: Final = (
    "respondent_id",
    "graduate_id",
    "age_group",
    "highest_education_level",
    "programming_level_before",
    "programming_level_after",
    "employment_before",
    "employment_after",
    "employment_type_before",
    "employment_type_after",
    "it_before",
    "it_after",
    "programmer_after",
    "continued_studying",
    "post_training_study_type",
    "course",
    "cohort",
    "improved_job_profile",
    "interested_job_opportunities",
)


def main() -> None:
    """Leave an explicit boundary until generation rules are approved."""
    raise NotImplementedError(
        "Synthetic data generation is scaffolded but not implemented."
    )


if __name__ == "__main__":
    main()
