from django.urls import path
from .views import DronModelList

urlpatterns = [
    path('drone_models/', DronModelList.as_view()),
    path('drone_models/<int:pk>/', DronModelList.as_view())
]