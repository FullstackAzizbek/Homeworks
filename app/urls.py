from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('themes/', include('themes.urls')),
    path('pupils/', include('pupils.urls')),
]
