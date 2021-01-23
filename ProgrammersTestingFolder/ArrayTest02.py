def solution(numbers):
    answer = []
    for i in range(0, len(numbers)-1) :
        for j in range(i+1, len(numbers)) :
            if numbers[i]+numbers[j] not in answer :
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer
#전부 지우고 다시 만들 예정
#커밋용 ... ㅡㅡ;;
