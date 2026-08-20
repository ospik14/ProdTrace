from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Part
from .serializers import PartSerializer
from .services import issuance_processing

class PartList(APIView):
    def get(self, request):
        parts = Part.objects.all()
        serializer = PartSerializer(parts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

class PartsDelivery(APIView):
    def post(self, request, pk):
        serializer = PartSerializer(data=request.data)

        if serializer.is_valid():
            return issuance_processing(serializer)

        return Response(serializer.errors, status=400)