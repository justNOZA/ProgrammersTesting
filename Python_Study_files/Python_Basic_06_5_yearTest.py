#년도를 입력받아 윤년, 평년 구분

year = int(input('year : '))
if year%4 == 0 and year%100 != 0 or year%400 == 0 :
    print('윤년')
else :
    print('평년')
