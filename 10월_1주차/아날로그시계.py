def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    time = (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)
    sh = (h1 * 3600 / 120 + m1 * 60 / 120 + s1 / 120) % 360
    sm = (m1 * 60 / 10 + s1 / 10) % 360
    ss = (s1 * 6) % 360
    
    if (h1 == 0 or h1 == 12) and (m1 == 0 and s1 == 0):
        answer += 1
    
    for i in range(time):
        h = (sh + i / 120) % 360 
        m = (sm + i / 10) % 360 
        s = (ss + 6 * i) % 360 
        
        nh = (sh + (1 + i) / 120) % 360 if (sh + (1 + i) / 120) % 360 else 360
        nm = (sm + (1 + i) / 10) % 360 if (sm + (1 + i) / 10) % 360 else 360
        ns = (ss + 6 * (1 + i)) % 360 if (ss + 6 * (1 + i)) % 360 else 360
        
        if s < h and ns >= nh:
            answer += 1
        if s < m and ns >= nm:
            answer += 1
        if ns == nm and ns == nh:
            answer -= 1
    return answer