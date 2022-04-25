prompt = "\nEnter something and I will Repeat it to you: "
prompt += "\nEnter 'quit' to exit. "

active = True

while active:
    msg = input(prompt)

    if msg == 'quit':
        active = False
    else:
        print(msg)    

print("---------------------------------------------------------------------")

unconfirmed_users = ['Jim', 'Pam', 'Dwight', 'Kevin', 'Andy']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"Confirming user: {user.title()}")
    confirmed_users.append(user)

print("\nConfirmed Users:")

for user in confirmed_users:
    print(f"\t{user}")




