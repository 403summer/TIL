# Lab: 웹 스크래핑 실습



## 1. 아이디 추출하기

<img src="../../image/14-4.PNG" alt="14-4" style="zoom:80%;" />

* 위에 데이터에서 아이디만 추출해보자. 일단 패턴을 파악해보자. 먼저 앞에는 숫자 또는 영문 대소문자가 여러개 있고 맨 끝에는 별표로 끝나는 것을 알 수 있다. 그러므로 정규 표현식을 만들면 `([A-Za-z0-9]+\*\*\*)`로 나타낼 수 있는데, 맨 끝에 있는` \*`는 *가 메타문자이기 때문에 특수 기호를 찾는 다는 의미로 추가하였다. 그런 다음 이 웹 페이지에 접속하여 HTML 문서를 가져오고 여기서 해당 정규 표현식 문자열만 추출하면 된다. 

```python
import re
import urllib.request

url = 'http://goo.gl/U7mSQl' # 접속할 웹 페이지
html = urllib.request.urlopen(url) # 웹 페이지 열기
html_contents = str(html.read()) # 웹 페이지 내용을 문자열로 가져옴
id_results = re.findall(r'([A-Za-z0-9]+\*\*\*)',html_contents)
# findall 전체 찾기, 정규 표현식 패턴대로 데이터 찾기

for result in id_results: # 찾은 정보를 화면에 출력
    print(result)
    
#codo***
#outb7***
#dubba4***
#multicuspi***
#...
```

* 정규 표현식에서 추출된 패턴은 튜플로 반환된다.



## 2. 파일 자동 다운로드

```python
import urllib.request # urllib 모듈 호출
import re

url = 'http://www.google.com/googlebooks/uspto-patents-grants-text.html' # url
html = urllib.request.urlopen(url) # url 열기
html_contents = str(html.read().decode('utf8')) # html 파일 읽고 문자열로 변환

url_list = re.findall(r'(http)(.+)(zip)',html_contents) # html 파일 읽고 문자열로 변환

for url in url_list:
    full_url = ''.join(url) # 출력된 튜플 형태 데이터를 문자열로 join
    print(full_url)
    fname, header = urllib.request.urlretrieve(full_url, file_name) # file_name에 다운로드 할 파일명 입력한 후, 파일 다운로드
    print('End Download')
```

* join() 함수를 사용하는 이유는 정규 표현식을 만들 때, (http)(.+)(zip)을 사용해서 만들었기 때문이다. 여기에서 () 단위로 튜플이 생성된다. 그러므로 (http, ,+,zip) 개별 값으로 생성되기 때문에 실제 사용할 때는 10행과 같이 join() 함수를 사용해야 한다.
* 12행에 파일 다운로드 코드를 작성하고, file_name 부분에 다운로드할 파일명을 입력하여 필요한 파일을 다운로드 한다.



## 3. HTML 파싱

* 네이버 삼성전자 주식 차트 HTML을 활용하여 파싱을 해보자
* https://finance.naver.com/item/main.nhn?code=005930

```text
<dl class="blind">
	        <dt>종목 시세 정보</dt>
	        <dd>2022년 09월 15일 16시 11분 기준 장마감</dd>
	        <dd>종목명 삼성전자</dd>
	        <dd>종목코드 005930 코스피</dd>
	        <dd>현재가 56,000 전일대비 하락 800 마이너스 1.41 퍼센트</dd>
	        <dd>전일가 56,800</dd>
	        <dd>시가 57,000</dd>
	        <dd>고가 57,100</dd>
	        <dd>상한가 73,800</dd>
	        <dd>저가 56,000</dd>
	        <dd>하한가 39,800</dd>
	        <dd>거래량 11,417,477</dd>
	        <dd>거래대금 643,694백만</dd>
        </dl>
```

* 위와 같이 파싱을 해보자



```python
import urllib.request
import re

url = 'http://finance.naver.com/item/main.nhn?code=005930'
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode('ms949'))

# 첫번째 HTML 패턴
stock_results = re.findall('(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)', html_contents)
samsung_stock = stock_results[0] # 두 개의 튜플 값 중 첫번째 패턴
samsung_index = samsung_stock[1] # 세 개의 듀플 값 중 두번째 패턴

# 주식 정보만 추출함
index_list = re.findall('(\<dd\>)([\s\S]+?)(\<\/dd\>)', samsung_index)

for index in index_list:
    print(index[1])
```

```text
2022년 09월 16일 11시 35분 기준 장중
종목명 삼성전자
종목코드 005930 코스피
현재가 55,900 전일대비 하락 100 마이너스 0.18 퍼센트
전일가 56,000
시가 55,600
고가 55,900
상한가 72,800
저가 55,500
하한가 39,200
거래량 5,190,915
거래대금 289,044백만
```



