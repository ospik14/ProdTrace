from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import DroneModelsSerializer, DroneSerializer, StagesSerializer
from .models import DroneModels, Drone, ProductionStages

class DronModelList(APIView):
    def get(self, request):
        data = DroneModels.objects.all()
        serializer = DroneModelsSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = DroneModelsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        drone_model = DroneModels.objects.get(pk=pk)
        serializer = DroneModelsSerializer(drone_model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        drone_model = DroneModels.objects.get(pk=pk)
        drone_model.delete()

        return Response(status=204)

class DroneList(APIView):
    def get(self, request):
            data = Drone.objects.all()
            serializer = DroneSerializer(data, many=True)
    
            return Response(serializer.data)

    def post(self, request):
        serializer = DroneSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        drone = Drone.objects.get(pk=pk)
        serializer = DroneSerializer(drone, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
            drone = Drone.objects.get(pk=pk)
            drone.delete()
    
            return Response(status=204)


class StageList(APIView):
    def get(self, request):
        data = ProductionStages.objects.all()
        serializer = StagesSerializer(data, many=True)
     
        return Response(serializer.data)

    def post(self, request):
        serializer = StagesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        return Response(serializer.errors, status=400)