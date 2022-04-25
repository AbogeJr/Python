responses = {}              #empty dictionary
poll_active = True          #flag

while poll_active:
    name = input("What is your name: ")
    dream = input("What do you want to do with your life: ")
    responses[name] = dream             #adss to dictionary

    poll = input("would you like someone else to take the poll (y/n)")
    if poll == 'n':
        poll_active =  False

for name, response in responses.items():
    print(f"{name.title()}'s dream is to {response}")        
