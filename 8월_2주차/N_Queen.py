def N_Queen(number, queens):
    if len(queens) == number: # 끝까지 배치 완료
        return 1
    
    else:
        cnt = 0
        
        for i in range(number):
            flag = 1
            for j in range(len(queens)):
                if queens[j] == i or abs(queens[j] - i) == abs(len(queens) - j):
                    flag = 0
                    break
                    
            if flag: # 배치 가능하면 다음으로 계속
                cnt += N_Queen(number, queens + [i])
        
        return cnt
    
    
def solution(n):
    return N_Queen(n, [])