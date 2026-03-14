class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model},Year:{self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, body_style):
        super().__init__(make,model,year)
        self.body_style = body_style

class ElectricalCar(Car):
    def __init__(self, make, model, year, body_style, battery_capacity):
        super().__init__(make, model, year, body_style)
        self.battery_capacity = battery_capacity
    def charger(self):
        print("Charging the electric car")

tesla = ElectricalCar("Tesla", "Cybertruck", 2023, "triangular", 122)
tesla.display_info()
print(tesla.body_style)
print(tesla.battery_capacity)
tesla.charger()
