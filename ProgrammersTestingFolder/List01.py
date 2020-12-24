def solution(array, commands):
    answer = []
    for a,b,c in commands :
        list = array[a-1:b]
        list.sort()
        answer.append(list[c-1])
    return answer

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


def solution(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer
