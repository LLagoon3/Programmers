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

new_id = "abcdefghijklmn.p"

def solution(new_id):

    def chk_comma(new_id):
        if  len(new_id) == 0:
            return new_id
        if new_id[0] == '.':
            new_id = new_id[1:]
        if  len(new_id) == 0:
            return new_id
        if new_id[len(new_id) - 1] == ".":
            new_id = new_id[:len(new_id) - 1]
        return new_id

    new_id = new_id.lower()
    new_id = re.sub(r'[^ \w._-]', "", new_id)
    new_id = re.sub(r'[.]+', ".", new_id)
    print(new_id)
    new_id = chk_comma(new_id)
    print(new_id)
    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = chk_comma(new_id)
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id = new_id + new_id[len(new_id) - 1]
    answer = new_id
    return answer

print(solution(new_id))