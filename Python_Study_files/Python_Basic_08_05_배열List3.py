#규칙적인 배열을 보다 쉽게 만들 수 있는 방법이 있다? for문의 응용 : List Comprehension
list1 = [ a*2 for a in range(1, 21, 2)]
print(list1)

#1. 3의 배수만
list2 = [a*a for a in range(1,31) if a % 3 == 0]
print(list2)

#2. 3또는 5의 배수
list3 = [a for a in range(1,101) if a % 3 == 0 or a % 5 == 0]

## 연습
asd = [[1,2,3],[4,6,8],[9,11,13]]

asd2 = []

for e in asd :
    e1 = [a+1 for a in e]
    asd2.append(e1)

print(asd,asd2)


i = 0
count = 0
while i < len(list3) :
    count += 1
    print(list3[i], end=" ")
    if count % 5 == 0 :
        print()
    i += 1

#3. 위의 코드를 수정
list4 = []
for n in range(1, 31) :
    if n % 3 == 0 :
        list4.append(n*n)
print(list4)

list5 = []
for n in range(1, 101) :
    if n % 3 == 0 or n % 5 == 0 :
        list5.append(n)
print(list5)
