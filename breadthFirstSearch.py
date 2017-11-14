#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from implementation import *

def breadthFirstSearch(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    cameFrom = {}
    cameFrom[start] = None
    
    if (goal in graph.getObstacles()): raise ValueError("Goal cannot be an obstacle.")
    
    while not frontier.isEmpty():
        currentNode = frontier.get()
        
        if currentNode == goal: break
    
        for nextNode in graph.getNeighbours(currentNode):
            if nextNode not in cameFrom:
                frontier.put(nextNode)
                cameFrom[nextNode] = currentNode
        
    return cameFrom
    


if __name__ == "__main__":
    graph = SquareGrid(30, 15, EXAMPLE_OBSTACLES)

    start = (0,0)
    goal = (25, 2)
    cameFrom = breadthFirstSearch(graph, start, goal)
    path = constructPath(cameFrom, start, goal)
    graph.draw(path)
    
    
