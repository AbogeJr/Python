class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Employee class instatiated!")

    def describe(self):
        print("Employee details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")    


class Waiter(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
        print("Waiter class instantiated!")

    def describe(self):
        super().describe()
        print(f"Department: {self.department}")    


emp = Employee('Eren', 24)
wtr = Waiter('Sasha', 22, 'Kitchen')
wtr.describe()
emp.describe()