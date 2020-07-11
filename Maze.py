import numpy as np

class Maze:
    def __init__(self, wall, path, went, pathTuple, start, end):
        self.size = (17, 36)
        self.wall = wall
        self.path = path
        self.went = went
        self.pathTuple = pathTuple
        self.start = start
        self.end = end

        self.maze = self.makeMaze()

    def makeMaze(self):
        table = self.initMaze()
        for tpl in self.pathTuple:
            table = self.makePath(table, tpl[0], tpl[1], tpl[2])
        table = self.convertToNumpy(table)
        return table

    def initMaze(self):
        matrix = []
        for _i in range(self.size[0]):
            row = ""
            for _j in range(self.size[1]):
                row += self.wall
            matrix.append(row)
        return matrix

    def makePath(self, table, row, start, end):
        if start < 0 or end > self.size[1]:
            print("You idiot, index out of range!")
            return
        
        if start >= end:
            print("Why the fuck is start >= end?!")
            return

        table[row] = table[row][:start] + self.path * (end - start) + table[row][end:]
        return table

    def isPath(self, y, x):
        if not (0 <= y < self.size[0]) or not (0 <= x < self.size[1]):
            print("Hey, what the fuck is this. One of these numer is out of range of the table")
            print(y, x)
            return None

        return self.maze[y, x] == self.path

    def isWall(self, y, x):
        if not (0 <= y < self.size[0]) or not (0 <= x < self.size[1]):
            print("Hey, what the fuck is this. One of these numer is out of range of the table")
            return None

        return self.maze[y, x] == self.wall

    def getNeighboorDic(self, y, x):
        neighboor = {}        
        if y == 0:
            neighboor["front"] = False
        else: 
            neighboor["front"] = self.isPath(y - 1, x)

        if y == self.size[0] - 1:
            neighboor["back"] = False
        else: 
            neighboor["back"] = self.isPath(y + 1, x)

        if x == 0:
            neighboor["left"] = False
        else: 
            neighboor["left"] = self.isPath(y, x - 1)

        if x == self.size[1] - 1:
            neighboor["right"] = False
        else: 
            neighboor["right"] = self.isPath(y, x + 1)

        return neighboor

    @staticmethod
    def convertToNumpy(table):
        tempL = []
        for row in table:
            row = list(row)
            tempL.append(row)
        return np.array(tempL)