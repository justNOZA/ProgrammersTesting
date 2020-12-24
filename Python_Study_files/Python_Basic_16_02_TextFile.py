#텍스트 파일에 쓰기

#파일 열기
f = open('ddd.txt', 'wt')
#파일 이름, 모드 (둘다 문자열 / 경로포함 입력)

#출력
f.write("""안녕하세요. 감사해요
잘있어요
다시 만나요\n""")
f.write('굿나잇')
#종료
f.close()

try :
    f = open("ddd.txt", "rt")
    text = f.read()
    print(text)
    while True :
        text = f.read(5)
        if len(text) == 0 : break
        print(text)
    line = 1
    while True :
        text = f.readline()
        if not text : break #변수가 없을경우 False인데 Not을 붙이면 True가 된다.
        print(line,":",text)
        line +=1
except FileNotFoundError :
    print('파일이 존재하지 않습니다.')
finally :
    f.close()

#파일이 있는지 없는지 확인 os모듈과 shutil 모듈에 정의되어 있음
