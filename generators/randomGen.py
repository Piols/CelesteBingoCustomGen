from generators.baseGens.slrv5 import slrv5
import random

def genRandomBoard(json, seed):
	board = slrv5.genBoardSlrv5(json, seed)

	result = [None] * 25
	permutation = [0] * 25
	for i in range(25):
		permutation[i] = i
	random.seed(seed)
	random.shuffle(permutation)

	for space in board:
		if space:
			dif = space["difficulty"]
			result[permutation[dif - 1]] = {"name" : space["name"]}

	return result