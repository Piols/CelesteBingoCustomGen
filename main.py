from tkinter import *
from tkinter.ttk import Combobox

import random

import generatorHandler
import bingoSyncConnection as bingosync


def execute():
	
	if gameModeChoice.get() == "":
		outputText("Please choose an option")
		return

	seed = seedBox.get()

	if seed != "":
		try:
			seed = int(seed)
		except ValueError():
			seed = random.randint(0,999999)
	else:
		seed = random.randint(0,999999)

	board = generatorHandler.generate(gameModeChoice.get(), str(seed))
	password = passwordBox.get()
	lockout = True if lockoutBox.get() else False
	roomId = boardIdBox.get()

	bingosync.joinRoom(roomId, password)

	bingosync.setBoard(roomId, lockout, board)

	bingosync.sendMessage(roomId, f"Changed the board to {gameModeChoice.get()}")
	
	outputText("Succesfull (probably, haven't coded error handling)")


def outputText(text:str):
	output["text"] = text


# UI stuff

window=Tk()
height = 400
width = 500

window.title('Celeste Bingo Custom Gen')
window.geometry(f"{width}x{height}+10+20")


lbl=Label(window, text="Celeste custom bingo gen", fg='Black', font=("Helvetica", 22))
lbl.place(x=(width-350)/2, y=20)

lbl=Label(window, text="Mode:", fg='black', font=("Helvetica", 12))
lbl.place(x=20, y=78)

gameModeChoice=Combobox(window, values=generatorHandler.gameModeSet)
gameModeChoice.place(x=80, y=80)

lbl=Label(window, text="Lockout:", fg='black', font=("Helvetica", 12))
lbl.place(x=20, y=110)

lockoutBox = IntVar()

b=Checkbutton(window, variable=lockoutBox)
b.place(x=80, y=110)

lbl=Label(window, text="BoardId:", fg='black', font=("Helvetica", 12))
lbl.place(x=20, y=138)

boardIdBox=Entry(window)
boardIdBox.place(x=85, y=140)

lbl=Label(window, text="Password:", fg='black', font=("Helvetica", 12))
lbl.place(x=20, y=168)

passwordBox=Entry(window)
passwordBox.place(x=100, y=170)

lbl=Label(window, text="Seed:", fg='black', font=("Helvetica", 12))
lbl.place(x=20, y=198)

seedBox=Entry(window)
seedBox.place(x=100, y=200)

btn = Button(window, text="Generate", fg='black', command=execute)
btn.place(x=20, y=250)

output=Label(window, text="", fg='red', font=("Helvetica", 12))
output.place(x=20, y=280)



window.mainloop()