from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Index, Schedule
from .serializer import CourseSerializer, IndexSerializer
from . import dataManager

class allCourseList(APIView):

    def get(self, request):
        return Response(dataManager.courseData(''))

    def post(request, post_id):
        return None

class CourseList(APIView):

    def get(self, request, query):
        param = request.GET
        return Response(dataManager.courseData(query))

    def post(request, post_id):
        return None

class allIndexList(APIView):

    def get(self, request):
        return Response(dataManager.indexData(''))

    def post(request, post_id):
        return None

class IndexList(APIView):

    def get(self, request, query):
        return Response(dataManager.indexData(query))

    def post(request, post_id):
        return None