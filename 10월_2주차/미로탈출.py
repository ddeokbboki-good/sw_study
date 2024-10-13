from collections import deque as q

def find_location(map, dst):
    row, col = len(map), len(map[0])
    for y in range(row):
        for x in range(col):
            if map[y][x] == dst:
                return [y, x, 0]

def find_distance(map, srt, dst):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    row, col = len(map), len(map[0])
    visited = [[0 for _ in range(col)] for _ in range(row)]
    curr = q([])
    curr.append(srt)
    dist = -1
    
    while curr:
        y, x, d = curr.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < row and 0 <= nx < col and map[ny][nx] != "X" and not visited[ny][nx]:
                if map[ny][nx] == dst:
                    if dist == -1:
                        dist = d+1
                    else:
                        dist = min(d+1, dist)
                else:
                    visited[ny][nx] = 1
                    curr.append([ny, nx, d+1])
                    
    return dist
        
def solution(maps):
    srt = find_location(maps, "S")
    lever = find_distance(maps, srt, "L")
    end = find_location(maps, "L")
    exit = find_distance(maps, end, "E")
    
    if lever == -1 or exit == -1:
        return -1
    
    return lever+exit