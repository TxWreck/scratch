import PySimpleGUI as sg
import numpy as np

from queue import PriorityQueue
openSet = PriorityQueue()

gridSize = 800
cellCount = 10
maxWallIndex = 10
wallIndex = 6
cellSize = gridSize/cellCount
map = np.random.randint(maxWallIndex, size=(cellCount, cellCount))

solution = 0
bug = [0, 0]
bugPrev = [0, 0]

goal = [cellCount-1, cellCount-1]

layout = [[sg.Canvas(size=(gridSize, gridSize),
                     background_color='white',
                     key='canvas')],
          [sg.Button('Run'),sg.Button('Stop'),sg.Button('Step')],
          [sg.Button('Reset'), sg.Exit()]
          ]

window = sg.Window('GridMaker', layout, resizable=True, finalize=True)
gd = window['canvas']



def setMap():

    global map 
    map = np.random.randint(maxWallIndex, size=(cellCount, cellCount))
    for row in range(map.shape[0]):
        for column in range(map.shape[1]):
            if(map[column][row] > wallIndex):
                map[column][row] = 1
            else:
                map[column][row] = 0
                
            if(map[column][row] == 1 and column == 0 and row == 0): 
                map[column][row] = 0

            if(map[column][row] == 1 and column == cellCount - 1 and row == cellCount - 1): 
                map[column][row] = 0


def drawGrid():

    gd.TKCanvas.create_rectangle(
        1, 1, gridSize, gridSize, outline='BLACK', width=1)
    
    for x in range(cellCount):
        gd.TKCanvas.create_line(
            ((cellSize * x), 0), ((cellSize * x), gridSize),
            fill='BLACK', width=1)
        gd.TKCanvas.create_line(
            (0, (cellSize * x)), (gridSize, (cellSize * x)),
            fill='BLACK', width=1)


def drawCell(x, y, color):
    gd.TKCanvas.create_rectangle(
        x, y, x + cellSize, y + cellSize,
        outline='BLACK', fill=color, width=1)

def drawMap():
    for row in range(map.shape[0]):
        for column in range(map.shape[1]):
            # Empty
            if(map[column][row] == 0):
                drawCell((cellSize*row), (cellSize*column), 'WHITE')

            # Wall
            if(map[column][row] == 1):
                drawCell((cellSize*row), (cellSize*column), 'GREY')

            # Goal
            if(map[column][row] == 4):
                drawCell((cellSize*row), (cellSize*column), 'GREEN')

            # Bug
            if(map[column][row] == 3):
                drawCell((cellSize*row), (cellSize*column), 'RED')

            # Visited
            if(map[column][row] == 2):
                drawCell((cellSize*row), (cellSize*column), 'YELLOW')


def update():
    drawCell((cellSize*bug[0]), (cellSize*bug[1]), 'RED')
    drawCell((cellSize*bugPrev[0]), (cellSize*bugPrev[1]), 'YELLOW')


def init():
    global bug
    bug = [0,0]

    setMap()
    map[bug[0],bug[1]] = 3
    map[goal[0],goal[1]] = 4
    drawGrid()
    drawMap()
    openSet.put(bug)

def moveBug():
    global bugPrev
    bugPrev = bug.copy()

    map[bug[0]][bug[1]] = 2
    bug[0] += 1
    bug[1] += 1
    map[bug[0],bug[1]] = 3
    update()



init()

while True:             # Event Loop
    event, values = window.read()
    
    if event in (None, 'Exit'):
        break

    if event in ('Step'):
        moveBug()
        if solution:
            break

    if event in ('Reset'):
        init()
        
window.close()

