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

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    id_nick_list = dict()
    res = list()
    for rec in record:
        rec = rec.split(" ")
        if rec[0] == "Enter" or rec[0] == "Change":
            id_nick_list[rec[1]] = rec[2]
    for rec in record:
        rec = rec.split(" ")
        if rec[0] == "Enter":
            res.append("{0}님이 들어왔습니다.".format(id_nick_list[rec[1]]))
        elif rec[0] == "Leave":
            res.append("{0}님이 나갔습니다.".format(id_nick_list[rec[1]]))

    answer = res
    
    return answer

print(solution(record))