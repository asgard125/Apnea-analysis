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
from rest_framework.parsers import FormParser, MultiPartParser
from .serializer import FileUploadSerializer


def index(request):
    return render(request, "index.html")
 

def predict(request):
    create_docx()
    checked_items = request.POST.getlist("item_checkbox")
    print(checked_items)
    file_path = 'result.docx'
    with open(file_path,'rb') as doc:
        response = HttpResponse(doc.read(), content_type='application/ms-word')
        response['Content-Disposition'] = 'attachment;filename=result.docx'
        return response


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

