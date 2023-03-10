####################
#----) Import (----#
####################
import replit
import random
import time
############################
#----) Space function (----#
############################
def space(lines):
	for i in range(lines):
		print(" ")
####################
#----) Task I (----#
####################

def menu(): # Working
	print("---------------")
	print("#Treasure Hunt#")
	print("---------------")

	print("1. Play Game")
	print("2. Exit")

	selection = int(input("Enter the corresponding number for your option: "))

	v = False
	while not v:
		replit.clear()
		if selection == 1:
			v = True
			size = int(input("What size do you want your map to be?: "))
			numOfBandits = int(input("How many bandits do you want to have?: "))
			numOfTreasure = int(input("How much treasure do you want to have?: "))
			map = generateMap(size, numOfBandits, numOfTreasure)
			display(map, None, None, 0, numOfBandits, numOfTreasure)
			move(map, numOfTreasure, numOfBandits)
		elif selection == 2:
			exit()
		
#######################
#----) Task II  (----#
#######################

def generateMap(size, numOfBandits, numOfTreasure): # Working
	print("##############")
	print("Map generation")
	print("##############")
	space(1)
	map = []
	for i in range(size):
		map.append([])
		for j in range(size):
			map[i].append(0)
	map[size-1][0] = 1 # player
	for i in range(numOfBandits): # bandits
		placed = False
		while not placed:
			xPos = random.randint(0, size-1)
			yPos = random.randint(0, size-1)
			if map[xPos][yPos] == 0:
				map[xPos][yPos] = 2
				placed = True
		
	for i in range(numOfTreasure): # treasure
		placed = False
		while not placed:
			xPos = random.randint(0, size-1)
			yPos = random.randint(0, size-1)
			if map[xPos][yPos] == 0:
				map[xPos][yPos] = 3
				placed = True
	return map

#######################
#----) Task III (----##
#######################
#----) AND (----#######
#######################
#----) TASK VIII (----#
#######################
	
def display(map, currentX, currentY, totalCoins, totalTreasure, totalBandits): # working
	for i in range(len(map)):
		line = ""
		for j in range(len(map)):
			if map[i][j] == 1:
				line += (" " + "1")
			else:
				line += (" " + "?")
		print(line)
	'''
	for i in range(len(map)):
		print(map[i])
	'''
	space(1)
	print(f"Current x position: {currentX}	Current y position: {currentY}")
	print(f"Total coins: {totalCoins}")
	print(f"Total treasure chests: {totalTreasure}")
	print(f"Total bandits: {totalBandits}")
	space(1)
	return map

######################
#----) Task III (----#
######################
#----) AND (----######
######################
#----) Task IV (----##
######################
#----) AND (----######
######################
#----) TASK VI (----##
######################	
def move(map, numOfTreasure, numOfBandits):
	totalTreasure = numOfTreasure 
	totalBandits = numOfBandits
	totalCoins = 0
	visitedTreasure = []
	banditList = []
	currentY, currentX = 7,0

	currentmoveValue = map[currentY][currentX]

	condition = input("Do you want to play? [Y/n]: ")
	while condition.lower() in ['Y', 'y']:

		y = int(input("How many do you want to move in the y direction? Positive for up and negative for down: "))
		x = int(input("How many do you want to move in the x direction? Positive for right and negative for left: "))

		if currentmoveValue == 0:
			map[currentY][currentX] = 0
		elif currentmoveValue == 1:
			map[currentY][currentX] = 0
		elif currentmoveValue == 2:
			map[currentY][currentX] = 2
		elif currentmoveValue == 3:
			map[currentY][currentX] = 3
		else:
			pass
			
		currentPos = [currentY, currentX]
		currentY -= y
		currentX += x
		currentmoveValue = map[currentY][currentX]

		if visitedTreasure != []:
			for i in range(len(visitedTreasure)):
				if visitedTreasure[i][0] == currentY and visitedTreasure[i][1] == currentX:
					previouslyVisited = True
		else:
			previouslyVisited = False
			
		if banditList != []:
			map[banditList[0][0]][banditList[0][1]] = 2
			banditList.pop(0)
			display(map, currentX, currentY, totalCoins, totalTreasure, totalBandits)

		if currentmoveValue == 2:
			print("Bandit!")
			totalCoins = 0
			map[currentY][currentX] = 1
			display(map, currentX, currentY, totalCoins, totalTreasure, totalBandits)
			map[currentY][currentX] = 2
		if map[currentY][currentX] == 3 and previouslyVisited:
			print("Previously visited")
			totalCoins += 10
			currentPos = [currentY, currentX]
			banditList.append(currentPos)
			totalTreasure -= 1
			totalBandits += 1
			map[currentY][currentX] = 1
			display(map, currentX, currentY, totalCoins, numOfTreasure, totalBandits)
		if map[currentY][currentX] == 3 and previouslyVisited == False:
			print("Not previously visited")
			currentPos = [currentY, currentX]
			totalCoins += 10
			visitedTreasure.append(currentPos) 
			map[currentY][currentX] = 1
			display(map, currentX, currentY, totalCoins, totalTreasure, totalBandits)
			map[currentY][currentX] = 3
		if currentmoveValue == 0:
			map[currentY][currentX] = 1
			display(map, currentX, currentY, totalCoins, totalTreasure, totalBandits)
			
		previouslyVisited = False

		if map[currentY][currentX] == 3 and previouslyVisited:
			print("Previously visited 2")
			map[currentY][currentX] = 2
			
		checkWin(totalCoins, totalTreasure)
		condition = input("Do you want to play again? [Y/n]: ")

######################
#----) Task VII (----#
######################

def checkWin(totalCoins, totalTreasure):
	if totalTreasure <= 0 and totalCoins <= 100:
		print("You lose!")
		time.sleep(2)
		replit.clear()
		menu()
	if totalTreasure > 0 and totalCoins >= 100:
		print("You win!")
		time.sleep(2)
		replit.clear()
		menu()
		
def main():
	menu()

if __name__ == '__main__':
	main()
