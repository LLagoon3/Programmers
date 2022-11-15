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

numbers = [1, 1, 1, 1, 1]	
target = 3




def solution(numbers, target):

    answer = [0]    
    def dfs(i, res, numbers):
        if i == len(numbers):
            if res == target:
                answer[0] += 1
            return
        dfs(i + 1, res + numbers[i], numbers)
        dfs(i + 1, res - numbers[i], numbers)
    dfs(0, 0, numbers)
    return answer[0]
print(solution(numbers, target))