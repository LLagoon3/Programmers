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

s = "cdcd"
def solution(s):
    s = deque(s)

    while 1:
        length = len(s)
        if length == 0:
            return 1
        elif length == 1:
            return 0
        elif length == 2:
            if s.pop() == s.pop():
                return 1
            else:
                return 0
        for i in range(0, length):
            print(s, i)
            if i == 0:
                s.append(s.popleft())
                continue
            s_right = s.pop()
            s_left = s.popleft()
            if s_right == s_left:
                cnt = length - i - 2
                s.rotate(cnt)
                break
            else:
                if i == length - 1:
                    return 0
                else:
                    s.append(s_right)
                    s.append(s_left)

            
            
    answer = 1
    return answer

print(solution(s))