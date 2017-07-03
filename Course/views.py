from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Index, Schedule
from .serializer import CourseSerializer, IndexSerializer

class CourseList(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializerCourse = CourseSerializer(courses, many=True)
        return Response(serializerCourse.data)

    def post(request, post_id):
        return None

class IndexList(APIView):

    def get(self, request):
        indexes = Index.objects.all()
        serializerIndex = IndexSerializer(indexes, many=True)
        return Response(serializerIndex.data)

    def post(request, post_id):
        return None