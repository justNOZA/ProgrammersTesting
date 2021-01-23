import calendar

def solution(a, b):
    day ={0 : 'MON', 1 : 'TUE', 2 : 'WED', 3 : 'THU', 4 : 'FRI', 5 : 'SAT', 6 : 'SUN'}
    answer = day[calendar.weekday(2016, 1, 5)]
    print(answer)

solution(2,11)
