def solution(n, tops):
    a = [0 for _ in range(n)] # 오른쪽 아래 타일을 쓰는 케이스의 경우
    b = [0 for _ in range(n)] # 아닌 경우
    
    a[0] = 1
    b[0] = 2 + tops[0]
    
    for i in range(1, n):
        a[i] = (a[i - 1] + b[i - 1]) % 10007 
        
        if tops[i]:
            b[i] = 2 * a[i - 1] + 3 * b[i - 1]
        else:
            b[i] = a[i - 1] + 2 * b[i - 1]
        
        b[i] %= 10007
    
    return (a[-1] + b[-1]) % 10007