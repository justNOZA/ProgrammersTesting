n = 0
try :
    n = 3 / 0
    print('n =',n)
except ZeroDivisionError as e :
    print('예외발생',e)
except :
    print('예외 잡음')  #전체를 다잡는 거는 맨 마지막으로 예외를 잡아야한다. 위에서 잡히면 해당하지 않음
else :
    print("예외 발생하지 않음")
finally :
    print("예외와 상관없이 무조건 실행")
print("예외처리 구문과 전혀 관계없는 부분",n)


try :
    1 + a                   # NameError (a가 정의되어 있지 않다.)
    1 + '2'                 # TypeError
    int('문자')               # ValueError
    3 / 0                   # ZeroDivisionError
    li = [1,2]
    li[3]                   #IndexError
except BaseException as e :
    print(e,"모든 오류 다잡는 BaseException")
except NameError as e :
    print(e,"name 'a' is not defined")
except TypeError as e :
    print(e,"unsupported operand type(s) for +: 'int' and 'str'")
except ValueError as e :
    print(e,"invalid literal for int() with base 10: '문자'")
except ZeroDivisionError as e :
    print(e,"division by zero")
except IndexError as e :
    print(e,"list index out of range")

while True :
    try :
        n = int(input('1~10까지의 정수를 입력하세요.'))
        if n % 2 == 0 :
            print("짝수입니다.")
            break
        if n <= 0 or n >= 11 :
            raise BaseException #Error를 발생시켜버림
    except :
        continue #아무것도 쓰지 않으면 syntaxerror 발생
#SyntaxError : 코드를 제대로 입력하지 않았을 경우 실행자체가 되지 않음 이 에러는 잡지 못한다. 수정하지 않는 한
