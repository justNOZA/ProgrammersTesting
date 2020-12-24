word = "Python is so easy"
print(word)                         #해당 값을 그대로 출력
print(word[0])                      #해당 위치에 존재하는 글자를 출력
print(word[-10])                    #뒤에서부터 -1로 시작하여 해당위치의 글자 출력
print(word[20])                     #범위를 벗어날 경우 error
word[0] = "a"                       #불가능하다.

#슬라이스
print(word[2:5])                    #tho
print(word[:10])                    #Python is
print(word[10:])                    #so easy
print(word[10:-2])                  #so ea

#검색
print(word.find('o'))               #해당 글자가 앞에서부터 어디에 존재하는가?
print(word.rfind('o'))              #해당 글자가 뒤에서부터 어디에 존재하는가?
print(word.index('o'))
print(word.rindex('o'))
#index와 find는 기능은 유사하지만 find의 경우 없는 글자를 찾으려고 하면 -1이 반환되지만 index의 경우에는 오류가 발생한다.
print(len(word))                    #글자의 길이값을 반환한다 공백의 길이를 모두 센다.
print(word.count('o'))              #해당 글자가 문자열에 몇개 존재하는지 알려준다.
print('on' not in word)              #글자가 문자열에 존재하지 않는가?
print('o' in word)                  #글자가 문자열에 존재하는가?
print(word.startswith('p'))
print(word.startswith("P"))         #글자가 해당 글자로 시작하는가? (endswith 특정문자로 끝나는가?)

print(word.isalpha())           #모든 문자가 알파벳인가?  공백이 있을 경우 False
print(word.islower())           #only 소문자? 역시 공백이 없어야 함
print(word.isupper())           #only 대문자?
print(word.isspace())           #모든 문자가 공백?
print(word.isalnum())           #모든 문자가 알파벳또는 숫자?
print(word.isdecimal())         #레알루다가 only 숫자
print(word.isdigit())               #숫자적 표현 제곱 등등도 숫자로 인식
print(word.isnumeric())            #더 큰 범주까지 숫자로 인식
print(word.isidentifier())             # 명칭으로쓸 수 있는 문자로만 구성?
print(word.isprintable())              #출력가능?

#변경
print(word.lower()) #소문자
print(word.upper()) #대문자
print(word.swapcase()) # 대소문자 반대로
print(word.capitalize()) # 문장의 첫글자만 대문자로
print(word.title()) #단어마다 첫글자를 대문자로
print(word.lstrip()) #왼쪽 공백 제거
print(word.rstrip()) #오른쪽 공백 제거
print(word.strip()) #양쪽 공백 제거

#분할
print(word.split()) #default값으로 기본적으로 공백을 기준으로 분할
p = word.split('9')
print(type(p))
print(word.split('9')) #해당 글자 기준으로 분할 (해당글자는 없어짐)

#대체
print(word.replace("Python", "JAVA")) #교체해버림
print(word.replace("python", "java"))   #교체하려는 글자가 없을경우 교체가 되지 않음
