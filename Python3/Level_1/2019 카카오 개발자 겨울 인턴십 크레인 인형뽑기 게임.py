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

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    box = []
    res = 0
    for pos in moves:
        for i in range(0, len(board)):
            if board[i][pos - 1] != 0:
                if not box:
                    box.append(board[i][pos - 1])
                else:
                    tmp = box.pop()
                    if tmp == board[i][pos - 1]:
                        print("res++ ", tmp, i, pos - 1)
                        res = res + 2
                    else:
                        box.append(tmp)
                        box.append(board[i][pos - 1])
                board[i][pos - 1] = 0
                break
            #print(box, i, pos - 1)
    answer = res
    return answer

print(solution(board, moves))
