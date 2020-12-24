#클래스 정의
class Product :
    #생성자
    def __init__(self, code, name, price) :
        self.code = code
        self.name = name
        self.price = price
    def __str__(self) :
        return "상품의 코드는 %s, 상품명은 %s, 가격은 %d입니다."%(self.code, self.name, self.price)

def test() :
    print("product 모듈의 Product클래스 실행")
