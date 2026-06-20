# Graduates Dataset Schema

## Descripción

Contiene el universo de graduados utilizado como población de referencia para el análisis.

Cada registro representa un graduado único.

## Tabla: graduates

| Campo        | Tipo    | Descripción                          |
| ------------ | ------- | ------------------------------------ |
| graduate_id  | Integer | Identificador sintético del graduado |
| gender       | Text    | Género declarado                     |
| jurisdiction | Text    | Jurisdicción de residencia           |
| course       | Text    | Curso realizado                      |
| course_type  | Text    | Categoría del curso                  |
| cohort       | Text    | Cohorte o período de cursada         |

## Valores esperados

### gender

* Female
* Male
* Other

### jurisdiction

* CABA
* Buenos Aires Province
* Other Provinces

### course

* Big Data
* UX/UI Design
* FullStack Java
* FullStack JavaScript / Node.js
* FullStack PHP
* FullStack Python
* Testing QA

### cohort

Valores observados:

* 2020-2
* 2021-1
* 2021-2
* 2022-1

#### Original Survey Scope

La encuesta intercohorte utilizada como base para este proyecto relevó graduados desde el segundo cuatrimestre de 2020 hasta el primer cuatrimestre de 2022.

### course_type

* Initial Programming
* 4.0
* Advanced

#### Business Rules

Initial Programming:
Programa introductorio de ingreso.

4.0:
Programa principal de formación tecnológica. La mayoría de los graduados pertenecen a esta categoría.

Advanced:
Cursos avanzados destinados a graduados del programa 4.0.

## Observaciones

El proyecto original incluía graduados de múltiples tipos de formación.

Sin embargo, la encuesta utilizada para este dashboard fue respondida exclusivamente por graduados de cursos pertenecientes al programa 4.0.
