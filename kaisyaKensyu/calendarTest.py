from datetime import datetime

tokyo = datetime(2020, 7, 24, 0, 0, 0)
today = datetime.today()

left = tokyo - today

sbt ='東京オリンピック'
sbb ='開催まであと' + str(left.days) + '日'
sbs = 'みんなの力で成功させよう'

deco = '='
width =20

print(deco *(width+12))
print(sbt.ljust(width))
print(sbb.rjust(width))
print(sbs.rjust(width))

print(deco *(width+12))
