li = [[1,2,3,4], [1,3,5], [2,4,6,8], [[1,2],[3,4]], [6,7,8,9]]
print(li)
print(len(li))
print(li[0])
print(li[0][0])
print(len(li[1]))
print(type(li))
print(type(li[0]))
print(type(li[3][1]))

if type(li) == list :
    print(type(li))

for n in li :
    for m in n :
        if type(m) != list :
            print(m, end="/")
        else :
            for o in m :
                print(o, end="/")
print()

for n in range(len(li)) :
    for m in range(len(li[n])) :
        if type(li[n][m]) != list :
            print('li[%d][%d] = %d'%(n, m, li[n][m]))
        else :
            for e in range(len(li[n][m])) :
                print("li[%d][%d][%d] = %d"%(n,m,e,li[n][m][e]))
