from generators.baseGens.slrv5 import slrv5

def genBoard(json, seed):
	board = slrv5.genBoardSlrv5(json, seed)

	result = []

	for space in board:
		if space:
			result.append({"name" : space["name"]})

	return result