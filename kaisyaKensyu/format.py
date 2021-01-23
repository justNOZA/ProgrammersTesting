a = "Spam"
"{0:s}".format(a)
#제 1인수를 문자열로
print("{0:06.2f}".format(12.3456))
#0열 부터 소수점 포함6개표시하는데 소수점은 2자리만
print("{0:07.2f}".format(12.3456))

print("Tech")
print("{0}".format("Tech"))
print("{0:s}".format("Tech"))

print("{0}, {1}, {2}".format(100,"Tech",200))
print("{2}, {0}, {1}".format(100,"Tech",200))

print("{0:d}".format(123))
print("{0:d}".format(5))
print("{0:04d}".format(5))
print("{0:f}".format(12.3456))
print("{0:06.2f}".format(12.3456))
#############################################333
def self_produce(first, last, age, hob) :
    print("내 이름은 ", first, last, " 입니다.", "나이는 ", age, " 취미는 ",hob," 입니다.")

self_produce("a", "b", "24", "ss")
self_produce(age="25", hob="ssw", first="v", last="d")

#합수 키워드 설정
####################################################3

vv = ["a", "b", "c", "d", "e"]

v1 = vv[1:2]
print(v1)
v2 = vv[1:-1]
print(v2)
v3 = vv[1:]
print(v3)
v4 = vv[:2]
print(v4)
v5 = vv[:]
print(v5)
