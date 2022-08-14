from generators.baseGens.slrv5 import slrv5
import random

def genInvasionBoard(json, seed):
	board = slrv5.genBoardSlrv5(json, seed)

	result = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

	batch1 = [0,1,3,4,5,9,15,19,20,21,23,24]
	cutoff1 = 12
	batch2 = [2,6,8,10,14,16,18,22]
	cutoff2 = 20
	batch3 = [7,11,12,13,17]

	random.shuffle(batch1)
	random.shuffle(batch2)
	random.shuffle(batch3)

	for space in board:
		if space:
			dif = space["difficulty"]
			if dif <= cutoff1:
				result[batch1.pop()] = {"name" : space["name"]}
			elif dif <= cutoff2:
				result[batch2.pop()] = {"name" : space["name"]}
			else:
				result[batch3.pop()] = {"name" : space["name"]}

	return result