from Node import Node

class Graph:
    def __init__(self, maze):
        self.maze = maze
        self.nodeList = self.createNodeList()
        self.nodeDicLoc = self.getNodeDic(self.nodeList, 0)
        self.nodeDicId = self.getNodeDic(self.nodeList, 1)
        self.edges = self.createEdge()
        self.graph = self.createGraph()

    def createNodeList(self):
        nodeList = []
        for i in range(self.maze.size[0]):
            for j in range(self.maze.size[1]):
                if self.maze.isPath(i, j):
                    neighboor = self.maze.getNeighboorDic(i, j)
                    if (neighboor["left"] or neighboor["right"]) and (neighboor["front"] or neighboor["back"]):
                        nodeList.append(Node((i, j)))
                    if (i, j) == self.maze.start or (i, j) == self.maze.end:
                        nodeList.append(Node((i, j)))

        return nodeList
    

    def createEdge(self):
        edges = []
        tempDy = self.listToDic(self.nodeList, 0, 1)
        tempDx = dict(sorted(self.listToDic(self.nodeList, 1, 0).items()))
        
        for key in tempDy:
            if len(tempDy[key]) > 1:
                for i in range(len(tempDy[key]) - 1):
                    nodeSet = (self.nodeDicLoc[(key, tempDy[key][i])], self.nodeDicLoc[(key, tempDy[key][i + 1])])
                    if self.maze.getNeighboorDic(key, tempDy[key][i])["right"]:
                        edges.append(nodeSet)

        for key in tempDx:
            if len(tempDx[key]) > 1:
                for i in range(len(tempDx[key]) - 1):
                    nodeSet = (self.nodeDicLoc[(tempDx[key][i], key)], self.nodeDicLoc[(tempDx[key][i + 1], key)])
                    # if (tempDx[key][i], key) == (10, 14):
                        # print(self.maze.getNeighboorDic(tempDx[key][i], key)["right"])
                        # print("i went here")
                    if self.maze.getNeighboorDic(tempDx[key][i], key)["back"]:
                        edges.append(nodeSet)
                        # if (tempDx[key][i], key) == (10, 14):
                            # print(self.maze.getNeighboorDic(tempDx[key][i], key)["right"])
                            # print("i went here")

        return edges

    def createGraph(self):
        tempD = {}
        for edge in self.edges:
            if not edge[0] in tempD:
                tempD[edge[0]] = [edge[1]]

            else:
                tempD[edge[0]].append(edge[1])

            if not edge[1] in tempD:
                tempD[edge[1]] = [edge[0]]

            else:
                tempD[edge[1]].append(edge[0])

        return tempD

    @staticmethod
    def listToDic(l, key, val):
        dic = {}
        for node in l:
            if not node.loc[key] in dic:
                dic[node.loc[key]] = [node.loc[val]]
            else:
                dic[node.loc[key]].append(node.loc[val])
    
        return dic

    @staticmethod
    def getNodeDic(l, type):
        dic = {}
        if type == 0:
            for node in l:
                dic[node.loc] = node.id
            return dic

        if type == 1:
            for node in l:
                dic[node.id] = node.loc
            return dic