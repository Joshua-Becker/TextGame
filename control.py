from classes import *
from tools import *
from combat import fight

def Go(scene):

	global user 
	user = person(10,0,"standing",'')
	user.create()
	#user.dmg(1)
	#print(user.health)

	def boat():
		import boat

		nl()
		print(reformat(boat.start[0]))
		nl()

		while user.complete == False:
			rsp = play()
			if rsp == 'exit':
				user.complete = True
				break
			result = testRsp(boat.options,rsp)
			if type(result) is str: 
				print(result)
			else:
				print(reformat(result[0]))

			nl()

	def darkness():
		#import text and make a user in the start state
		import darkness
		user.state = darkness.start
		nl()
		print(reformat(user.state.start[0]))
		nl()

		while user.complete == False:
			#User response
			rsp = play()
			#User escape option
			if rsp == 'exit':
				user.complete = True
				break

			#For testing only
			if rsp == 'list':
				print(user.state.options.keys())
				rsp = play()
			if rsp == 'skip':
				user.state = darkness.state42
				rsp = play()


			#Result of response
			result = testRsp(user.state.options,rsp)
			#Test if response is generated error message else run function
			if type(result) is str: 
				print(result)
			else:
				print(reformat(result[0]))
				try:
					#How to call a combat scenario
					if result[1][0] == 'combat':
						x = fight(result[2],result[3])
						#Successful combat means you move on
						if x == 'success':
							state = result[1][1]
							user.state = getattr(darkness, state)
						#If combat doesn't return success then it is a fail
						else:
							print (reformat(user.state.fail[0]))
							nl()
							user.complete = True
							break
					else:
						state = result[1]
						user.state = getattr(darkness, state)

					#The way to print end lines
					if result[1] == 'end' or result[1][1] == 'end':
						nl()
						print (reformat(darkness.end.closing[0]))
						nl()
						user.complete = True
						break
				#except:
				#	pass
				#in case of tests
				except Exception:
					raise


			nl()



	if scene == "boat":
		boat()
	if scene == "darkness":
		darkness()

