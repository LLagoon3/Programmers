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

w = 1
h = 12



def solution(w,h):
    if w == h:
        return int(w * h - w)
    elif w == 1 or h == 1:
        return 0
    num = 1
    for i in range(2, w + 1):
        if w % i == 0 and h % i == 0:
            num = i
    res = 0
    last_pos = 0
    for x_pos in range(0, int(w / num) + 1):
        y_pos = h / w * x_pos
        tmp = y_pos
        if last_pos % 1 != 0:
            last_pos = int(last_pos)
        if y_pos % 1 != 0:
            y_pos = int(y_pos) + 1
        res = res + y_pos - last_pos
        last_pos = tmp
    #print(res, num)
    return int(w * h - res * num)

print(solution(w, h))