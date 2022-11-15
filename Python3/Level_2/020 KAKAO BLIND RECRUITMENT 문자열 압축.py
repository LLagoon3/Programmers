from __future__ import absolute_import
import collections
import heapq
import functools
import itertools
from os import TMP_MAX
from pkgutil import read_code
import re
import sys
import math
import bisect
from typing import *

from collections import deque
s = "aabbaccc"

def solution(s):
    length = 0
    res = list()
    if len(s) % 2 == 0:
        length = int(len(s) / 2)
    else:
        length = int((len(s) - 1) / 2)
    for i in range(0, length):
        res.append(0)
    tmp = list(s)
    for i in range(1, length + 1):
        tmp = list(s)
        leftpos = 0
        rightpos = 0
        cnt = 0
        for j in range(0, len(s) - i):
            print(i, "tmp : ", tmp)
            if (tmp[j] == tmp[i + j]) and (tmp[j] != 0):
                cnt = cnt + 1
                if cnt == i:
                    for k in range(j + 1, i + j + 1):
                        tmp[k] = 0
                    res[i - 1] = res[i - 1] + 1
            else:
                cnt = 0
        while 0 in tmp:
            tmp.remove(0)
        res[i - 1] = res[i - 1] + len(tmp)
        print(res, tmp)

    
    
    answer = 0
    return answer

print(solution(s))