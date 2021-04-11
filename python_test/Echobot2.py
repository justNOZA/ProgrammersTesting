# respond( )라는 함수를 정의하고 있다.
# 이 함수는 사용자의 메시지를 파라미터로 받아서 대답을 반환한다.
def respond(user_message):
    if user_message == 'bye' or user_message == 'see you' or user_message == "":
        return('bye')
    elif user_message == 'hi' or user_message == 'hello':
        return('hi')
    elif user_message == 'good to see you':
        return('nice to meet you')
    else:
        return("i don't get it")


# 아래는 while True라고 해서 무한 반복하게 만들었다.
while True:
    user_message = input('[Say Something]: ')
    user_message = " ".join(user_message.split()).lower()
    chatbot_message = respond(user_message)
    print(chatbot_message)
    if chatbot_message == 'bye':
        break # while 문을 break하고 탈출한다. 즉 전체 프로그램이 종료한다.
