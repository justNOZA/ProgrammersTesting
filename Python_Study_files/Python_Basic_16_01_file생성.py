import os.path

string = ""
while True:
    temp_string = input("내용을 입력하세요 : ")
    if(len(temp_string) != 0):
        string += temp_string + "\n"
    else:
        break

select = input("저장 ? (1/0)")
if(select == "1"):
    while True:
        filename = input("파일명 : ")

        if os.path.isfile(filename) != True:
            file = open(filename, "wt") #경로 값까지....
            file.write(string)
            file.close()
            print(filename + " 파일이 저장되었습니다.")
            break
        else:
            print("이미 존재하는 파일입니다. 다시 입력하세요.")
else:
    print("종료")
