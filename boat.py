#Cellroom

start = [
"""A wash sprays through the porthole  
and the floor sways with a creek back the other way. 
You find yourself sitting on the floor, arms tied behind your back, 
and iron bars in front of you. Torchlight illuminates the cell.""" 
]

cellLook = [
"""You see a cellroom. The room lifts and sways with the lilting movement of the vessel.
There is a waste bin in a wooden box nailed to the ground in the corner, a bed with a few linens
attached to the wall, a small window looking out onto the ocean and iron bars barring the way out.
"""
]

atBars = [
"""
The bars look like a sturdy metal, all vertical, and there is a lock on the iron door.
"""
]

atBed = [
"""
The bed is unkempt and the blanket is stained from use without washing.
"""
]

atWastebin = [
"""
The waste pot is in a wooden crate nailed to the floor. As the boat reels the contents swish about most distastfully.
"""
]


lookOutsideBars = [
"""
There is lantern in the hall of cells and down the way a dog can be seen trotting to and fro. 
A man is sitting at a table next to a door with a hat on his face and his legs propped. 
Many other cells are lining the walls, but you can only see into the three in front of you. 
The two cells on the right are empty, but the cell on the left holds a man that is sleeping on his cot.
"""
]

sitOnBed = [
"""
You sit on the bed.
"""
]

callDog = [
"""
The dog looks up at you and wobbles over with a stick in its mouth. He looks up thoughtfully while wagging his tale.
"""
]

pickUpBlanket = [
"""
You successfully obtain a blanket.
"""
]

peeOnBlanket = [
"""
Your blanket is moistened.
"""
]

takeStickFromDog = [
"""
You successfully obtain a stick. The dog is waiting outside the bars patiently.
"""
]

useBlanketAndStickOnBars = [
"""
You begin twisting the blanket to give it strength and then wrap it around the bars with the stick 
as a lever. Using all your might you begin turning the stick and the iron bars begin to move towards eachother 
until there is enough space for you to squeeze through. At this point the dog is whining and looking longingly at his stick.
"""
]

callGuard1 = [
"""
The guard does not budge.
"""
]

callGuard2 = [
"""
The guard stirs but does not say anything.
"""
]

callGuard3 = [
"""
The guard puts down a foot hard on the floor, but does not move. Here, the other cell member acros the way says 
'I would not wake him if I were you'.
"""
]

callGuard4 = [
"""
The guard gets up and walks out the door. The dog goes to the door and begins barking."
"""
]

wait1 = [
"""
The ship rocks back and forth with the waves.
"""
]

wait2 = [
"""
A gull can be heard crying out from outside your window and a seaspray washes into your cell."
"""
]

wait3 = [
"""
Outside your cell you here footsteps and the opening and closing of a door.
"""
]

wait4 = [
"""
The man in the cell across the way begins to hum and eery tune. 'Humm him hmm humm'
"""
]

wait5 = [
"""
A door opens and you can hear a voices coming towards your cell. A retinue of three guards approach your cell, 
open it and tell you to get a move on.
"""
]

followGuards = [
"""
You follow the guards orders, leave the cell and leave surrounded by three guards out the door.
"""
]

attackGuardsSucceed = [
"""
You jump at the closest guard and in a fit of rage while at that very moment the ship rocks.
The guards fall atop eachother and you clear past the fallen men into the hallway.
"""
]

attackGuardsFail = [
"""
You leap at the guards with all your remaining strength, but the exursion is too much for your tired body.
After flailing violently at the three men you are held down and your hands are bound by rope whil your neck is given a leash.
"""
]

searchGround = [
"""
You see wooden planks lining the floor! They lead everywhere, out the doors, 
under your bed, and around the waste pot.
"""
]

lookUnderBed = [
"""
The under side of the bed is much like the other parts of the floor save a small wooden spoon laying there on the ground.
"""
]

pickUpSpoon = [
"""
You obtain a wooden spoon!
"""
]

moveWastebin = [
"""
Pressing against the wood waste bin, the object begins to budge and the entire wooden 
crate and pot are slightly lifted from the ground.
There is a hole here that leads to darkness.
"""
]

enterHole = [
"""
You lift the bin and slide it away to reveal a hole and slowly slip into the space 
pulling the bin back over you as you descend.
"""
]



options1 = {'look':cellLook, 'look at bars':atBars, 'look at bed':atBed, 'look at wastebin':atWastebin, 
'look outside bars':lookOutsideBars, 'sit on bed':sitOnBed, 'call dog':callDog, 'pick up blanket':pickUpBlanket,
'call guard':callGuard1, 'wait':wait1, 'search ground':searchGround, 'look under bed':lookUnderBed,
'move wastebin':moveWastebin}








