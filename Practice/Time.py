import time

#def 함수 정의
def gettime() :
    now = time.localtime()
    return now.tm_hour, now.tm_min
#python은 함수의 리턴값을 튜플로 묶어 여러개 보낼 수 있다.
# 함수는 위에서 먼저 정의를 해주어야 사용이 가능하다.

result = gettime()
print("지금은 %d시 %d분 입니다."%(result[0], result[1]))
print(type(result)) #result의 형식은 tuple
