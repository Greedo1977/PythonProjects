# def greet_user(username):
#     print(username)
#
# greet_user("Madhu")
#
# def favourite_book(book_title):
#     print(f"My favourite book title is {book_title.title()}")
#
# favourite_book("dune")

# Keyword arguments
# def describe_pet(animal_type, pet_name):
#    #Display information about a pet.
#    print(f"\nI have a {animal_type}")
#    print(f"My {animal_type}'s name is {pet_name.title()}")
# describe_pet(animal_type='hamster', pet_name = 'harry')


# Default arguments
# def describe_pet(pet_name, animal_type='dog'):
#     # Display information about a pet.
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
#
#
# describe_pet("Harry")


# def make_shirt(text, size='Large'):
#     print(f"Size of shirt is {size} sentence to print \"{text}\"")
#
#
# make_shirt('Help, get me outta here!')
#
# def describe_city(city, country='UK'):
#     print(f"{city} is in {country}")
#
#
# describe_city('Reykjavik', 'Iceland')
# describe_city('London')
# describe_city('New York', 'USA')
# describe_city(country='India', city='Mumbai')

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#
#     return full_name
#
# # musician = get_formatted_name(first_name='Amadeus', last_name='mozart')
# # print(musician)
#
# print(get_formatted_name('John', 'Lee', 'Hooker'))
# print(get_formatted_name('Elvis', 'Presley'))


# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#
#     return person
#
#
# musician = build_person('Madhu', 'Mepani')
# print(musician)

def make_album(artist_name, album, number_songs = None):
    album= {'artist_name': artist_name, 'album': album}

    if number_songs:
        album['Songs'] = number_songs

    return album

# while True:
#     artist = input('Enter artist or quit(q): ')
#     if artist == 'q':
#         break
#
#     album = input('Enter album or quit(q): ')
#     if album == 'q':
#         break
#
#
#     print(f"{make_album(artist, album)}")

def greetings(names):
    for name in names:
        print(f"Hello {name}")

# print(make_album('Michael Jackson', 'Thriller'))
# print(make_album('Guns n Roses', 'Appetite for Destruction'))
# print(make_album('AC DC', 'Thunderstruck'))
# print(make_album('Beatles', 'Help', 20))


# unprinted_designs = ['Phone', 'robot pendant', 'dodecahedron']
# completed_designs= []
#
# def print_designs(unprinted_designs, completed_designs):
#     while unprinted_designs:
#         design = unprinted_designs.pop(0).title()
#         print(f"Printing {design}")
#
#         completed_designs.append(design)
#
# def show_completed(completed_designs):
#     print(f"Printed following {completed_designs}")
#
# print_designs(unprinted_designs[:], completed_designs)
# show_completed(completed_designs)

# messages = ['Hello', 'The year is 1999', 'The song is written by Prince']
# printed_messages = []
# def print_each_message(messages, printed_messages):
#     while messages:
#         message = messages.pop(0)
#         print(f"Printing message: {message}")
#         printed_messages.append(message)

#print_each_message(messages[: ], printed_messages)

#print(f"Contents of messages: {messages}, printed_messages: {printed_messages}")

# def make_pizza(size, *toppings):
#     print(f"Making a {size} inch pizza with following toppings - ")
#     for topping in toppings:
#         print(topping)
#
# make_pizza(12,'Pepper')
# make_pizza(21, 'Pepper', 'Olives')

def build_profiles(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    return user_info


user_profile = build_profiles("Madhusudan",
                              "Mepani",
                              location='Greenwich',
                              field='Mathematics',
                              age = 58)

def create_sandwich(*fillings):
    print(f"Your sandwich will have following fillings:")
    for filling in fillings:
        print(f"\t{filling}")

#create_sandwich("Cheese", "Mustard", "Tomato")
def car_desc(manufacturer, model, **desc):
    desc['manufacturer'] = manufacturer
    desc['model'] = model

    return desc

car_info = car_desc('Suburu',
                'Outback',
                    color='blue',
                    tow_package = True)

print(f"Car description: {car_info}")
