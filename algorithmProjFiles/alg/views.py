from django.views.generic.base import TemplateView
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.core import management, serializers
import json

# Create your views here.
def index(request):
	return render(request, 'alg/index.html')

def ShortestPathMain(request):
    #this page will be static
    return render(request, 'alg/ShortestPathMain.html')

def ShortestPathGame(request):
	shortestpath = []
	example = {"nodes":[{"id": "1", "group": 1},{"id":"2","group":1}], "links":[{"source": "1", "target": "2", "value": 1}]}
	#Now, run thru all steps. Create random graph & run dijkstras
	#Give graph (IN JSON FORMAT) to graph.json & create list of nodes of shortest path
	with open('algorithmProj/static/graph.json', 'w') as fp:
		json.dump(example, fp)
	return render(request, 'alg/ShortestPathGame.html',{
    'shortestpath':shortestpath
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
