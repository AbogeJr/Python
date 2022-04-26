print("Give me two numbers, I'll divide them. Type 'q' to quit.")

while True:
    num_1 = input("Enter first number: ")
    if num_1 == 'q':
        break
    num_2 = input("Enter second number: ")
    if num_2 == 'q':
        break

    try:
        ans = int(num_1)/int(num_2)
    except ZeroDivisionError:
        print("Math Error: Division by Zero")
    else:
        print(f"Ans: {ans}")                
