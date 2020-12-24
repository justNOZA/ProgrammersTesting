#변수, 자료형
a = 1
print(type(a))
a = '1'
print(type(a)) #동적 타입
#del 메모리에서 변수를 삭제

width = input('폭')
height = input('높이')
d = int(width)*int(height)
print('면적 =', d)

# **  : 거듭제곱
print(2**10)
del a
a = 0xf #16진수의 경우 앞에 0x를 붙여준다. 0~9 abcdef
print(a) #16진수 값을 10진수로 변환하여 알려준다.
print(hex(a))
del a
a = 0o10 #8진수는 0o
print(a)
del a
a = 0b10 #2진수는 0b
print(a)

#2진법, 8진법, 16진법 활용
second = input()
second2 = bin(int(second)) # 받은 숫자값을 2진법으로 변환
print(second2)
second3 = '0b'+second
print(second3)
second4 = int(second3, 2)
print(second4)
#int(형변환에 맞는 값, 2 /8 / 16을 입력해주면 그에 맞게 변환)
#hex(16) / bin(2) / oct(8) 이안에 숫자값을 넣으면 그것에 맞게 변환한 값을 제공
#str() 문자열로 변환 / float() 실수형으로 변환

b = 1.23456 #실수형
c = 1.5e10 #실수형
d = 1.23e10
print(d)
print(type(b), type(c))
print(c)


#복소수
j = 1+2j
print(j)

#확장열 > 특수문자를 사용하기 위해 앞에 역슬러쉬를 입력 (역슬러쉬 2번 쓰거나 역슬러쉬 + r을 입력하면 특수문자로 변환하지 않는다.)
print('\n, \t,\", \', \\')
#긴문자열 >> 큰따옴표 세개를 입력해서 시작하면 긴문자열로 인식한다. 그리고 혹은 엔터이후 백슬러쉬를 썼을 경우 긴 문자열로 받아들인다.
# >> 문자열을 나열하면 알아서 묶여버린다. 혹은 괄호로 묶었을 경우에도
s = """안녕하세요 감사해요
잘있어요
다시 만나요"""
print(s)

s2 = 'dksusdgktpdy \
rkatkgody \
ahffkdy'
print(s2)

s3 = ('dddd'
'divmoddd'
'ddd')
print(s3)

s4 = 'aaa''bbb''ccc'
print(s4)

# 문자형은 별도로 존재하지 않는다. / ord는 문자코드 값을 chr은 숫자값으로 문자코드로 ....
print(ord('K'))
print(chr(100))

#다이아몬드 만들기
for i in range(1, 4) :
    for j in range(i, 3) :
        print(" ", end='')
    for k in range(1, 2*i) :
        print("*", end="")
    print()
for p in range(1, 3) :
    for q in range(0, p) :
        print(" ", end="")
    for o in range(2*p, 5) :
        print("*", end="")
    print()
