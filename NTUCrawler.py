import requests
from bs4 import BeautifulSoup
import json

URL = 'https://wish.wis.ntu.edu.sg/webexe/owa/AUS_SCHEDULE.main'

def GET(url):
    # Crawl Data
    page = requests.get(url)
    return page

def getFaculty():
    data = GET(URL)
    soups = BeautifulSoup(data.text, "lxml")

    indexFac = []
    breakInd = False
    for selects in soups.find_all("select"):
        if selects.get('name') == 'r_course_yr':
            for opt in selects.find_all('option'):
                if opt.text.strip() == 'Minor in Art History':
                    breakInd = False
                if opt.text.strip() == '---Double Degree---':
                    breakInd = True
                if breakInd: continue
                if not(opt.get('value') is None) and opt.get('value') != '':
                    indexFac.append({'name':opt.text.strip(), 'option_value': opt.get('value')})

    return indexFac

def getName(param):
    getURL = 'https://wish.wis.ntu.edu.sg/webexe/owa/AUS_SCHEDULE.main_display1?' \
             'boption=CLoad&staff_access=false&acadsem=2017;1&r_course_yr=' + param
    data = GET(getURL)
    soups = BeautifulSoup(data.text, "lxml")

    tableNo = 0
    course = []

    for table in soups.find_all('table'):
        rowNo = 0

        tempCourse = {}
        tempCourse['course_code'] = ''
        tempCourse['course_name'] = ''
        tempCourse['course_au'] = ''
        for row in table.find_all('tr'):
            if tableNo % 2 == 0 and rowNo == 0:
                text = row.text.split('\n')
                del text[0]
                del text[-1]

                tempCourse['course_code'] = text[0]
                tempCourse['course_name'] = text[1]
                tempCourse['course_au'] = text[2]
            rowNo += 1
        if tableNo % 2 == 0:
            course.append(tempCourse)
        tableNo += 1

    return course


def getCourse(param):
    getURL = 'https://wish.wis.ntu.edu.sg/webexe/owa/AUS_SCHEDULE.main_display1?' \
             'boption=CLoad&staff_access=false&acadsem=2017;1&r_course_yr=' + param
    data = GET(getURL)
    soups = BeautifulSoup(data.text, "lxml")

    tableNo = 0
    course = []

    def getSlot(day, time):
        if(day == '\u00a0' or time == '\u00a0'):
            return ''

        dayList = ['MON','TUE','WED','THU','FRI','SAT','SUN']
        slotDay = dayList.index(day)

        slotTime = time.split('-')
        a = []
        for i in slotTime:
            hour = i[0:2]
            min = i[2:4]
            slot = (int(hour) - 8) * 2
            if int(min) == 0:
                slot -= 1
            a.append(slot)
        return str(slotDay)+','+str(a[0])+','+str(a[1])

    for table in soups.find_all('table'):
        rowNo = 0

        tempCourse = {}
        tempSchedule = []
        tempCourse['course_code'] = ''
        tempCourse['course_name'] = ''
        tempCourse['course_au'] = ''
        tempCourse['schedule'] = []
        for row in table.find_all('tr'):
            if tableNo % 2 == 0 and rowNo == 0:
                text = row.text.split('\n')
                del text[0]
                del text[-1]

                tempCourse['course_code'] = text[0]
                tempCourse['course_name'] = text[1]
                tempCourse['course_au'] = text[2]

            if tableNo % 2 == 1 and rowNo != 0:
                text = row.text.split('\n')
                del text[0]
                del text[-1]

                if text[0] != '':
                    temp = {}
                    temp['index'] = text[0]
                    temp['info'] = []
                    temp['info'].append({
                        'type': text[1],
                        'group': text[2],
                        'day': text[3],
                        'time': text[4],
                        'slot': getSlot(text[3], text[4]),
                        'venue': text[5],
                        'remark': text[6],

                    })
                    tempSchedule.append(temp)
                else:
                    temp['info'].append({
                        'type': text[1],
                        'group': text[2],
                        'day': text[3],
                        'time': text[4],
                        'slot': getSlot(text[3], text[4]),
                        'venue': text[5],
                        'remark': text[6],

                    })
                    tempSchedule.append(temp)
                tempCourse['schedule'].append(temp)
            rowNo += 1
        if tableNo % 2 == 0:
            course.append(tempCourse)
        else:
            course[tableNo//2]['schedule'] = tempCourse['schedule']
        tableNo += 1
    return course

def getAllCourses():
    temp = []
    tempCode = []

    for i in getFaculty():
        for n in getCourse(i['option_value']):
            if not (n['course_code'] in tempCode):
                temp.append(n)
                tempCode.append(n['course_code'])
    return temp

def getAllCourseNames():
    temp = []
    tempCode = []
    for i in getFaculty():
        for n in getName(i['option_value']):
            if not(n['course_code'] in tempCode):
                temp.append(n)
                tempCode.append(n['course_code'])

    return temp
#print(json.dumps(cr.getFaculty(),indent=4))
#print(json.dumps(cr.getAllCourseNames(),indent=4))
#print(json.dumps(getAllCourses(),indent=4))