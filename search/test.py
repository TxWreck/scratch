import PySimpleGUI as sg

# from queue import PriorityQueue
from Map import Map as map

# openSet = PriorityQueue()

size = 10 
gridSize = 800
cellSize = gridSize/size
mp = map(size)


layout = [[sg.Canvas(size=(gridSize, gridSize),
                     background_color='white',
                     key='canvas')],
          [sg.Button('Run'),sg.Button('Stop'),sg.Button('Step')],
          [sg.Button('Reset'), sg.Exit()]
          ]

window = sg.Window('GridMaker', layout, resizable=True, finalize=True)
gd = window['canvas']



def drawGrid():

    gd.TKCanvas.create_rectangle(
        1, 1, gridSize, gridSize, outline='BLACK', width=1)
    
    for x in range(size):
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

    tmp = mp.getMap()

    for row in range(tmp.shape[0]):
        for column in range(tmp.shape[1]):
            # Empty
            if(tmp[column][row] == 0):
                drawCell((cellSize*row), (cellSize*column), 'WHITE')

            # Wall
            if(tmp[column][row] == 1):
                drawCell((cellSize*row), (cellSize*column), 'GREY')

            # Goal
            if(tmp[column][row] == 4):
                drawCell((cellSize*row), (cellSize*column), 'GREEN')

            # Bug
            if(tmp[column][row] == 3):
                drawCell((cellSize*row), (cellSize*column), 'RED')

            # Visited
            if(tmp[column][row] == 2):
                drawCell((cellSize*row), (cellSize*column), 'YELLOW')

# def update():
#     drawCell((cellSize*bug[0]), (cellSize*bug[1]), 'RED')
#     drawCell((cellSize*bugPrev[0]), (cellSize*bugPrev[1]), 'YELLOW')


def init():

    mp.build()
    drawGrid()
    drawMap()

    # global bug
    # bug = [0,0]
    #
    # setMap()
    # map[bug[0],bug[1]] = 3
    # map[goal[0],goal[1]] = 4
    # openSet.put(bug)

# def moveBug():
    # global bugPrev
    # bugPrev = bug.copy()
    #
    # map[bug[0]][bug[1]] = 2
    # bug[0] += 1
    # bug[1] += 1
    # map[bug[0],bug[1]] = 3
    # update()



init()

while True:             # Event Loop
    event, values = window.read()
    
    if event in (None, 'Exit'):
        break

    # if event in ('Step'):
        # moveBug()
        # if solution:
        #     break

    if event in ('Reset'):
        init()
        
window.close()
