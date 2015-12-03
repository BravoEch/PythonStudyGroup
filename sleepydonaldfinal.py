import runWorld as rw
import drawWorld as dw
import pygame as pg

from random import randint
print(randint (1,5))
################################################################

# Initialize world
name = "DON'T WAKE DONALD!"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
cat = dw.loadImage("cat.bmp")
sleepydonald = dw.loadImage("sleepydonald.bmp")
angrydonald = dw.loadImage("angrydonald.bmp")
donald = dw.loadImage("donald3.bmp")
gameover = dw.loadImage("gameOver.bmp")

def updateDisplay(state):

    if state[4] == (2):
        label = dw.makeLabel("Lives = " + str(state[4]), 'serif', 20, (255, 255, 255))
        dw.fill(dw.blue)
        dw.draw(sleepydonald, (350, 250))
        dw.draw(cat, (state[0], state[2]))
        dw.draw(label, (850, 50))
    elif state[4] == (1):
        label = dw.makeLabel("Lives = " + str(state[4]), 'serif', 20, (255, 255, 255))
        dw.fill(dw.red)
        dw.draw(angrydonald, (350, 250))
        dw.draw(cat, (state[0], state[2]))
        dw.draw(label, (850, 50))
    else:
        dw.fill(dw.black)
        dw.draw(donald, (100, 100))
        dw.draw(gameover, (350, 350))



################################################################

# state -> state
def updateState(state):
    if (state[0]<0 or state[0]+100>1000):
        return(state[0]-state[1], -state[1],state[2]+state[3],state[3],state[4])
    elif (state[2]<0 or state[2]+100>800):
        return(state[0]+state[1],state[1],state[2]-state[3], -state[3], state[4])
    elif ((state[0]<525 and state[0]>300) and (state[2]<550 and state[2]>250)):
        return (state[0]-state[1],-state[1],state[2]-state[3], -state[3], (state[4] - 1))
    else:
        return(state[0]+state[1],state[1],state[2]+state[3],state[3], state[4])

################################################################

# End Simulation
# state -> bool
def endState(state):
    if state[4] == -1:
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
        return(state[0],newStateDX,state[2],newStateDY, state[4])
    else:
        return(state)

################################################################

initState = (randint(50,499),randint(-5,5),randint(50,499),randint(-5,5), 2)

# Run the simulation no faster than 60 frames per second
frameRate = 10

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)

pg.quit()
