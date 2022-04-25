developer = {}

developer['salary'] = 50_000
developer['hours'] = 40
developer['goal'] = 'FAANG'

developer['salary'] = 10_000
developer['hours'] = 80
developer['goal'] = 'Startup'

print(developer)

print("----------------------------------------------------------------")

languages = {
    'sarah' : 'Spanish',
    'jon' : 'Chinese',
    'jane' : 'Korean'
}

for k, v in languages.items():
    print(f"{k.title()}'s favourite language is {v}\n")

print("------------------------------------------------------------------------------------------")

# List of Aliens

aliens = []

for alien in range(1, 31):
    alien = {'color' : 'green', 'speed' : 'slow', 'points' : '5'}
    aliens.append(alien)

for alien in aliens[:5]:
    print(alien)

print(f"{len(aliens)} aliens have been created") 

print("------------------------------------------------------------------------------------------")

users = {
    'aaboge' : {
        'fname': 'Aloys',
        'lname': 'Aboge',
        'location': 'Kisumu',
        'stack': ['Python', 'java', 'javascript']
    },
    'jdoe': {
        'fname': 'John',
        'lname': 'Doe',
        'location': 'Vietnam',
        'stack': ['Wordpress', 'PHP']
    }
}

for user, info in users.items():
    username = user
    name = f"{info['fname']} {info['lname']}"
    location = info['location']
    stack = info['stack']

    print(f"Username: {username.lower()}")
    print(f"\tName: {name}")
    print(f"\tLocation: {location}")
    print(f"Tech Stack:")
    for data in stack:
        print(f"\t{data}")
    print("\n\n")    

print("------------------------------------------------------------------------------------------")
