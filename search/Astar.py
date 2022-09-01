class Node:
    def __init__(self):
        self.fCost = 0
        self.gCost = 0
        self.closed = False
        self.cameFrom = Node()


