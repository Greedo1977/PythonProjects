from pathlib import Path

path = Path('Resources/programming.txt')

contents = 'Hello Madhu, I love programming\n'
contents += 'Do you like programming?\n'
contents += 'What else do you like?\n'

path.write_text(contents, newline='\n')