from gc import get_objects

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Equipment
from .serizlizers import EquipmentSerializer


from .models import Equipment
from .serizlizers import EquipmentSerializer

@api_view(["GET"])
def helloAPI(request):
    return Response({"msg": "hello"})

@api_view(["GET", "POST"])
def equipmentsAPI(request):
    if request.method == "GET":
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "DELETE", "PUT"])
def equimentAPI(request, id):
    equipment = get_object_or_404(Equipment, eid=id)
    if request.method == "GET":
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = EquipmentSerializer(equipment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)