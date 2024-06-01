from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status, viewsets
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView, ListCreateAPIView)
from django.shortcuts import get_object_or_404, render
from .models import Patient, Experiment
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PatientListSerializer, PatientSerializer
from .prediction import model


def index(request):
    return render(request, "index.html")
 
def postuser(request):
    checked_items = request.POST.getlist("item_checkbox")
    return HttpResponse(f"<h2>Selected: {checked_items}</h2>") 


class PatientList(ListCreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = PatientListSerializer

# Create your views here.
