from django.views.generic.base import TemplateView
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.core import management, serializers

# Create your views here.
def index(request):
	return render(request, 'alg/index.html')

def ShortestPathMain(request):
    #this page will be static
    return render(request, 'alg/ShortestPathMain.html')

def ShortestPathGame(request,id):
    amtNodes = id
    testvar = 'hello'
    #this will generate a random graph with amtNodes & random edges/weights
    # THEN i'll run dijkstra's on it & save the shortest path value
    #it will then give the page an adjacency list of the graph & the shortest path value
    #probably should just generate a json file & put in static every time
    return render(request, 'alg/ShortestPathGame.html',{
    'testvar':testvar
    })

def ShortestPathResult(request):
    testvar = 'hello'
    #???? I'm unsure what i'll do here..
    return render(request, 'alg/ShortestPathResult.html',{
    'testvar':testvar
    })

def dijkstra(request):
	return render(request, 'alg/dijkstra.html')
