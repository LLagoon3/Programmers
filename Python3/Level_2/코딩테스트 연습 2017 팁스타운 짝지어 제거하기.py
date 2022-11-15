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

s = "aaaaa"
def solution(s):
    if s == "":
        return 0
    def same_spell(s):
        print(s)
        if s == "":
            return 1
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                return same_spell(s.replace(s[i], "", 2))
        return 0
    answer = same_spell(s)
    return answer

print(solution(s))