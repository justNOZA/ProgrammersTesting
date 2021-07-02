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

def solution(list):
     answer = True
     check = False
     list = sorted(list, key=len)
     for i in range(0, len(list)):
        if check:
             break
        current = list[i]
        for j in range(i+1, len(list)):
            comp = list[j]
            if len(current)<len(comp) and current == comp[0:len(current)]:
                answer = False
                check = True 
                break
    return answer


class Solution {
    public boolean solution(String[] pb) {
        boolean a = true;

        for(String b : pb){
            int i = 0;
            for(String c : pb){
                if(c.indexOf(b) == 0){
                    i++;
                }
                if(i == 2){
                    return false;
                }
            }
        }
        return a;
    }
}
