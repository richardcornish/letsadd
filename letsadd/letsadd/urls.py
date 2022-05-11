from django.contrib import admin
from django.urls import include, path

from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', include('add.urls')),
    path('series/', include('series.urls')),
    path('clicker/', include('clicker.urls')),
    path('initial/', include('initial.urls')),
    path('oscars/', include('oscars.urls')),
    path('random/', include('rando.urls')),
    path('alphabetize/', include('alphabetize.urls')),
    path('warhammer/', include('warhammer.urls')),
    path('choices/', include('choices.urls')),
    path('twilidator/', include('twilidator.urls')),
    path('fetch/', include('fetch.urls')),
    path('geocode/', include('geocode.urls')),
    path('haversine/', include('haversine.urls')),
    path('agents/', include('agents.urls')),
    path('csvexporter/', include('csvexporter.urls')),
    path('counter/', include('counter.urls')),
    path('', home, name='home'),
]
