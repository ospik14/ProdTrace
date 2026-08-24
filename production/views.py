from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import DroneModelsSerializer
from .models import DroneModels

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
