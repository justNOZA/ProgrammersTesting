#내용을 입력하세요. (종료는 새로운 행에서 엔터키)
#저장하시겠습니까? (y.n)
#파일명 : a.txt
#이미 존재하는 파일입니다. 다시 입력하세요.
#파일명 : b.txt
#b.txt 파일이 저장되었습니다.
import os

sli = []
while True :
    try :
        s = input('내용을 입력해주세요. 공백으로만 입력 시 입력이 멈춥니다.')
        if s.isspace() or len(s) == 0:
            break
        s += "\n"
        sli.append(s)
    except :
        continue

def save() :
    while True :
        name = input('저장할 파일명을 입력해주세요.')
        name += ".txt"
        while True :
            if not os.path.exists(name) :
                break
            name = input('이미 존재하고 있습니다. 다시 입력해 주세요.')
            name += ".txt"
        f = open(name, "wt")
        global sli
        for s in sli :
            f.write(s)
        f.close()
        break

while True :
    try :
        check = input('파일을 저장하시겠습니까? (Y/N)')
        if not check.lower() in "yn" :
            raise BaseException
        if check.lower() == "y" :
            save()
            break
        else :
            break
    except BaseException :
        continue
