from .models import Course, Index, Schedule
from .serializer import CourseSerializer, IndexSerializer
from simple_search import search_filter

def courseData(query):
    if query == '':
        courses = Course.objects.all()
        serializerCourse = CourseSerializer(courses, many=True)
    else:
        search_fields = ['^course_name', 'course_code','id']
        courses = Course.objects.filter(search_filter(search_fields, query))
        serializerCourse = CourseSerializer(courses, many=True)
    return serializerCourse.data

def indexData(query):
    if query == '':
        indexes = Index.objects.all()
    else:
        search_fields = ['^index_code','id']
        indexes = Index.objects.filter(search_filter(search_fields, query))
    serializerIndex = IndexSerializer(indexes, many=True)
    return serializerIndex.data