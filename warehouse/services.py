from django.db import transaction
from .models import StockOperation, Part
from .serializers import StockOperationSerializer

def issuance_processing(serializer: StockOperationSerializer):
    data = serializer.data
    part = Part.objects.get(id=data['id'])

    if data['operation_type'] == 1:
        with transaction.atomic():
            part.quantity += data['quantity']
            serializer.save()
            return data

    if part.quantity >= data['quantity']:
        with transaction.atomic():
            part.quantity -= data['quantity']
            serializer.save()
            return data
