import xml.etree.ElementTree as ET
from time import sleep
import random
import os

class AdventureGame:
	def __init__(self):
		self.loadPrompts()
		self.initialPlayerHealth = 3
		self.playerHealth = self.initialPlayerHealth
		self.playerName = "Player 1"
		self.playerScore = 0
		self.currentRealm = 1
		self.currentStage = 1
		self.numberOfStages = len(self.promptsDict)
		self.validInputs = ["1", "2"]

	def loadPrompts(self):
		tree = ET.parse('prompts.xml')
		xmlRoot = tree.getroot()
		self.promptsDict = {}
		for stage in xmlRoot:
			promptList = []
			outcomePromptList = []
			for prompt in stage:
				promptText = prompt.find("promptText").text
				promptList.append(promptText)
				option1SuccessPromptText = prompt.find("option1Success").text
				option2SuccessPromptText = prompt.find("option2Success").text
				option1FailPromptText = prompt.find("option1Fail").text
				option2FailPromptText = prompt.find("option2Fail").text
				outcomePromptList.append((option1SuccessPromptText, option2SuccessPromptText, option2FailPromptText, option1FailPromptText))
			self.promptsDict[stage.tag] = {"prompts": promptList, "outcomePrompts": outcomePromptList}
		self.stagePrompts = []
		self.stageOutcomePrompts = []
		for key in self.promptsDict:
			self.stagePrompts.append(self.promptsDict[key]["prompts"])
			self.stageOutcomePrompts.append(self.promptsDict[key]["outcomePrompts"])

	def getUserChoice(self):
		print("\n " + self.playerName + "\033[96m > \033[0m", end="")
		choice = input("")
		while choice not in self.validInputs:
			print("\033[96m >\033[0m Invalid choice, choose 1 or 2")
			choice = input("\n " + self.playerName + "\033[96m > \033[0m")
		return int(choice)

	def waitUntilUserIsReady(self):
		print("\033[96m > \033[0m Are you ready to enter the adventure realm, " + self.playerName + "?")
		choice = input(" " + self.playerName + "\033[96m > \033[0m")
		while choice.lower() != "yes":
			print("\n\033[96m > \033[0m Type 'yes' to begin.")
			choice = input(" " + self.playerName + "\033[96m > \033[0m")

	def outputDeadPlayerPrompt(self):
		print("\033[96m >\033[91m You have died.\033[0m ")
		sleep(2)
		return self.getRestartChoice()

	def setNumberOfLives(self, numLives):
		if numLives > self.numberOfStages:
			numLives = self.numberOfStages
		self.initialPlayerHealth = numLives
		self.playerHealth = self.initialPlayerHealth

	def getPlayerName(self):
		name = input("\033[96m > \033[0m Enter player name: ")
		self.playerName = name

	def fetchCurrentStage(self, stageNum):
		self.currentStage = stageNum + 1
		promptChoice = random.choice(range(len(self.stagePrompts[stageNum])))
		prompt = self.stagePrompts[stageNum][promptChoice]
		winningChoice = random.randint(0, 1)
		losingChoice = winningChoice + 2
		winningPrompt = self.stageOutcomePrompts[stageNum][promptChoice][winningChoice]
		losingPrompt = self.stageOutcomePrompts[stageNum][promptChoice][losingChoice]
		stageInfo = {
			"prompt": prompt,
			"winner": winningChoice + 1,
			"winningPrompt": winningPrompt,
			"losingPrompt": losingPrompt
		}
		return stageInfo

	def outputResult(self, stageInfo, choice):
		if stageInfo["winner"] == choice:
			print("\033[96m > \033[0m" + stageInfo["winningPrompt"])
			sleep(2)
			return True
		else:
			print("\033[96m > \033[0m" + stageInfo["losingPrompt"])
			sleep(2)
			return False

	def getRestartChoice(self):
		print("\033[96m >\033[0m Would you like to play Again? Enter 'yes' or 'no'.")
		playAgain = input(" " + self.playerName + "\033[96m >\033[0m ")
		while playAgain.lower() not in ["yes", "no"]:
			print("\033[96m >\033[0m Enter 'yes' or 'no'.")
			playAgain = input(" " + self.playerName + "\033[96m >\033[0m ")
		return playAgain.lower() == "yes"

	def loseHealth(self, numLives):
		self.playerHealth -= numLives

	def incrementScore(self):
		self.playerScore += 1
		self.currentRealm += 1

	def playerIsDead(self):
		return self.playerHealth < 1

	def outputPrompt(self, stageInfo):
		print("\033[96m >\033[0m " + stageInfo["prompt"])

	def outputPlayerStatus(self):
		print("-------------------------------------------")
		print("\033[96m > \033[0m Stage " + str(self.currentStage) + "/" + str(self.numberOfStages) +
		      ", Score: " + str(self.playerScore) + ", Health: " + "\u2764\uFE0F" * self.playerHealth)

	def outputIntro(self):
		os.system('clear')
		print("\033[92m-- CSE03's Adventure Realm --\033[0m")
		print("\033[96m > \033[0m Welcome to our adventure realm! In this world, you will make choices which decide your fate. Make the wrong choice, and it could be your last. Find your way through the realm and you'll earn a point. Lets see how high of a score you can earn... Good luck!\n")

	def outputNewRealmPrompt(self):
		os.system('clear')
		print("\033[96m " + self.playerName + " enters the Adventure Realm ...\033[0m")

	def resetPlayerHealth(self):
		self.playerHealth = self.initialPlayerHealth

	def outputSuccessPrompt(self):
		print("\033[96m >\033[92m Congratulations, you made it through the adventure realm!\033[0m ")
		sleep(2)
		print("\033[96m > \033[0m Your score is now at " + str(self.playerScore) + ". Generating a new realm...")
		sleep(3)
