class Car:
    def __init__(self, manufacturer, model, yom):
        self.manufacturer = manufacturer
        self.model = model
        self.yom = yom
        self.mileage = 0

    def describeCar(self):
        print("Car Description:")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Year of Manufacture: {self.yom}")
        print(f"Mileage: {self.mileage}")    

    def updateMileage(self, miles):
        self.mileage += miles    

    def checkMileage(self):
        return self.mileage

class ElectricCar(Car):
    def __init__(self, manufacturer, model, yom):
        super().__init__(manufacturer, model, yom)
        self.battery_rating = 0

    def recharge(self):
        print(f"{self.manufacturer} {self.model} is recharging...")

    def describeCar(self):
        print("Electric Vehicle")
        super().describeCar()
        print(f"Battery Rating: {self.battery_rating}")

    def setBattery(self, rating):
        self.battery_rating = rating

    def getBatteryRating(self):
        return self.battery_rating


