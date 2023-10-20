from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


def splittlines(path):
    lines = path.read_text(encoding='utf-8').splitlines()
    reader_ = csv.reader(lines)
    header_row_ = next(reader_)

    return header_row_, reader_


def extract_values(reader_, index_):
    highs, dates_ = [], []
    for row in reader_:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        print(current_date)

        try:
            high = float(row[index_])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            highs.append(high)
            dates_.append(current_date)

    return highs, dates_


dates, high_dvs, high_sitkas = [], [], []
header_dict_s, header_dict_dv = {}, {}

path_sitka = Path('weather_data/sitka_weather_2021_simple.csv')
path_dv = Path('weather_data/death_valley_2021_simple.csv')
#path = Path('weather_data/death_valley_2021_full.csv')


header_row_s, reader_s = splittlines(path_sitka)
header_row_dv, reader_dv = splittlines(path_dv)

for index, column_header in enumerate(header_row_s):
    header_dict_s[column_header] = index

print('=====================')

for index, column_header in enumerate(header_row_dv):
    header_dict_dv[column_header] = index

high_sitkas, dates_s = extract_values(reader_s, header_dict_s['TMAX'])
high_dvs, dates_v = extract_values(reader_dv, header_dict_dv['TMAX'])



plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates_s, high_sitkas, color = 'blue', alpha = 0.5)
ax.plot(dates_v, high_dvs, color = 'red', alpha = 0.5)
#ax.fill_between(dates, high_dvs, high_sitkas, facecolor='blue', alpha = 0.1)

#Format the plot
ax.set_title("Precipation, 2021\n Sitka", fontsize = 24)
ax.set_xlabel('', fontsize=16)

fig.autofmt_xdate()

ax.set_ylabel("Rainfall in mm", fontsize = 16)
ax.tick_params(labelsize=8)

plt.show()
