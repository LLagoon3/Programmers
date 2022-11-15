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

progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]	

def complete_time(progress, speed):
    tmp = (100 - progress) / speed
    if tmp % 1 == 0:
        return int(tmp)
    else:
        return int(tmp) + 1
def solution(progresses, speeds):
    tmp = list(map(complete_time, progresses, speeds))
    res = []
    max_day = 0
    cnt = 0
    for day in tmp:
        if day > max_day:
            max_day = day
            if cnt != 0:
                res.append(cnt)
            cnt = 1
        else:
            cnt = cnt + 1
    res.append(cnt)
    answer = res
    return answer

print(solution(progresses, speeds))