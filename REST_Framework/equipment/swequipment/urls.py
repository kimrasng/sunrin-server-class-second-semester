from django.urls import path
from .views import helloAPI, equipmentsAPI, equimentAPI

urlpatterns = [
	path('hello/', helloAPI),
    path('equipments/', equipmentsAPI),
    path('equipment/<int:id>/', equimentAPI)
]
