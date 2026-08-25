from django.urls import path
from .views import PartList, PartsDelivery, OperationList

urlpatterns = [
    path('parts/', PartList.as_view()),
    path('parts/<int:pk>/', PartsDelivery.as_view()),
    path('operations/', OperationList.as_view())
]