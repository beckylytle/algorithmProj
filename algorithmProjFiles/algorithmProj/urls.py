from django.conf.urls import include, url
from django.contrib import admin
from algorithmProj.views import index,ShortestPathGame

urlpatterns = [
    # Examples:
    # url(r'^$', 'algorithmProj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    #url(r'^Main$', 'alg.views.ShortestPathMain', name = "shortestPath"),
    url(r'^Game$', ShortestPathGame, name = "shortestPathGame"),
    #url(r'^Result$', 'alg.views.ShortestPathResult', name = "shortestPathResult"),
    #url(r'^HowTo$', 'alg.views.dijkstra', name = "dijkstra"),
    #url(r'^graph.json$', 'alg.views.json', name = "json"),
]
