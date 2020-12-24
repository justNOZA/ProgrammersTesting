class Account : #클래스 정의
    def __init__(self,balance) :        #생성자
        self.balance = balance         #맴버 변수 초기화 // 맴버변수를 별도로 정의할 필요는 없다.
    def deposit(self, money) :
        self.balance += money       #맴버변수를 이용하려면 self를 무조건 입력을 해주어야 한다.
    def inquire(self) :                    #self는 꼭 입력을 해주어야 한다.
        print("잔액은 %d원 입니다."% self.balance)

sinhan = Account(8000)
sinhan.deposit(1000)
sinhan.inquire()

nonghyup = Account() #__init__에  맴버변수를 입력받아야 하는데 없어서 오류발생
nonghyup.inquire()


#클래스 정의
class Product :
    #생성자
    def __init__(self, code, name, price) :
        self.code = code
        self.name = name
        self.price = price
    def printProduct(self) :
        print("상품의 코드는 %s, 상품명은 %s, 가격은 %d입니다."%(self.code, self.name, self.price))
#클래스 정의 끝

ob = Product('A01', 'Monitor', 10000)
print(ob.name)
ob.printProduct() #이 매서드를 실행하면 상품의 코드와 상품명 가격이 출력되도록 만들어라

#클래스의 상속
class Product2(Product) :
#이 클래스는 위의 Product클래스를 상속받는다,

#336페이지 엑세서에서 __ 정보은폐가 불가능하다.
#340페이지 __ 클래스 차원에 존재하는 static변수(맴버변수가 아니다.) 
