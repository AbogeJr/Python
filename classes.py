from unicodedata import name


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking")    


doggy = Dog('Lucky', 'German Sheppherd')


# print(f"{doggy.name} is a {doggy.breed}")
# doggy.bark()

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} is a fine restaurant that specializes in {self.cuisine} cuisines")

    def open_restaurant(self):
        print(f"{self.name} is open for business!") 

res1 = Restaurant('The Peninsuala', 'Italian')

# res1.describe_restaurant()
# res1.open_restaurant()

res2 = Restaurant('Festo\'s', 'Kenyan')

# res2.describe_restaurant()
# res2.open_restaurant()


class User:
    def __init__(self, username, fname, lname, age, location, profession):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.age = age
        self.location = location
        self.profession = profession

    def describe_user(self):
        print(f"User profile for: {self.username.title()}")
        print(f"\t-First Name: {self.fname.title()}")
        print(f"\t-Last Name: {self.lname.title()}")
        print(f"\t-Age: {self.age}")
        print(f"\t-Location: {self.location.title()}")
        print(f"\t-Profession: {self.profession.title()}")


usr = User('aboge', 'aloys', 'aboge', 21, 'nairobi', 'software engineer' )
usr.describe_user()