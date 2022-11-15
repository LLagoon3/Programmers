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

scoville = [1, 2, 3, 9, 10, 12]	
K = 7

def solution(scoville, K):
    cnt = 0
    min_num = min(scoville)
    length = len(scoville)
    while min_num < K:
        if length < 2:
            return -1
        scoville.remove(min_num)
        sec_min_num = min(scoville)
        scoville.remove(sec_min_num)
        scoville.append(min_num + (sec_min_num * 2))
        min_num = min(scoville)
        cnt = cnt + 1
        length = length - 1
    answer = cnt
    return answer

print(solution(scoville, K))