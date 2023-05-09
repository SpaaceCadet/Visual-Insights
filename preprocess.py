import pandas as pd
import numpy as np


"""df = pd.read_csv("energy_dataset.csv")
#target.index = dataset.index

df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)

df.index = pd.to_datetime(df.index,utc=True)
target = df["price actual"]

target.to_csv("target_csv")
"""

df = pd.read_csv("model_params/target_csv2", index_col="time", parse_dates=True)
#df.index = df.index.strftime('%Y/%m/%d/%H')
#df.index = pd.to_datetime(df.index)
print(list(df.index.year.unique().values))
print(df.loc[df.index.year==2018,"price actual"])


