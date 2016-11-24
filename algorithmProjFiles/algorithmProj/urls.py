from django.conf.urls import include, url
from django.contrib import admin
from alg import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'algorithmProj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'alg.views.index', name='index'),
    url(r'^shortestPath/main$', 'alg.views.ShortestPathMain', name = "shortestPath"),
    url(r'^shortestPath/game/(?P<id>\d+)/', 'alg.views.ShortestPathGame', name = "shortestPathGame"),
    url(r'^shortestPath/result$', 'alg.views.ShortestPathResult', name = "shortestPathResult"),
    url(r'^HowTo/$', 'alg.views.dijkstra', name = "dijkstra"),
]
