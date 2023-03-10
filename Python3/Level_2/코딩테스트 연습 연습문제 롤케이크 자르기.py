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

def solution_(topping):
    a, b, ta, tb, l = 1, 1, 0, 0, len(topping)
    for i in range(1, (lambda x : x // 2 if x % 2 == 0 else x // 2 + 1)(l)):
        ta, tb = 0, 0
        
        if topping[i] not in topping[0:a]:
            a += 1
            ta = 1
        if topping[l - i - 1] not in topping[l - b:l]:
            b += 1
            tb = 1
        if (i == l - i - 1) and (ta == tb == 1):
            return 0
        print(i, a, b)
    if a == b:
        return a - 1    
    else:  
        return 0

#print(solution([1, 1, 1, 1, 1]))

def solution_(topping):
    res = 0
    for i in range(1, len(topping) ):
        if len(set(topping[:i])) == len(set(topping[i:])):
            res += 1
    return res

#print(solution([1, 2, 1, 3, 1, 4, 1, 2])

def solution(topping):
    length = len(set(topping))
    tast = set()
    tast_cnt, res = 0, 0
    if length % 2 != 0:
        return 0
    while True:
        tmp = topping.pop()
        if tmp not in tast:
            tast.add(tmp)
            tast_cnt += 1
        if tast_cnt == tmp / 2:
            res += 1
        elif tast_cnt > tmp / 2:
            return res

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
        