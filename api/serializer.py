from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.fields import CurrentUserDefault
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from .models import Patient, Experiment

class CreateOrganizationSerialize(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


