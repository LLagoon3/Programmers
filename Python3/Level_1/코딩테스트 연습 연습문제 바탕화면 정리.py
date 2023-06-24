wallpaper = [".#...", "..#..", "...#."]

def solution(w):
    lux, luy, rdx, rdy = 50, 50, 0, 0
    for x in range(0, len(w)):
        for y in range(0, len(w[0])):
            if w[x][y] == '#':
                if lux > x: lux = x
                if luy > y: luy = y
                if rdx < x: rdx = x
                if rdy < y: rdy = y
    return [lux, luy, rdx + 1, rdy + 1]

print(solution(wallpaper))