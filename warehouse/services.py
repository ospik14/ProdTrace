from django.db import transaction
from .models import Part
from .serializers import StockOperationSerializer
from .exceptions import InsufficientStockError

def issuance_processing(serializer: StockOperationSerializer, pk: int):
    serializer.save(part_id=pk)
    data = serializer.validated_data
    part = Part.objects.get(pk=pk)

    if data.get('operation_type') == 1:
        with transaction.atomic():
            part.quantity += data.get('quantity')
            part.save()
            serializer.save()
            return data

    if part.quantity >= data.get('quantity'):
        with transaction.atomic():
            part.quantity -= data.get('quantity')
            part.save()
            serializer.save()
            return data
    else:
        raise InsufficientStockError()
