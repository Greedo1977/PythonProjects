
import random
from collections import Counter


rolls = []

for number in range(1_000_001):
    rolls.append(random.randrange(1,7))

frequencies = Counter(rolls)

print(frequencies)
