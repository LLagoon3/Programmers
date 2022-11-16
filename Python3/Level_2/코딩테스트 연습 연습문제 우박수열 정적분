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

import math

def mk_pos(num, res, cnt = 0):
    pos = 0
    if num % 2 == 0:
        pos = num / 2
    else:
        pos = num * 3 + 1
    res.append(cal_area(pos, num))
    if pos > 1:
        return mk_pos(pos, res, cnt + 1)
    else:
        return cnt

def cal_area(num, t_num):
    return abs(num - t_num) / 2 + min(num, t_num)

def solution(k, ranges):
    arr , res= [], []
    cnt = mk_pos(k, arr)
    for i in ranges:
        start, end = i[0], i[1] + cnt + 1
        if end - start < 0 or end > cnt + 1:
            res.append(-1)
        elif end - start == 0:
            res.append(0)
        else:
            tmp = 0
            for j in range(start, end):
                tmp += arr[j]
            res.append(tmp)
    return res

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))