def solution(number):
    answer = ''
    num = [str(i) for i in number]
    num.sort(key = lambda x : 3*x, reverse = True)
    
    if list(set(num)) == ['0']:
        answer = '0'
    else :
        answer = ''.join(num)
    
    return answer