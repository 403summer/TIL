# Lab: XML 파싱



## 1. BeautifulSoup 모듈 개요



* XML 문서는 HTML 문서와 구조가 같은 마크업 언어이므로 정규 표현식을 활용하여 파싱을 해도 문제 없다. 여기서는 가장 많이 사용되고 파이썬 마크업 언어 스크래핑 도구인 BeautifulSoup 모듈을 사용하여 XML 문서를 스크래핑하는 과정을 배우겠다.
* BeautifulSoup 모듈은 일종의 래퍼로, 기존 파싱 기능이 있는 다른 라이브러리를 쉽게 사용할 수 있도록 한다. 전통적인 파이썬 XML 파서에는 lxml과 html5lib 등이 있으며, BeautifulSoup 모듈을 이를 차용하여 데이터를 쉽고 빠르게 처리한다.

* 파서의 성능 비교

|               파서               | 속도(파이썬 2.7) | 성공률(파이썬 2.7) |
| :------------------------------: | :--------------: | :----------------: |
|  BeautifulSoup 3.2(SGMLParser)   |       221        |        100         |
|    html5lib(BS3 treebuilber)     |       253        |         99         |
|     BeautifulSoup 4.0 + lxml     |       255        |        100         |
|    html5lib(lxml treebuilber)    |       270        |         99         |
|   BeautifulSoup 4.0 + html5lib   |       271        |         98         |
| BeautifulSoup 4.0 + HTRMLParser  |       299        |         59         |
| html5lib(simpletree treebuilber) |       332        |        100         |
|            HTMLParser            |       5194       |         58         |
|               lxml               |      179252      |        100         |



## 2. BeautifulSoup 모듈 설치

```cmd
conda create -n python_mooc python=3.6
conda create lxml
conda install -c anaconda beautifulsoup4=4.5.1
```

```python
from bs4 import BeautifulSoup
```



## 3. BeautifulSoup 모듈 사용법



* BeautifulSoup 모듈의 주요 코드

|   목적    |                  코드                   |                             설명                             |
| :-------: | :-------------------------------------: | :----------------------------------------------------------: |
| 객체 생성 | soup = BeautifulSoup(books_xml, 'lxml') | xml 문서를 분석하는 새로운 객체를 생성, books_xml은 문자열형, lxml은 파서의 이름 |
| 태그 검색 |         soup.find_all('author')         | 필요한 태그를 검색하여 여러개를 반환하는 함수, 여기서는 'author' 라는 이름의 태그를 검색하여 반환 |



* 소스 파일에서 'books.xml' 파일을 가져와서 코드를 실행해보자

```python
from bs4 import BeautifulSoup

with open("books.xml", "r", encoding="utf8") as books_file:
    books_xml = books_file.read()               # 파일을 문자열로 읽어 오기

soup = BeautifulSoup(books_xml, "lxml")         # lxml 파서를 사용해 데이터 분석

# author가 들어간 모든 요소의 값 추출
for book_info in soup.find_all("author"):
    print(book_info)
    print(book_info.get_text())                 # 해당 요소에서 값 추출

```

``` text
<author>Carson</author>
Carson
<author>Sungchul</author>
Sungchul
```



## 4. USPTO XML 데이터



* 미국 특허청 틍허 데이터를 이용하여 필요한 정보를 가져와보자

```python
import urllib.request
from bs4 import BeautifulSoup

with open("US08621662-20140107.XML", "r", encoding="utf8") as patent_xml:
    xml = patent_xml.read()             # 파일을 문자열로 읽어 오기

soup = BeautifulSoup(xml,"lxml")        # lxml 파서 호출

# invention-title 태그 찾기
invention_title_tag = soup.find("invention-title")
print(invention_title_tag.get_text())

# Adjustable shoulder device for hard upper torso suit
 
```



* US08621662-20140107.XML 파일의 구조는 다음과 같이 되있다.

```xml
<publication-reference> # 특허 관련 정보
	<document-id>
	<country>US</country>
	<doc-number>08621662</doc-number> # 등록 번호
	<kind>B2</kind> # 상태
	<date>20140107</date> # 등록일자
	</document-id>
</publication-reference>
<application-reference appl-type="utility"> # 출원 관련 정보
	<document-id>
	<country>US</country>
	<doc-number>13175987</doc-number> # 출원 번호
	<date>20110705</date> # 출원일
	</document-id>
</application-reference>
```



* 하위 태그 정보를 접근하기위해 다음과 같은 코드로 접근해보자

```python
publication_reference_tag = soup.find('publication-reference')
p_document_id_tag = publication_reference_tag.find('document-id')
p_country = p_document_id_tag.find('country').get_text()
p_doc_number = p_document_id_tag.find('doc-number').get_text()
p_kind = p_document_id_tag.find('kind').get_text()
p_date = p_document_id_tag.find('date').get_text()

application_reference_tag = soup.find('application-reference')
a_document_id_tag = application_reference_tag.find('document-id')
a_country = a_document_id_tag.find('country').get_text()
a_doc_number = a_document_id_tag.find('doc-number').get_text()
a_date = a_document_id_tag.find('date').get_text()
```

