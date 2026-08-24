from django.urls import path
from .views import DronModelList

urlpatterns = [
    path('dron_models/', DronModelList.as_view()),
]