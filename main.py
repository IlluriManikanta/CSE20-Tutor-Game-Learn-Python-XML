from AdventureGame import AdventureGame
from time import sleep

def runGame():
	game = AdventureGame()
	game.setNumberOfLives(3)

	game.outputIntro()
	game.getPlayerName()
	game.waitUntilUserIsReady()

	while(True):
		game.outputNewRealmPrompt()

		for stage in range(game.numberOfStages):
			stageInfo = game.fetchCurrentStage(stage)
			game.outputPlayerStatus()
			game.outputPrompt(stageInfo)
			choice = game.getUserChoice()
			winner = game.outputResult(stageInfo, choice)

			if (winner == False):
				game.loseHealth(2)

			if(game.playerIsDead()):
				game.outputPlayerStatus()
				restart = game.outputDeadPlayerPrompt()
				if (restart):
					runGame()
				else:
					exit()

		game.outputPlayerStatus()
		game.resetPlayerHealth()
		game.incrementScore()
		game.outputSuccessPrompt()

if __name__ == '__main__':
	runGame()
