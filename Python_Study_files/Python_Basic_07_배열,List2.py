nlist = [5,4,3,2,5,6,8,9,3,1,7,8,7,5]
print(nlist.index(10)) #없을 경우 에러
print(nlist.index(5)) #여러개 존재할 경우 가장 먼저 위치한 값의 위치값을 반환
print(nlist.index(1)) #존재하는 해당 위치값을 반환
print(nlist.count(5)) #해당 값이 존재하는 개수를 반환
print(nlist.count(10)) #존재하지 않을 경우 0
print(max(nlist)) #존재하는 값중 가장 큰 값을 반환
print(min(nlist)) #존재하는 값중 가장 작은 값을 반환

nlist.sort() #순서대로 정렬
print(nlist)
nlist.reverse() #역순으로 정렬
print(nlist)
