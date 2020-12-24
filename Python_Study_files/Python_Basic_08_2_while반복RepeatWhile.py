# [ while ] practice

#1
n = 1
while n < 5 :
    print('Repeat While',n)
    n += 1
print('_'*17)

#2
n = 1
while True :
    print('Repeat While', n)
    n += 2
    if n == 9 :
        break
print('_'*17)

#3
n = 1
while n < 5 :
    n += 1
    if n == 2 :
        continue
    print("Repeat While",n)
print("_"*17)
