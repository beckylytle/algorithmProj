from django.views.generic.base import TemplateView
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.core import management, serializers
import json
import random
from dijkstras import *
from MST import *

# Create your views here.
def index(request):
	return render(request, 'alg/index.html')

def ShortestPathMain(request):
    #this page will be static
    return render(request, 'alg/ShortestPathMain.html')

def MST(request):
	#example = {"nodes":[{"id": "1", "group": 1},{"id":"2","group":1}], "links":[{"source": "1", "target": "2", "value": 1}]}
	graph = {"nodes":[], "links":[]}
	numNodes = random.randint(9,14)
	for i in range(0,numNodes):
		if i == 0:
			graph["nodes"] += [{"id":str(i), "group":2}] #make all groups the same
		elif i == numNodes-1:
			graph["nodes"] += [{"id":str(i), "group":2}]
		else:
			graph["nodes"] += [{"id":str(i), "group":2}]
	needed = list(range(numNodes)) #all nodes included
	Special = list(range(numNodes))
	needed.remove(0)
	Special.remove(0)
	Special.remove(numNodes-1)
	Special.remove(numNodes-2)
	needed2 = list(range(numNodes)) #all nodes included
	Special2 = list(range(numNodes))
	needed2.remove(0)
	Special2.remove(0)
	Special2.remove(numNodes-1)
	Special2.remove(numNodes-2)
	edges = {}
	edges2 = {}
	for j in range(0,numNodes):
		edges[j] = [] #adjacencylist
		edges2[j] = [] #adjacencylist2
	for i in range(0,numNodes):
		if not i == numNodes - 1 and not len(needed) == 0: #we only want edges coming out of previous nodes
		#{"source": "1", "target": "2", "value": 1}
			edgeWeight = random.randint(1,20)
			if i == 0:
				targetval = random.choice(Special)
			else:
				targetval = random.choice(needed)
			#needed.remove(targetval)
			#first = str(targetval)
			cont = True
			counter = 0
			while (targetval in edges[i] or i in edges[targetval] or i == targetval) and cont==True:
				targetval = random.choice(needed)
				counter += 1
				if counter > 100:
					cont = False #infinite loop
			if cont == True:
				needed.remove(targetval)
				edges[i] += [targetval]
				edges2[i] += [(targetval,edgeWeight)]
				first = str(targetval)
				graph["links"] += [{"source":str(i),"target":first,"value":edgeWeight}]
	for i in range(0,numNodes):
		if not i == numNodes - 1 and not len(needed2) == 0 and i%2 == 0: #we only want edges coming out of previous nodes
		#{"source": "1", "target": "2", "value": 1}
			edgeWeight = random.randint(1,20)
			if i == 0:
				targetval = random.choice(Special2)
			else:
				targetval = random.choice(needed2)
			#needed.remove(targetval)
			#first = str(targetval)
			cont = True
			counter = 0
			while (targetval in edges[i] or i in edges[targetval] or i == targetval) and cont==True:
				targetval = random.choice(needed2)
				counter += 1
				if counter > 100:
					cont = False #infinite loop
			if cont ==True:
				needed2.remove(targetval)
				edges[i] += [targetval]
				edges2[i] += [(targetval,edgeWeight)]
				first = str(targetval)
				graph["links"] += [{"source":str(i),"target":first,"value":edgeWeight}]
	#shortestpath = dijkstras(edges2,0,numNodes-1) #call function to run this
	MST = prims(graph)
	graph = increment(graph)
	return render(request, 'alg/MST.html',{
    'graph':graph, 'MST':MST,
    })

def increment(graph):
	for node in graph["nodes"]:
		node["id"] = str(int(node["id"])+1)
	for edge in graph["links"]:
		a = str(int(edge["source"])+1)
		b = str(int(edge["target"])+1)
		edge["source"] = a
		edge["target"] = b
	return graph
	#example = {"nodes":[{"id": "1", "group": 1},{"id":"2","group":1}], "links":[{"source": "1", "target": "2", "value": 1}]}

def ShortestPathGame(request):
	#example = {"nodes":[{"id": "1", "group": 1},{"id":"2","group":1}], "links":[{"source": "1", "target": "2", "value": 1}]}
	graph = {"nodes":[], "links":[]}
	numNodes = random.randint(8,13)
	for i in range(0,numNodes):
		if i == 0:
			graph["nodes"] += [{"id":str(i), "group":1}]
		elif i == numNodes-1:
			graph["nodes"] += [{"id":str(i), "group":3}]
		else:
			graph["nodes"] += [{"id":str(i), "group":2}]
	needed = list(range(numNodes)) #all nodes included
	Special = list(range(numNodes))
	needed.remove(0)
	Special.remove(0)
	Special.remove(numNodes-1)
	Special.remove(numNodes-2)
	needed2 = list(range(numNodes)) #all nodes included
	Special2 = list(range(numNodes))
	needed2.remove(0)
	Special2.remove(0)
	Special2.remove(numNodes-1)
	Special2.remove(numNodes-2)
	edges = {}
	edges2 = {}
	for j in range(0,numNodes):
		edges[j] = [] #adjacencylist
		edges2[j] = [] #adjacencylist2
	for i in range(0,numNodes):
		if not i == numNodes - 1 and not len(needed) == 0: #we only want edges coming out of previous nodes
		#{"source": "1", "target": "2", "value": 1}
			edgeWeight = random.randint(1,20)
			if i == 0:
				targetval = random.choice(Special)
			else:
				targetval = random.choice(needed)
			#needed.remove(targetval)
			#first = str(targetval)
			cont = True
			counter = 0
			while (targetval in edges[i] or i in edges[targetval] or i == targetval) and cont==True:
				targetval = random.choice(needed)
				counter += 1
				if counter > 100:
					cont = False #infinite loop
			if cont == True:
				needed.remove(targetval)
				edges[i] += [targetval]
				edges2[i] += [(targetval,edgeWeight)]
				first = str(targetval)
				graph["links"] += [{"source":str(i),"target":first,"value":edgeWeight}]
	for i in range(0,numNodes):
		if not i == numNodes - 1 and not len(needed2) == 0 and i%2 == 0: #we only want edges coming out of previous nodes
		#{"source": "1", "target": "2", "value": 1}
			edgeWeight = random.randint(1,20)
			if i == 0:
				targetval = random.choice(Special2)
			else:
				targetval = random.choice(needed2)
			#needed.remove(targetval)
			#first = str(targetval)
			cont = True
			counter = 0
			while (targetval in edges[i] or i in edges[targetval] or i == targetval) and cont==True:
				targetval = random.choice(needed2)
				counter += 1
				if counter > 100:
					cont = False #infinite loop
			if cont ==True:
				needed2.remove(targetval)
				edges[i] += [targetval]
				edges2[i] += [(targetval,edgeWeight)]
				first = str(targetval)
				graph["links"] += [{"source":str(i),"target":first,"value":edgeWeight}]
	shortestpath = dijkstras(edges2,0,numNodes-1) #call function to run this
	#Now, run thru all steps. Create random graph & run dijkstras
	#Give graph (IN JSON FORMAT) to graph.json & create list of nodes of shortest path
	short = ""
	for value in shortestpath:
		short += str(value)
	shortestpath = "[" + short + "]"
	newgraph = str(graph)
	with open('algorithmProj/static/graph.json', 'w') as fp:
		json.dump(graph, fp)
	return render(request, 'alg/ShortestPathGame.html',{
    'shortestpath':shortestpath, 'newgraph':newgraph
    })

def ShortestPathResult(request):
    testvar = 'hello'
    #???? I'm unsure what i'll do here..
    return render(request, 'alg/ShortestPathResult.html',{
    'testvar':testvar
    })

def dijkstra(request):
	return render(request, 'alg/dijkstra.html')



"""
EXAMPLE json

{
  "nodes": [
	{"id": "1", "group": 1, "clicked":'False'},
	{"id": "2", "group": 2, "clicked":'False'},
	{"id": "3", "group": 2, "clicked":'False'},
	{"id": "4", "group": 2, "clicked":'False'},
	{"id": "5", "group": 2, "clicked":'False'},
	{"id": "6", "group": 2, "clicked":'False'},
	{"id": "7", "group": 2, "clicked":'False'},
	{"id": "8", "group": 2, "clicked":'False'},
	{"id": "9", "group": 2, "clicked":'False'},
	{"id": "10", "group": 2, "clicked":'False'},
	{"id": "12", "group": 1, "clicked":'False'},
  ],
  "links": [
	{"source": "1", "target": "2", "value": 1},
	{"source": "1", "target": "3", "value": 6},
	{"source": "2", "target": "5", "value": 10},
	{"source": "3", "target": "4", "value": 6},
	{"source": "3", "target": "5", "value": 8},
	{"source": "5", "target": "6", "value": 4},
	{"source": "2", "target": "6", "value": 5},
	{"source": "4", "target": "7", "value": 1},
#    {"source": "6", "target": "7", "value": 6},
	{"source": "7", "target": "8", "value": 10},
	{"source": "5", "target": "8", "value": 6},
	{"source": "6", "target": "9", "value": 8},
	{"source": "7", "target": "9", "value": 4},
	{"source": "4", "target": "9", "value": 5},
	{"source": "9", "target": "10", "value": 6},
	{"source": "10", "target": "8", "value": 10},
	{"source": "8", "target": "12", "value": 4},
	{"source": "7", "target": "12", "value": 5},
  ]
}
"""


"""	# NumNodes = random number from 8 to 16?
	# EdgeWeight = random number from 1 thru 20?
	# Every node must have at least one thing coming OUT of it and at least one thing going INTO it
	# Preferably, most will have 2 coming in / 1 going out (or vise versa)
	# All edges go from LESSER NODE --> BIGGER NODE
    # THEN i'll run dijkstra's on it & save the shortest path value!!! as a list
    #it will then give the page an adjacency list of the graph & the shortest path value
    #probably should just generate a json file & put in static every time"""
