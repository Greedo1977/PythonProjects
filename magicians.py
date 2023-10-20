magicians = ["Paul daniels", "Tommy cooper", "David Copperfield", "Lance evans", "Ronaldo"]
footballers = ['Ronaldo', 'Messi']

for magician in magicians:
    print(f"That was a great trick {magician.title()}")
    print(f"Looking forward to the next trick, {magician.title()}\n")

print("Goodbye Magicians")

mf = magicians in footballers

print(mf)