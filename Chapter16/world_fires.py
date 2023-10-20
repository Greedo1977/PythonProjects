import csv
from pathlib import Path
import plotly.express as px


def extract_values(reader_):
    lats_, longs_, brightnesses_ = [], [], []
    for row in reader_:
        try:
            lat_ = row[0]
            long_ = row[1]
            brightness_ = float(row[2])
        except:
            print(f'Exception occurred')
        else:
            lats_.append(lat_)
            longs_.append(long_)
            brightnesses_.append(brightness_)

    return lats_, longs_, brightnesses_

path = Path('eq_1_day/world_fires_7_day.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader_ = csv.reader(lines)
header_row_ = next(reader_)



header_dict_s = {}
for index, column_header in enumerate(header_row_):
    header_dict_s[column_header] = index

latitudes_, longitudes_, brightness_ = extract_values(reader_)

map_title = 'World fires in past 1 day'
fig = px.scatter_geo(lat=latitudes_, lon=longitudes_, title=map_title,
                     color=brightness_,
                     color_continuous_scale='icefire',
                     labels={'color':'Intensity'},
                     projection='natural earth',
                     )

# fig = px.scatter_geo(lat=latitudes_, lon=longitudes_, title=map_title,
#                      size=brightness_
#                      )
fig.show()
