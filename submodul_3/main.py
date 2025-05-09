import math
import pandas as pd
import numpy as np

df  = pd.read_excel('submodul_3/Pivot.xlsx')
print(df.head())

pt = df.pivot_table(values='Sprzedaż', index='Przedstawiciel', columns='Region', aggfunc='sum')
print(pt)

pt = df.pivot_table(values='Sprzedaż',index='Przedstawiciel',columns='Region',aggfunc='sum').fillna(0).round(2)
print(pt)


pt = df.pivot_table(values='Sprzedaż',index=['Przedstawiciel','Region'],aggfunc='sum').fillna(0).round(2)
print(pt)

pt = df.pivot_table(values='Sprzedaż',index='Region',aggfunc=[len,'max', 'min', 'sum']).fillna(0).round(2)
print(pt)



# FUNKCJA APPLY (dodawanie nowych kolumn z lambdą)
# funkcja zwraca wysokość prowizji
def commission_fee(x):
  if x <= 300:
    return 0
  elif x<= 900:
    return x * 0.03
  else:
    return x * 0.06


# df['commission_fee'] = df['Sprzedaż'].apply(lambda x: commission_fee(x))
df['commission_fee'] = df['Sprzedaż'].apply(commission_fee)
print(df.head())


df['#_opakowań'] = df['Sztuki'].apply(lambda x: math.ceil(x/5))
print(df.head())


# funkcja zwraca wysokość bonusu od transakcji
def bonus(row):
  margin = (row['Sprzedaż'] - row['Koszty']) / row['Sprzedaż']

  if margin > 0.55:
    return 200
  else:
    return 0

df['bonus'] = df.apply(lambda row: bonus(row), axis=1)
print(df.sample(10))


# FUNKCJA MAP

car_dict = dict(zip(df['Przedstawiciel'].unique(),['Mazda','Toyota','BMW','Audi','Fiat','Seat']))
print(car_dict)

# Podstawianie wartości ze słownika do nowej kolumny
df['Marka_samochodu'] = df['Przedstawiciel'].map(car_dict)
print(df.head())


# FUNKCJA APPLYMAP

print(df.applymap(lambda x: x.upper() if isinstance(x,str) else x).head(10))
# print(df.head())


# Accessor methods

# .dt - datetime
"""
Inne funkcje i atrybuty, z których możemy korzystać poprzez accessor .dt:
 date, days_in_month, second, minute, hour, day, week, month, quarter, year, is_leap_year,
 is_month_start, is_month_end, is_quarter_start, is_quarter_end, is_year_start, is_year_end
"""

df['Data'] = pd.to_datetime(df['Data'])
print(df['Data'].dt.day_name().head(10))
print(df['Data'].dt.month_name().head(10))

print(df[df['Data'].dt.day_name()=='Thursday'].head(10))

# .str - string
"""
Inne przykładowe metody, jakich możemy użyć za pośrednictwem accessora str:
 lower(), zfil(), startswith(), swapcase(), repeat().
"""

print(df['Produkt'].str.upper().head())
print(df[df['Region'].str.contains('Zachód')].sample(5))




