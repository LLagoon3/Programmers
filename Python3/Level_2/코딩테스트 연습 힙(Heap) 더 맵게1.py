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

scoville = [1, 2, 3, 9, 10, 12]	
K = 7

def solution(scoville, K):
    res = 0
    length = len(scoville)
    scoville = deque(scoville)
    min_num = scoville.popleft()
    while min_num < K:
        if length < 2:
            return -1
        sec_min_num = scoville.popleft()
        tmp = min_num + (sec_min_num * 2)
        if length == 2:
            scoville.append(tmp)
        elif tmp >= scoville[length - 3]:
            scoville.append(tmp)
        else:
            for i in range(0, length - 2):
                if scoville[i] > tmp:
                    scoville.insert(i, tmp)
                    break
        length = length - 1
        res = res + 1
        print(scoville)
        min_num = scoville.popleft()
    answer = res
    return answer

print(solution(scoville, K))