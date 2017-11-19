#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections, heapq
from math import sqrt

def idToLocation(id, width):
    return (id%width, id // width)
        
        

EXAMPLE_OBSTACLES_01 = [idToLocation(id, width=30) for id in \
                     [21,22,51,52,81,82,93,94,111,112,123,124,133, \
                      134,141,142,153,154,163,164,171,172,173,174, \
                      175,183,184,193,194,201,202,203,204,205,213, \
                      214,223,224,243,244,253,254,273,274,283,284, \
                      303,304,313,314,333,334,343,344,373,374,403, \
                      404,433,434]]


def generateObstacles():
    obstacles = []
    for x in range(12,29):
        for y in range(25,29):
            obstacles.append((x,y))
    for x in range(25,29):
        for y in range(22,25):
           obstacles.append((x,y))
    
    for x in range(9,13):
        for y in range(16,21):
            obstacles.append((x,y))
    
    
    for x in range(18,25):
        for y in range(16,20):
            obstacles.append((x,y))
            
    for x in range(14,18):
        for y in range(11,16):
            obstacles.append((x,y))
            
    for x in range(6,13):
        for y in range(4,11):
            if (x > 13 - y):
                obstacles.append((x,y))
                
    for x in range(20,29):
        for y in range(6,20):
            if (y <= 1.625*x - 26.5):
                obstacles.append((x,y))
    return obstacles

EXAMPLE_OBSTACLES_02 = generateObstacles()



class Graph:
    def __init__(self):
        self._edges = {}
        self._nodes = {}
        
    def getNeighbours(self, node):
        return self.edges[node._location]
    

class Node:
    def __init__(self, location):
        self._location = location
        self._origin = None
    
    def getLocation(self):
        return self._location
    
    def setLocation(self, location):
        self._location = location
        
    def getOrigin(self):
        return self._origin
    
    def setOrigin(self, originNode):
        self._origin = originNode
    
    def __hash__(self):
        return hash(self._location)
    
    def __eq__(self, other):
        return self._location == other.getLocation()
                            
    
                            
class Queue:
    def __init__(self):
        self._elements = collections.deque()
        
    def isEmpty(self):
        return len(self._elements) == 0
    
    def put(self, element):
        self._elements.append(element)
        
    def get(self):
        return self._elements.popleft()
    
class SquareGrid:
    def __init__(self, width=10, height=10, obstacles=[]):
        self._width = width
        self._height = height
        self._obstacles = obstacles
    
    def isInBounds(self, location):
        (x, y) = location
        return 0 <= x < self._width and 0 <= y < self._height
    
    def isPassable(self, location):
        return location not in self._obstacles
    
    def getWidth(self):
        return self._width
    
    def setWidth(self, width):
        self._width = width
        
    def getHeight(self):
        return self._height
        
    def setHeight(self, height):
        self._height = height
    
    def setObstacles(self, obstacles, append=True):
        if append: self._obstacles.append(obstacles)
        else: self._obstacles = obstacles
        
    def getObstacles(self):
        return self._obstacles
        
    def getNeighbours(self, location):
        (x, y) = location
        neighbours = [(x+1, y), (x+1, y+1), (x+1, y-1), (x-1, y), (x-1, y+1), (x-1,y-1), (x, y+1), (x, y-1)]
        neighbours = filter(self.isInBounds, neighbours)
        neighbours = filter(self.isPassable, neighbours)
        return neighbours
    
    def draw(self, path=[]):
        for y in range(self._height - 1, -1, -1):
            for x in range(self._width):
                location = (x, y)
                print("{}".format(self._drawTile(location, path)), end="")
        
    def _drawTile(self, location, path=[]):
        tile = " "
        if location in self._obstacles:
            tile += "#"
        elif location in path:
            if location == path[0]:
                tile += "G"
            elif location == path[-1]:
                tile += "S"
            else:
                tile += "X"
        else:
            tile += " "
        if location[0] is (self._width - 1):
            tile += "\n"
        return tile
        
class PriorityQueue:
    def __init__(self):
        self._elements = []
    
    def isEmpty(self):
        return len(self._elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self._elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self._elements)[1]
    
class WeightedGrid(SquareGrid):
    

    def __init__(self, width, height, obstacles=[], weights=None):
        super().__init__(width, height, obstacles)
        self.setWeights(weights)
        
    def getWeights(self):
        return self._weights
    
    def setWeights(self, weights=None):
        if (weights == None): self._weights = self._generateDefaultWeights()
        else: self._weights = weights
    
    def cost(self, fromNode, toNode):
        return self._weights.get((fromNode, toNode), 1)
    
    def _generateDefaultWeights(self):
        weights = {}
        
        for x in range(self._width):
            for y in range(self._height):
                diagonals = ((x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1))
                for neighbour in self.getNeighbours((x,y)):
                    if neighbour in diagonals:
                        weights[((x, y), neighbour)] = sqrt(2)
                    else:
                        weights[((x, y), neighbour)] = 1
        return weights
    
    
def constructPath(cameFrom, start, goal):
    currentNode = goal
    path = [goal]
    while currentNode is not start:
        currentNode = cameFrom[currentNode]
        path.append(currentNode)
    return path
    
        

        
    
    
        
        
                
        


