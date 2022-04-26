class Car:
    def __init__(self, manufacturer, model, yom):
        self.manufacturer = manufacturer
        self.model = model
        self.yom = yom
        self.mileage = 0

    def describe_car(self):
        print("Car Description:")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Year of Manufacture: {self.yom}")
        print(f"Mileage: {self.mileage}")    

    def update_mileage(self, miles):
        self.mileage += miles    

    def check_mileage(self):
        return self.mileage

class ElectricCar(Car):
    def __init__(self, manufacturer, model, yom):
        super().__init__(manufacturer, model, yom)
        self.battery_rating = 0

    def recharge(self):
        print(f"{self.manufacturer} {self.model} is recharging...")

    def describe_car(self):
        print("Electric Vehicle")
        super().describe_car()
        print(f"Battery Rating: {self.battery_rating}")

    def set_battery(self, rating):
        self.battery_rating = rating

    def get_battery_rating(self):
        return self.battery_rating


