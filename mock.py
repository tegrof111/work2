import json
from random import randint, sample
from env import *

info = []  # 课程的全部人员到勤信息


for i in range(COURSES):
    courseInfo = {'courseId': i, 'lessons': []}

    skip = randint(*SKIP)  # 选出总是翘这门课的同学数
    # range(0,50)
    skipStu = sample(range(STUDENTS), skip)  # 选出总是翘这门课的同学ID
    skipLessons = {Id: set(sample(range(LESSONS), int(LESSONS * SKIP_RATE)))
                   for Id in skipStu}  # 保存翘课同学和他翘的课，映射为ID->set(课程次号)
    #skipLessons = {0:{1,2,3}}
    
    restStu = list(set(range(STUDENTS)) - set(skipStu))  # 剩下的同学ID
    for j in range(LESSONS):
        absence = randint(*ABSENCE)  # 产生本节课缺课的人数
        absenceStu = sample(restStu, absence)  # 产生本节课缺课的学生ID

        lessonInfo = {'lessonId': j, 'absence': []}

        for k in range(STUDENTS):
            if k in skipLessons and j in skipLessons[k] or k in absenceStu:
                lessonInfo['absence'].append(k)

        courseInfo['lessons'].append(lessonInfo)

    info.append(courseInfo)


with open('mock.json', 'w') as data:
    json.dump(info, data, indent=4)