from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Part, StockOperation
from .serializers import PartSerializer, StockOperationSerializer
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
        serializer = StockOperationSerializer(data=request.data)

        if serializer.is_valid():
            issuance_processing(serializer.validated_data, pk)
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        part = Part.objects.get(pk=pk)
        part.delete()

        return Response(status=204)

class OperationList(APIView):
    def get(self, request):
        operations = StockOperation.objects.all()
        serializer = StockOperationSerializer(operations, many=True)

        return Response(serializer.data)