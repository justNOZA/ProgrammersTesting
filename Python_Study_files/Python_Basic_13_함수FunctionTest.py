#전달된 정수 사이의 합계 리턴
def sum(num1, num2) :
    sum = 0
    num3 = 0
    if num1 > num2 :
        num3 = num2; num2 = num1; num1 = num3
    for i in range(num1, num2+1) :
        sum += i
    return sum
n = sum(5, 1); print(n)

#전달된 정수까지의 팩토리얼
def fact(num) :
    a = 1
    if num <= 0 :
        a = 0
    for i in range(1, num+1) :
        a *= i
    return a
n = fact(-4); print(n)

#전달된 정수까지의 짝수의 합계
def sum2(num) :
    a = 0
    for i in range(num+1) :
        if i % 2 == 0 :
            a += i
    return a

def sum3(num) :
    a = 0
    for i in range(0, num+1, 2) :
        a += i
    return a

n = sum2(10); print(n)

#정수를 5개 전달받아 합계와 평균 리턴
def test(num1, num2, num3, num4, num5) :
    sum = 0
    avg = 0
    sum = num1 + num2 + num3 + num4 + num5
    avg = sum / 5
    return sum, str(avg)

def test2(*num) : #*가 붙으면 가변인수라고 해서 개수가 정해져 있지 않다. (타입은 튜플)
    sum = 0
    avg = 0
    for i in num :
        sum += i
    avg = sum / len(num)
    return sum, str(round(avg,2))

while True :
    try :
        n = test2(int(input('정수1를 입력해 주세요,'))
                    ,int(input('정수2를 입력해 주세요,'))
                    ,int(input('정수3를 입력해 주세요,'))
                    ,int(input('정수4를 입력해 주세요,'))
                    ,int(input('정수5를 입력해 주세요,'))
                    ,int(input('정수6를 입력해 주세요,')))
        print("합계 : %d, 평균 : %s"%(n[0], n[1]))
        break
    except :
        continue


#전달된 정수 사이의 합계 리턴 ## 추가 기본값 정의(끝에서부터 가능함)
def sum(num1, num2, ste = 1) :
    sum = 0
    num3 = 0
    if num1 > num2 :
        num3 = num2; num2 = num1; num1 = num3
    for i in range(num1, num2+1, ste) :
        sum += i
    return sum
n = sum(5, 10); print(n)


#키워드 인수
#함수에 값을 보낼 때 함수에 정의된 변수명과 동일하게 변수명을 적고 값을 전달하는 방식도 있다.
n = sum(num2 = 10, num1 = 5), print(n)
