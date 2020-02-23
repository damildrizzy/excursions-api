from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Excursion
from django.views import View
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import  ExcursionSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import  Http404
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    return HttpResponse("working")


class ExcursionList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        excursions = Excursion.objects.all()
        serializer = ExcursionSerializer(excursions, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class ExcursionDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, format=None):
        try:
            excursion = Excursion.objects.get(pk=pk)
        except Excursion.DoesNotExist:
            raise Http404
        serializer = ExcursionSerializer(excursion)
        return Response(serializer.data, status = status.HTTP_200_OK)


    
    def put(self, request, pk):
        try:
            excursion = Excursion.objects.get(pk=pk)
        except Excursion.DoesNotExist:
            raise Http404
        serializer = ExcursionSerializer(excursion, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)