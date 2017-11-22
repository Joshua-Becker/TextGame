import control
import Character
from tools import *

print("Welcome to the Mad Librarian!")
print("New character (1). Continue game (Character Name)")
responce = raw_input("--> ")
if(responce == "1"):
	user = Character.create()
else:
	user = Character.getCharacter(responce)
	print(user.getName() + '\n' + user.getHealth())

Adventures.explore(Dreadnot,user)

#control.Go("darkness")



