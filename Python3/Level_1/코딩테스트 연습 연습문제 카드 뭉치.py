c1, c2, g = ["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]


def solution(cards1, cards2, goal):
    from collections import deque
    c1, c2, g = deque(cards1), deque(cards2), deque(goal)
    while g:
        t = g.popleft()
        if c1 and c1[0] == t: c1.popleft()
        elif c2 and c2[0] == t: c2.popleft()
        else: return 'No'
    if len(g) == 0: return 'Yes'
    return 'No'

print(solution(c1, c2, g))

