def solution(N, number):
    if N == number : 
        return 1

    nums = [set() for _ in range(8)]
    for i in range(8):
        nums[i].add(int(str(N)*(i+1)))

    for i in range(8):
        for j in range(i):
            for n1 in nums[j]:
                for n2 in nums[i-j-1]:
                    nums[i].add(n1 + n2)
                    nums[i].add(n1 - n2)
                    nums[i].add(n1 * n2)
                    if n2:
                        nums[i].add(n1 // n2)
                        
        if number in nums[i]:
            return i+1
        
    return -1
                    