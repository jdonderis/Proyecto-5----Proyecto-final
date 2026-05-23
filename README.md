# Proyecto-5----Proyecto-final

_1. Descripción_
Este proyecto tiene como objetivo el análisis de la longevidad de la carrera de los jugadores de la NBA mediante el uso de técnicas de Data Analytics. A través de un proceso completo de extracción, limpieza, transformación y análisis exploratorio de datos, se busca identificar los factores que determinan la duración de la carrera de un jugador profesional de baloncesto.

_2. Requisitos_
Software Python 3.1
Librerías pandas numpy datetime matplotlib seaborn

Software Power BI 2.15 

Microsoft Excel 97

_3. Instalación_
Antes de comenzar, asegúrate de que los siguientes requisitos se cumplen:
  1. Instalación funcional de Visual Studio Code.
  2. Instalación de las extensiones de VSC de Jupyter Notebook y Python.
Ejecución de las consultas:
  3. Asegúrate de que el fichero se abre en formato Jupyter. (.ipynb)
  4. Instala Python y su extensión en VSC
  5. Importa el archivo con los scripts de Python creados.
  6. Ejecuta los scripts

_4. Estructura del Proyecto_
Proyecto 5 - Proyecto final/
├── Data/
│   ├── common_player_info.csv            # Dataset con información general de jugadores
│   ├── draft_combine_stats.csv           # Dataset con datos del draft de los jugadores
│   └── draft_history.csv                 # Dataset con datos históricos del draft
│   └── player.csv                        # Dataset con datos básicos de jugadores
│   └── players_general.csv               # Dataset con datos generales de los jugadores
├── Clean_data/
│   ├── Dataframe_original.csv            # Dataset original
│   ├── Dataframe_limpio.csv              # Dataset tras limpieza
│   └── Dataframe_sin_nulos.csv           # Dataset tras eliminación de nulos
│   └── Dataframe_EDA.csv                 # Dataset listo para el estudio y las visualizaciones
├── Jupyters/
│   ├── 1_Prework.ipynb                   # Creación de un dataset único
│   ├── 2.1_Limpieza de nulos.ipynb       # Jupyter con la limpieza de nulos
│   ├── 2.2_Limpieza de duplicados.ipynb  # Jupyter con la limpieza de duplicados
│   ├── 3_Transformación.ipynb            # Transformación de datos
│   ├── 4.1_EDA.ipynb                     # Análisis univariante del dataset final
│   ├── 4.2_EDA.ipynb                     # Análisis bivariante del dataset final
│   └── soporte_def.py                    # Funciones de soporte
├── PowerBI/
│   ├── 5_Data visualization              # Dashboards de datos generales y seniority
└── README.md

_5.Resultados y conclusiones_

- La variable from_year es el predictor más potente de la longevidad con una correlación de -0,668
- La variable num_equipos presenta una correlación de 0,583 con la seniority
- Los jugadores que no han pasado por la G-League tienden a tener carreras más largas
- El 64,57% de los jugadores proceden del sistema universitario estadounidense
- Casi el 23,60% de los jugadores llegaron a la NBA sin ser drafteados
- El jugador típico de la NBA mide 200 cm, pesa 100 kg y tiene una carrera de 8,46 temporadas

_6. Próximos pasos_

El presente proyecto se considera concluido en relación a su objetivo principal original de analizar el impacto de diferentes variables sobre la longevidade de una carrera en la NBA. Sin embargo, de proseguir con su desarrollo, se sugiere como próximos pasos el refinamiento y mejora de los scripts ya creados con el objetivo de crear scripts más robustos y efectivos, y el desarrollo de un estudio con respecto al impacto en la longevidad del jugador de las posiciones del draft. Este enfoque proporcionaría una mejora notable a los scripts ya creados, ayudando a cualquier futuro usuario del fichero a un uso más fácil y veloz de los scripts en sus propósitos y ahondaría más en el objetivo del estudio.

_7. Contribuciones_
Las contribuciones son bienvenidas. Por favor abra un issue primero para discutir los cambios que deseas realizar.
