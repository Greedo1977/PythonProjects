from pathlib import Path
from collections import Counter

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)

        print(f"The file {path} has about {num_words} words.\n")

files_list = ['Resources/alice.txt', 'Resources/little_women1.txt', 'Resources/moby_dick.txt']

for file in files_list:
    path = Path(file)
    count_words(path)