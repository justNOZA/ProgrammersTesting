# 별찍기

for a in range(0, 3) :
    for b in range(0, 5) :
        print(" ", end=" ")
    for c in range(0, a+1) :
        print(" *", end="")
    print()
for a in range(0, 3) :
    for b in range(0, 6) :
        if b < 5 :
            print(" ", end=" ")
        else :
            print(" *")
for a in range(0, 3) :
    for b in range(0, a) :
        print(" ", end=" ")
    for c in range(11, a*2, -1) :
        print("*", end=" ")
    print()
