#%%

import pandas as pd

df = pd.read_csv("/PANDAS_2025/data/clientes.csv")
df
df.to_csv("clientes.cvs", index=False)

#%%
import os

file_path = "C:/PANDAS_2025/data/clientes.csv"

if os.path.exists(file_path):
    print("File exists!")
else:
    print("File does not exist at the specified path.")
