from cars import Car, ElectricCar

mycar = Car('Toyota', 'Celica', 2020)
mycar.update_mileage(2000)
mycar.describe_car()

print("---------------------------------------------------------------------------")

tesla = ElectricCar('Tesla', 'S', 2021)
tesla.set_battery(75)
tesla.update_mileage(205)
tesla.describe_car()