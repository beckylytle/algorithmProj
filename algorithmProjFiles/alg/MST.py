#!/usr/bin/python
# -*- coding: utf-8 -*-

def construct(graph):
    adjGraph = {}
    d = {}
    e = {}
    heap = [0]
    for node in graph["nodes"]:
        adjGraph[int(node["id"])] = []
        d[int(node["id"])] = float("inf") #every vertex is infinity away
        e[int(node["id"])] = None
    for node in graph["nodes"]:
        if not node["id"] == "0":
            heap = insert(heap,int(node["id"]),d) #add to heap
    for edge in graph["links"]:
        a = int(edge["source"])
        b = int(edge["target"])
        weight = int(edge["value"])
        adjGraph[a] += [(b,weight)]
        adjGraph[b] += [(a,weight)]
        #d[(a,b)] = float("inf") #set every edge weight to infinity
        #heap = insert(heap,(a,b),d) #put every edge in the heap
        # a < b by construction
    return adjGraph,d,e,heap

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

def prims(graph):
    tree = []
    found = []
    graph,d,e,heap = construct(graph) #Create proper adjacency list from json object, make heap, compute distances
    while len(found)<len(graph.keys()):
        if len(heap) > 1:
            print heap
            current,heap = getMin(heap,d)
        else:
            current = heap[0]
        if not e[current] == None:
            tree += [e[current]]
        found += [current]
        for edge in graph[current]:
            vertex=edge[0]
            weight=edge[1]
            if vertex in heap:
                if weight < d[vertex]: #if this edge is shorter than previous edge to this vertex
                    d[vertex] = weight
                    e[vertex] = (current,vertex)
                    heap = decrease(heap,vertex,d)
    #now we must format it for proper javascript input
    output = ""
    for link in tree:
        if link[0] < link[1]:
            output += (str(link[0]+1)+str(link[1]+1))+","
        else:
            output += (str(link[1]+1)+str(link[0]+1))+","
    #we add +1 to all the vertexes so we dont have a vertex 0 anymore
    return output[:-1]


graph = {'nodes': [{'group': 2, 'id': '0'}, {'group': 2, 'id': '1'}, {'group': 2, 'id': '2'}, {'group': 2, 'id': '3'}, {'group': 2, 'id': '4'}, {'group': 2, 'id': '5'}, {'group': 2, 'id': '6'}, {'group': 2, 'id': '7'}, {'group': 2, 'id': '8'}, {'group': 2, 'id': '9'}, {'group': 2, 'id': '10'}, {'group': 2, 'id': '11'}], 'links': [{'source': '0', 'target': '1', 'value': 5}, {'source': '1', 'target': '3', 'value': 8}, {'source': '2', 'target': '8', 'value': 18}, {'source': '3', 'target': '6', 'value': 6}, {'source': '4', 'target': '2', 'value': 7}, {'source': '5', 'target': '4', 'value': 19}, {'source': '6', 'target': '9', 'value': 5}, {'source': '7', 'target': '10', 'value': 3}, {'source': '8', 'target': '7', 'value': 12}, {'source': '9', 'target': '5', 'value': 17}, {'source': '10', 'target': '11', 'value': 13}, {'source': '0', 'target': '4', 'value': 9}, {'source': '2', 'target': '10', 'value': 13}, {'source': '4', 'target': '3', 'value': 3}, {'source': '6', 'target': '5', 'value': 15}, {'source': '8', 'target': '11', 'value': 18}, {'source': '10', 'target': '9', 'value': 16}]}
print prims(graph) #get the MST
