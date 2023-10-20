players = ["Charles", "Elizabeth", "Henry", "Edward", "James"]


favourite_foods = ["pizza","ice cream", "pau bhaji", "Bhajia", "black eye beans"]

for food in favourite_foods[0:3]:
    print(f"My favourite foods is {food}")


print(f"Three items from list are {favourite_foods[1:4]}")
print(f"Last three items from list are {favourite_foods[:2]}")


chandni_favorite = favourite_foods[:]

print(f"favourite foods init {favourite_foods}")
print(f"chandni favourite foods init {chandni_favorite}")
print("\n")
favourite_foods.append("dal")
chandni_favorite.append("kichri")

print(f"favourite foods after {favourite_foods}")
print(f"chandni favourite foods after {chandni_favorite}")

chandni_favourite = favourite_foods

print(f"Chandni favourite foods {chandni_favourite}")

