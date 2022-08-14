from generators.baseGens.slrv5 import slrv5
import random

def genFogOfWarBoard(json, seed):
	board = slrv5.genBoardSlrv5(json, seed)

	result = [None] * 25
	used = [False] * 25
	objectivePositions = [0] * 25
	positions = []
	random.seed(seed)
	start = random.randint(0, 24)
	used[start] = True
	positions.append(start)

	for i in range(25):
		random.shuffle(positions)
		currentPosition = positions.pop(0)
		objectivePositions[i] = currentPosition
		if currentPosition >= 5: # Up
			if not used[currentPosition - 5]:
				used[currentPosition - 5] = True
				positions.append(currentPosition - 5)
		if currentPosition % 5 != 4: # Right
			if not used[currentPosition + 1]:
				used[currentPosition + 1] = True
				positions.append(currentPosition + 1)
		if currentPosition < 20: # Down
			if not used[currentPosition + 5]:
				used[currentPosition + 5] = True
				positions.append(currentPosition + 5)
		if currentPosition % 5 != 0: # Left
			if not used[currentPosition - 1]:
				used[currentPosition - 1] = True
				positions.append(currentPosition - 1)

	for space in board:
		if space:
			dif = space["difficulty"]
			result[objectivePositions[dif - 1]] = {"name" : space["name"]}

	return result