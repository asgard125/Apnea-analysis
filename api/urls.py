from django.urls import include, path
from rest_framework import routers

from .views import *

urlpatterns = [path('patients/', PatientList.as_view()),
               path('selected/', ListSelected.as_view())
               ]

