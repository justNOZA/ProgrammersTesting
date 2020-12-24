import math # math module의 함수를 가져옴
from math import sqrt #math module에서 sqrt 함수만 불러온다.
import math as m #math.sqrt() 이렇게 쓰지 않고 m.sqrt() 로 부를 수 있게 별명을 지정
from math import sqrt as sq #역시 별명을 붙인 것

print(math.pi) #원주율
print(math.tau) #원주율의 2배
print(math.e) #자연 대수 상수
print(math.inf) #무한대 값은 inf라고 나온다. (float)
print(math.nan) # 숫자가 아닌 값 (float)

math.sqrt(4) #4의 제곱근
math.pow(2,4) #2의 4제곱
math.hypot(3,4) #피타고라스의 정의를 이용한 것으로 빗변의 값을 나타낸다.
math.factorial(3) #팩토리얼 값을 반환 음수를 입력시 에러
