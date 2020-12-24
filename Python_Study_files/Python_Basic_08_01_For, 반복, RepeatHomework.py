
#구구단
for a in range(1, 10, 3) :
    for b in range(1, 10) :
        for c in range(a, a+3) :
            print("\t",c,"*",b,"=",c*b, end=" ")
        print()
    print()

# 짝수만 출력
for a in range(1,10) :
    if a % 2 == 0 :
        print(a, end=" ")

# 홀수만 출력
for a in range(1,10) :
    if a % 2 != 0 :
        print(a, end=" ")

#10씩 증가 0부터 100까지
for a in range(10,101,10) :
    print(a, end=" ")

#거꾸로 출력 10 ~ 1
for a in range(10, 0, -1) :
    print(a, end=" ")

#1 10 100 1000 10000 출력
for a in range(0, 5) :
    print(10**a, end=" ")


# 1 ~ 100 (20, 50 제외)
i = 0
for a in range(1, 101) :
    if a == 20 or a == 50 :
        continue
    print(a, end=" ")
    i += 1
    if i == 10 :
        print()
        i = 0

# 숫자를  5개 입력받고 해당 숫자의 전체 합계를 구하시오.
sum = 0
for a in range(0, 5) :
    try :
        num = int(input('숫자를 입력해주세요.'))
        sum += num
    except :
        pass
print("전체합계 :",sum)

# 위에서 짝수만 합계
sum = 0
for a in range(0, 5) :
    try :
        num = int(input('숫자를 입력해 주세요.'))
        if num % 2 == 0 :
            sum += num
    except :
        pass
print("짝수 합계 :",sum)

#위에서 홀수 합계
sum = 0
for a in range(0, 5) :
    try :
        num = int(input('숫자를 입력해 주세요.'))
        if num % 2 == 1 :
            sum += num
    except :
        pass
print("홀수 합계 :",sum)

#숫자를 계속 입력받고, 합계가 4000이 넘으면 stop and print
sum = 0
while True :
    try :
        num = int(input('숫자입력'))
        sum += num
        if sum > 4000 :
            print(sum)
            break
    except :
        pass


# 로또 번호 뽑기
import random
i = 0
list = []
while True :
    if i < 6 :
        num = random.randint(1,45)
        list.append(num)
        if list.count(num) > 1 :
            continue
        print(num, end=" ")
        i += 1
    else :
        break
