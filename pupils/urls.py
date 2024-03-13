from django.urls import path
from .views import pupils, list_user

urlpatterns = [
    path('', pupils, name='pupils'),
    path('list/pupils/<int:id>/', list_user, name="list_user"),
]
