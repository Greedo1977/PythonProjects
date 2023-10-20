from pathlib import Path

import json

username = {}

favourite_number = input('Favourite Number?: ')
name = input("Name?: ")
username[name] = favourite_number

favourite_path = Path('favourite_number.txt')

contents = json.dumps(username)
favourite_path.write_text(contents)
