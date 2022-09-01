import numpy as np

wallThreshold = 60  # Percent of tiles that should be open

class cord:
    def __init__(self, row:int, col:int):
        self.row = row
        self.col = col

class Map:
    def __init__(self, size):
        self.size = size
        self.start = cord(0, 0)
        self.goal = cord(size - 1, size - 1)
        
    def build(self):
        self.map = np.random.randint(100, size = (self.size, self.size))

        for row in range(self.map.shape[0]):
            for col in range(self.map.shape[1]):
                if(self.map[col][row] > wallThreshold):
                    self.map[col][row] = 1
                else:
                    self.map[col][row] = 0
                    
    def getMap(self):
        return self.map
