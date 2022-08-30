from generators.baseGens.slrv5 import slrv5
import random

def genFoWNoEdgeStartBoard(json, seed):
	board = slrv5.genBoardSlrv5(json, seed)

	def okBoard(board):
		for i in range(26):
			if board[i] and board[i]['difficulty'] == 1:
				return i % 5 != 1 and i % 5 != 0 and 5 < i <= 20

	random.seed(seed)
	while not okBoard(board):
		seed = random.randint(0, 999999)
		board = slrv5.genBoardSlrv5(json, seed)

	result = []

	for space in board:
		if space:
			result.append({"name": f"{space['name']} $" if space['difficulty'] == 1 else space["name"]})

	return result