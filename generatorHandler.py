import json

import generators.generatorJsons.newLockout as newLockout
import generators.generatorJsons.newLongo as newLongo
import generators.generatorJsons.oldLongo as oldLongo
import generators.generatorJsons.soloBlackout as soloBlackout
import generators.generatorJsons.teamsBlackout as teamsBlackout

import generators.normalGen as normalGen
import generators.sortBaseGen as sortBaseGen
import generators.invasionGen as invasionGen

def generate(genType:str, subType:str, seed:str) -> dict:
	return gameModeDict[genType](submodeDict[subType], seed)

gameModeDict = {
	"Normal" :
		lambda json, seed : normalGen.genBoard(json, seed),
	"Sorted" :
		lambda json, seed : sortBaseGen.genSortedBoard(json, seed),
	"Invasion" :
		lambda json, seed : invasionGen.genInvasionBoard(json, seed),
}

gameModeSet = tuple(list(gameModeDict.keys()))

submodeDict = {
	"New Lockout" :
		newLockout.newLockoutJson,
	"Solo Blackout" :
		soloBlackout.soloBlackoutJson,
	"Teams Blackout" :
		teamsBlackout.teamsBlockoutJson,
	"Old Longo" :
		oldLongo.oldLongoJson,
	"New Longo" :
		newLongo.newLongoJson,
	
}

submodeSet = tuple(list(submodeDict.keys()))