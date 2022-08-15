from generators.baseGens.slrv5 import slrv5
import random

def genInvasionSymmetryBoard(json, seed):
	board = slrv5.genBoardSlrv5(json, seed)

	boardtemp = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

	for space in board:
		if space:
			boardtemp[space["difficulty"]-1] = {"name" : space["name"]}

	result = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

	

	random.seed(seed)
	slots = list(range(0,25))
	random.shuffle(slots)

	while slots:
		slot = slots.pop(0)
		result[slot] = boardtemp.pop(0)
		print(slot)
		print(result[slot]["name"])
		if slot != 12:
			result[24-slot] = boardtemp.pop(0)
			print(24-slot)
			print(result[24-slot]["name"])
			slots.remove(24-slot)
			
	return result