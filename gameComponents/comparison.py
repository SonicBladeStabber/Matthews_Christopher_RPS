from gameComponents import gameVars

def PvC(test):
	print(test)
	if (gameVars.CPU == gameVars.player):
		print("tie! Try again")

	elif (gameVars.player == "rock"):
		if (gameVars.CPU == "paper"):
			print("you loose!")
			gameVars.playerLives = gameVars.playerLives - 1

		else:
			print("you win!")
			gameVars.computerLives = gameVars.computerLives - 1


	elif (gameVars.player == "paper"):
		if (gameVars.CPU == "scissors"):
			print("you loose!")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("you win!")
			gameVars.computerLives = gameVars.computerLives - 1


	elif (gameVars.player == "scissors"):
		if (gameVars.CPU == "rock"):
			print("you loose!")
			gameVars.playerLives = gameVars.playerLives - 1
		else:
			print("you win!")
			gameVars.computerLives = gameVars.computerLives - 1
