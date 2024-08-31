def wordcheck(a,b):
    r = 0
    for i in range(len(a)):
        if a[i] == b[i] : 
            r+=1
    if r ==len(a)-1 : 
        return True
    return False

def solution(begin, target, words):
    if target not in words : return 0
    words,begin,r = set(words),{begin},0
    words = words-begin
    while words :
        r+=1
        temp = set()
        for b in begin:
            temp |= {i  for i in words if wordcheck(i,b)}
        if target in temp : return r
        elif not len(temp) : break
        words = words-temp
        begin = temp
    return 0