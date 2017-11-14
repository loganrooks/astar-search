#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from implementation import *

def taxiCabDistance(locationA, locationB):
    return abs(locationA[0] - locationB[0]) + \
            abs(locationA[1] - locationB[1])
    


def aStarSearch(graph, startNode, goalNode, heuristic=taxiCabDistance):
    frontier = PriorityQueue()
    frontier.put(startNode, 0)
    cameFrom = {}
    cameFrom[startNode] = None
    cost = {}
    cost[startNode] = 0
    
    while not frontier.isEmpty():
        currentNode = frontier.get()
        
        if currentNode == goalNode:
            break
        
        for nextNode in graph.getNeighbours(currentNode):
            newCost = cost[currentNode] + graph.cost(currentNode, nextNode)
            if nextNode not in cost or newCost < cost[nextNode]:
                cost[nextNode] = newCost + heuristic(goalNode, nextNode)
                frontier.put(nextNode, cost[nextNode])
                cameFrom[nextNode] = currentNode
    return cameFrom, cost

if __name__ == "__main__":
    start = (0, 0)
    goal = (26, 3)
    weightedGraph = WeightedGrid(30, 15, EXAMPLE_OBSTACLES)
    cameFrom, cost = aStarSearch(weightedGraph, start, goal)
    path = constructPath(cameFrom, start, goal)
    weightedGraph.draw(path)
