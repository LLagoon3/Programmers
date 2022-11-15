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

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    zero = 0
    res = 0
    for select_num in lottos:
        if select_num == 0:
            zero = zero + 1
            continue
        if select_num in win_nums:
            res = res + 1
    if res == 0 and zero == 0:
        answer = [6, 6]
        return answer
    elif res == 0 and zero != 0:
        answer = [7 - zero, 6]
        return answer
    else:
        print(res, zero)
        answer = [7 - res - zero, 7 - res]
        return answer

print(solution(lottos, win_nums))