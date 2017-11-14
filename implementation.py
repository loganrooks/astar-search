#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections

def idToLocation(id, width):
    return (id%width, id // width)

EXAMPLE_OBSTACLES = [idToLocation(id, width=30) for id in \
                     [21,22,51,52,81,82,93,94,111,112,123,124,133, \
                      134,141,142,153,154,163,164,171,172,173,174, \
                      175,183,184,193,194,201,202,203,204,205,213, \
                      214,223,224,243,244,253,254,273,274,283,284, \
                      303,304,313,314,333,334,343,344,373,374,403, \
                      404,433,434]]

class Graph:
    def __init__(self):
        self._edges = {}
        self._nodes = {}
        
    def getNeighbours(self, node):
        return self.edges[node._location]
    

class Node:
    def __init__(self, location):
        self._location = location
        self._origin
        self._costFromStart
        self._costToGoal
    
    def getLocation(self):
        return self._location
    
    def setLocation(self, location):
        self._location = location
        
    def getOrigin(self):
        return self._origin
    
    def setOrigin(self, originNode):
        self._origin = originNode
    
    def getCostFromStart(self):
        return self._costFromStart
    
    def setCostFromStart(self, startNode):
        startLocation = startNode.getLocation
        self._costFromStart = abs(startLocation[0] - self._location[0]) \
                            + abs(startLocation[1] - self._location[1]) 
                            
    def getCostToGoal(self):
        return self._costFromStart
    
    def setCostToGoal(self, startNode):
        startLocation = startNode.getLocation
        self._costFromStart = abs(startLocation[0] - self._location[0]) \
                            + abs(startLocation[1] - self._location[1]) 
                            
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
        neighbours = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        neighbours = filter(self.isInBounds, neighbours)
        neighbours = filter(self.isPassable, neighbours)
        return neighbours
    
    def draw(self, path=[]):
        for y in range(self._height):
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
        
        

        
    
    
        
        
                
        


