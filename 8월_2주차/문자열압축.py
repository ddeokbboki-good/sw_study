def solution(s):
    number = []
    if len(s) == 1:
        return 1
    for n in range(1, len(s)//2 + 1):
        result = ''
        cnt = 1
        count = []
        string = [s[x:x+n] for x in range(0, len(s), n)]
        for i, w in enumerate(string[:-1]):
            if w == string[i+1]:
                cnt += 1
            else:
                count.append(cnt)
                cnt = 1
        count.append(cnt)
        tmp = 0
        for idx, num in enumerate(count):
            if num == 1:
                result += string[tmp]
            else:
                result += str(num)+string[tmp]
            tmp += num
        if result:    
            number.append(len(result))   
    return min(number)