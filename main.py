import time
from gameComponents import WinLose, gameVars
from random import randint
#----------------------------------------


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
	gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
	CPU = gameVars.weapon[randint(0, 2)]

	print("player chose: " + gameVars.player)
	time.sleep(0.3)
	print("computer chose: " + CPU)

	time.sleep(1)

	if (CPU == gameVars.player):
		print("tie! Try again")

	elif (gameVars.player == "rock"):
		if (CPU == "paper"):
			print("you loose!")
			gameVars.playerLives = gameVars.playerLives - 1

		else:
			print("you win!")
			gameVars.computerLives = gameVars.computerLives - 1


	elif (gameVars.player == "paper"):
		if (CPU == "scissors"):
			print("you loose!")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("you win!")
			gameVars.computerLives = gameVars.computerLives - 1


	elif (gameVars.player == "scissors"):
		if (CPU == "rock"):
			print("you loose!")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("you win!")
			gameVars.computerLives = gameVars.computerLives - 1

	print("player lives: " + str(gameVars.playerLives))
	print("computer lives: " + str(gameVars.computerLives))


	if gameVars.playerLives == 0:
		WinLose.WinOrLose("lost")

	elif gameVars.computerLives == 0:
		WinLose.WinOrLose("won")
		gameVars.player = False

	gameVars.player = False

	time.sleep(1)

	print("------------------------------------------------------------------")
