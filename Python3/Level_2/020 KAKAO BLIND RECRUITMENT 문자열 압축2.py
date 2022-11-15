
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
#s = "aabbaccc"
s = "ababcdcdababcdcd"
s = "aaaaaaaaaaaaaaabbbbbbbbbbc"#15a10bc
s = "aaaaaaaaabaa" #9ab2a
s = "xababcdcdababcdcd"


def list_length(s):
    if len(s) % 2 == 0:
        length = int(len(s) / 2)
    else:
        length = int((len(s) - 1) / 2)
    return length

def solution(s):
    length = 0
    res = list()
    length = list_length(s)
    for i in range(0, length):
        res.append(0)
    tmp = list(s)

    i = 1
    while i <= length:
        tmp = list(s)
        cnt = 0
        j = 0
        pos = 0
        last_pos = -1
        num_cnt = -1
        while pos < int((len(tmp) / i) - 1):
            cnt = 0
            for j in range(0, i):
                now_pos = pos * i + j
                next_pos = (pos + 1) * i + j
                if tmp[now_pos] == tmp[next_pos]:
                    cnt = cnt + 1
                else:
                    break
                if cnt == i:
                    for k in range(0, i):
                        del tmp[now_pos + 1]
                    pos = pos - 1
                    num_cnt = num_cnt + 1
                    
                    if last_pos != now_pos:
                        if num_cnt != 0:
                            res[i - 1] = res[i - 1] + len(str(num_cnt))
                        #print(num_cnt)
                        last_pos = now_pos
                        num_cnt = 1
                    
            pos = pos + 1
            #print(i, pos, tmp, res)
        #print(res, len(tmp), num_cnt)
        res[i - 1] = res[i - 1] + len(tmp)
        if num_cnt != -1:
           res[i - 1] = res[i - 1] + len(str(num_cnt + 1)) 
        i = i + 1
        last_pos = -1
    
                 
            

    
    if not res:
        res.append(1)
    answer = min(res)

    return answer

print(solution(s))

