from django.db import transaction
from .models import Part, StockOperation
from .exceptions import InsufficientStockError

def issuance_processing(data: dict, pk: int):
    
    operation_type = data['operation_type']
    quantity = data['quantity']

    with transaction.atomic():
        part = Part.objects.select_for_update().get(pk=pk)

        if operation_type == 1:
            part.quantity += quantity
        elif operation_type in (2, 3):
            if part.quantity < quantity:
                raise InsufficientStockError()
            
            part.quantity -= quantity

        part.save()
        StockOperation.objects.create(**data, part=part)
    
                
