#키보드로부터 정수를 입력받아 중복되지 않는 정수 5개의 리스트를 생성
#검색할 정수 입력받음 >> 몇번째 있는지 결과를 출력(index()함수 사용)

li = [ ]
count = 0
while count < 5 :
    try :
        num = int(input('정수를 입력해 주세요.'))
        if num in li :
            raise ValueError
        li.append(num)
        count += 1
    except ValueError :
        continue

lnum = ""
while True :
    try :
        lnum = int(input('검색할 정수를 입력해 주세요.'))
        break
    except ValueError :
        continue

try :
    print(li.index(lnum)+1,"번째에 존재합니다.")
except ValueError :
    print('존재하지 않습니다.')
