import pandas as pd

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    # regla: cantidad no negativa
    return df[df["cantidad"] >= 0]

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # limpieza
    df['producto'] = df['producto'].str.strip()
    df['ciudad'] = df['ciudad'].str.strip().str.title()

    # tipos
    df['precio'] = pd.to_numeric(df['precio'], errors='coerce')
    df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce')

    # nulos
    df['precio'].fillna(df['precio'].mean(), inplace=True)
    df['ciudad'].fillna("Desconocido", inplace=True)

    # validación
    df = validate_data(df)

    # feature
    df['total'] = df['precio'] * df['cantidad']

    return df