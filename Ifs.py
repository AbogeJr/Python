employees = ['admin', 'John', 'Eren', 'Levi', 'Sasha', 'Mikasa']

for employee in employees:
    if employee == 'admin':
        print("Welcome back Boss!")
    else:    
        print(f"Hello {employee}. Get to work")

print("------------------------------------------------------------------------------------------")

employees = []
if employees:
    for employee in employees:
        if employee == 'admin':
            print("\nWelcome back Boss!")
        else:    
            print(f"Hello {employee}. Get to work")
else:
    print("We really need some bodies up in here")      

print("------------------------------------------------------------------------------------------")

age = 17
if age < 18:
    print("Enjoy your soda")   #output
elif age >= 18 and age < 25:
    print("Would you like a Heineken?")
else:
    print("Whiskey or Vodka?")

print("------------------------------------------------------------------------------------------")
# Ordinal Numbers

nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
    
print("------------------------------------------------------------------------------------------")