from name_function import formatName

print("Enter your names below: ('q' to quit)")

while True:
    first_name = input("Enter your First Name: ")
    if first_name == 'q':
        break
    last_name = input ("Enter your Last Name: ")
    if last_name == 'q':
        break
    full_name = formatName(first_name, last_name)
    print(f"\tFull name: {full_name}\n")