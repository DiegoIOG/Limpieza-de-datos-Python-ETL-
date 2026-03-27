import pandas as pd
from src.clean_data import clean_sales_data

def test_no_negative_values():
    df = pd.DataFrame({
        "producto": ["Laptop"],
        "precio": [100],
        "cantidad": [-1],
        "ciudad": ["Monterrey"]
    })

    result = clean_sales_data(df)

    assert len(result) == 0