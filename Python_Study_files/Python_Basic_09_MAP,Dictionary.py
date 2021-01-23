#JAVA의 MAP구조
#키와 값으로 이루어지는데 키 값은 중복될 수 없다.
#키의 값으로 검색해서 가져오는 것이기 때문에

dic = { 'a' : 'A', 'b' : 35}
print(dic) # 위의 값이 출력됨
print(type(dic)) #dict
print(dic['a']) #A
print(dic['c']) #error
dic['a'] = 'B' # 키 a의 값이 B로 변경된다.
dic['c'] = 13 # 새로운 키 c가 생성되고 값으로 13이 들어간다.
print(dic.get('a')) #딕셔너리 안의 a라는 키의 값에 해당하는 값을 읽어온다.
print(dic.get('d')) #없는 값을 불러오면 None값이 불러진다.
print(dic.get('d', '값이 존재하지 않습니다.')) #값이 존재하지 않을 경우 해당 글자가 출려된다,
del dic['c'] #없는 키를 삭제하려 하면 error  /  존재하는 키를 삭제할 경우 해당 키와 값이 삭제된다.
print(dic.keys()) # 해당 dictionary에 존재하는 키들을 불러온다,
print(dic.values()) #해당 dictionary에 존재하는 값들을 불러온다,
print(dic.items()) # 키와 값을 묶어서 출력한다.
klist = list(dic.keys()) # 키의 값을 배열로 묶어서 변수에 저장
print(type(klist))
print('a' in dic) #키 값에 있는지 없는지 True False로 알려줌
print('A' in dic) #value는 검색 안됨

li = [['boys', '소년'], ['girls', '소녀']]
di = dict(li) #2차원 배열을 dictionary로 만들 수도 있다.
print(di)

li2 = [['a','a'],['b',['a','b']]]
di2 = dict(li2)
print(di2)
