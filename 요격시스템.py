def solution(targets):
    answer = 0
    targets.sort()
    ts, te = 0, 0 
    
    for target in targets:
        s, e = target[0], target[1]
        
        if s < te:
            if e < te:
                te = e
            
        else:
            answer += 1
            ts, te = s, e
    return answer