# Limpieza-de-datos-Python-ETL

##  Descripción

Este proyecto implementa un pipeline sencillo de tipo **ETL (Extract, Transform, Load)** utilizando Python.
El objetivo es simular un flujo real de ingeniería de datos, donde se generan datos sucios, se limpian y se almacenan listos para análisis.


##  Estructura del proyecto

```
data-cleaning-project/
│
├── data/
│   ├── raw/          # Datos generados (sucios)
│   └── processed/    # Datos limpios
│
├── src/
│   ├── generate_data.py   # Generación de datos
│   ├── clean_data.py      # Limpieza y transformación
│   └── utils.py           # Configuración y logging
│
├── tests/                 # Pruebas unitarias
├── .env                   # Variables de entorno (no incluido en repo)
├── .env.example           # Ejemplo de configuración
├── requirements.txt
├── main.py                # Orquestador del pipeline
└── README.md
```

---

##  Configuración

### 1. Clonar repositorio

```
git clone <tu-repo>
cd data-cleaning-project
```

### 2. Crear entorno virtual

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear archivo `.env` basado en `.env.example`:

```
RAW_DATA_PATH=data/raw/ventas.csv
PROCESSED_DATA_PATH=data/processed/ventas_limpio.csv
NUM_ROWS=50
```

---

##  Ejecución del pipeline

```
PYTHONPATH=. python main.py
```

Esto realizará:

1. Generación de datos simulados (sucios)
2. Limpieza y transformación
3. Guardado de datos procesados

---

##  Ejecutar pruebas

```
pytest -v
```

---

## Funcionalidades principales

* Generación de datos con inconsistencias
* Limpieza de datos:

  * Eliminación de espacios
  * Conversión de tipos
  * Manejo de valores nulos
  * Eliminación de registros inválidos
* Creación de nuevas variables (feature engineering)
* Uso de variables de entorno (`.env`)
* Logging del proceso
* Pruebas unitarias con pytest

---

## Resultados

* `data/raw/ventas.csv` → datos sin procesar
* `data/processed/ventas_limpio.csv` → datos listos para análisis

---

##  Objetivo del proyecto

Simular un flujo básico de trabajo de un **Data Engineer Junior**:

* Pipeline ETL

---

