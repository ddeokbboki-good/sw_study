def solution(picks, minerals):
    answer = 0
    tmp = min(len(minerals), sum(picks) * 5)
    if tmp%5 : five = [[0] * 3 for _ in range(tmp//5 + 1)]
    else : five = [[0] * 3 for _ in range(tmp//5)]
    arr = [0, 0, 0]
    
    for idx, m in enumerate(minerals[:tmp]):
        if m == "diamond":
            arr[0] += 1
        elif m == "iron":
            arr[1] += 1
        else:
            arr[2] += 1
            
        if ((idx + 1) % 5 == 0) or (idx == (len(minerals) - 1)):
            five[idx // 5][0] = arr[0]
            five[idx // 5][1] = arr[1]
            five[idx // 5][2] = arr[2]
            arr = [0, 0, 0]
            
    five.sort(key=(lambda x: (-x[0], -x[1], -x[2])))
    
    for d, i, s in five:
        if picks[0]:
            answer += d + i + s
            picks[0] -= 1
        elif picks[1]:
            answer += 5*d + i + s
            picks[1] -= 1
        elif picks[2]:
            answer += 25*d + 5*i + s
            picks[2] -= 1
    return answer