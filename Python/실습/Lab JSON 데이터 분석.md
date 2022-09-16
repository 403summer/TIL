# Lab: JSON 데이터 분석



* 파이썬에서 JSON을 사용하기 위해서는 json 모듈을 이용한다. JSON 데이터 포맷은 데이터 저장 및 읽기가 딕셔너리형과 완벽히 상호 호환되어, 딕셔너리형에 익숙한 사용자가 매우 쉽게 사용할 수 있다는 장점이 있다.
* 최근 많이 사용하는 웹에서는 데이터 제공을 위하여 REST API라는 서비스를 제공한다. REST 서버는 페이스북, 트위터, Github 등 거의 모든 웹 사이트에서 REST API를 통해 사용자에게 검색 등의 정보를 제공하는데, 이때 정보 교환 데이터 포맷으로 가장 많이 사용하는 것이 JSON이다.



## 1. JSON 읽기

* 소스파일 'json_example.json' 의 내용은 다음과 같다.

```json
{"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]}
```

```python
import json

with open("json_example.json", "r", encoding = "utf8") as f:
    contents = f.read()                     # 파일 내용 읽어 오기
    json_data = json.loads(contents)        # json 파싱
    print(json_data["employees"])           # 딕셔너리처럼 사용하기
```

```text
[{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, {'firstName': 'Peter', 'lastName': 'Jones'}]
```



## 2. JSON 쓰기

* 딕셔너리형으로 구성된 데이터를 json 형태의 파일로 변환하는 과정에 대해 알아보자

```python
import json

dict_data ={'Name':'Zara','Age':7,'Class':'First'} # 딕셔너리 생성

with open("data.json", "w") as f:
    json.dump(dict_data, f)
```



## 3. 트위터 데이터 읽어오기

* 다른 서비스에서 제공하는 API의 결과로 JSON 데이터를 받아 활용해 보자. 페이스북, 트위터, 유튜브 등의 SNS와 네이버, 카카오, 같은 포털 사이트는 자사가 제공하는 서비스와 다른 회사의 여러 제품을 연결하기 위해 다양한 API를 제공한다. API(Application Programming Interface)는 일종의 함수로, 해당 회사가 제공하는 서비스를 활용하기 위한 함수를 뜻한다. 일반적으로 API 서비스는 JSON으로 데이터를 주고 받기 때문에 JSON 데이터를 연습하기에 매우 좋은 환경이다.
* 트위터를 사용하기 위해서는 몇 가지 준비가 필요하다. 먼저 트위터를 사용하기 위한 계정이 있어야 한다. 첫 번째로 트위터를 가입한다. 두 번째로 해당 계정에 대한 인증을 받아야 한다. 흔히 OAuth라고 하는 인증 작업을 통해 API를 사용할 때, 서비스 대부분에서 받아야하는 작업니다.
* `https://apps.twitter.com` 이 사이트에서는 자신의 앱을 만들어야 한다. 앱은 특별한 것이 아니고, 자신이 만드는 프로그램의 이름이다. 먼저 앱을 만들고 오른쪽 상단의 [CREATE New App] 버튼을 클릭하여 앱을 생성한다.
* 다음으로 앱에 관한 정보를 입력한다. 입력 정보는 넣고 싶은 내용을 임의로 넣을 수 있다.
* 다음으로 앱의 API 키와 액세스 토큰을 확인한다. 생성된 앱으로 들어가면 'Keys and Access Tokens' 탭이 있고, 이 탭에서 API 키와 토큰 정보를 확인할 수 있다. 이 정보는 트위터 서비스에 접근하기 위한 일종의 열쇠로, 반드시 혼자만 가지고 있어야 한다.
* 마지막으로 트위터 접속을 위한 모듈을 설치한다. 모듈은 API 서비스와 OAuth 인증을 지원하는 서비스이다. cmd 창에 다음 명령어를 입력하여 해당 모듈을 설치한다.

```cmd
conda install requests
pip install requests-oauthlib
```



```python
import requests
from requests_oauthlib import OAuth1

# 사용자의 OAuth 정보 입력
consumer_key = '확인한 consumer_key'
consumer_secret = '확인한 consumer_secret'
access_token = '확인한 access_token'
access_token_secret = '확인한 access_token_secret'

# 사용자의 OAuth 인증 정보 생성
oauth = OAuth1(client_key=consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

# Twitter REST API를 사용해 특정 계정 정보 요청,s creen_name은 트위터 계정명
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}'.format('naver_d2')

# API URL과 계정 인증 정보를 HTTP로 전송
r = requests.get(url=url,auth=oauth)

# 결과를 json 형태로 다운로드함
statuses = r.json()

# 결과 출력
for status in statuses:
    print(status['text'], status['created_at'])
```

