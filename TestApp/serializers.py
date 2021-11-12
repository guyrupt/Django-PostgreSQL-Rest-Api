from django.db.models import fields
from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'


class Acad_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acad_level
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.JSONField()
    location = serializers.CharField()
    tag = serializers.CharField()
    level = serializers.CharField()
    gender = serializers.CharField()
    race = serializers.CharField()
    academic_level = serializers.CharField()

    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    