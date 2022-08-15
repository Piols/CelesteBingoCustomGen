import generators.baseGens.invasion as invasionGen
import random

def genSymmetricalInvasionBoard(json, seed):
	board = invasionGen.genBoardInvasion(json, seed)

	result = []

	for space in board:
		if space:
			result.append({"name": space["name"]})

	return result