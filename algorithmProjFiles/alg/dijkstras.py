#!/usr/bin/python
# -*- coding: utf-8 -*-

def insert(total,node,d):
    newParentNum = (len(total)-1)/2
    parent = total[newParentNum] #node
    nodeNum = len(total)
    total += [node] #add all unfound nodes to total
    while d[parent] > d[node] and not nodeNum==0:
        total[newParentNum] = node
        total[nodeNum] = parent
        #We switch them
        nodeNum = newParentNum #assign new index
        newParentNum = (nodeNum-1)/2
        parent = total[newParentNum]
    return total

def getMin(total,d):
    minHeap = total[0] #get min!
    indexofEnd = len(total)-1 #find the last index
    total[0] = total[indexofEnd] #REPLACE!
    total = total[:-1]
    nodeNum = 0 #current place of this node
    currentNode = total[0] #current node
    end = False
    if 2*nodeNum+1 > len(total)-1: #NO CHILDREN!
        end = True
    elif 2*nodeNum+2 > len(total)-1: #Has 1 child (at 2*nodeNum+1)
        if d[total[2*nodeNum+1]] < d[currentNode]:
            newNode = total[2*nodeNum+1]
            total[nodeNum] = newNode
            total[2*nodeNum+1] = currentNode
        end = True
    while end == False and (d[total[2*nodeNum+1]] < d[currentNode] or d[total[2*nodeNum+2]] < d[currentNode]):
        if d[total[2*nodeNum+1]] < d[total[2*nodeNum+2]]:
            newNode = total[2*nodeNum+1]
            total[nodeNum] = newNode
            total[2*nodeNum+1] = currentNode
            #switchin em!
            nodeNum = 2*nodeNum+1
        else:
            newNode = total[2*nodeNum+2]
            total[nodeNum] = newNode
            total[2*nodeNum+2] = currentNode
            #switchin em!
            nodeNum = 2*nodeNum+2
        if 2*nodeNum+1 > len(total)-1: #NO CHILDREN!
            end = True
        elif 2*nodeNum+2 > len(total)-1: #Has 1 child (at 2*nodeNum+1)
            if d[total[2*nodeNum+1]] < d[currentNode]:
                newNode = total[2*nodeNum+1]
                total[nodeNum] = newNode
                total[2*nodeNum+1] = currentNode
            end = True
    return (minHeap,total)


def decrease(total,node,d):
    #idea: compare against parent and switch until done
    nodeNum = total.index(node) #find current index
    if not nodeNum == 0:
        newParentNum = (nodeNum-1)/2
        parent = total[newParentNum] #node
        while d[parent] > d[node] and not nodeNum==0:
            total[newParentNum] = node
            total[nodeNum] = parent
            #We switch them
            nodeNum = newParentNum #assign new index
            newParentNum = (nodeNum-1)/2
            parent = total[newParentNum]
    return total


def dijkstras(graph,s,t):
    found = False # set this true once we find shortest path
    path = {} # use this to save shortest path
    d = {} # empty dictionary to store distance
    total = [] # this will hold a binary heap!
    edgesFromS = [] #first step: update distances for edges out of s
    eFS = {}
    for j in range(0,len(graph[s])):
        edgesFromS += [graph[s][j][0]]
        eFS[graph[s][j][0]] = graph[s][j][1]
        path[graph[s][j][0]] = 0
    for node in graph.keys():
        if node in edgesFromS:
            d[node] = eFS[node] #saved from previous loop
        else:
            d[node] = float("inf") #set all other distances to infinity
        if not node == 0:
            if len(total)>0:
                total = insert(total,node,d)
            else:
                total+=[node] #first thing in binary heap!
    d[s] = 0
    stored = [s]
    while found == False:
        if len(total)>1:
            minHeap,total = getMin(total,d)
        else:
            minHeap = total[0]
        u = minHeap
        #get rid of the min & fix the heap
        for i in range(0,len(graph[u])): # edges of u
            newdist = d[u] + graph[u][i][1] # distance to u + dist(u,i)
            currentdist = d[graph[u][i][0]] # current dist to i
            if newdist < currentdist:
                d[graph[u][i][0]] = newdist
                path[graph[u][i][0]] = u #so we can find the path @ the end
                total = decrease(total,graph[u][i][0],d)
        if u == t:
            found = True #end loop if we reach t!
    m = t
    shortestPath = [] #this will hold shortest
    findPath = False
    while findPath == False:
        if m == 0:
            shortestPath.remove(0)
            findPath = True
        else:
            shortestPath += [path[m]]
            m = path[m]
    shortestPath.sort()
    return shortestPath
