import runWorld as rw
import drawWorld as dw
import pygame as pg

from random import randint
print(randint (1,5))
################################################################

# Initialize world
name = "Press the mouse to change the cat's direction!"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
cat = dw.loadImage("cat.bmp")
sleepydonald = dw.loadImage("sleepydonald.bmp")

def updateDisplay(state):
    dw.fill(dw.blue)
    dw.draw(sleepydonald, (250, 250))
    dw.draw(cat, (state[0], state[2]))


################################################################

# state -> state
def updateState(state):
    return((state[0]+state[1],state[1],state[2]+state[3], state[3]))

################################################################
#((state[0] > width or state[0] < 0) or (state[2] > height or state[2] < 0) or
# End Simulation
# state -> bool
def endState(state):
    if ((state[0] < 500 and state[0] > 250) and (state[2] < 250 and state[2]>150)):
        return True
    else:
        return False


################################################################

# Mouse Click
def handleEvent(state, event):  
    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        newStateDX = randint(-10,10)
        newStateDY = randint(-10,10)
        return((state[0],newStateDX,state[2],newStateDY))
    else:
        return(state)

################################################################

initState = (randint(50,499),randint(-5,5),randint(50,499),randint(-5,5))

# Run the simulation no faster than 60 frames per second
frameRate = 10

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
