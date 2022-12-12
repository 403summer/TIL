from bs4 import BeautifulSoup

with open("books.xml", "r", encoding="utf8")as books_file:
    books_xml = books_file.read()               # 파일을 문자열로 읽어 오기

soup = BeautifulSoup(books_xml, "lxml")         # lxml 파서를 사용해 데이터 분석

# author가 들어간 모든 요소의 값 추출
for book_info in soup.find_all("author"):
    print(book_info)
    print(book_info.get_text())                 # 해당 요소에서 값 추출
