def solution(n):
    if n < 2 or n % 2 == 1:
        return 0
    
    answer = [0, 3]
    idx = int(n/2)
    for i in range(2,idx+1):
        answer.append((3*answer[i-1]+sum(answer[1:i-1])*2+2)%1000000007)
    return answer[-1]