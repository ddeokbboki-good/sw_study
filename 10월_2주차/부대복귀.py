def solution(n, roads, sources, destination):
    matrix = [[] for _ in range(n+1)]
    
    for a, b in roads:
        matrix[a].append(b)
        matrix[b].append(a)
        
    road_map = [-1] * (n+1)
    road_map[destination] = 0
    queue = [(destination, 0)]

    while queue:
        q = queue.pop(0)
        for i in matrix[q[0]]:
            if road_map[i] == -1:
                queue.append((i, q[1]+1))
                road_map[i] = q[1]+1
    return [road_map[j] for j in sources]