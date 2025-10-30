from django.urls import path
from .views import helloAPI, equipmentAPI

urlpatterns = [
	path('hello/', helloAPI),
    path('equipments/', equipmentAPI),
]
