from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status, viewsets
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView)
from django.shortcuts import get_object_or_404, render
from .models import Patient, Experiment
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CreateOrganizationSerialize


def index(request):
    return render(request, "index.html")
 
def postuser(request):
    checked_items = request.POST.getlist("item_checkbox")
    return HttpResponse(f"<h2>Selected: {checked_items}</h2>") 


class CreateOrganizatonApi(ListAPIView, CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = CreateOrganizationSerialize

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CreateOrganizationSerialize(queryset, many=True)
        return Response(serializer.data)


# Create your views here.
