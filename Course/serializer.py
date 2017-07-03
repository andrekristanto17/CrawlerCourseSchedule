from rest_framework import serializers
from .models import Course, Index, Schedule

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        fields = '__all__'