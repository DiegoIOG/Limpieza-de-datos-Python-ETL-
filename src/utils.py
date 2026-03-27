import logging
import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(name: str, default=None):
    value = os.getenv(name, default)
    if value is None:
        raise ValueError(f"Falta la variable: {name}")
    return value

def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()