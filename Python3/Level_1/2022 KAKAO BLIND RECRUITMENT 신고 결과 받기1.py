
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
import copy

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]


def solution(id_list, report, k):
    dic_report_list = dict()
    ban_list = list()
    tmp = list()

    report = list(set(report))
    """
    for id in report:
        if id not in tmp:
            tmp.append(id)
    report = copy.deepcopy(tmp)
    tmp.clear()
    """
    dic_report_list = dict.fromkeys(id_list, 0)
    dic_res = dict.fromkeys(id_list, 0)
    
    for i in range(0, len(report)):
        print(i, dic_report_list, dic_res, ban_list)
        report_id = report[i].split(" ")[1]
        report_man = report[i].split(" ")[0]
        if report_id in ban_list:
            dic_res[report_man] = dic_res[report_man] + 1
            continue
        dic_report_list[report_id] = dic_report_list[report_id] + 1
        if dic_report_list[report_id] >= k:
            ban_list.append(report_id)
            dic_res[report_man] = dic_res[report_man] + 1
            continue
        tmp.append(report[i])
    print(tmp)
    for report_id in tmp:
        report_id = report_id.split(" ")
        if report_id[1] in ban_list:
            dic_res[report_id[0]] = dic_res[report_id[0]] + 1

    answer = list(dic_res.values())
    return answer

print(solution(id_list, report, 2))