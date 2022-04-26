# def format_name(fname, lname):
#     name = f"{fname.title()} {lname.title()}"
#     return name

# username = format_name('john', 'doe')
# # print(username)


# # with optional parameter

# def format_name(fname, lname, mname = ''):
#     name = f"{fname.title()} {mname.title()} {lname.title()}"
#     return name

# username = format_name('john', 'doe')
# # print(username)

# username = format_name('john', 'doe', 'otieno')
# # print(username)

# # returning a dictionary

# def format_name(fname, lname, mname = ''):
#     name = {'first_name': fname.title(), 'middle_name': mname.title(), 'last_name': lname.title()}
#     return name

# name_dict = format_name('aloys', 'aboge', 'junior')
# # print(name_dict)

# cars = ['Ferrari', 'Mercedes', 'Audi']
# purchased_cars = []

# def purchase(cars):
#     while cars:
#         car = cars.pop()
#         print(f"Buying {car}...")
#         purchased_cars.append(car)

# def show_cars(cars):
#     print(f"My cars: {cars}")        

# purchase(cars[:])
# show_cars(sorted(cars))


# with Arbitrary arguments

# def make_pizza(*toppings):
#     print("Making a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"\t-{topping.title()}")

# make_pizza('pineapple', 'sausage', 'maccaroni')

# def sign_racer(*racers):
#     print('Mercedes Signing: ')

#     for racer in racers:
#         print(f"\t-{racer.title()}")

# sign_racer('Verstappen', 'Occon')

def create_profile(fname, lname, **profile):
    profile['f_name'] = fname
    profile['l_name'] = lname
    return profile

racer = create_profile('Esteban', 'Occon', car = 'Ferari', age = 22, contract = 'active')

print(racer)


