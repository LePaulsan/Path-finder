from Stack import Stack

class PathFinder:
    def __init__(self, graph, start, end):
        self.graph = graph.graph
        self.start = graph.nodeDicLoc[start]
        self.end = graph.nodeDicLoc[end]
        self.treversedStack = Stack()
        self.wentNode = []
        self.done = False
        self.takeStep(self.start, self.end)

    def takeStep(self, start, end):
        if self.isInList(start, self.wentNode):
            return
        self.treversedStack.push(start)  
        self.wentNode.append(start)
        
        if start == end:
            self.done = True
            return

        connectedNodes = self.graph[start]

        for node in connectedNodes:
            if self.done:
                return
            self.takeStep(node, end)
            if self.done:
                return
        
        _ = self.treversedStack.pop()
        return

    @staticmethod
    def isInList(item, l):
        for thing in l:
            if item == thing:
                return True

        return False