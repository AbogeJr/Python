import json


filename = 'profile.json'


try:
    with open(filename) as f:
        user = json.load(f)   
except FileNotFoundError:
    username = input("Enter a username: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We will remember you {username}")  
else:
    print(f"Welcome back {user}")
