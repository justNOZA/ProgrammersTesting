order = []
for spam in range(1,11):
	order.append(spam)

order2 = [spam for spam in range(1,21)]
#list 안에 내부 포문으로 값을 넣기, 내부표기

print(order)
print(order2)

data = [ i for i in range(2,11, 2)]
print(data)

a = [ i*2 for i in range(1,6)]
print(a)

b = [i for i in range(1,11) if i%2 == 0]
print(b)
