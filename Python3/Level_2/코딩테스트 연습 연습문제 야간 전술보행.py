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

def mk_scope(scope, times, _scope):
    cnt = 0
    for scp in scope:
        scp.sort()
        start, end = times[cnt]
        cnt += 1
        for i in range(scp[0], scp[1] + 1):
            if i % (start + end) > start or i % (start + end) == 0:
                _scope[i - 1] = 0
            else:
                _scope[i - 1] = 1
            

def solution(distance, scope, times):
    _scope = [0] * distance
    mk_scope(scope, times, _scope)
    for i in range(0, distance):
        if _scope[i] == 1:
            return i + 1
    return distance

print(solution(12, [[1, 2]], [[1, 1]]))