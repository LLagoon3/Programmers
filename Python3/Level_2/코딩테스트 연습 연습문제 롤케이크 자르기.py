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

def solution_(topping):
    a, b, ta, tb, l = 1, 1, 0, 0, len(topping)
    for i in range(1, (lambda x : x // 2 if x % 2 == 0 else x // 2 + 1)(l)):
        ta, tb = 0, 0
        
        if topping[i] not in topping[0:a]:
            a += 1
            ta = 1
        if topping[l - i - 1] not in topping[l - b:l]:
            b += 1
            tb = 1
        if (i == l - i - 1) and (ta == tb == 1):
            return 0
        print(i, a, b)
    if a == b:
        return a - 1    
    else:  
        return 0

#print(solution([1, 1, 1, 1, 1]))

def solution_(topping):
    res = 0
    for i in range(1, len(topping) ):
        if len(set(topping[:i])) == len(set(topping[i:])):
            res += 1
    return res

#print(solution([1, 2, 1, 3, 1, 4, 1, 2])

def solution(topping):
    length = len(set(topping))
    tast = set()
    tast_cnt, res = 0, 0
    if length % 2 != 0:
        return 0
    while True:
        tmp = topping.pop()
        if tmp not in tast:
            tast.add(tmp)
            tast_cnt += 1
        if tast_cnt == tmp / 2:
            res += 1
        elif tast_cnt > tmp / 2:
            return res
        
def solution(topping):
    a, b, da, db = [], [], dict(), dict()
    lptr, rptr = 0, len(topping) - 1
    while lptr <= rptr:
        if len(da) == len(db) and lptr == rptr:
            if topping[lptr] in da.keys(): a.append(topping[lptr])
            elif topping[rptr] in db.keys(): b.append(topping[rptr])
            else:
                a.append(topping[lptr])
                da[topping[lptr]] = 1
            break
        elif len(da) <= len(db):
            if topping[lptr] in da.keys(): da[topping[lptr]] += 1
            else: da[topping[lptr]] = 1
            a.append(topping[lptr])
            lptr += 1
        elif len(da) > len(db):
            if topping[rptr] in db.keys(): db[topping[lptr]] += 1
            else: db[topping[rptr]] = 1
            b.append(topping[rptr])
            rptr -= 1
    print(a, da, b, db)
    if len(da) != len(db): return 0
    res, cnt = 1, -1
    while cnt > -len(a):
        if a[cnt] in db.keys() and da[a[cnt]] > 1:
            da[a[cnt]] -= 1
            res += 1
            cnt -= 1
        else: break
    cnt = -1
    while cnt > -len(b):
        if b[cnt] in da.keys() and db[b[cnt]] > 1:
            db[b[cnt]] -= 1
            res += 1
            cnt -= 1
        else: break
    return res

def solution(topping):
    left, right, ldic, rdic, llist, rlist = 0, len(topping) - 1, dict(), dict(), [], []
    while left <= right:
        if len(ldic) == len(rdic) and left == right:
            if topping[left] in ldic.keys():
                llist.append(topping[left])
                break
            elif topping[right] in rdic.keys():
                rlist.append(topping[left])
                break
            
        elif len(ldic) <= len(rdic):
            if topping[left] in ldic.keys():
                ldic[topping[left]] += 1
            else: ldic[topping[left]] = 1
            llist.append(topping[left])
            left += 1
        else: 
            if topping[right] in rdic.keys():
                rdic[topping[right]] += 1
            else: rdic[topping[right]] = 1
            rlist.append(topping[right])
            right -= 1
        print((llist, rlist, left, right))
 
    res, cnt = 1, -1
    while cnt > -len(llist):
        if llist[cnt] in rdic.keys() and ldic[llist[cnt]] > 1:
            ldic[llist[cnt]] -= 1
            res += 1
            cnt -= 1
        else: break
    cnt = -1
    while cnt > -len(rlist):
        if rlist[cnt] in ldic.keys() and rdic[rlist[cnt]] > 1:
            rdic[rlist[cnt]] -= 1
            res += 1
            cnt -= 1
        else: break
    return res

def solution(topping):
    from collections import Counter
    res, ptr = 0, 0
    cleft, cright,  = dict(), dict(Counter(topping))
    while 0 <= ptr < len(topping):
        if len(cleft) == len(cright):
            res += 1
        elif len(cleft) > len(cright):
            break
        
        if topping[ptr] in cleft.keys(): 
            cleft[topping[ptr]] += 1
        else: cleft[topping[ptr]] = 1
        
        cright[topping[ptr]] -= 1
        if cright[topping[ptr]] == 0: del cright[topping[ptr]]
        ptr += 1
    
    return res

        
    

print(solution([1, 2, 3, 1, 4]))
print(solution([1, 2, 3, 3, 4, 4, 5, 6]))
print(solution([1, 2, 3, 3, 4, 4, 4, 5, 6]))
        