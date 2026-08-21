from rest_framework.response import Response
from rest_framework.views import exception_handler
from .exceptions import InsufficientStockError

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response

    if isinstance(exc, InsufficientStockError):
        return Response(
            {
                'error': 'insufficient_stock'
            },
            status=409,
        )

    return None