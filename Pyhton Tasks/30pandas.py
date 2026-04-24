import pandas as pd
# 
df = pd.read_csv("sample_superstore.csv", encoding="latin1")
# print(df.info())
# print(df.info())
# change col name ship mode
# df = df.rename(columns={"Ship Mode": "Ship mode"}, inplace=True)
# print(df.columns)
# remove postl code col
# df = df.drop(columns=["Postal Code"])
# print(df.columns)