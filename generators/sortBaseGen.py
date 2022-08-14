from generators.baseGens.slrv5 import slrv5

def genSortedBoard(json, seed):
	board = slrv5.genBoardSlrv5(json, seed)

	result = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

	for space in board:
		if space:
			result[space["difficulty"]-1] = {"name" : space["name"]}

	return result