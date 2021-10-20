import time
from random import randint
#----------------------------------------
weapon = ["rock", "paper", "scissors"]
#----------------------------------------
# player defines which choise the player chooses via input
player = input("Choose your weapon: rock, paper or scissors:")

time.sleep(0.5)

CPU = weapon[randint(0, 2)]

playerLives = 5
computerLives = 5

print("player chose: " + player)
time.sleep(0.5)
print("computer chose: " + CPU)

time.sleep(1.5)

if (CPU == player):
	print("tie! Try again")

elif (player == "rock"):
	if (CPU == "paper"):
		print("you loose!")
		playerLives = playerLives - 1

	else:
		print("you win!")
		computerLives = computerLives - 1


elif (player == "paper"):
	if (CPU == "scissors"):
		print("you loose!")
		playerLives = playerLives - 1
	else:
		print("you win!")
		computerLives = computerLives - 1


elif (player == "scissors"):
	if (CPU == "rock"):
		print("you loose!")
		playerLives = playerLives - 1
	else:
		print("you win!")
		computerLives = computerLives - 1

print("player lives: " + str(playerLives))
print("computer lives: " + str(computerLives))
time.sleep(3)
