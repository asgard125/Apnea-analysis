from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status, viewsets
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView, ListCreateAPIView)
from django.shortcuts import get_object_or_404, render
from .models import Patient, Experiment, Result
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PatientListSerializer, PatientSerializer, SelectedWriteSerializer, ResultSerializer
from .prediction import create_docx
from rest_framework.parsers import FormParser, MultiPartParser
from .serializer import FileUploadSerializer
import glob
import os
import pandas as pd
from .comparison import calc


def index(request):
    return render(request, "index.html")


def PredictResult(request):
    res = ""
    res = calc()
    print(res)
    create_docx(res)

    result = Result.objects.create(
            prediction = res
            ) 

    file_path = 'result.docx'
    with open(file_path,'rb') as doc:
        response = HttpResponse(doc.read(), content_type='application/ms-word')
        response['Content-Disposition'] = 'attachment;filename=result.docx'
        return response


class ResultJSON(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


def predict(request):
    res = ""
    create_docx(res)
    file_path = 'result.docx'
    with open(file_path,'rb') as doc:
        response = HttpResponse(doc.read(), content_type='application/ms-word')
        response['Content-Disposition'] = 'attachment;filename=result.docx'
        return response


class ListSelected(ListCreateAPIView):

    patients = Patient.objects.all()

    serializer_class = SelectedWriteSerializer

    patient_id = 1

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer = SelectedWriteSerializer(data=request.data, partial=True)

            if serializer.is_valid():
                instance = serializer.save()

            response_data = serializer.data
            response_data['id'] = instance.id
            print(response_data)

            print("response_data['id'] = ", response_data['id'])

            global patient_id

            patient_id = response_data['id']
            PredictResult(request)

            #print(serializer)
            #print(serializer.initial_data['id'])
            #selected_patient = request.POST.get("id")
            #print("selected_patient = ", selected_patient)
            #patients = Patient.objects.all().filter(id = selected_patient)
            #predict(request)
            return Response(status=status.HTTP_200_OK)

    queryset = patients.filter(id=patient_id)
    serializer_class = PatientSerializer


class PatientList(ListCreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = PatientListSerializer


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

