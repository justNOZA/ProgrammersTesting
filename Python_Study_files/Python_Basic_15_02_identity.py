import calendar

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

    if id[7] == "9" or id[7] == "0":
        continue

    month = int(id[2:4])
    if 12 < month:
        continue

    if id[7] == "1" or id[7] == "2" or id[7] == "5" or id[7] == "6":
        year = int("19" + id[0:2])
    if id[7] == "3" or id[7] == "4" or id[7] == "7" or id[7] == "8":
        year = int("20" + id[0:2])

    date = int(id[4:6])
    if int(calendar.monthrange(year, month)[1]) < date:
        continue

    if id[7] == "1" or id[7] == "3":
        sex = "남자"
    if id[7] == "5" or id[7] == "7":
        sex = "외국인 남자"
    if id[7] == "2" or id[7] == "4":
        sex = "여자"
    if id[7] == "6" or id[7] == "8":
        sex = "외국인 여자"

    break
print(str(year) + "년 " + str(month) + "월 " + str(date) + "일생 " + sex)
