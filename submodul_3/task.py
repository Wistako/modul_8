import pandas as pd

def grab_series(df, sheet_name, colname, startcol=0, startrow=0):

    col_index = df.columns.tolist().index(colname)
    col_letter = chr(ord('@')+(col_index+2+startcol))
    first_row = startrow + 2
    last_row = startrow + 1 + len(df)
    return f"='{sheet_name}'!{col_letter}{first_row}:{col_letter}{last_row}"

# Zadanie 1
df = pd.read_csv('submodul_3/fatal-police-shootings-data.csv')
# print(df.head())

# Zadanie 2
pt = df.pivot_table(values='id', index=['race', 'signs_of_mental_illness'], aggfunc='count')
# print(pt)
# print(pt.columns)

# Zadanie 3
"""
Za pomocą Map, Applymap lub Apply dodaj do tego zestawienia kolumnę wskazującą jaki odsetek
ofiar interwencji wykazywało oznaki choroby psychicznej dla każdej z ras.
"""
pt['mental_illness_percentage'] = pt.apply(lambda row: row['id'] / pt.loc[row.name[0]].sum() * 100, axis=1)

# print(pt)
max_mental_illness = pt[pt.index.get_level_values('signs_of_mental_illness') == True]['mental_illness_percentage'].max()
race_with_max = pt[pt['mental_illness_percentage'] == max_mental_illness].index[0][0]

print(f"Rasa z największym odsetkiem osób wykazujących oznaki choroby psychicznej to {race_with_max}")

# Zadanie 4
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.day_name()

# Zliczenie wystąpień dnia tygodnia
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_counts = df['day'].value_counts().reindex(days_order)
day_counts = day_counts.reset_index()
# print(day_counts)

writer = pd.ExcelWriter('submodul_3/day_counts.xlsx', engine='xlsxwriter')
day_counts.to_excel(writer, sheet_name='Day Counts')
workbook = writer.book
worksheet = writer.sheets['Day Counts']

chart = workbook.add_chart({'type': 'column'})
chart.add_series({
    'categories': grab_series(day_counts, 'Day Counts', 'day'),
    'values': grab_series(day_counts, 'Day Counts', 'count')})
chart.set_x_axis({'name': 'Dzień tygodnia'})
chart.set_y_axis({'name': 'Liczba wystąpień'})
chart.set_legend({'none': True})

worksheet.insert_chart('F2', chart)
writer._save()

# Zadanie 5

state_population = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population')[0]
print(state_population.columns[3])
state_population = state_population[['State', 'Census population, April 1, 2020 [1][2]']]
state_population.columns = ['state', 'population']

state_abbreviations = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations')[1]
state_abbreviations = state_abbreviations[['Name', 'ANSI']]
state_abbreviations.columns = ['state', 'abbreviation', 'code']
state_abbreviations.drop(columns=['code'], inplace=True)

state_data = pd.merge(state_abbreviations, state_population, on='state', how='left')
print(state_data.columns)
print(state_data.head())

count_state_police_shootings = df['state'].value_counts().reset_index()
count_state_police_shootings.columns = ['abbreviation', 'count']

state_data = pd.merge(state_data, count_state_police_shootings, on='abbreviation', how='left')

state_data['liczba_incydentów_na_1000_mieszkańców'] = state_data['count'] / (state_data['population'] / 1000)
print(state_data.head(10))


























