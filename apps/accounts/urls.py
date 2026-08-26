from django.urls import path
from .views import WorkerList

urlpatterns = [
    path('workers/', WorkerList.as_view())
]