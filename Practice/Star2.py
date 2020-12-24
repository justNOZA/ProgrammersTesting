num = 0
while True :
    try :
        num = int(input("홀수를 입력해 주세요."))
        if num % 2 != 1 :
            continue
        break
    except :
        continue

for i in range(0, int((num+1)/2)) :
    for j in range(int(num/2), i, -1) :
        print("   ", sep="", end="")
    for j in range(0, i*2+1) :
        print(" * ", sep="", end="")
    print()
for i in range(0, int(num/2)) :
    for j in range(0, i+1) :
        print("   ", sep="", end="")
    for j in range(int(num/2)*2-1, 2*i, -1) :
        print(" * ", sep="", end="")
    print()
    
