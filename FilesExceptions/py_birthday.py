from pathlib import Path
pi_million = ''

lines = Path('Resources/pi_million_digits.txt').read_text().strip()

lines = lines.splitlines()

#pi_million = ''
#for line in lines:
#    pi_million += line.strip()

print(f"{pi_million[:52]}")
print(len(pi_million))
#print(pi_million)

birthday = ''
while True:
    birthday = input('Enter you a birthday in format YYYYMMDD (or q to quit:) ')

    if birthday == 'q':
        break

    if birthday in pi_million:
        print(f"Your birthday ({birthday}) appears in the first million digits of pi")
    else:
        print(f"Your birthday ({birthday}) does not in the first million digits of pi")
