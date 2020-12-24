#리스트 사용
nlist = [1,2,3,4,5]
print(nlist) # 배열 전체를 출력
print(nlist[0]) # 해당 배열에 존재하는 순서에 따라 값이 출력
# print(nlist[5]) 오류발생
print(len(nlist)) # 배열의 길이
print(3 in nlist) # 해당 값이 배열에 존재하는지 여부를 알려준다.
print(7 not in nlist) # 해당 값이 존재하지 않은지 여부를 알려줌

slist = ['aaa', 'bbb', 'ccc']
print(slist)
print(slist[1])
print(len(slist))
print(len(slist[0])) #배열에 존재하는 문자의 길이값
#print(len(nlist[0]))
print('bbb' in slist)
print('bbbb' in slist)
print('bb' not in slist)
print('bb' in slist[1]) #문자열안에 해당 문자가 존재하는지를 알려준다.

sublist = nlist[2:4] #배열번호 2번부터 3번까지 가져온다.
print(sublist)
sublist2 = nlist[0:5:2] #0번부터 4번까지 한개씩 뛰고
print(sublist2)

print(nlist)
nlist[0] = 10
print(nlist)
nlist[0:5:2] = [100, 200, 300]
print(nlist) #해당위치에 새로운 값으로 변환시킨다.

nlist.append(500); print(nlist) #배열의 마지막에 해당 값을 추가한다.
nlist.insert(5,99); print(nlist) #앞의 숫자의 위치에 뒤의 값을 추가한다.
nlist.insert(88,99); #맨 마지막에 값이 추가가 될 뿐이다.
nlist = nlist + [5,6,7]; print(nlist) #새로운 배열을 뒤에 더한다.(추가한다.)
nlist = nlist * 2; print(nlist) #배열의 내용을 똑같이 뒤에 추가한다.
del nlist[0]; print(nlist) #해당 배열의 위치에 해당하는 값을 삭제한다.
# del nlist[1000];  없는 값은 삭제할 수 없다.
print(nlist[-2]) # 음수 값을 입력하면 뒤의 숫자부터 순서대로 출력한다.
print(nlist[-20]) #길이가 20일때 -20이면 가장 앞의 숫자
