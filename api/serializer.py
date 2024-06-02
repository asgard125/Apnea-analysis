from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.fields import CurrentUserDefault
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from .models import Patient, Experiment, UploadedFile, Result

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class PatientListSerializer(serializers.ModelSerializer):
    question_pk = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), write_only=True
    )

    class Meta:
        model = Experiment
        fields = '__all__'
        depth = 1


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadedFile
        fields = ('file', 'uploaded_on',)


class SelectedWriteSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)

    class Meta:
        model = Patient
        fields = ('id', 'full_name', 'age', 'sex', 'height', 'weight', 'pulse', 'BPsys', 'BPdia', 'ODI')


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'
