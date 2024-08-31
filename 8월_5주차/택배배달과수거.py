def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver, pick = 0, 0
    
    for i in range(n-1, -1, -1):
        deliver += deliveries[i]
        pick += pickups[i]
        
        while (deliver > 0 or pick > 0) :
            answer += 2 * (i + 1)
            deliver -= cap
            pick -= cap
    return answer