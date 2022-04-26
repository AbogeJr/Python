from cars import Car, ElectricCar

mycar = Car('Toyota', 'Celica', 2020)
mycar.updateMileage(2000)
mycar.describeCar()

print("---------------------------------------------------------------------------")

tesla = ElectricCar('Tesla', 'S', 2021)
tesla.setBattery(75)
tesla.updateMileage(205)
tesla.describeCar()