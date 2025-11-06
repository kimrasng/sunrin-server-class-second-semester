from django.urls import path
from .views import helloAPI, equipmentsAPI, equimentAPI, EquimentsAPI, EquimentAPI

urlpatterns = [
	path('hello/', helloAPI),
    path('equipments/', equipmentsAPI),
    path('equipment/<int:id>/', equimentAPI),
    path('class/equipments/', EquimentsAPI.as_view()),
    path('class/equipment/<int:id>/', equimentAPI),
]
