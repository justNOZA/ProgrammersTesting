#정수 10개를 입력받아 리스트에 저장
#값의 평균과 10이상 차이나는 정수들을 출력한다.

#결과의 예
# 입력한 정수 [1,2,3,4,40,55,-31,-5,10]
#평균 : 8.4
# 결과 : 40, 55, -31, -5

i = 1
nlist = []
sum = 0
while True :
    try :
        num = int(input('정수를 입력해 주세요.'))
        nlist.append(num)
        sum += num
        if i == 10 :
            break
        i += 1
    except :
        continue

print("입력한 정수 : ", nlist)
avg = round(sum / 10,2)
print("평균 :",avg)

print("결과 :",end=" ")
for n in nlist :
    if abs( n - avg) >= 10 :
        print(n, end=" ")

#---------------------------------------------------------------------------------------#

nlist = []
sum = 0
while True :
    try :
        num = int(input('정수를 입력해 주세요. 0입력시 종료'))
        if num == 0 :
            break
        nlist.append(num)
        sum += num
    except :
        continue

print("입력한 정수 : ", nlist)
avg = round(sum / len(nlist),2)
print("평균 :",avg)
#abs는 절대값
print("결과 :",end=" ")
for n in nlist :
    if abs( n - avg) >= 10 :
        print(n, end=" ")
