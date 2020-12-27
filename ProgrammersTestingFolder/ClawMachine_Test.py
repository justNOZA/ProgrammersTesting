def solution(board, moves) :
    answer = 0
    list = []
    for i in moves :
        for j in board :
            if j[i-1] != 0 :
                list.append(j[i-1])
                if len(list) > 1 and list[-1] == list[-2] :
                     del list[-2] #del list[-1] 도 가능
                     del list[-1]
                     answer += 2
                j[i-1] = 0
                #print(list)
                break

    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
