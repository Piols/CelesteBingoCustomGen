To extend this program:

- Make a new python file in the generators directory.

- Code your generator in there, it should return a list of dictionairies
   [
	{"name" : "beat 1A"},
	ect..
   ]

(If you want to make use of the normal slr v5 generator used my bingosync. Import it using 
		from generators.baseGens.slrv5 import slrv5
then call     
		slrv5.genBoardSlrv5(json, seed)
)

- Go to the generatorHandler.py file and a value to the gameModeDict dictionairy. Which key is the name of your generator, 
  and its value is a lambda function from seed to board file.

(The generator will always recieve a number between 0 and 999999 as a string (TODO: Make this not true))

- Add your name to the credits

(and test the code obviously)