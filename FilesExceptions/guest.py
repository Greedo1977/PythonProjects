from pathlib import Path

names = []

while True:
    guest = input('What is your name? (enter q to quit) ')
    if guest == 'q':
        break

    names.append(guest)

guest_file = Path('Resources/guest.txt')

line = ''
for name in names:
    line += f'{name}\n'

guest_file.write_text(line)
