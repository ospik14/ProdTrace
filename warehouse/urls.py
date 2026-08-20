from django.urls import path
from .views import PartList, PartsDelivery

urlpatterns = [
    path('parts/', PartList.as_view()),
    path('parts/<int:pk>/', PartsDelivery.as_view())
]