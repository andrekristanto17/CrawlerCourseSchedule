from rest_framework import serializers
from .models import Course, Index, Schedule

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('course_name','course_code','course_au')

class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        fields = ('from_course_code','index_code')