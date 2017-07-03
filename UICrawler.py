import requests
from bs4 import BeautifulSoup
import json
from NTUCrawler import NTUCrawler

'''
Documentation By Andre Kristanto

API Method:
1. GET(URL) -> returning HTML page which got form 'GET' request to given URL

    ex:

2. getAllIndex() -> returning array consists of all faculty index with all sub-study indexes

    ex:
    [
        {
            "name": "Kedokteran",
            "index": "01.01",
            "study": [
                {
                    "name": "Fisioterapi, D3",
                    "index": "37.00.01.01"
                },
                {
                    "name": "Okupasi Terapi, D3",
                    "index": "38.00.01.01"
                }
    ]

3. getCourse(faculty index, sub-study index, search query) -> returning JSON with values consist of
                                                                1. Name
                                                                2. Language
                                                                3. Period
                                                                4. Time
                                                                5. Room Number
                                                                6. Teacher
                                                                
    ex:
    [
            {
                "name": "Kelas Administrasi Sistem",
                "language": "Indonesia",
                "period": [
                    "06/02/2017 - 03/06/2017",
                    "06/02/2017 - 03/06/2017"
                ],
                "time": [
                    "Kamis, 16.00-17.40",
                    "Jumat, 10.00-11.40"
                ],
                "room": "Lab 99.01Lab 99.01",
                "teacher": "Heri Kurniawan S.Kom., M.Kom."
            },
            {
                "name": "Kelas Analitika Medsos",
                "language": "Indonesia",
                "period": [
                    "06/02/2017 - 03/06/2017",
                    "06/02/2017 - 03/06/2017"
                ],
                "time": [
                    "Kamis, 10.00-11.40",
                    "Jumat, 08.00-08.50"
                ],
                "room": "2.24042.2404",
                "teacher": "Alfan Farizki Wicaksono S.T., M.Sc."
            }
    ]




'''
with requests.session() as req:
    #Login
    url = 'https://academic.ui.ac.id/main/Authentication/'
    username = 'kevin.prakasa'
    password = '140498kp'

    login_data = dict(u=username, p=password)
    req.post(url, data=login_data)

def GET(url):
    # Crawl Data
    page = req.get(url)
    return page

def getAllIndex():
    baseURL = 'https://academic.ui.ac.id/main/Schedule/IndexOthers?fac='
    data = GET(baseURL)
    soups = BeautifulSoup(data.text, "lxml")

    indexFac = {}
    for soup in soups.find_all("option"):
        lenSTR = len(soup.get('value'))
        if lenSTR == 5:
            indexFac[soup.text] = soup.get('value')

    fullIndex = []
    for key, value in indexFac.items():
        tempURL = baseURL + value
        tempData = GET(tempURL)
        tempSoups = BeautifulSoup(tempData.text, "lxml")
        tempDict = {}
        tempDict['name'] = key
        tempDict['index'] = value
        tempDict['study'] = []
        for soup in tempSoups.find_all("option"):
            data = soup.get('value')
            if len(data) == 11:
                tempDict['study'].append({'name':soup.text, 'index':data})
        fullIndex.append(tempDict)

    return fullIndex


def getCourse(fac, org, param):

    baseURL = 'https://academic.ui.ac.id/main/Schedule/IndexOthers'
    compData = GET(baseURL + '?fac=' + fac + '&org=' + org + '&per=2016-2' + '&search=' + param)
    compSoups = BeautifulSoup(compData.text, "lxml")

    allCourses = []
    for soup in compSoups.find_all('tr'):
        classValue = soup.get('class')
        if not (classValue is None):
            noTable = 0
            tempCourseDict = {}
            for i in soup.find_all('td'):
                if(noTable == 1):
                    tempCourseDict['name'] = i.text
                if(noTable == 2):
                    tempCourseDict['language'] = i.text
                if(noTable == 3):
                    tempCourseDict['period'] = [x for x in i.contents if str(x) != '<br/>']
                if(noTable == 4):
                    tempCourseDict['time'] = [x for x in i.contents if str(x) != '<br/>']
                if(noTable == 5):
                    tempCourseDict['room'] = i.text
                if(noTable == 6):
                    tempCourseDict['teacher'] = i.text
                noTable += 1
            allCourses.append(tempCourseDict)

    return allCourses

# print(getCourse("12.01", "06.00.12.01", ""))
# print(getAllIndex()[1])