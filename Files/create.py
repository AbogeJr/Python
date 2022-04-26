msg = input("Enter a message: ")

with open('text.txt', 'w') as file:             #creates a 'text.txt' file if it doesn't already exist in dir
    file.write(msg)                             #ovewrites contetnts if it already exists