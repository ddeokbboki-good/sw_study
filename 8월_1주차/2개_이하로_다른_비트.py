def solution(numbers):
    answer = []
    
    for num in numbers:
        bin = list("{0:b}".format(num))
        for idx in range(len(bin) - 1, -1, -1):
            if bin[idx] == "0":
                bin[idx] = "1"
                if idx != len(bin) - 1:
                    bin[idx+1] = "0"
                break
            if idx == 0:
                bin = ["1", "0"]+bin[1:]
        
        bin = ''.join(bin)
        digit = int(bin, 2)
        
        answer.append(digit)    
    return answer