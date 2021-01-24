try:
	f = open('foo.txt', 'r')
except FileNotFoundError as e:
	print('Error', str(e))
	print(type(e))
	print(e.args)
else:
	data = f.read()
	f.close()
finally :
	print('a') #무조건 실행

aa = "asfVdsdEE"
bb = "dsdaAA"
print(aa.capitalize() )
#最初の文字を大文字に
print(bb.lower() )
#小文字に変換
print(bb.swapcase())
#大文字は小文字へ、小文字は大文字に
print(aa.title() )
#タイトルケース（大文字からはじまって残りはすべて小文字）
print(aa.upper() )
#大文字に変換
