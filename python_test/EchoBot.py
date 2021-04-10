"""
제어문을 사용해서 연속적으로, 여러 종류의 질문에 답변해보자.
사용자와 계속적으로 질의/응답을 진행하기 위해서 반복문(while)을 사용하자.
다양한 질문을 처리하기 위해 if 문을 사용하자.
"""

while True: # 무한 반복문이다.

    # 입력을 받아들인다
    user_message = input('[Say Something]: ')

    # 입력된 문자열의 공백을 정리한 후 소문자로 변환한다
    user_message = " ".join(user_message.split()).lower()


    # 사용자가 bye, see you  등을 입력하면 종료한다.
    if user_message == 'bye' or user_message == 'see you' or user_message == "":
        print('bye')
        break
    elif user_message == 'hi':
        print('hi')
    elif user_message == 'good to see you':
        print('nice to meet you')
    else:
        print("I don't get it")

# 이 프로그램은 무한 반복이기 때문에
# bye를 입력하거나
# 아니면 셀 좌측 상단의 종료 버튼을 눌러서 강제 종료해야한다.
