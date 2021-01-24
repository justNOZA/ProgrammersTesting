a = 0xf
b = 1.53456
print(type(b))
c = 1.54e10
print(hex(a)) #16진수 표기법으로 출력해줌

d = '100'
a = int(d, 2)

print(a)

e = 'ff'
a = int(e, 16)
print(a)

a = int(b)
print(a)

a = int(round(b, 0)) #round는 기본적으로 실수형을 반환한다.  소수점을 기준으로 0일 경우 정수부분 즉, 소수첫쨰자리에서 반올림
print(a)

aa = 12345
a = round(aa,-2) #-2는 십의 자리에서 반올림
print(a)

#--------------------------------------------------------------------------------------------------------------------------------------------------#
#진위형
a = True
b = False
print(a, b, type(a), type(b))

c = 3 > 0
print(c, type(c))
