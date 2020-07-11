import numpy as np
from Maze import Maze
from Mario import Mario
from Node import Node
from Graph import Graph
from PathFinder import PathFinder

WALL = "#"
PATH = " "
WENTPATH = "~"
PATHTUPLE = (
    (1, 13, 32), 
    (2, 10, 14), (2, 18, 19), (2, 31, 32),
    (3, 4, 8), (3, 11, 12), (3, 18, 19), (3, 24, 25), (3, 31, 36),
    (4,3 ,12), (4, 22, 25),
    (5, 11, 12), (5, 18, 25),
    (6, 11, 32),
    (7, 16, 19), (7, 27, 33),
    (8, 3, 22), (8, 30, 31),
    (9, 10, 15), (9, 30, 32),
    (10, 13, 15), (10, 24, 32),
    (11, 13, 19), (11, 24, 25), 
    (12, 9, 15), (12, 24, 30), 
    (13, 24, 25),
    (14, 8, 25),
    (15, 0, 9), (15, 15, 30),
    (16, 0, 1)
)
START = (16, 0)
STARTNEIGHBOORS = {
    "left": False, 
    "right": False, 
    "front": True, 
    "back": False
}

END = (3, 35)
ENDNEIGHBOORS = {
    "left": True,
    "right": False, 
    "front": False, 
    "back": False
}

maze = Maze(WALL, PATH, WENTPATH, PATHTUPLE, START, END)
graph = Graph(maze)
pathFinder = PathFinder(graph, START, END)

mario = {
    "show": "@",
    "loc": START
}

def display():
    for i in range(maze.size[0]):
        tempr = ""
        for j in range(maze.size[1]):
            tempr = tempr + maze.maze[i, j] + " "
        print(tempr)

def takeStep(y, x):
    maze.maze[mario["loc"]] = WENTPATH
    maze.maze[y, x] = mario["show"]
    mario["loc"] = (y, x)

def walkBetween(node1, node2):
    vel = (node2[0]- node1[0], node2[1]- node1[1])
    if vel[0] != 0:
        if vel[0] == 1:
            takeStep(node1[0] + 1, node1[1])

        if vel[0] > 1:
            for i in range(vel[0]):
                takeStep(node1[0] + i + 1, node1[1])
        
        if vel[0] == -1:
            takeStep(node1[0] - 1, node1[1])            

        if vel[0] < -1:
            for i in range(-vel[0]):
                takeStep(node1[0] - i - 1, node1[1])

    elif vel[1] != 0:
        if vel[1] == 1:
            takeStep(node1[0], node1[1] + 1)        
        
        if vel[1] > 1:
            for i in range(vel[1]):
                takeStep(node1[0], node1[1] + i + 1)

        if vel[1] == -1:
            takeStep(node1[0], node1[1] - 1)      
        
        if vel[1] < -1:
            for i in range(-vel[1]):
                takeStep(node1[0], node1[1] - i - 1)       


if __name__ == "__main__":
    path1 = []
    for thing in pathFinder.treversedStack.items:
        path1.append(graph.nodeDicId[thing])
    
    maze.maze[START] = mario["show"]
    for i in range(len(path1) - 1):
        walkBetween(path1[i], path1[i + 1])
    
    display()