line = int(input("Diamond 의 길이를 입력하세요(2~30) : "))

for x in range(1, line * 2, 2):
    print((" " * ( (line * 2 - 1 - x) // 2 )) + ("*" * x))

for y in range(line * 2-3, 0, -2):
    print((" " * ( (line * 2 - 1 - y) // 2 )) + "*" * y)
