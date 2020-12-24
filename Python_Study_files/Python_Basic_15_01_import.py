#주민버호를 입력받은 이후 나이, 성별, 생일
import time
import calendar

id = []
age = 0
wd = 0
gen = "19"
sex = "남성"
yoil = ['월', '화', '수', '목', '금', '토', '일']
year = 0
month = 0
day = 0

def checkForm(check) :
    global id
    id = check.split("-")
    if len(id[0]) != 6 :
        return False
    if len(id[1]) != 7 :
        return False
    if  0 == int(id[1][0]) or int(id[1][0]) == 9 :
        return False
    if 3 <= int(id[1][0]) <= 4 or 7 <= int(id[1][0]) <= 8 :
        global gen
        gen = "20"
    global year
    global month
    global day
    year =  int(gen+id[0][:2])
    month = int(id[0][2:4])
    day = int(id[0][4:])
    if int(id[1][0]) == 2 or int(id[1][0]) == 4 or int(id[1][0]) == 6 or int(id[1][0]) == 8:
        global sex
        sex = "여성"
    t = time.localtime()
    if t.tm_year <= year :
        if t.tm_mon > month :
            return True
        elif t.tm_mon == month and t.tm_mday >= day :
            return True
        return False
    global wd
    wd = calendar.weekday(year, month, day)
    return True

while True :
    try :
        identity = input("주민등록번호를 입력하시오.")
        if not checkForm(identity) :
            gen = "19"
            sex = "남성"
            continue
        break
    except :
        gen = "19"
        sex = "남성"
        continue

now = time.localtime()
if now.tm_mon < month :
    age = now.tm_year - year - 1
else :
    if now.tm_mon == month and now.tm_mday < day :
        age = now.tm_year - year - 1
    else :
        age = now.tm_year - year

print("나이 : ",age)
print("성별 : ",sex)
print("생일은 %s월 %s일 입니다. %s요일에 태어났습니다."%(month, day, yoil[wd]))
