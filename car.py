class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.colour = 'blue'

    def get_description_name(self):
        long_name = f"{self.year} {self.make} {self.model} {self.colour}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it")

    def set_odometer(self, odometer):
        self.odometer = odometer

    def increment_odometer(self, mileage):
        self.odometer += mileage

class Battery:

    def __init__(self, size):
        self.size = size

    def getBatterySize(self):
        return self.size



class ElectricCar(Car):

    def __init__(self, make, model, year, batterysize):
        super().__init__(make, model, year)
        self.battery = Battery(100)

    def describe_battery(self):
        print(f"This car has a battery size of {self.battery.getBatterySize()}-kwH battery")
