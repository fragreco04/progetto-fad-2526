import pandas as pd
import numpy as np


df = pd.read_csv('train-data.csv')


df['Brand'] = df['Name'].apply(lambda x: x.split(' ')[0])


premium_brands = ['Audi', 'BMW', 'Mercedes-Benz', 'Land', 'Jaguar', 'Volvo', 'Porsche', 'Mini', 'Lamborghini', 'Bentley']
df['Segment'] = df['Brand'].apply(lambda x: 'Premium' if x in premium_brands else 'Mass Market')


current_year = df['Year'].max() + 1
df['Car_Age'] = current_year - df['Year']


df_clean = df[(df['Car_Age'] <= 10) & (df['Price'] < 100)].copy()


depreciation_data = df_clean.groupby(['Car_Age', 'Segment'])['Price'].mean().unstack()


all_ages = range(1, 11)
depreciation_data = depreciation_data.reindex(all_ages)

print("--- TABELLA SVALUTAZIONE  ---")
print(depreciation_data.round(2))


try:
    
    prem_start = depreciation_data.loc[2, 'Premium']
    prem_end = depreciation_data.loc[8, 'Premium']
    mass_start = depreciation_data.loc[2, 'Mass Market']
    mass_end = depreciation_data.loc[8, 'Mass Market']

    print("\n--- ANALISI DEL CROLLO (Anno 2 vs Anno 8) ---")
    print(f"Premium:      {prem_start:.2f} -> {prem_end:.2f} (Perdita: {prem_start - prem_end:.2f} Lakhs)")
    print(f"Mass Market:  {mass_start:.2f} -> {mass_end:.2f} (Perdita: {mass_start - mass_end:.2f} Lakhs)")
except KeyError:
    print("\nDati insufficienti per calcolare la perdita esatta tra anno 2 e 8.")