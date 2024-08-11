def solution(board):
    answer = 1
    bingo = 0
    flag = {"X" : 0, "O" : 0, "." : 0}
    bingo = {"X" : 0, "O" : 0, "." : 0}
    
    for y in range(3):
        for x in range(3):
            flag[board[y][x]] += 1
                
            if y - 1 == 0 and y + 1 == 2 :
                if board[y - 1][x] == board[y][x] and board[y + 1][x] == board[y][x]:
                    bingo[board[y][x]] += 1

            if x - 1 == 0 and x + 1 == 2 :
                if board[y][x - 1] == board[y][x] and board[y][x + 1] == board[y][x]:
                    bingo[board[y][x]] += 1

            if x - 1 == 0 and y + 1 == 2 :
                if board[y + 1][x - 1] == board[y][x] and board[y - 1][x + 1] == board[y][x]:
                    bingo[board[y][x]] += 1

            if x - 1 == 0 and y - 1 == 0 :
                if board[y - 1][x - 1] == board[y][x] and board[y + 1][x + 1] == board[y][x]:
                    bingo[board[y][x]] += 1
    
    if bingo["O"] >= 1 and bingo["X"] >= 1:
        answer = 0
    
    elif bingo["X"] >= 1 and flag["O"] != flag["X"]:
        answer = 0
        
    elif bingo["O"] >= 1 and flag["O"] - flag["X"] != 1:
        answer = 0
        
    elif flag["O"] - flag["X"] > 1 or flag["X"] > flag["O"]:
        answer = 0
    
    return answer
    