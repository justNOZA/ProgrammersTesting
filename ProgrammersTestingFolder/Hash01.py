def solution(participant, completion):
    answer = ""
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)) :
        if participant[i] != completion[i] :
            answer = participant[i]
            break

    if answer == "" :
         answer = participant[len(participant) - 1]
    return answer

#다른 사람 풀이 collection 모듈의 counter함수: 데이터의 개수를 셀 때 유용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

#다른 사람 풀이2 #해시 함수 사용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

list = solution(["a","b","d","z","x"], ["b","x","a","d"])
print(list)
