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
	slots = range(0,25)
	random.shuffle(slots)

	while slots:
		slot = slots.pop(0)
		result[slot] = boardtemp.pop(0)
		if slot != 12:
			result[24-slot] = boardtemp.pop(0)
			slots.remove(24-slot)
			
	return result