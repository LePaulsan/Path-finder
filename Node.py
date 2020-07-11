class Node:
    classCounter = 0
    def __init__(self, loc):
        self.id = Node.classCounter
        self.loc = loc

        Node.classCounter += 1 

    def __repr__(self):
        return f" {self.id}: ({self.loc[0]}, {self.loc[1]})"