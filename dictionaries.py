# Empty dictionary

# {} with k,v is dict, {} values is set, () is tuple, [] is list

dictionary = {'fav': 'Pizza', 'fav_1': 'Kichri', 'fav_2': 'Ice Cream'}
set_ = {'Pizza', 'Kichri', 'Ice Cream'}
tuple_1 = ('Pizza', 'Kichri', 'Ice Cream')
list_ = ['Pizza', 'Kichri', 'Ice Cream']


alien_0 = {}
alien_0['colour'] = 'Yellow'
alien_0['points'] = 5

alien_0['colour'] = 'Red'
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}

print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Remove Key/value pair
del alien_0['speed']
print(alien_0)


favourite_language = {
    'Jane': 'c',
    'peter': 'c++',
    'Sarah': 'pascal',
    'John':  'python',
    'Madhu': 'c++'
}

Chandni = {
    'Name': 'Chandni',
    'Last Name': 'Mepani',
    'Age': 26,
    'City': 'London'
}

Avnish = {
    'Name': 'Avnish',
    'Last Name': 'Mepani',
    'Age': 29,
    'City': 'London'
}

Shailesh = {
    'Name': 'Shailesh',
    'Last Name': 'Mepani',
    'Age': 34,
    'City': 'London'
}

print (Chandni['Name'])
print (Chandni['Last Name'])
print (Chandni['Age'])
print (Chandni['City'])

Glossary = {
    'Dictionary': 'In Python, a collection of key value pairs',
    'Tuple': 'A list that cannot change',
    'List': 'A collection of items in a particular order',
    'if': 'A conditional statement',
    'if-else': 'Similar to if statement, but the else statement allows you to define an action or set of actions to '
               'execute when if condition fails'
}

print(f"Dictionary Meaning\n\t{Glossary['Dictionary']}\n")
print(f"Tuple Meaning\n\t{Glossary['Tuple']}\n")
print(f"List Meaning\n\t{Glossary['List']}\n")
print(f"if Meaning\n\t{Glossary['if']}\n")
print(f"if-else Meaning\n\t{Glossary['if-else']}\n")

for key,value in Glossary.items():
    print(f"{key} Meaning\n\t{value}")

#Get Keys from dictionary
for term in Glossary.keys():
    print(term)

#Get Values from dictionary
for definition in Glossary.values():
    print(definition)

print('\n')

#Same as above
for term in Glossary:
    print(term)

#Associate key to dictionary
friends = ['John','Sarah']


for name, language in favourite_language.items():
    print(f"Hi {name.title()}")
    if name in friends:
        print(f"\tYour favourite language is {language.title()}")


#get function returns if cannot find key
print(favourite_language.get('erin', 'Hi Erin, you\'re not my friend'))

for unique_language in set(favourite_language.values()):
    print(f"Languages: {unique_language}")

#This is a set {} without key and only values is set. Set values must be unique
unique_food = {'Pizza', 'Pau Bhaji', 'Ice Cream', 'Pizza'}

rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yellow': 'china'}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

for river in rivers:
    print(f'River: {river.title()}')

for country in rivers.values():
    print(f'Country: {country.title()}')

people = ('John', 'Peter','Kevin', 'Paul', 'Sarah', 'Paul')
people_s = set(people)

for person in people_s:
    if person in set(favourite_language.keys()):
        print (f'Thank you {person.title()} for taking the poll')
    else:
        print(f'{person.title()} please take the poll')

#list of dictionaries
alien_0 = {'colour': 'green', 'points': 5, 'speed': 'slow'}
alien_1 = {'colour': 'yellow', 'points': 10, 'speed': 'medium'}
alien_2 = {'colour': 'red', 'points': 15, 'speed': 'fast'}


aliens = [alien_0, alien_1, alien_2]
print(aliens)

for alien in aliens:
    print(f"{alien['colour']}, {alien['points']}")

aliens = []

for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)

print('=====================\n')

pizza = {
    'crust': 'thick',
    'toppings': ['sweetcorn', 'olives']
}

print(f"Your crust is {pizza['crust']} with following toppings")
for topping in pizza['toppings']:
    print(topping)

favourite_languages = {
    'Janet': ['C', 'Rust'],
    'Richard': ['Pascal'],
    'Sarah': ['Java', 'C++', 'Python'],
    'Peter': ['Haskell','Scala']
}

for name, languages in favourite_languages.items():
    if (len(languages)) == 1:
        print(f"{name}'s favourite language is")
    else:
        print(f"{name}'s favourite languages are")
    for language in languages:
        print(f"\t{language}")

print('=====================\n')

people = [Chandni, Avnish, Shailesh]

for person in people:
    print(f"Name: {person['Name']}, Last Name:{person['Last Name']}, Age: {person['Age']}, City: {person['City']}")

print('=====================\n')

pet_0 = {'Kind': 'Cat', 'Owner': 'Peter', 'Age': 2, 'Name': 'Cybil'}
pet_1 = {'Kind': 'Dog', 'Owner': 'John', 'Age': 5, 'Name': 'Max'}
pet_2 = {'Kind': 'Mouse', 'Owner': 'Sarah', 'Age': 1, 'Name': 'Harry'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"{pet['Kind']}, {pet['Owner']}, {pet['Age']}, {pet['Name']}")

print('=====================\n')

person_1 = {'Name': 'Chandni', 'Favourite Places': ['Paris']}
person_2 = {'Name': 'Avnish', 'Favourite Places': ['NY', 'Dubai', 'Mauritius']}
person_3 = {'Name': 'Shailesh', 'Favourite Places': ['London', 'Sydney']}

favourite_places = {
    'Chandni': ['Paris'],
    'Avnish': ['NY', 'Dubai', 'Mauritius'],
    'Shailesh': ['London', 'Sydney']
}

for name, places in favourite_places.items():
    print(f"{name} your favourite places are ")
    for place in places:
        print(f"\t{place}")

print('=====================\n')

cities = {
    'London': {
        'Pop': 8_000_000,
        'Country': 'UK',
        'Fact': 'Capital of UK'
    },
    'New York': {
        'Pop': 9_000_000,
        'Country': 'USA',
        'Fact': 'Largest city in USA'
    },
    'Vatican City': {
        'Pop': 2_000,
        'Country': 'Vatican',
        'Fact': 'Smallest capital in world'
    }
}

for city, attributes in cities.items():
    print(f"City: {city}")
    print(f"\tPopulation: {attributes['Pop']}")
    print(f"\tCountry: {attributes['Country']}")
    print(f"\tFact: {attributes['Fact']}")



