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


def gcd(B, R):#B >= R
    if B % R == 0:
        return R
    else:
        return gcd(R, B % R)

def gcd_mul(arr):
    arr.sort(reverse = False)
    if len(arr) == 1:
        return arr[0]
    tmp2, tmp1 = arr.pop(), arr.pop()#tmp1 >= tmp2
    res = gcd(tmp1, tmp2)
    for i in arr:
        if i != None:
            res = gcd(i, res)
        else:
            break
    return res

def cmp(arr, num):
    for i in arr:
        if i % num == 0:
            return True
    return False

def solution(arrayA, arrayB):
    if arrayA == None or arrayB == None:
        return 0
    tmp1, tmp2 = gcd_mul(arrayA[:]), gcd_mul(arrayB[:])
    if tmp1 == tmp2:
        return 0
    elif tmp1 > tmp2:
        if cmp(arrayB, tmp1):
            if cmp(arrayA, tmp2):
                return 0
            return tmp2
        else:
            return tmp1
    else:
        if cmp(arrayA, tmp2):
            if cmp(arrayB, tmp1):
                return 0
            return tmp1
        else:
            return tmp2


print(solution([0], [0]))