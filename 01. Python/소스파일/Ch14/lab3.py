import urllib.request
import re

url ="http://finance.naver.com/item/main.nhn?code=005930"
html = urllib.request.urlopen(url)
html_contents =str(html.read().decode("ms949"))

# 첫 번째 HTML 패턴
stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_results[0]     # 두 개의 튜플 값 중 첫 번째 패턴
samsung_index = samsung_stock[1]     # 세 개의 튜플 값 중 두 번째 패턴

# 주식 정보만 추출함
index_list= re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

for index in index_list:
    print(index[1])                # 세 개의 튜플 값 중 두 번째 값
