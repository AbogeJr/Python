# Python Crash Course TIY Exercise 
print('--------------------------------------------------------------------------')
# 3-1

friends = ['Eren', 'Levi', 'Sasha', 'Mikasa']
for friend in friends:
    print(friend)

print('--------------------------------------------------------------------------')
# 3-2

for friend in friends:
    print(f"Good morning {friend}")

print('--------------------------------------------------------------------------')
# 3-3

cars = ['Mercedes Benz', 'Cupra Leone', 'Audi R6', 'Kia', 'Tesla']
print(f"I would like to own a {cars[-1]}")

print('--------------------------------------------------------------------------')
# 3-4

legends = ['Jordan Peterson', 'Albert Camus', 'Elon Musk']
for legend in legends:
    print(f"Hey {legend}! Come through!")

print('--------------------------------------------------------------------------')
# 3-5

dead = 'Albert Camus'
legends.remove(dead)

legends.insert(1, 'Lex Fridman')
print(f"{dead} won't be attending for obvious reasons")

for legend in legends:
    print(f"Hey {legend}! Come through!")

print('--------------------------------------------------------------------------')
# 3-8

destinations = ['Italy', 'London', 'Rwanda', 'Brasil', 'Germany']
print(destinations)
print(sorted(destinations))
print(destinations)
print(sorted(destinations, reverse=True))
print(destinations)


print('--------------------------------------------------------------------------')
# 3-9

print(f"I am inviting {len(legends)} people to dinner")


print('--------------------------------------------------------------------------')
# Numbers List Generation
even = []
for num in range(0, 11, 2):
    even.append(num)

print(even)

squares = []
for num in range(1, 11):
    square = num ** 2
    squares.append(square)

print(squares)

print('--------------------------------------------------------------------------')
# List Comprehension

cubes = [num ** 3 for num in range(1, 11)]
print(cubes)

print('--------------------------------------------------------------------------')
# List Slicing
racers = ['Ricciardo', 'Occon', 'Hammilton', 'Verstappen', 'Magnussen']
print("The first three racers are:")
print(racers[:3])
print("The Last three racers are:")
print(racers[-3:])

print('--------------------------------------------------------------------------')
# List Copying
my_devices = ['Charger', 'Powerbank', 'Phone']
her_devices = my_devices[:]

print("Before Copy:")
print(my_devices)
print(her_devices)

my_devices.append('Laptop')
print("After Copy:")
print(my_devices)
print(her_devices)

print('--------------------------------------------------------------------------')
# Tuples
specials = ('Samosa', 'Caviar', 'Lobster')
print(specials)

specials = ('Mtura', 'Caviar', 'Lobster')
print(specials)
