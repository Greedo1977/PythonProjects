from pathlib import Path
import json

path = Path("Resources/favourite_number.txt")
contents = path.read_text()

username = json.loads(contents)

for name, number in username.items():
    print(f"{name} your favourite number is {number}")