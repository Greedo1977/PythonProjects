from pathlib import Path
import plotly.express as px
import json

def extract_eq_features(all_eq_data):
    all_eq_dicts = {}
    all_eq_dicts = all_eq_data['features']
    return all_eq_dicts

# ===========================


def extract_eq_main_title(all_eq_data):
    return all_eq_data['metadata']['title']

# ===========================

def extract_eq_mags(all_eq_feature_dicts):
    mags = []
    for eq_dict in all_eq_feature_dicts:
        mag = eq_dict['properties']['mag']
        mags.append(mag)

    return mags

# ===========================

def extract_eq_lon_lat(all_eq_feature_dicts):
    lons, lats = [], []
    for eq_dict in all_eq_feature_dicts:
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]

        lons.append(lon)
        lats.append(lat)

    return lons, lats

# ===========================


def extract_eq_title(all_eq_feature_dicts):
    eq_titles = []
    for eq_dict in all_eq_feature_dicts:
        title = eq_dict['properties']['title']

        eq_titles.append(title)

    return eq_titles

# ===========================

# Read data as a string and convert to a Python object.
path = Path("eq_1_day/4.5_month.geojson")
contents = path.read_text(encoding='utf-8')

all_eq_data = json.loads(contents)
# ===========================


# Create a more readable version of the file.
path = Path('eq_1_day/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# ===========================
map_title = extract_eq_main_title(all_eq_data)
all_eq_feature_dicts = extract_eq_features(all_eq_data)

mags = extract_eq_mags(all_eq_feature_dicts)
lons, lats = extract_eq_lon_lat(all_eq_feature_dicts)
titles = extract_eq_title(all_eq_feature_dicts)


# ===========================

fig = px.scatter_geo(lat=lats, lon=lons, title=map_title,
                     color=mags,
                     color_continuous_scale='balance',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=titles
                     )
fig.show()


