import pandas as pd
import numpy as np

df_raw = pd.read_csv('train-data.csv', index_col=0) 

# Funzione di pulizia rapida solo per questa analisi
def clean_currency_raw(x):
    if isinstance(x, str):
        return float(x.split(' ')[0])
    return x

# Pulizia al volo
df_raw['Power_clean'] = df_raw['Power'].apply(lambda x: clean_currency_raw(x) if isinstance(x, str) and 'null' not in x else np.nan)
df_raw['Engine_clean'] = df_raw['Engine'].apply(clean_currency_raw)


df_raw.dropna(subset=['Price', 'Power_clean', 'Engine_clean', 'Name'], inplace=True)


similar_cols = ['Name', 'Year', 'Fuel_Type', 'Transmission', 'Owner_Type']


grouped = df_raw.groupby(similar_cols)['Price'].agg(['min', 'max', 'count'])
grouped['diff'] = grouped['max'] - grouped['min']


shocking_cars = grouped[(grouped['count'] > 1) & (grouped['diff'] > 3)].sort_values('diff', ascending=False)

print("--- TOP 5 CASI DI PREZZI FOLLI (Auto Identiche) ---")
print(shocking_cars.head(5))



# trovate queste:
print(df_raw[df_raw['Name'] == 'Porsche Panamera Diesel'])
print(df_raw[df_raw['Name'] == 'Audi Q7 4.2 TDI Quattro Technology'])