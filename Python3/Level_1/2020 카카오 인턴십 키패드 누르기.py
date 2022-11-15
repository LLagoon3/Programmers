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

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"


def solution(numbers, hand):
    keyboard_list = [[1, 3], [0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [0, 3], [2, 3]]
    res = list()
    global left, right
    left = keyboard_list[10]
    right = keyboard_list[11]

    def updatepos(hand, pos):
        res.append(hand)
        return pos

    
    for num in numbers:
        fromleft = abs(keyboard_list[num][0] - left[0]) + abs(keyboard_list[num][1] - left[1])
        fromright = abs(keyboard_list[num][0] - right[0]) + abs(keyboard_list[num][1] - right[1])
        #print("num = {0}, FL = {1}, FR = {2}, Left = {3}, Right{4}".format(num, fromleft, fromright, left, right))
        if num in [1, 4, 7]:
           left = updatepos("L", keyboard_list[num]) 
        elif num in [3, 6, 9]:
           right = updatepos("R", keyboard_list[num]) 
        else:
            if fromleft < fromright:
                left = updatepos("L", keyboard_list[num])
            elif fromleft > fromright:
                right = updatepos("R", keyboard_list[num])
            else:
                if hand == "left":
                    left = updatepos("L", keyboard_list[num])
                if hand == "right":
                    right = updatepos("R", keyboard_list[num]) 
    answer = ''.join(res)
    return answer

print(solution(numbers, hand))