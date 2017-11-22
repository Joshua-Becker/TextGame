import control
import classes
'''
A  host of evils like the steps up to the fight. Fighting the inner evils to get to the real fight.
1) Darkness
2) Hut and home
3) Battle with self in comfort 
4) Light is entrance to a gladiator stadium
'''

#Contents:
#Battle with self states 20s
#Front of Hut states 30s
#The Arena states 40s

#Beginning 

class start:

	def __init__(self, user):
		self.user = user

	start = [ 
	"""
	Darkness. Complete and Utter. You feel as though you are standing in a puddle and you can hear the water as you plod along. Although all is dark, you can see your form clearly. You are human. And you are naked... A sphere of light can be seen far off and bobbing. One thought comes to your mind: I am  """ + control.user.name + """ *TEXT* -> Indicates the thoughts of the character you are controlling """
	]

	wait01 = [ 
	"""
	While waiting you notice the light bob up and down in a meserizing fashion, to a point where you barely hear the sound of a deep throated croak from behind you. A mix of a voice and a dog bark. Alarming, but also intriguing.
	"""
	]

	listen01 = [ 
	"""
	You stop and listen. Nothing sounds in front of you, but there is a slight noise coming 
	from behind of moving water.
	"""
	]

	#1 - 30
	goToOrb = [ 
	"""
	As you move forward the water level lowers and you feel the touch of wooden planks below you. Moving forward the planks seem to lead like a pier to a wooden hut. The light is in the window.
	""", 'state30'
	]

	#1 - 20
	goOtherWay = [
	"""
	You turn and flee from the light. Plunging forth you defy the clear path forward and the darkness closes in on you until you feel limbless. As if you were floating. Your thoughts begin to resonate inside your head as loud as a voice, pure and succinct.
	*This is right. Me on the road! Out and about, heeding nobody but my own self. Good to finally be on my own adventure and forging my own way. *
	""",'state20'
	]

	options = {'look':start, 'wait': wait01, 'go to orb': goToOrb}


#Front of Hut states 30s
class state30:

	def __init__(self, user):
		self.user = user

	look = [ 
	"""
	There are wooden planks below you. The planks seem to lead like a pier to a wooden hut. The light is in the window.
	"""
	]

	#30 - 31
	enterHut = [ 
	"""
	The door has no handle so you push through easily. You come into a cozy room with stairs on the left, a firepit straight in front of you illuminating a chair with side table and a cup of something that smells delicious. A door is to the right of the fireplace with a window, the light can be seen through the window.
	""", 'state31'
	]

	#30 - 33
	goAroundHut = [ 
	"""
	Circling the hut you see piles of wood and the light farther off beyond.
	""", 'state33'
	]

	options = {'look':look, 'go inside':enterHut, 'go around':goAroundHut}


#Other side of hut
#State 33
class state33:

	def __init__(self, user):
		self.user = user

	collectWood = [ 
	"""
	You pick up a log of wood! A nice dry piece of oak.
	"""
	]

	#33 - 30
	goToFront = [
	"""
	You are now back in front of the hut.
	""", 'state30'
	]

	goToLight = [
	"""
	You move further towards the light. On and on you move until you come to a staircase.
	""",'state40'
	]

	options = {'collect wood':collectWood, 'go to front':goToFront, 'go to orb': goToLight}


#In hut
#State 31
class state31:

	def __init__(self, user):
		self.user = user

	look = [
	"""
	a cozy room with stairs on the left, a firepit straight in front of you illuminating a chair with side table and a cup of something that smells delicious. A door is to the right of the fireplace with a window, the light can be seen through the window.
	"""
	]

	#31 -32
	goUpstairs = [ 
	"""
	Heading upstairs the darkness grows and falls onto you like a fog. at the top you turn to see two eyes in the dark.
	This is not alarming. But you feel like you should be alarmed. A voice sounding like an old woman
	resonates in the attic like rolling marbles and states thus: 

	'Honey dearest, would you be my little marble and pass me the kettle?'

	A kettle appears on a table to the left of you.
	""", 'state32'
	]

	drink = [ 
	"""
	The wonderful aroma overwhelms you and you give in to the temptation to consume a great cup of delightful drink.
	You slip into a slumber instantly falling into the chair!

	*Tasty*
	"""
	]

	waitInHut = [ 
	"""
	While viewing the fire and enjoying the fine seat you hear a voice come from upstairs. 
	A voice sounding like an old woman
	resonates like rolling marbles and states thus: 

	'Tommy Dear, please come tend to your nana!'

	*Jeepers!*
	"""
	]

	listenInHut = [ 
	"""
	You hear a creeking in the floorboards above you. Probably just the wind.
	*There is no wind* 
	"""
	]

	options = {'go upstairs': goUpstairs,'look':look,'drink':drink, 'listen':listenInHut, 'wait':waitInHut}


#Upstairs hut
#State 32
class state32:

	def __init__(self, user):
		self.user = user

	fetchKettle = [ 
	"""
	You retrieve the kettle and walk forward. A tentacle comes from the dark and wrap around your wrist. 
	*THE HORROR*
	The shadow flees from around you and you see a tentacle monster in front of you with a gaping mouth full of teeth
	as it prepares to make you its dinner! As the room empties of the darkness you see a barnacle encrusted room.
	"""
	]

	pourKettle = [ 
	"""
	Pouring out the hot kettle on the tentacles the monster shrinks back in pain and releases your arm!
	"""
	]

	#32 - 31
	runAway =[ 
	"""
	You run back down the stairs and here the tentacle plops in pursuit!
	""",'state31'
	]

	options = {'get kettle':fetchKettle, 'pour kettle':pourKettle, 'run': runAway}



# Battle with self states 20s


class state20:

	def __init__(self, user):
		self.user = user

	wait01 = [
		"""
		*All the comforts I could want! Not much but it could be home.*
		"""
	]

	listen = [
	"""
	A gentle hum and toon set into your mind ringing in your ears:
	*Hum dum a dittle, doom boom a bittle. Wickey wackey wash, here the cat has a riddle. Take my tail and swat my my knees. I'll sit up and what'll I be? Pissed. You took my tail!*
	"""
	]

	look = [
		"""
		You see nothing. You are enveloped in darkness. Oh wait! You do in fact see a light speckle in the distance every once in a while as you turn around. But you don't like to look that way. Too obviously the set course. No. You are making your own way. Press forward into the depths!
		"""
	]

	goBack = [
	"""
	You draw yourself up from your rut, swing about and head determinedly toward the speck that is the light. After some time you come up to wooden planks out of the water. Still naked, you approach a hut gently set in the midst of the darkness. The light can be seen through the window.
	""", 'state30'
	]

	options = {'wait':wait01, 'listen':listen, 'look':look, 'go back':goBack}


# The Arena states 40s

#Grand stair state 40
class state40:

	def __init__(self, user):
			self.user = user

	look = [
		"""
		Horns are sounding in the distance. The light is splayed across a golden staircase fit with a red carpet. The darkness is behind you and the light fills the staircase and stone walls leading up. To your sides you see tapestries lining the walls leading farther up. Scenes can be seen of battles, brawls, pleasantly arranged fruits, and market flurry.
		"""
	]

	goUpstairs = [
		"""
		You take the stairs leisurely as a clamour begins to get louder echoing off the walls. You come to an armory at the top of the stairs. A rough looking fellow with an eyepatch grunts at you in seeming distaste and gestures to the weapon's rack. There held amongst pegs you see three labels above various objects reading: Swords, Blasters, shields.
		""",'state41'
	]

	options = {'look':look, 'go upstairs':goUpstairs}


#Armory state 41
class state41:

	def __init__(self, user):
			self.user = user
		
	selectSword = [
		"""
		You retrieve from the pegs a double-edged longsword with a golden crossbar and wooden pommel depicting the semblance of a lion's head. entitled along the base of the blade it reads: Dancing Fang. 
		""",'','Dancing Fang'
	]

	selectBlaster = [
		"""
		You pick a blaster off the wall. A small handheld pistol. Made of metal with leather handle, it is heavy in your hand. A simply wrought weapon with an elegant white barrel. 
		""",'','blaster'
	]

	selectShield = [
		"""
		You collect a small wooden shield from the pegs. It is round with a comfortable leather and wool strap holding secure on your arm. The front is plain.
		"""
	]

	enterArena = [
		"""
		You come to the gate next to the gaurd and he holler-growls 'Let him in the ring!' The gate opens wide and you are ushered into an arena. The lights shine down on you and are blinding if you look straight up. Your ears are ringing with the sound of voices raised as you walk forward in a daze. You cannot see above the tall walls without the light making you look away. but in front of you, illuminated in the bright lights is another warrior clad in black armor to the top. and you are only wearing 
		""" + control.user.clothes,'state42'
	]

	options = {'sword': selectSword, 'blaster':selectBlaster, 'shield':selectShield, 'enter arena': enterArena}


#combat in arena state 42
class state42:

	def __init__(self, user):
			self.user = user

	engage = [
		"""
		You engage the enemy! 
		""", ['combat','end'], control.user, 'enemy'
	]

	fail = [
		"""
		You are torn apart viciously!
		"""
	]
	
	options = {'engage':engage, 'fail':fail}

#end of scene
class end:

	def __init__(self, user):
			self.user = user

	closing = [
	"""
	Perishing your foe you emerge victorious! As the crowd roars and your heart pulses mightily, the light begins to fade...
	"""
	]















