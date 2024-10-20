# 다른 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면 인센티브x
# 두 점수의 합이 높은 순으로 석차를 내고, 점수의 합이 동일한 사원들은 동석차이며, 동석차의 수만큼 다음 석차 pass

def solution(scores):
    answer = 1
    w0, w1 = scores[0]
    scores.sort(key = lambda x : (-x[0], x[1]))
    max1 = scores[0][1]
    for i, j in scores:
        if w0 < i and w1 < j:
            return -1
            
        if i + j > w0 + w1:
            if max1 <= j:
                max1 = j
                answer += 1
                
    return answer 