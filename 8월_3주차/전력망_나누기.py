from collections import deque as q

def bfs(tower, start, visited):
    tmp = q([start])
    visited[start] = 1
    cnt = 0
    
    while tmp: 
        t = tmp.popleft()
        cnt += 1
            
        for s in tower[t]:
            if visited[s] == 0 :
                visited[s] = 1
                tmp.append(s)
    return cnt
            
        
def solution(n, wires):
    ans = n - 2
    for i in range(len(wires)):
        if i == 0:
            tmp = wires[1:]
        elif i == len(wires) - 1:
            tmp = wires[:-1]
        else:
            tmp = wires[:i] + wires[i+1:]
        new = [[] for _ in range(n+1)]
        visited = [0 for _ in range(n+1)]
        for i, j in tmp:
            new[i].append(j)
            new[j].append(i)
            
        for i in new[1:]:
            if i != []:
                idx = i[0]
                break
                
        cnt = bfs(new , idx, visited)
        ans = min(ans, abs(n - 2 * cnt))
    return ans