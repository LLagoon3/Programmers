
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

from collections import deque
s = "abcabcdede"
#s = "xababcdcdababcdcd"


def list_length(s):
    if len(s) % 2 == 0:
        length = int(len(s) / 2)
    else:
        length = int((len(s) - 1) / 2)
    return length

def solution(s):
    length = 0
    res = list()
    length = list_length(s)
    for i in range(0, length):
        res.append(0)
    tmp = list(s)

    i = 1
    while i <= length:
        tmp = list(s)
        cnt = 0
        j = 0
        last_pos = -1
        while j < len(tmp) - i:
            if tmp[j] == tmp[j + i]:
                cnt = cnt + 1
                if cnt == i:
                    for k in range(0, i):
                        del tmp[j + 1]
                    if j != last_pos:
                        res[i - 1] = res[i - 1] + 1
                        print("!!!")
                    print("res")
                    cnt = 0
                    last_pos = j
                    j = j - 1
            else:
                cnt = 0
            print(i, j, tmp)
            j = j + 1
        res[i - 1] = res[i - 1] + len(tmp)
        i = i + 1
    print(res)

    
    
    answer = min(res)
    return answer

print(solution(s))