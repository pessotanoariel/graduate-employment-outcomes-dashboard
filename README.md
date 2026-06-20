# Graduate Employment Outcomes Dashboard

**Idioma:** Español | [English](README_EN.md)

Evaluación de empleabilidad, inserción laboral en IT y formación continua utilizando Power BI.

---

## Descripción

Este proyecto presenta un dashboard analítico desarrollado en Power BI para evaluar resultados de empleabilidad posteriores a la graduación de un programa de formación tecnológica.

El análisis combina información de graduados y resultados de una encuesta de seguimiento realizada a ex participantes del programa, permitiendo analizar cambios en la situación laboral, inserción en el sector tecnológico, continuidad educativa y evolución de habilidades percibidas.

La versión pública de este repositorio utiliza datos sintéticos y anonimizados con fines exclusivamente demostrativos.

---

## Objetivo

El objetivo del proyecto es medir resultados posteriores a la graduación y responder preguntas como:

* ¿Qué proporción de egresados consiguió empleo luego de finalizar la formación?
* ¿Cuántos ingresaron al sector tecnológico?
* ¿Cuántos realizaron una transición laboral hacia tecnología?
* ¿Cómo evolucionó el nivel de programación percibido por los participantes?
* ¿Cuántos continuaron formándose después de finalizar el programa?

El proyecto busca demostrar técnicas de análisis de empleabilidad, seguimiento de graduados, modelado de datos y diseño de dashboards utilizando Power BI.

---

## Inicio rápido

1. Abrí `dashboard/graduate_employment_outcomes.pbix` con Power BI Desktop.
2. Los datasets demostrativos se encuentran en `data/synthetic/`.
3. Para regenerarlos desde la raíz del repositorio, ejecutá:

```powershell
python scripts/generate_synthetic_data.py
```

El script genera y valida `graduates_synthetic.csv` (3.000 registros) y `survey_synthetic.csv` (900 respuestas), reemplazando los archivos existentes con resultados reproducibles.

---

## Dashboard

### 1. Resultados Laborales Posteriores a la Formación

Análisis de la situación laboral antes y después de la formación, evolución del empleo y cambios en los niveles de programación declarados por los participantes.

![Resultados Laborales](images/01_employment_outcomes.jpg)

---

### 2. Inserción Laboral en el Sector IT

Análisis de transición hacia empleos tecnológicos, conversión laboral hacia el sector IT y distribución de perfiles de programación por cohorte y curso.

![Inserción IT](images/02_it_sector_insertion.jpg)

---

### 3. Desarrollo Profesional y Formación Continua

Análisis de continuidad educativa, percepción de impacto de la formación y características de los estudios realizados posteriormente por los graduados.

![Formación Continua](images/03_professional_development.jpg)

---

### 4. Perfil de los Participantes

Caracterización demográfica y educativa de la muestra analizada para contextualizar los resultados presentados en el dashboard.

![Perfil de Participantes](images/04_participant_profile.jpg)

---

## Principales dimensiones analizadas

* Género
* Edad
* Jurisdicción
* Curso realizado
* Cohorte de cursada
* Nivel educativo alcanzado

---

## Principales indicadores

* Tasa de respuesta de la encuesta
* Empleabilidad posterior a la graduación
* Inserción laboral en el sector IT
* Inserción laboral en programación
* Cambio laboral hacia el sector IT
* Evolución del nivel de programación
* Continuidad educativa post graduación

---

## Herramientas utilizadas

* Power BI
* Power Query
* DAX
* Excel
* Modelado dimensional

---

## Mi participación

Participé en todas las etapas del proyecto.

### Diseño de la evaluación

* Definición de objetivos de evaluación junto al equipo responsable del programa.
* Diseño de indicadores para medir empleabilidad, inserción en el sector IT y continuidad educativa.
* Participación en la construcción del cuestionario de relevamiento.
* Coordinación con equipos de comunicación para la ejecución de campañas de contacto con graduados.
* Seguimiento de tasas de respuesta y cobertura de la muestra.

### Preparación y modelado de datos

* Construcción y depuración de datasets de análisis.
* Desarrollo del modelo de datos.
* Transformaciones y enriquecimiento mediante Power Query.
* Construcción de métricas y KPIs utilizando DAX.

### Desarrollo del dashboard

* Diseño y desarrollo del dashboard en Power BI.
* Elaboración de análisis y conclusiones para la evaluación del programa.

---

## Estructura del repositorio

```text
dashboard/
├── graduate_employment_outcomes.pbix

data/
├── synthetic/
├── data_dictionary.md
├── graduates_schema.md
└── survey_schema.md

docs/
├── graduate_employment_outcomes.pdf
└── methodology.md

images/
├── cover.jpg
├── 01_employment_outcomes.jpg
├── 02_it_sector_insertion.jpg
├── 03_professional_development.jpg
└── 04_participant_profile.jpg

scripts/
├── generate_synthetic_data.py
└── README.md

README.md
README_EN.md
```

---

## Consideraciones metodológicas

El relevamiento se realizó sobre múltiples cohortes de graduados mediante una encuesta de seguimiento posterior a la finalización del programa.

Debido a que la evaluación fue implementada una vez que varias cohortes ya habían egresado, las tasas de respuesta presentan diferencias entre períodos. Las cohortes más recientes fueron contactadas más cerca de su fecha de graduación, mientras que las cohortes más antiguas tuvieron mayores intervalos temporales entre egreso y relevamiento.

Estas diferencias pueden afectar la comparabilidad entre cohortes y deben considerarse al interpretar los resultados.

---

## Aviso sobre los datos

Los datos originales utilizados durante la ejecución del proyecto pertenecían a una iniciativa real y contenían información personal de participantes.

Para esta versión pública:

* Se eliminaron todos los datos originales.
* Se removieron identificadores personales.
* Se reemplazaron los datasets por datos sintéticos.
* Los valores y resultados presentados fueron modificados o generados sintéticamente para preservar la confidencialidad de la información original.

El objetivo de este repositorio es mostrar el enfoque analítico, el modelado de datos y la construcción del dashboard.
