#Python에 선언한 것은 전역변수
#내장 함수와 정의된 함수의 차이 len(a)  /  a.aaa()

#함수 정의
def test1() :
    return "test"

#함수 호출
a = test1()
print(a)

#함수를 정의하는 형식
# 1. Parameter 값이 존재하는 함수
num = 20
def test2(num) :
    print("전달된 숫자는 %d입니다."%(num)) #전역변수로 위에 존재하더라도 이름이 같은 다른 변수를 먼저 사용한다.

test2(10)
print(num)

# 2. Return 값이 존재하는 함수
def test3() :
    return 99 #return Type을 규정하지 않는다. (return 값에 맞추어서 알아서 return 됨)

n = test3()
print(n)

# 3-1. 인수 또는 리턴 값이 여러 개인 함수
def test4(a,b,c) :
    print("들어온 값은 각각 %d, %d, %d 이다."%(a,b,c))
    return a

n = test4(1,2,3)
print(n)

# 3-2.
def test5() :
    return 1,2,3 #tuple로 전환

n = test5()
print(n) #tuple로 리턴된다.
