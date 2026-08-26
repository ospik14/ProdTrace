from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import User

# only for admins
class WorkerList(APIView):
    def get(self, request):
        workers = User.objects.filter(role=3)