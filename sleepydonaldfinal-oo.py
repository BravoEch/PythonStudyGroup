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

class State:
    def __init__(self, x, dx, y, dy, Lives):
        self.x = x
        self.dx = dx
        self.y = y
        self.dy = dy
        self.Lives = Lives

initState = State(
    x = randint(1,499),
    dx = randint(-5,5),
    y = randint(1,499),
    dy = randint(-5,5),
    Lives = (2))

def updateDisplay(state):
    if state.Lives == (2):
        label = dw.makeLabel("Lives = " + str(state.Lives), 'serif', 20, (255, 255, 255))
        dw.fill(dw.blue)
        dw.draw(sleepydonald, (250, 250))
        dw.draw(cat, (state.x, state.y))
        dw.draw(label, (850, 50))
    elif state.Lives == (1):
        label = dw.makeLabel("Lives = " + str(state.Lives), 'serif', 20, (255, 255, 255))
        dw.fill(dw.red)
        dw.draw(angrydonald, (250, 250))
        dw.draw(cat, (state.x, state.y))
        dw.draw(label, (850, 50))
    else:
        dw.fill(dw.black)
        dw.draw(donald, (100, 100))
        dw.draw(gameover, (350, 350))
    return state

################################################################

# state -> state
def updateState(state):
    if (state.x<0 or state.x+100>1000):
        state.x = state.x-state.dx
        state.dx = -state.dx
        state.y = state.y+state.dy
    elif (state.y<0 or state.y+100>800):
        state.x = state.x+state.dx
        state.y = state.y-state.dy
        state.dy = -state.dy
    elif ((state.x<525 and state.x>300) and (state.y<550 and state.y>250)):
        state.x = state.x-state.dx
        state.dx = -state.dx
        state.y = state.y-state.dy
        state.dy = -state.dy
        state.Lives = state.Lives - 1
    else:
        state.x = state.x+state.dx
        state.y = state.y+state.dy
    return state

################################################################

# End Simulation
# state -> bool
def endState(state):
    if (state.Lives ==-1):
        return True
    else:
        return False

################################################################

# Mouse Click
def handleEvent(state, event):
    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        state.dx = randint(-10,10)
        state.dy = randint(-10,10)
    return(state)

################################################################

# Run the simulation no faster than 60 frames per second
frameRate = 10

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
pg.quit()
