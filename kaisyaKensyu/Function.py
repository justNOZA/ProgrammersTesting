def Solution() :
    price = int(input('How much is it? :'))
    quantity = int(input("Waht's the quantity? :"))
    royaltyRate = float(input('How much is the royalty? :'))
    royalty = price * quantity * royaltyRate
    return royalty

print('印税は','円です', sep=str(Solution()))
#######################################################
def spam(num = 10): #default값 설정
    return 'spam'*num

order = spam(3)
print(order)

order = spam()
print(order)
#######################################################3
def survey(message = 'Question') :
    print(message + ":" , end=str())
    answer = input()
    return answer

question1 = survey("Please input your Family name")
question2 = survey("Please input your First Name")
file = open("list.txt", 'a') #파일의 위치는 워크스페이스의 위치/ 작업하고 있는 파일의 같은 폴더 위치가 아님
# ’ｒ’읽기 / 'w' 쓰기 / 'a' 추가하기 .. 이미 존재하는 파일을 'w'로 열면 초기화가 되버림 그래서 'a'를 사용
file.write(question2+" "+question1+"\n")
file.close()
