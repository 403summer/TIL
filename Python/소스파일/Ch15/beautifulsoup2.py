import urllib.request
from bs4 import BeautifulSoup

with open("US08621662-20140107.XML", "r", encoding="utf8") as patent_xml:
    xml = patent_xml.read()             # 파일을 문자열로 읽어 오기

soup = BeautifulSoup(xml,"lxml")        # lxml 파서 호출

# invention-title 태그 찾기
invention_title_tag = soup.find("invention-title")
print(invention_title_tag.get_text())
