
class Company:
    def __init__(self, name, industry, employees=100000):
        self.name = name
        self.industry = industry
        self.employees = employees

    def change_employees(self, delta_employees = 10_000):
        self.employees += delta_employees

        