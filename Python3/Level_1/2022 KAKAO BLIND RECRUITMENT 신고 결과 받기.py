import collections
import heapq
import functools
import itertools
from pkgutil import read_code
import re
import sys
import math
import bisect
from typing import *

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]


def solution(id_list, report, k):
    dic_report_list = dict()
    ban_list = list()
    tmp = list()

    for id in id_list:
        if id not in tmp:
            tmp.append(id)
    id_list = tmp

    dic_report_list = dict.fromkeys(id_list, 0)

    for report_id in report:
        report_id = report_id.split(" ")[1]
        dic_report_list[report_id] = dic_report_list[report_id] + 1

    print(dic_report_list)

    items = dic_report_list.items()
    for item in items:
        if item[1] >= k:
            ban_list.append(item[0])

    print(ban_list)
    dic_report_list = dict.fromkeys(id_list, 0)

    for report_id in report:
        report_id = report_id.split(" ")
        if report_id[1] in ban_list:
            dic_report_list[report_id[0]] = dic_report_list[report_id[0]] + 1   

    answer = list(dic_report_list.values())
    return answer

print(solution(id_list, report, 2))