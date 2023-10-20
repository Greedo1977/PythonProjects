from car import Car, ElectricCar



my_new_car = Car('ford', 'Escort', '1983')
my_new_car.set_odometer(50000)
print (my_new_car.get_description_name())
my_new_car.read_odometer()

my_electric_car = ElectricCar('Nissan', 'Leaf', '2020', 40)

print(my_electric_car.get_description_name())
my_electric_car.describe_battery()

# class Restaurant:
#
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cusine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"This restaurant - {self.name} - is of type {self.cusine_type}")
#
#     def open_restaurant(self):
#         print(f"{self.name} restaurant is open")
#
#
# class IceCreamStand(Restaurant):
#
#     def __init__(self, name, cuisine_type):
#         super().__init__(name, cuisine_type)
#
#         self.flavours = ['Cookies n Creme', 'Strawberry', 'Vanilla']
#
#     def getFlavours(self):
#         for flavour in self.flavours:
#             print(f'Flavour {flavour.title()}')
#
# ice_cream_stand = IceCreamStand('Baskins', "Ice Cream Parlour")
# ice_cream_stand.open_restaurant()

class User:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name} Gender: {self.gender} Age: {self.age}")

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show(self):
        print("This user can do following")
        for privilege in self.privileges:
            print(f"\t{privilege}")



class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges(['Can delete post', 'Can add user', 'Can delete user', 'Can modify user'])



Madhu = Admin("Madhu", "Mepani", "Male", 58)
Madhu.privileges.show()