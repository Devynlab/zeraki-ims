from rest_framework import serializers

from . import models

class InstitutionSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Institution
    fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Student
    fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Course
    fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Unit
    fields = '__all__'
