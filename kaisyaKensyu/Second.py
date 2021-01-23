##########################################################################
a = int(input("number please : "))
if a%2 != 0 :
    print('入力された数字',str(a),'は奇数です。')
else :
    print('入力された数字',str(a),'は偶数です。')
##########################################################################
for i in range(1, 21) :
    if i % 15 == 0 :
        print('FizzBuzz', end=" ")
    elif i % 5  == 0:
        print('buzz', end=" ")
    elif i % 3  == 0:
        print('fizz', end =" ")
    else :
        print(i, end = " ")
    if i % 10 == 0 :
        print()

##########################################################################
count = int(input('Please insert number:'))

while count > 0 :
    print('Spam' * count)
    count -= 1
else :
    print('Last but not least')
##########################################################################
for i in range(1,4):
    if i == 3:
        print(i)
    print('pass')
###Pass와 비어있는 무언가를 만들때 사용
###########################################################################
plist = []
studentNum = int(input('学生の数？'))
for i in range(1, studentNum+1) :
    plist.append(int(input('学生','の点数？')))

#print(plist)
sumP = 0;
for i in plist :
    sumP += i
print('学生たちの点数の合計：',str(sumP))
print('学生たちの点数の平均：',str(sumP/studentNum))

sumP2 = sum(plist,0)
print('学生たちの点数の合計2：',str(sumP2))
print('学生たちの点数の平均2：',str(sumP/len(plist)))

##########################################################################

cityDict = {'Kanagawa' : 'Yokohama', 'Miyagi' : 'Sendai'}
print('Kanagawaの県庁所在地は',cityDict.get('Kanagawa'),'です。')
print('Miyagiの県庁所在地は',cityDict['Miyagi'],'です。')
cityDict['Hokkaido'] = 'Sapporo'
print('Hokkaidoの県庁所在地は',cityDict.get('Hokkaido'),'です。')

#dic['a'] = 'b' 바로 추가는 불가
dic ={}
dic[1] = 2
print(type(dic))
print(dic.items())
###########################################################################
