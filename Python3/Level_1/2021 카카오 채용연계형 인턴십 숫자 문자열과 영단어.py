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

s = "23four5six7nine"

def solution(s):
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(0, 10):
        s = re.sub(num_list[i], str(i), s)
    return int(s)
print(solution(s))