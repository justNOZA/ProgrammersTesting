#if문

n = input('점수 : ')
if int(n) < 70 :
    print('에라이 바보 ㅉㅉ')
    print('재시험이다.')
elif int(n) < 80 :
    print('Bronze')
elif int(n) < 90 :
    print('Sliver')
else :
    print('Gold')


#점수에 따라 수우미양가 중 하나 출력
while True :
    point = input('점수를 입력해 주세요 : ')
    if point != "" :
        try :
            point2 = float(point)
        except :
            print('숫자로 제대로 입력해주세요')
            continue
    if 0 <= point2 <= 100 :
        if point2 >= 90 :
            print('수'); break
        elif point2 >= 80 :
            print('우'); break
        elif point2 >= 70 :
            print('미'); break
        elif point2 >= 60 :
            print('양'); break
        else :
            print('가'); break
    else :
        print('재입력 해주세요'); continue
