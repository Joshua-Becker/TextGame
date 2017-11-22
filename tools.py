import textwrap

''' This code is an example of how to call a function and return an answer from a hash/dictionary
def f(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 9)
'''

def nl():
	print('\n')

def reformat(stng):
	import re
	new = str(stng)
	new = re.sub("[\\\\]" + "n", "", new, flags=re.M)
	new = re.sub("  ", " ", new, flags=re.M)
	new = re.sub("[{}]", "", new, flags=re.M)
	new = new.strip('\'')
	new = textwrap.fill(new, 100)
	return new

def testRsp(options, response):
	strsp = str(response)
	txt = "You can't seem to " + strsp + ". But you wish you could."
	if strsp == '':
		strsp = 'wait'
	for key in options:
		if strsp == key:
			txt = options[key]
	if txt == "You can't seem to " + strsp + ". But you wish you could.":
		xstrsp = strsp.split()
		for i in xstrsp:
			for key in options:
				if i in key:
					txt = "Did you mean to: " + key

	return txt

def play():
	x = input("--> ")
	return x
