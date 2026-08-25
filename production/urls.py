from django.urls import path
from .views import DronModelList, DroneList, StageList

urlpatterns = [
    path('drone_models/', DronModelList.as_view()),
    path('drone_models/<int:pk>/', DronModelList.as_view()),
    path('drone/', DroneList.as_view()),
    path('drone/<int:pk>/', DroneList.as_view()),
    path('stages/', StageList.as_view())

]