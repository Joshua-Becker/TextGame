from classes import *
import random
from tools import *

def fight(user,enemy):
	slaying = True
	youHit = random.getrandbits(1)
	damageThisRound = random.getrandbits(1) + 1
	totalDamage = 0
	nl()
	while(slaying):
	    if(youHit):
	        print(reformat("Fair warrior, Your strike rings true!"))
	        print(str(damageThisRound) + " damage dealt")
	        print(totalDamage + damageThisRound)
	    if(totalDamage >= 4):
	        slaying = False
	        youHit = random.getrandbits(1)
	        nl()
	        print ("A final mighty blow fells the Dragon. The dust clears and hero emerges!")
	        nl()
	       	return 'success'
	        
	    else:
	        slaying = False
	        print ("Your grip slips, the beast feasts!")
	        nl()
	        return 'failure'