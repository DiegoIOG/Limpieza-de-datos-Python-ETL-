from src.generate_data import generate_sales_data
from src.clean_data import clean_sales_data
from src.utils import get_env_variable, get_logger

import pandas as pd

logger = get_logger()

def main():
    raw_path = get_env_variable("RAW_DATA_PATH")
    processed_path = get_env_variable("PROCESSED_DATA_PATH")
    n_rows = int(get_env_variable("NUM_ROWS", 50))

    # EXTRACT (simulado)
    logger.info("Generando datos...")
    df_raw = generate_sales_data(n_rows)
    df_raw.to_csv(raw_path, index=False)

    # TRANSFORM
    logger.info("Limpiando datos...")
    df = pd.read_csv(raw_path)
    df_clean = clean_sales_data(df)

    # LOAD
    logger.info("Guardando datos limpios...")
    df_clean.to_csv(processed_path, index=False)

    logger.info("Pipeline ETL completado")

if __name__ == "__main__":
    main()