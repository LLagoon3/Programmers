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

numbers = [1,2,3,4,6,7,8,0]	

def solution(numbers):
    answer = 0
    for i in range(0, 10):
        if i not in numbers:
            answer = answer + i
    return answer

print(solution(numbers))