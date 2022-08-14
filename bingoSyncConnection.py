import json
import requests

s = None

def joinRoom(roomId:str, password:str):
	global s
	s = requests.session()

	s.post("https://bingosync.com/api/join-room", json={
		"room" : roomId,
		"password" : password,
		"nickname" : "Custom Bingo Gen"
	})

def sendMessage(roomId:str, text:str):
	if s == None:
		raise ValueError("Session has not been started yet.")

	s.post("https://bingosync.com/api/chat", json={
		"room" : roomId,
		"text" : text
	})

def setBoard(roomId:str, lockout:bool, board:[dict], seed:str = ""):
	s.post("https://bingosync.com/api/new-card", json={
		"room" : roomId,
		"lockout_mode" : "2" if lockout else "1",
		"hide_card" : True,
		"custom_json" : json.dumps(board),
		"game_type" : "18",
		"variant_type" : "18",
		"seed" : seed
	})