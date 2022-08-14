import json

import generators.sortBaseGen as sortBaseGen
import generators.invasionGen as invasionGen

def getJson(filename) -> [dict]:
	with open(f"generators/generatorJsons/{filename}.json", 'r') as file:
		return json.load(file)

def generate(genType:str, seed:str) -> dict:
	return gameModeDict[genType](seed)

gameModeDict = {
	"Sorted New Lockout" :
		lambda seed : sortBaseGen.genSortedBoard(getJson("newLockout"), seed),
	"Invasion New Lockout" :
		lambda seed : invasionGen.genInvasionBoard(getJson("newLockout"), seed),
}

gameModeSet = tuple(list(gameModeDict.keys()))