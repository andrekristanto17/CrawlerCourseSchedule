from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/allcourse$', views.allCourseList.as_view()),
    url(r'^api/course/(?P<query>[''A-Za-z0-9]+)$', views.CourseList.as_view()),
    url(r'^api/allindex$', views.allIndexList.as_view()),
    url(r'^api/index/(?P<query>[''A-Za-z0-9]+)$', views.IndexList.as_view()),
]
