from django.urls import include, path
from rest_framework import routers

from .views import *

urlpatterns = [path('organization/', CreateOrganizatonApi.as_view())]
