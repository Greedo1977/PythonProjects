from pathlib import Path

file = 'Resources/KingJamesBible.txt'


def word_count(path, word):
    path_ = Path(path)
    try:
        contents = path_.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().split().count(word)
        print(f"'{word}' occurs {word_count} times in file {file}")


word_count(file, word = 'god')
