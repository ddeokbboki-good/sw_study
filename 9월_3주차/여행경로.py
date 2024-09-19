def solution(tickets):
    answer = ["ICN"]
    visited = [0 for _ in range(len(tickets))]
    addr = ["ICN"]
    tickets.sort(key = lambda x: x[1])
    last = []
    while 0 in visited:
        temp = 1
        j = addr.pop()
        for i in range(len(tickets)):
            if j == tickets[i][0] and not visited[i] :
                visited[i] = 1
                addr.append(tickets[i][1])
                answer.append(tickets[i][1])
                break
            else:
                temp += 1
                if temp == len(tickets)+1:
                    last.append(answer.pop())
                    addr.append(answer[-1])
    last.reverse()
    if last:
        for i in last:
            answer.append(i)
    return answer