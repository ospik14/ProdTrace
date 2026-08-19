from django.urls import path
from .views import PartList

urlpatterns = [
    path('parts/', PartList.as_view()),
    path('parts/<int:pk>/')
]