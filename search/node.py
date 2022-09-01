class Node:
    def __init__(self):
        self.fCost = 1
        self.gCost = 0
        self.location = [0,0]
        self.closed = False
        self.cameFrom = Node()


