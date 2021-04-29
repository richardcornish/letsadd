from django.contrib import admin
from django.urls import include, path

from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', include('add.urls')),
    path('series/', include('series.urls')),
    path('counter/', include('counter.urls')),
    path('initial/', include('initial.urls')),
    path('oscars/', include('oscars.urls')),
    path('random/', include('rando.urls')),
    path('', home, name='home'),
]
