from django.urls import include, path

from .views import home


urlpatterns = [
    path('add/', include('add.urls')),
    path('series/', include('series.urls')),
    path('counter/', include('counter.urls')),
    path('initial/', include('initial.urls')),
    path('', home, name='home'),
]
