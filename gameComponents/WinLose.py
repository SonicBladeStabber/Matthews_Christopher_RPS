from gameComponents import gameVars
import time

def WinOrLose(status):
	print("you " + status)

	choice = input("do you want to play again? (y/n): ")

	if choice == "n":
		print("========== see ya! (looser) ==========")
		time.sleep(3)
		exit()
	elif choice == "y":
		gameVars.playerLives = 5
		gameVars.computerLives = 5
		gameVars.player = False
