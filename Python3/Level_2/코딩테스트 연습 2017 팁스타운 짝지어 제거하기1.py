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

s = "cdcd"
def solution(s):
    if s == "":
        return 0
    
    while s != "":
        stack = []
        for i in range(0, len(s)):
            if len(s) == 1:
                return 0
            if not stack:
                stack.append(s[i])
            else:
                tmp = stack.pop()
                if tmp == s[i]:
                    s = s[:i - 1] + s[i + 1:]
                    #print(s)
                    break
                elif i == len(s) - 1:
                    return 0
                else:
                    stack.append(tmp)
                    stack.append(s[i])
                    
    answer = 1
    return answer

print(solution(s))