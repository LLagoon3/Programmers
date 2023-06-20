def solution(s):
    import re
    if re.search('\D', s) == None and (len(s) == 4 or len(s) == 6): return True
    return False

print(solution("1234ab"))
#re.findall("[a-z]+|[A-Z]+", s)
#re.match("[0-9]" + '{' + str(4) + '}', s)
#s.isdigit()