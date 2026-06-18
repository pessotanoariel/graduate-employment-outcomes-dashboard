"""Generate reproducible, fully synthetic graduate and survey datasets.

The categorical domains and table structure follow the repository schemas.
All probabilities below are deliberately simple, fictional assumptions. They
are not estimated from confidential data and must not be interpreted as real
program outcomes.
"""

from __future__ import annotations

import argparse
import csv
import random
from collections.abc import Sequence
from pathlib import Path
from typing import Final, TypeVar


PROJECT_ROOT: Final = Path(__file__).resolve().parents[1]
SYNTHETIC_DATA_DIR: Final = PROJECT_ROOT / "data" / "synthetic"
GRADUATES_OUTPUT: Final = SYNTHETIC_DATA_DIR / "graduates_synthetic.csv"
SURVEY_OUTPUT: Final = SYNTHETIC_DATA_DIR / "survey_synthetic.csv"

DEFAULT_GRADUATES_COUNT: Final = 3_000
DEFAULT_SURVEY_COUNT: Final = 900
DEFAULT_SEED: Final = 42

GRADUATES_COLUMNS: Final = (
    "graduate_id",
    "gender",
    "jurisdiction",
    "course",
    "course_type",
    "cohort",
)

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

GENDERS: Final = ("Female", "Male", "Other")
JURISDICTIONS: Final = ("CABA", "Buenos Aires Province", "Other Provinces")
COURSE_TYPES: Final = ("Initial Programming", "4.0", "Advanced")
COURSES: Final = (
    "Big Data",
    "UX/UI Design",
    "FullStack Java",
    "FullStack JavaScript / Node.js",
    "FullStack PHP",
    "FullStack Python",
    "Testing QA",
)
COHORTS: Final = ("2020-2", "2021-1", "2021-2", "2022-1")
AGE_GROUPS: Final = ("Under 25", "25-34", "35-44", "45+")
EDUCATION_LEVELS: Final = (
    "Secondary Incomplete",
    "Secondary Complete",
    "Tertiary Incomplete",
    "Tertiary Complete",
    "University Incomplete",
    "University Complete",
    "Postgraduate Incomplete",
    "Postgraduate Complete",
)
PROGRAMMING_LEVELS_BEFORE: Final = (
    "Senior",
    "Semi Senior",
    "Junior",
    "Trainee",
    "No Programming Knowledge",
)
PROGRAMMING_LEVELS_AFTER: Final = ("Senior", "Semi Senior", "Junior", "Trainee")
EMPLOYMENT_STATUSES: Final = (
    "Employed",
    "Unemployed and Looking for Work",
    "Unemployed and Not Looking for Work",
    "Retired",
)
EMPLOYMENT_TYPES: Final = ("Employee", "Self-employed", "Informal Worker", "Own Business")
STUDY_TYPES: Final = (
    "Free Quarterly Course",
    "Paid Quarterly Course",
    "Free Annual Course",
    "Paid Annual Course",
    "Free Tertiary Education",
    "Paid Tertiary Education",
    "Free University Education",
    "Paid University Education",
    "Other",
)
JOB_PROFILE_LEVELS: Final = ("A Lot", "Quite a Bit", "Neutral", "A Little", "Not at All")

# Fictional weights are explicit and intentionally uncomplicated. Course does
# not influence employment outcomes, avoiding unsupported claims about courses.
GENDER_WEIGHTS: Final = (0.48, 0.48, 0.04)
JURISDICTION_WEIGHTS: Final = (0.35, 0.45, 0.20)
COURSE_TYPE_WEIGHTS: Final = (0.20, 0.60, 0.20)
AGE_WEIGHTS: Final = (0.25, 0.40, 0.25, 0.10)
EMPLOYMENT_BEFORE_WEIGHTS: Final = (0.55, 0.30, 0.12, 0.03)
EMPLOYMENT_AFTER_BY_BEFORE: Final = {
    "Employed": (0.82, 0.10, 0.05, 0.03),
    "Unemployed and Looking for Work": (0.52, 0.36, 0.10, 0.02),
    "Unemployed and Not Looking for Work": (0.35, 0.30, 0.32, 0.03),
    "Retired": (0.08, 0.04, 0.03, 0.85),
}

Row = dict[str, object]
T = TypeVar("T")


def weighted_choice(rng: random.Random, values: Sequence[T], weights: Sequence[float]) -> T:
    """Return one value using the supplied fictional weights."""
    return rng.choices(values, weights=weights, k=1)[0]


def generate_graduates(
    graduates_count: int, survey_count: int, rng: random.Random
) -> list[Row]:
    """Create a graduate population containing enough 4.0 survey candidates."""
    course_types = ["4.0"] * survey_count
    course_types.extend(
        weighted_choice(rng, COURSE_TYPES, COURSE_TYPE_WEIGHTS)
        for _ in range(graduates_count - survey_count)
    )
    rng.shuffle(course_types)

    return [
        {
            "graduate_id": graduate_id,
            "gender": weighted_choice(rng, GENDERS, GENDER_WEIGHTS),
            "jurisdiction": weighted_choice(rng, JURISDICTIONS, JURISDICTION_WEIGHTS),
            "course": rng.choice(COURSES),
            "course_type": course_types[graduate_id - 1],
            "cohort": rng.choice(COHORTS),
        }
        for graduate_id in range(1, graduates_count + 1)
    ]


def education_for_age(age_group: str, rng: random.Random) -> str:
    """Apply broad fictional age-dependent weights for plausible combinations."""
    weights_by_age = {
        "Under 25": (0.12, 0.28, 0.22, 0.08, 0.25, 0.04, 0.01, 0.00),
        "25-34": (0.04, 0.18, 0.15, 0.12, 0.22, 0.20, 0.05, 0.04),
        "35-44": (0.03, 0.16, 0.10, 0.15, 0.15, 0.25, 0.07, 0.09),
        "45+": (0.04, 0.20, 0.08, 0.16, 0.10, 0.24, 0.06, 0.12),
    }
    return weighted_choice(rng, EDUCATION_LEVELS, weights_by_age[age_group])


def programming_after(before: str, rng: random.Random) -> str:
    """Generate a related, non-deterministic post-training level."""
    weights_by_before = {
        "Senior": (0.72, 0.18, 0.07, 0.03),
        "Semi Senior": (0.16, 0.62, 0.17, 0.05),
        "Junior": (0.04, 0.20, 0.60, 0.16),
        "Trainee": (0.01, 0.07, 0.46, 0.46),
        "No Programming Knowledge": (0.01, 0.03, 0.34, 0.62),
    }
    return weighted_choice(rng, PROGRAMMING_LEVELS_AFTER, weights_by_before[before])


def generate_survey(graduates: list[Row], survey_count: int, rng: random.Random) -> list[Row]:
    """Create one response for sampled 4.0 graduates."""
    eligible = [row for row in graduates if row["course_type"] == "4.0"]
    respondents = rng.sample(eligible, k=survey_count)
    rows: list[Row] = []

    for respondent_id, graduate in enumerate(respondents, start=1):
        age_group = weighted_choice(rng, AGE_GROUPS, AGE_WEIGHTS)
        level_before = weighted_choice(
            rng, PROGRAMMING_LEVELS_BEFORE, (0.03, 0.08, 0.24, 0.30, 0.35)
        )
        employment_before = weighted_choice(
            rng, EMPLOYMENT_STATUSES, EMPLOYMENT_BEFORE_WEIGHTS
        )
        employment_after = weighted_choice(
            rng,
            EMPLOYMENT_STATUSES,
            EMPLOYMENT_AFTER_BY_BEFORE[employment_before],
        )

        it_before = employment_before == "Employed" and rng.random() < 0.28
        it_after = employment_after == "Employed" and rng.random() < 0.48
        programmer_after = it_after and rng.random() < 0.62
        continued_studying = rng.random() < 0.58
        selected_studies: list[str] = []
        if continued_studying:
            selected_studies = rng.sample(STUDY_TYPES, k=rng.randint(1, 3))

        rows.append(
            {
                "respondent_id": respondent_id,
                "graduate_id": graduate["graduate_id"],
                "age_group": age_group,
                "highest_education_level": education_for_age(age_group, rng),
                "programming_level_before": level_before,
                "programming_level_after": programming_after(level_before, rng),
                "employment_before": employment_before,
                "employment_after": employment_after,
                "employment_type_before": rng.choice(EMPLOYMENT_TYPES),
                "employment_type_after": rng.choice(EMPLOYMENT_TYPES),
                "it_before": it_before,
                "it_after": it_after,
                "programmer_after": programmer_after,
                "continued_studying": continued_studying,
                "post_training_study_type": ";".join(selected_studies),
                "course": graduate["course"],
                "cohort": graduate["cohort"],
                "improved_job_profile": weighted_choice(
                    rng, JOB_PROFILE_LEVELS, (0.22, 0.28, 0.22, 0.18, 0.10)
                ),
                "interested_job_opportunities": rng.random() < 0.67,
            }
        )

    return rows


def validate_datasets(
    graduates: list[Row], survey: list[Row], graduates_count: int, survey_count: int
) -> None:
    """Validate schemas, domains, row counts, and cross-table business rules."""
    errors: list[str] = []
    graduate_ids = [row["graduate_id"] for row in graduates]
    respondent_ids = [row["respondent_id"] for row in survey]
    survey_graduate_ids = [row["graduate_id"] for row in survey]
    graduates_by_id = {row["graduate_id"]: row for row in graduates}

    if len(graduates) != graduates_count:
        errors.append("graduates row count does not match --graduates-count")
    if len(survey) != survey_count:
        errors.append("survey row count does not match --survey-count")
    if len(graduate_ids) != len(set(graduate_ids)):
        errors.append("graduate_id is not unique in graduates")
    if len(respondent_ids) != len(set(respondent_ids)):
        errors.append("respondent_id is not unique in survey")
    if len(survey_graduate_ids) != len(set(survey_graduate_ids)):
        errors.append("a graduate_id has more than one survey response")
    if not set(survey_graduate_ids).issubset(graduate_ids):
        errors.append("survey contains graduate_id values absent from graduates")

    graduate_domains = {
        "gender": GENDERS,
        "jurisdiction": JURISDICTIONS,
        "course": COURSES,
        "course_type": COURSE_TYPES,
        "cohort": COHORTS,
    }
    survey_domains = {
        "age_group": AGE_GROUPS,
        "highest_education_level": EDUCATION_LEVELS,
        "programming_level_before": PROGRAMMING_LEVELS_BEFORE,
        "programming_level_after": PROGRAMMING_LEVELS_AFTER,
        "employment_before": EMPLOYMENT_STATUSES,
        "employment_after": EMPLOYMENT_STATUSES,
        "employment_type_before": EMPLOYMENT_TYPES,
        "employment_type_after": EMPLOYMENT_TYPES,
        "course": COURSES,
        "cohort": COHORTS,
        "improved_job_profile": JOB_PROFILE_LEVELS,
    }
    for field, allowed in graduate_domains.items():
        if any(row[field] not in allowed for row in graduates):
            errors.append(f"graduates.{field} contains an undocumented value")
    for field, allowed in survey_domains.items():
        if any(row[field] not in allowed for row in survey):
            errors.append(f"survey.{field} contains an undocumented value")

    for row in survey:
        graduate = graduates_by_id.get(row["graduate_id"])
        if graduate is None:
            continue
        if graduate["course_type"] != "4.0":
            errors.append("survey contains a graduate outside course_type 4.0")
        if row["course"] != graduate["course"] or row["cohort"] != graduate["cohort"]:
            errors.append("survey course/cohort does not match its graduate")
        if row["programmer_after"] and not row["it_after"]:
            errors.append("programmer_after=True without it_after=True")
        if row["employment_after"] != "Employed" and (
            row["it_after"] or row["programmer_after"]
        ):
            errors.append("post-training IT/programmer flags conflict with employment")
        if row["employment_before"] != "Employed" and row["it_before"]:
            errors.append("it_before=True conflicts with employment_before")

        study_value = str(row["post_training_study_type"])
        if not row["continued_studying"] and study_value:
            errors.append("continued_studying=False has a study type")
        if row["continued_studying"]:
            selected = study_value.split(";") if study_value else []
            if not selected or any(value not in STUDY_TYPES for value in selected):
                errors.append("continued_studying=True lacks valid study types")

    if errors:
        raise ValueError("Synthetic data validation failed:\n- " + "\n- ".join(sorted(set(errors))))


def write_csv(path: Path, columns: Sequence[str], rows: list[Row]) -> None:
    """Write a dataset using a stable column order and UTF-8 encoding."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def positive_int(value: str) -> int:
    """Parse a strictly positive CLI integer."""
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def parse_args() -> argparse.Namespace:
    """Parse command-line generation parameters."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graduates-count", type=positive_int, default=DEFAULT_GRADUATES_COUNT)
    parser.add_argument("--survey-count", type=positive_int, default=DEFAULT_SURVEY_COUNT)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    if args.survey_count > args.graduates_count:
        parser.error("--survey-count cannot exceed --graduates-count")
    return args


def main() -> None:
    """Generate, validate, and write both synthetic datasets."""
    args = parse_args()
    rng = random.Random(args.seed)
    graduates = generate_graduates(args.graduates_count, args.survey_count, rng)
    survey = generate_survey(graduates, args.survey_count, rng)

    validate_datasets(graduates, survey, args.graduates_count, args.survey_count)
    write_csv(GRADUATES_OUTPUT, GRADUATES_COLUMNS, graduates)
    write_csv(SURVEY_OUTPUT, SURVEY_COLUMNS, survey)

    print(f"Generated {len(graduates):,} rows: {GRADUATES_OUTPUT}")
    print(f"Generated {len(survey):,} rows: {SURVEY_OUTPUT}")
    print(f"Validation passed (seed={args.seed}).")


if __name__ == "__main__":
    main()
