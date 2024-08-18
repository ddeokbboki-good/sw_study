answer = []

def hanoi(start, target, extra, n): # (시작, 옮길 위치, 남는 봉, 옮겨야하는 개수)
    global answer
    
    if n == 1: # 현재 기둥에 하나 밖에 없는 경우
        answer.append([start, target])
        return
    else:
        hanoi(start, extra, target, n-1) # 위에 판 먼저 옮기기
        answer.append([start, target]) # 밑에 판 목표 봉으로 이동
        hanoi(extra, target, start, n-1) # 옮겨 뒀던 나머지 판 목표 봉으로 옮겨 주기
        

def solution(n):
    hanoi(1, 3, 2, n)
    return answer