from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.
def home(request):
    return HttpResponse("Jay Ganesh!")

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
