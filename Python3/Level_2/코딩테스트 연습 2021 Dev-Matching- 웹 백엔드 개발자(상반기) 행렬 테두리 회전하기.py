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

def mk_arr(rows, columns):
    cnt = 1
    arr = list()
    for i in range(0, rows):
        line = []
        for j in range(0, columns):
            line.append(cnt)
            cnt += 1
        arr.append(line)
    return arr
#
def rotation(arr, queries):
    tmp = 0
    tmp1 = 0
    for rows in range(queries[1] - 1,  queries[3]):
        for columns in range(queries[0] - 1, queries[2]):
            if rows == queries[1] - 1:
                if columns == queries[0] - 1:
                    tmp = arr[columns][rows + 1]
                    arr[columns][rows + 1] = arr[columns][rows]
                else:
                    arr[columns - 1][rows] = arr[columns][rows]
            elif rows == queries[3] - 1:
                if columns == queries[2] - 1:
                    tmp1 = arr[columns][rows - 1]
                    arr[columns][rows - 1] = arr[columns][rows]
                    arr[columns][rows] = tmp
                    tmp = tmp1
                else:
                    tmp = arr[columns + 1][rows]
                    arr[columns + 1][rows] = arr[columns][rows]
            else:
                if columns == queries[0] - 1:
                    tmp1 = arr[columns][rows + 1]
                    arr[columns][rows + 1] = tmp
                    tmp = tmp1
                elif columns == queries[2] - 1:
                    tmp1 = arr[columns][rows - 1]
                    arr[columns][rows] = tmp
                    tmp = tmp1

    print(arr)
    return arr

    
def solution(rows, columns, queries):
    arr = mk_arr(columns, rows)
    rotation(arr, queries[0])
    answer = []
    return answer

#solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])

a = int(input())
tmp = tuple(range(-10, 10, a))
print(tmp)