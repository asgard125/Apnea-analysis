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
from .prediction import model, create_docx


def index(request):
    return render(request, "index.html")
 

def postuser(request):
    create_docx()
    checked_items = request.POST.getlist("item_checkbox")
    print(checked_items)
    file_path = 'table1.docx'
    with open(file_path,'rb') as doc:
        response = HttpResponse(doc.read(), content_type='application/ms-word')
        response['Content-Disposition'] = 'attachment;filename=resut.docx'
        return response


class PatientList(ListCreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = PatientListSerializer

# Create your views here.
