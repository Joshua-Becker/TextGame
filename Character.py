from tools import *

class person:

	def __init__(self, name, health = 10, state = 0, position = "standing", inventory = '', complete = False, clothes = []):
		self.health = health
		self.state = state
		self.position = position
		self.inventory = []
		self.complete = False
		self.name = name
		self.clothes = []

	def getHealth(self):
		return self.health

	def setHealth(self, health):
		self.health = health

	def getState(self):
		return self.state

	def setState(self, state):
		self.state = state

	def getPosition(self):
		return self.position

	def setPosition(self, position):
		self.position = position

	def getInventory(self):
		return self.inventory

	def setInventory(self, inventory):
		self.inventory = inventory

	def addToInventory(self, item):
		self.inventory.append(item)

	def getComplete(self):
		return self.complete

	def setComplete(self, val):
		self.complete = val

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def getClothes(self):
		return self.clothes

	def setClothes(self, clothes):
		self.clothes = clothes

	def addToClothes(self, item):
		self.clothes.append(item)

	def updateChar(self):
		f = open("profiles/" + self.name + ".txt",'w')
		f.write(self.name + '\n' + str(self.getHealth()) + '\n' + str(self.getState()) + '\n' + str(self.getPosition()) + '\n' + str(self.getInventory()) + '\n' + str(self.getComplete()) + '\n' + str(self.getClothes()) + '\n')
		f.close()



def getCharacter(toon):
	with open("profiles/" + toon + ".txt", 'r') as f:
		lines = f.read().splitlines()
	character = person(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6])
	return character

def create():
	print("Please enter name: \n")
	toon = raw_input("--> ")
	toon = str(toon)
	user = person(toon)
	user.updateChar()
	return user