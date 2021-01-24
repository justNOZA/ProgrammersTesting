class Calculator:
	def __init__(self):
		self.price = 0
		self.shippingFee = 1000
	def addItem(self, a):
		self.price += a
#	def setShippingFee(self, b) :
#		self.shippingFee = b
	def calculate(self):
		print('price is ', str(self.price + self.shippingFee))
a = Calculator()
a.addItem(500)
a.calculate()

b = Calculator()
b.addItem(500)
b.addItem(800)
#b.setShippingFee(1500)
b.shippingFee = 1500
b.calculate()

###############################################
class best :
	c = 1
	def __init__(self):
		print("aa2")
		self.f = 7
	def aa(self) :
		print("aa")
	def bb(self, mm) :
		print(mm)

a = best()
a.aa()
a.bb("hh")
print(a.c)
print(a.f)
