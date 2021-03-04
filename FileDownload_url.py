import requests
#requests 모듈을 사용하기 위해서는
#pip install requests를 통해 먼저 인스틀을 해야 사용이 가능하다.
url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
open('google.ico', 'wb').write(r.content)
