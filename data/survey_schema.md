# Survey Dataset Schema

## Descripción

Contiene las respuestas sintéticas de la encuesta de seguimiento realizada a graduados.

Cada registro representa una respuesta individual.

## Tabla: survey_responses

| Campo                        | Tipo    | Descripción                                        |
| ---------------------------- | ------- | -------------------------------------------------- |
| respondent_id                | Integer | Identificador sintético de la respuesta            |
| graduate_id                  | Integer | Relación con tabla graduates                       |
| age_group                    | Text    | Grupo etario                                       |
| highest_education_level      | Text    | Máximo nivel educativo alcanzado                   |
| programming_level_before     | Text    | Nivel de programación antes de la formación        |
| programming_level_after      | Text    | Nivel de programación después de la formación      |
| employment_before            | Text    | Situación laboral antes de la formación            |
| employment_after             | Text    | Situación laboral después de la formación          |
| employment_type_before       | Text    | Tipo de empleo antes de la formación               |
| employment_type_after        | Text    | Tipo de empleo después de la formación             |
| it_before                    | Boolean | Trabajaba en el sector IT antes                    |
| it_after                     | Boolean | Trabaja en el sector IT después                    |
| programmer_after             | Boolean | Trabaja actualmente como programador               |
| continued_studying           | Boolean | Continuó formándose luego de finalizar el programa |
| post_training_study_type     | Text    | Tipo de formación posterior                        |
| course                       | Text    | Curso realizado                                    |
| cohort                       | Text    | Cohorte de cursada                                 |
| improved_job_profile         | Text    | Percepción de mejora del perfil laboral            |
| interested_job_opportunities | Boolean | Interés en recibir oportunidades laborales         |

## Valores esperados

### age_group

Derivado a partir de la fecha de nacimiento relevada en la encuesta.

Ejemplos:

* Under 25
* 25-34
* 35-44
* 45+

### highest_education_level

* Secondary Incomplete
* Secondary Complete
* Tertiary Incomplete
* Tertiary Complete
* University Incomplete
* University Complete
* Postgraduate Incomplete
* Postgraduate Complete

### programming_level_before

* Senior
* Semi Senior
* Junior
* Trainee
* No Programming Knowledge

### programming_level_after

* Senior
* Semi Senior
* Junior
* Trainee

### employment_before

* Employed
* Unemployed and Looking for Work
* Unemployed and Not Looking for Work
* Retired
  
Note:
Retired responses are included for completeness but represent a very small proportion of the synthetic dataset.

### employment_after

* Employed
* Unemployed and Looking for Work
* Unemployed and Not Looking for Work
* Retired

### employment_type_before

* Employee
* Self-employed
* Informal Worker
* Own Business

### employment_type_after

* Employee
* Self-employed
* Informal Worker
* Own Business

### it_before

* Yes
* No

### it_after

* Yes
* No

### programmer_after

* Yes
* No

### continued_studying

* Yes
* No

### post_training_study_type

Multiple selections are allowed.

* Free Quarterly Course
* Paid Quarterly Course
* Free Annual Course
* Paid Annual Course
* Free Tertiary Education
* Paid Tertiary Education
* Free University Education
* Paid University Education
* Other

### course

* Big Data
* UX/UI Design
* FullStack Java
* FullStack JavaScript / Node.js
* FullStack PHP
* FullStack Python
* Testing QA

### cohort

* 2020-2
* 2021-1
* 2021-2
* 2022-1

### improved_job_profile

* A Lot
* Quite a Bit
* Neutral
* A Little
* Not at All

### interested_job_opportunities

* Yes
* No

## Derived Metrics

A partir de estas columnas pueden construirse:

* Employment Rate
* IT Employment Rate
* Programming Employment Rate
* Employment Transition
* IT Transition
* Programming Transition
* Continuing Education Rate
* Job Profile Improvement Rate
* Interest in Employment Opportunities
  """
