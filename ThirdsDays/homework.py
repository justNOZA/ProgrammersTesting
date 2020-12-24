a = int(input('입력할 진법 2 / 8 / 10 / 16'))
b = input('값')
c = int(input('변환할 진법 2 / 8/ 10 / 16'))
d = int(b, a)
e = 0

if c == 2 :
    e = bin(d)
elif c == 8 :
    e = oct(d)
elif c == 10 :
    e = d
else :
    e = hex(d)
print('변환된 값은 ',e)
