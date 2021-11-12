import time
from gameComponents import WinLose, gameVars, comparison
from random import randint
#----------------------------------------


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:

	gameVars.player = input("Choose your weapon: rock, paper or scissors [Or type end to quit]: ")
	gameVars.CPU = gameVars.weapon[randint(0, 2)]

	print("player chose: " + gameVars.player)
	time.sleep(0.3)

	if (gameVars.player == "end"):
		exit()

	print("computer chose: " + gameVars.CPU)

	time.sleep(1)

	comparison.PvC(test = 1)

	

	print("player lives: " + str(gameVars.playerLives))
	print("computer lives: " + str(gameVars.computerLives))


	if gameVars.playerLives == 0:
		WinLose.WinOrLose("lost")

	elif gameVars.computerLives == 0:
		WinLose.WinOrLose("won")
#		gameVars.player = False

	gameVars.player = False

	time.sleep(1)

	print("------------------------------------------------------------------")
