import NTUCrawler
from .models import Course, Index, Schedule

def populateAllIndex():
    indexindicator = []
    for i in NTUCrawler.getAllCourses():
        tempCourse = Course(course_name=i['course_name'],
                            course_code=i['course_code'],
                            course_au=i['course_au'])
        tempCourse.save()

        for n in i['schedule']:
            if not(n['index'] in indexindicator):
                tempIndex = Index(course=tempCourse,
                                  index_code=n['index'])
                tempIndex.save()
                indexindicator.append(n['index'])
                for o in n['info']:
                    tempSchedule = Schedule(
                        index=tempIndex,
                        type=o['type'],
                        group=o['group'],
                        day=o['day'],
                        time=o['time'],
                        slot=o['slot'],
                        venue=o['venue'],
                        remark=o['remark'])
                    tempSchedule.save()

