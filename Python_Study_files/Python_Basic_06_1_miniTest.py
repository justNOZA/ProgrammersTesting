#입력받을 진법(2, 8, 10, 16)
#입력받은 값
#입력할 진법 (2, 8, 10, 16)
#결과 ff(16)> 0b11111111(2)

checkType = 1
while True :
    try :
        checkType = int(input('입력할 진법을 적어주세요. (2, 8, 10, 16)'))
        if checkType != 2 and checkType != 8 and checkType != 10 and checkType != 16:
            print('한정된 범위에서 선택해 주세요.')
            continue
        else :
            break
    except :
        print('다시 입력해 주세요.'); continue

while True :
    if checkType == 2 :
        try :
            number = int(input('값을 입력해 주세요'), 2)
            changeType = int(input('변환할 진법을 적어주세요. (8, 10, 16)'))
            if changeType == 8 :
                print("8진법으로 변환한 값은 ",oct(number),"입니다.")
                break
            elif changeType == 10 :
                print("10진법으로 변환한 값은 ", str(number),"입니다.")
                break
            elif changeType == 16 :
                print("16진법으로 변환한 값은 ",hex(number),"입니다.")
                break
            else :
                print('한정된 범위에서 골라주세요2')
                continue
        except :
            print('정상적으로 입력해 주세요.')
            continue 
    elif checkType == 8 :
        try :
            number = int(input('값을 입력해 주세요'), 8)
            changeType = int(input('변환할 진법을 적어주세요. (2, 10, 16)'))
            if changeType == 2 :
                print("2진법으로 변환한 값은 ",bin(number),"입니다.")
                break
            elif changeType == 10 :
                print("10진법으로 변환한 값은 ", str(number),"입니다.")
                break
            elif changeType == 16 :
                print("16진법으로 변환한 값은 ",hex(number),"입니다.")
                break
            else :
                print('한정된 범위에서 골라주세요2')
                continue
        except :
            print('정상적으로 입력해 주세요.')
            continue
    elif checkType == 10 :
        try :
            number = int(input('값을 입력해 주세요'))
            changeType = int(input('변환할 진법을 적어주세요. (2, 8, 16)'))
            if changeType == 8 :
                print("8진법으로 변환한 값은 ",oct(number),"입니다.")
                break
            elif changeType == 2 :
                print("2진법으로 변환한 값은 ", bin(number),"입니다.")
                break
            elif changeType == 16 :
                print("16진법으로 변환한 값은 ",hex(number),"입니다.")
                break
            else :
                print('한정된 범위에서 골라주세요2')
                continue
        except :
            print('정상적으로 입력해 주세요.')
            continue
    else :
        try :
            number = int(input('값을 입력해 주세요'), 16)
            changeType = int(input('변환할 진법을 적어주세요. (2, 8, 10)'))
            if changeType == 8 :
                print("8진법으로 변환한 값은 ",oct(number),"입니다.")
                break
            elif changeType == 10 :
                print("10진법으로 변환한 값은 ", str(number),"입니다.")
                break
            elif changeType == 2 :
                print("2진법으로 변환한 값은 ",bin(number),"입니다.")
                break
            else :
                print('한정된 범위에서 골라주세요2')
                continue
        except :
            print('정상적으로 입력해 주세요.')
            continue
