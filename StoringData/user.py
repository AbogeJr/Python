import json

def getUsername():
    filename = 'profile.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = setUsername()
    else:
        return username            


def setUsername():
    filename = 'profile.json'
    username = input("Enter a username: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greetUser():
    username = getUsername()
    if username:
        print(f"Welcome back {username}!")
    else:
        username = setUsername()
        print(f"We will remember you {username}")    


greetUser()