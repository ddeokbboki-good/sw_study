def solution(seq, k):
    
    e_idx = 0
    length = len(seq) 
    answer = [0, length - 1]   
    val = seq[0]
    
    for s_idx in range(length):
        while e_idx < length - 1 and val < k:
            e_idx += 1
            val += seq[e_idx]
        
        if val == k and e_idx - s_idx < answer[1] - answer[0]:
            answer = [s_idx, e_idx]
            
        val -= seq[s_idx]
             
    return answer