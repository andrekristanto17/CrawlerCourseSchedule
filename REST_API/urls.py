from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from Course import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/Courses/', views.CourseList.as_view()),
    url(r'^api/Index/', views.CourseList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
