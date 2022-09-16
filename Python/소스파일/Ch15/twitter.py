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
