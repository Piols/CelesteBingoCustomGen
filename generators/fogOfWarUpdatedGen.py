from generators.baseGens.slrv5 import slrv5
import random

def genFogOfWarUpdatedBoard(json, seed):
	board = slrv5.genBoardSlrv5(json, seed)

	fullRevealCutoff = 20

	result = [None] * 25
	used = [False] * 25
	objectivePositions = [0] * 25
	positions = []
	random.seed(seed)

	visited = [False] * 25

	def clearVisited():
		for i in range(25):
			visited[i] = False

	def countVisited():
		res = 0
		for i in range(25):
			if (visited[i]): res += 1
		return res

	def DFS(x):
		visited[i] = True
		if x >= 5: # Up
			if not used[x - 5]:
				used[x - 5] = True
				positions.append(x - 5)
		if x % 5 != 4: # Right
			if not used[x + 1]:
				used[x + 1] = True
				positions.append(x + 1)
		if x < 20: # Down
			if not used[x + 5]:
				used[x + 5] = True
				positions.append(x + 5)
		if x % 5 != 0: # Left
			if not used[x - 1]:
				used[x - 1] = True
				positions.append(x - 1)

	for i in range (fullRevealCutoff, 25):
		used[i] = True

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
			result[objectivePositions[dif - 1]] = {"name" : f"{space['name']} $" if dif == 1 else space["name"]}

	return result