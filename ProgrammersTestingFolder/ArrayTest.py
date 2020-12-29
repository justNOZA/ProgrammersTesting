def solution(numbers):
    answer = []
    for i in range(0, len(numbers)-1) :
        for j in range(i+1, len(numbers)) :
            if numbers[i]+numbers[j] not in answer :
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer

def solution2(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

def solution2`(numbers):
    sum_set = set([])

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum_set.add(numbers[i]+numbers[j])
    return sorted(list(sum_set))

def solution3(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer
numbers = [2,1,3,4,1]
numbers2 = [5,0,2,7]
print(solution(numbers))
print(solution(numbers2))
