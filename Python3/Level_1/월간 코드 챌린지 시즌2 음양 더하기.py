from __future__ import absolute_import
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

absolute = [4,7,12]	
signs = [True,False,True]	

def solution(absolute, signs):
    answer = 0
    for i in range(0, len(absolute)):
        if signs[i]:
            answer = answer + absolute[i]
        else:
            answer = answer - absolute[i]
    return answer

print(solution(absolute, signs))