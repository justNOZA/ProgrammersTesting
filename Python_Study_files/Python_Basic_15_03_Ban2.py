import calendar
import time
id = ""
year = -1
month = -1
date = -1
sex = ""
while True:
    id = input("주민등록번호 : ")

    if len(id) != 14:
        continue

    if id.find("-") != 6 or id.rfind("-") != 6:
        continue

    temp = id.split("-")
    if temp[0].isdigit() != True or temp[1].isdigit() != True:
        continue

    if id[7] in "90":
        continue

    month = int(id[2:4])
    if 12 < month:
        continue


    if id[7] in "1256":
        year = int("19" + id[0:2])
    if id[7] in "3478":
        year = int("20" + id[0:2])

    date = int(id[4:6])
    if int(calendar.monthrange(year, month)[1]) < date:
        continue

    if id[7] in "13":
        sex = "남자"
    if id[7] in "57":
        sex = "외국인 남자"
    if id[7] in "24":
        sex = "여자"
    if id[7] in "68":
        sex = "외국인 여자"

    break
print(str(year) + "년 " + str(month) + "월 " + str(date) + "일생 " + str(time.localtime().tm_year - year + 1) + "살 " + sex)
