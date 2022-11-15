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

import heapq

scoville = [1, 2, 3, 9, 10, 12]	
K = 7

def solution(scoville, K):
    length = len(scoville)
    cnt = 0
    heapq.heapify(scoville)
    min_num = heapq.heappop(scoville)
    while min_num < K:
        if length < 2:
            return -1
        sec_min_num = heapq.heappop(scoville)
        heapq.heappush(scoville, min_num + sec_min_num * 2)
        length = length - 1
        min_num = heapq.heappop(scoville)
        cnt = cnt + 1
    return cnt

print(solution(scoville, K))
