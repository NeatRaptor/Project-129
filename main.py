import pandas as pd
import csv

df = pd.read_csv("dwarf_stars.csv")
# print(df.head())
# print(df.columns)
# print(df.dtypes)

df = df.dropna()
# print(df.dtypes)

df['Radius'] = 0.102763 * df['Radius']
df['Mass'] = df['Mass'].apply(lambda x:x.replace('$','').replace(',','')).astype('float')
df['Mass'] = df['Mass'] * 0.000954588

print(df.head())
print(df.columns)
print(df.dtypes)

df.drop(['Unnamed: 0'], axis=1, inplace=True)

print(df.head())

df.reset_index(drop = True, inplace=True)

df.to_csv("dwarf_stars_sorted.csv")

print(df.dtypes)