
class Person:
    def __init__(self, name, age):      #constructor
        self.name = name;               #self refers to the instantiated object
        self.age = age;                     

p1 = Person("Aloys", 20)
txt = "Name: {} \nAge: {}" 
print(txt.format(p1.name, p1.age))      #string formatting

