import pandas as pd
import numpy as np
import missingno as msno

data = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/', header=0)

df = data[0]
print(df)
print('======================================')
print('Zadanie nr 1')
# Zamień nagłówki kolumn na polskie odpowiedniki: ['TYTUŁ','ARTYSTA','ROK','MAX POZ']
df.columns = ['POZYCJA', 'TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']
print("Dane po zmianie nazw kolumn:")
print(df.head())

print('======================================')
print('Zadanie nr 2')
# Ilu pojedynczych artystów znajduje się na liście?
artists = df['ARTYSTA'].unique()
print(len(artists))

print('======================================')
print('Zadanie nr 3')
# Które zespoły pojawiają się najczęściej na liście?
max_count = df['ARTYSTA'].value_counts().max()
most_popular_artist = df['ARTYSTA'].value_counts()[df['ARTYSTA'].value_counts() == max_count]
print(most_popular_artist)

print('======================================')
print('Zadanie nr 4')
# Zmień nagłówki kolumn, tak aby każdy z nich rozpoczynał się od wielkiej litery, a pozostałe były wprowadzone małymi literami.
df.columns = df.columns.str.title()
print(df.head())

print('======================================')
print('Zadanie nr 5')
# Wyrzuć z tabeli kolumnę ‘Max Poz’.
df = df.drop(columns=['Max Poz'])
print(df.head())

print('======================================')
print('Zadanie nr 6')
# W którym roku wyszło najwięcej albumów znajdujących się na liście?
most_albums_year = df['Rok'].value_counts().max()
most_albums_year = df['Rok'].value_counts()[df['Rok'].value_counts() == most_albums_year]
print(most_albums_year)

print('======================================')
print('Zadanie nr 7')
# Ile albumów wydanych między 1960 a 1990 rokiem włącznie znajduje się na liście?
albums_between_1960_and_1990 = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)]
print(len(albums_between_1960_and_1990))

print('======================================')
print('Zadanie nr 8')
# Ile albumów wydanych między 1960 a 1990 rokiem włącznie znajduje się na liście?
childest_album = df['Rok'].max()
childest_album = df[df['Rok'] == childest_album]
print(childest_album)

print('======================================')
print('Zadanie nr 9')
# Przygotuj listę najwcześniej wydanych albumów każdego artysty, który znalazł się na liście.
earliest_albums = df.groupby('Artysta')['Rok'].min()
earliest_albums = earliest_albums.reset_index()
print(earliest_albums)

print('======================================')
print('Zadanie nr 10')
# Listę zapisz do pliku csv.
csv = earliest_albums.to_csv('earliest_albums.csv', index=False)







