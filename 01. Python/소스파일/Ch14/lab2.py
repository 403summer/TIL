import urllib.request                           # urllib 모듈 호출
import re

url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html" # url 값 입력
html = urllib.request.urlopen(url)      # url 열기
html_contents = str(html.read().decode("utf8")) # html 파일 읽고, 문자열로 변환

url_list = re.findall(r"(http)(.+)(zip)", html_contents)  # html 파일 읽고, 문자열로 변환
for url in url_list:
    full_url = "".join(url)                               # 출력된 튜플 형태 데이터 문자열로 join
    print(full_url)
    fname, header = urllib.request.urlretrieve(full_url, file_name) # file_name에 다운로드할 파일명 입력한 후, 파일 다운로드
    print ("End Download")
