from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=250)
    course_code = models.CharField(max_length=250)
    course_au = models.CharField(max_length=250)

    def __str__(self):
        return self.course_name

class Index(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    index_code = models.CharField(max_length=250)

    def __str__(self):
        return self.course.course_code + '_' + self.index_code

class Schedule(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, null=True)
    group = models.CharField(max_length=10, null=True)
    day = models.CharField(max_length=10, null=True)
    time = models.CharField(max_length=10, null=True)
    slot = models.CharField(max_length=10, null=True)
    venue = models.CharField(max_length=10, null=True)
    remark = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.index.index_code + '_' + self.type