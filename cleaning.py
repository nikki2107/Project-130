import csv
import pandas as pd

df=pd.read_csv("file.csv")
print(df.shape)

del df ["lum"]
del df ["name"]
del df ["distance"]
del df ["mass"]
del df ["radius"]

df.to_csv("final.csv")