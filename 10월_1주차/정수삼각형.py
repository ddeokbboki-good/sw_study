def solution(triangle):
    answer = triangle[0][0]
    dp = [[] for _ in range(len(triangle)-1)]
    dp.append(triangle[-1])
    
    for i in range(len(triangle) - 2, -1, -1):
        rowLength = len(triangle[i])
        for j in range(0, rowLength):
            dp[i].append(max(dp[i+1][j] + triangle[i][j], dp[i+1][j+1] + triangle[i][j]))

    answer = dp[0][0]
    return answer