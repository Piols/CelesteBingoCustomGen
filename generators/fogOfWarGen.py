import random

dist1 = [[5, 1], [0, 6, 2], [1, 7, 3], [2, 8, 4], [3, 9], [0, 10, 6], [5, 1, 11, 7], [6, 2, 12, 8], [7, 3, 13, 9], [8, 4, 14], [5, 15, 11], [10, 6, 16, 12], [11, 7, 17, 13], [12, 8, 18, 14], [13, 9, 19], [10, 20, 16], [15, 11, 21, 17], [16, 12, 22, 18], [17, 13, 23, 19], [18, 14, 24], [15, 21], [20, 16, 22], [21, 17, 23], [22, 18, 24], [23, 19]]
dist2 = [[10, 6, 2], [5, 11, 7, 3], [0, 6, 12, 8, 4], [1, 7, 13, 9], [2, 8, 14], [15, 1, 11, 7], [0, 10, 16, 2, 12, 8], [5, 1, 11, 17, 3, 13, 9], [6, 2, 12, 18, 4, 14], [7, 3, 13, 19], [0, 20, 6, 16, 12], [5, 15, 1, 21, 7, 17, 13], [10, 6, 16, 2, 22, 8, 18, 14], [11, 7, 17, 3, 23, 9, 19], [12, 8, 18, 4, 24], [5, 11, 21, 17], [10, 20, 6, 12, 22, 18], [15, 11, 21, 7, 13, 23, 19], [16, 12, 22, 8, 14, 24], [17, 13, 23, 9], [10, 16, 22], [15, 11, 17, 23], [20, 16, 12, 18, 24], [21, 17, 13, 19], [22, 18, 14]]
dist3 = [[15, 11, 7, 3], [10, 16, 12, 8, 4], [5, 11, 17, 13, 9], [0, 6, 12, 18, 14], [1, 7, 13, 19], [20, 16, 2, 12, 8], [15, 21, 17, 3, 13, 9], [0, 10, 16, 22, 18, 4, 14], [5, 1, 11, 17, 23, 19], [6, 2, 12, 18, 24], [1, 21, 7, 17, 13], [0, 20, 2, 22, 8, 18, 14], [5, 15, 1, 21, 3, 23, 9, 19], [10, 6, 16, 2, 22, 4, 24], [11, 7, 17, 3, 23], [0, 6, 12, 22, 18], [5, 1, 7, 13, 23, 19], [10, 20, 6, 2, 8, 14, 24], [15, 11, 21, 7, 3, 9], [16, 12, 22, 8, 4], [5, 11, 17, 23], [10, 6, 12, 18, 24], [15, 11, 7, 13, 19], [20, 16, 12, 8, 14], [21, 17, 13, 9]]

distPenalty = [0, 2, 1, 0]
objectivePackSize = 3
fullRevealCutoff = 20

def getObjectives(json, seed, objPos):
	random.seed(seed)

	board = [None] * 25
	permutation = [0] * 25
	for i in range(25):
		permutation[i] = i
	random.shuffle(permutation)

	for dif in permutation:
		bestObjectives = []
		bestScore = 1e9
		for objective in json[dif]:
			currentScore = 0
			for neigh in dist1[objPos[dif]]:
				if board[neigh]:
					for myType in objective['types']:
						for theirType in board[neigh]['types']:
							if myType == theirType:
								currentScore += distPenalty[1]
			for neigh in dist2[objPos[dif]]:
				if board[neigh]:
					for myType in objective['types']:
						for theirType in board[neigh]['types']:
							if myType == theirType:
								currentScore += distPenalty[2]
			for neigh in dist3[objPos[dif]]:
				if board[neigh]:
					for myType in objective['types']:
						for theirType in board[neigh]['types']:
							if myType == theirType:
								currentScore += distPenalty[3]
			if currentScore < bestScore:
				bestObjectives = []
				bestScore = currentScore
			if currentScore <= bestScore:
				bestObjectives.append(objective)
		random.shuffle(bestObjectives)
		bestObjectives[0]["difficulty"] = dif + 1
		board[objPos[dif]] = bestObjectives[0]

	return board



def genFogOfWarBoard(json, seed):
	result = []
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
			if visited[i]:
				res += 1
		return res

	def DFS(x):
		visited[x] = True
		if x >= 5: # Up
			if not visited[x - 5]:
				visited[x - 5] = True
				if not used[x - 5]:
					DFS(x - 5)
		if x % 5 != 4: # Right
			if not visited[x + 1]:
				visited[x + 1] = True
				if not used[x + 1]:
					DFS(x + 1)
		if x < 20: # Down
			if not visited[x + 5]:
				visited[x + 5] = True
				if not used[x + 5]:
					DFS(x + 5)
		if x % 5 != 0: # Left
			if not visited[x - 1]:
				visited[x - 1] = True
				if not used[x - 1]:
					DFS(x - 1)


	def BFS(x):
		dist = [-1] * 25
		dist[x] = 0
		queue = [x]
		while len(queue) > 0:
			pos = queue[0]
			queue.pop(0)
			for neigh in dist1[pos]:
				if not used[neigh] and dist[neigh] == -1:
					dist[neigh] = dist[pos] + 1
					queue.append(neigh)
		return max(dist)

	def okTile(x):
		if used[x]:
			return False
		used[x] = True
		clearVisited()
		for i in range(25):
			if not used[i]:
				DFS(i)
				break
		used[x] = False
		return countVisited() == 25

	hardObjectives = []
	for i in range(fullRevealCutoff, 25):
		hardObjectives.append(i)
	random.shuffle(hardObjectives)

	for obj in hardObjectives:
		position = random.randint(0, 24)
		while not okTile(position):
			position = random.randint(0, 24)
		used[position] = True
		objectivePositions[obj] = position

	startCandidates = []
	smallestDist = 10
	for i in range(25):
		if not used[i]:
			maxDist = BFS(i)
			if maxDist < smallestDist:
				smallestDist = maxDist
				startCandidates = []
			if maxDist <= smallestDist:
				startCandidates.append(i)

	random.shuffle(startCandidates)
	start = startCandidates[0]
	used[start] = True
	positions.append(start)

	availableObjectives = []
	easyObjectiveOrder = [0]
	for i in range(fullRevealCutoff - 1):
		for j in range(objectivePackSize):
			if i * objectivePackSize + 1 + j < fullRevealCutoff:
				availableObjectives.append(i * objectivePackSize + 1 + j)
		random.shuffle(availableObjectives)
		easyObjectiveOrder.append(availableObjectives.pop(0))

	for i in range(fullRevealCutoff):
		random.shuffle(positions)
		currentPosition = positions.pop(0)
		objectivePositions[easyObjectiveOrder[i]] = currentPosition
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

	board = getObjectives(json, seed, objectivePositions)

	for space in board:
		dif = space['difficulty']
		if dif == 1:
			result.append({"name": f"{space['name']} $"})
		elif dif > fullRevealCutoff:
			result.append({"name": f"{space['name']}"})
		else:
			result.append({"name": space['name']})

	return result