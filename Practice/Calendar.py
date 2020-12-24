import calendar

while True :
    try :
        year = int(input("검색하고 싶은 해당 년도를 입력하세요."))
        month = int(input("검색하고 싶은 월을 입력해 주세요."))
        print(calendar.month(year,month))
        break
    except :
        continue

print(calendar.weekday(2000,2,30))
