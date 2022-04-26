import random as r

'''Spin The Bottle Console Game'''
print("---------------------------------SPIN THE BOTTLE-----------------------------------")

players = []
no_of_players = int(input("How many players? "))

for entry in range(0, no_of_players):
    entry = input(f"Enter Player Name: ")
    players.append(entry)


print("Bottle Spinning...")

print(f"----->{r.choice(players)}")