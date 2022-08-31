import re
import urllib.request

url = "http://goo.gl/U7mSQl"             # 접속할 페이지
html = urllib.request.urlopen(url)       # 페이지 열기
html_contents = str(html.read())         # 페이지의 내용을 문자열로 가져옴
id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)
# findall 전체 찾기, 정규 표현식 패턴 대로 데이터 찾기

for result in id_results:                 # 찾은 정보를 화면에 출력
    print (result)
