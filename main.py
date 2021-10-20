import time
from random import randint
#----------------------------------------
weapon = ["rock", "paper", "scissors"]
#----------------------------------------
# player defines which choise the player chooses via input
player = input("Choose your weapon: rock, paper or scissors:")

time.sleep(0.5)

CPU = weapon[randint(0, 2)]

print("player chose: " + player)
time.sleep(0.5)
print("computer chose: " + CPU)

time.sleep(1.5)

if (CPU == player):
	print("tie! Try again")

elif (player == "rock"):
	if (CPU == "paper"):
		print("you loose!")
	else:
		print("you win!")


elif (player == "paper"):
	if (CPU == "scissors"):
		print("you loose!")
	else:
		print("you win!")


elif (player == "scissors"):
	if (CPU == "rock"):
		print("you loose!")
	else:
		print("you win!")

time.sleep(3)
