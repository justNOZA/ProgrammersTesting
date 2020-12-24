#1 정수를 입력받아서 양의 정수만 합계, 0을 입력하면 종료하고 결과 출력
sum = 0
count = 0
while True :
    try :
        num = int(input('정수를 입력해 주세요.'))
        if num > 0 :
            count += 1
            sum += num
        if num == 0 :
            print("입력한 양의 정수의 개수 :",count,"합계 :",sum, "평균 :", sum/count)
            break
    except :
        continue

#2 문자 1개와 정수 1개를 입력받고, 해당 문자부터 입력받은 정수의 개수 만큼 Unicode표를 출력한다.
word = 0
num = 0
while True :
    try :
        word =ord(input('문자를 1개 입력해 주세요.'))
        num = int(input('개수를 입력해주세요.'))
        break
    except :
        continue
i = 0
while i < num :
    print(chr(word),"(",word,")",sep='', end='  ')
    i += 1
    word += 1
