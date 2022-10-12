import json
from random import choices
from env import *

TOTAL_REQ_PER_LESSON = 20  # 每次课抽的人数
PUNISH = 10000  # 缺课一次的惩罚（可以改成0对比效率）


weights = {i: [1] * STUDENTS for i in range(COURSES)}  # 每种课和它对应的每个学生的权重


def core(info):
    effectiveReq = 0  # 有效请求数
    for i in range(LESSONS):
        for j in range(COURSES):
            chosens = choices(range(STUDENTS), weights=weights[j],
                              k=TOTAL_REQ_PER_LESSON)  # 按权重随机抽n个幸运学生

            for c in chosens:
                if c in info[j]['lessons'][i]['absence']:
                    effectiveReq += 1
                    weights[j][c] += PUNISH

    return effectiveReq


with open('mock.json', 'r') as data:
    info = json.load(data)
    TIMES = 10  # 测试次数
    for _ in range(TIMES):
        print(f'E = {core(info) / ( TOTAL_REQ_PER_LESSON * LESSONS * COURSES)}')