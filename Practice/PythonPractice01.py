#주민번호를 이용하여 어디 지역 츌산안자 확인
# 정상적으로 입력할 것을 가정하고 있다. 일단 3월 27일 기준
identifiedNum=input("주민등록번호를 입력하세요: ")

areaNum=int(identifiedNum[8]+identifiedNum[9])

if areaNum>=0 and areaNum<=8:
    print("%s: 출생 지역은 서울 입니다." % identifiedNum)
elif areaNum>=9 and areaNum<=12:
    print("%s: 출생 지역은 부산 입니다." % identifiedNum)
elif areaNum>=13 and areaNum<=15:
    print("%s: 출생 지역은 인천 입니다." % identifiedNum)
elif areaNum>=16 and areaNum<=25:
    print("%s: 출생 지역은 경기 입니다." % identifiedNum)
elif areaNum>=26 and areaNum<=34:
    print("%s: 출생 지역은 강원 입니다." % identifiedNum)
elif areaNum>=35 and areaNum<=47:
    print("%s: 출생 지역은 충청 입니다." % identifiedNum)
elif areaNum>=48 and areaNum<=66:
    print("%s: 출생 지역은 전라 입니다." % identifiedNum)
elif areaNum>=67 and areaNum<=91:
    print("%s: 출생 지역은 경상 입니다." % identifiedNum)
elif areaNum>=92 and areaNum<=95:
    print("%s: 출생 지역은 제주 입니다." % identifiedNum)
else:
    print("잘못된 주민등록번호입니다.")
