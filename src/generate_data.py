import pandas as pd 
import random 

def generate_sales_data(n_rows:int) -> pd.DataFrame:
     productos=["laptop","Mouse","Teclado","Monitor"]
     ciudades=["Monterrey","monterrey","Guadalajar",None]

     data=[]

     for _ in range(n_rows):
          row = {
               "fecha":"2024-01-01",
               "producto":random.choice(productos),
               "precio":random.choice([15000,300,None,"500"]),
               "cantidad":random.choice([1,2,3,-1]),
               "ciudad": random.choice(ciudades)
          }
          data.append(row)

     return pd.DataFrame(data)