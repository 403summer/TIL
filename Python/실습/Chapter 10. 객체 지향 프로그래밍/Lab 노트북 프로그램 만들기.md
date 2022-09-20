# Lab: 노트북 프로그램 만들기



## 1. 실습내용

* 노트를 정리하는 프로그램이다
* 사용자는 노트에 컨텐츠를 적을 수 있다
* 노트는 노트북에 삽입된다
* 노트북은 타이틀이 있다
* 노트북은 노트가 삽입될 때 페이지를 생성하며, 최대 300 페이지까지 저장할 수 있다
* 300페이지를 넘기면 노트를 더는 삽입하지 못한다

| 구분   | Notebook                                           | Note                          |
| ------ | -------------------------------------------------- | ----------------------------- |
| 메서드 | add_note<br />remove_note<br />get_number_of_pages | write_content<br />remove_all |
| 변수   | title<br />page_number<br />notes                  | contents                      |



## 2. 문제해결

```python
# Note 클래스

class Note(object):
    def __init__(self, contents = None):
        self.contents = contents
        
    def write_contents(self, contents):
        self.contents = contents
        
    def remove_all(self):
        self.contents = ""
        
    def __str__(self):
        return self.contents
```

```python
# Notebook 클래스

class Notebook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}
        
    def add_note(self,note, page = 0):
        if self.page_number < 300:
            if page == 0 :
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page:note}
                self.page_number += 1
            else:
                print('페이지가 모두 채워졌다.')
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print('해당 페이지는 존재하지 않는다')
    def get_number_of_pages(self):
        return len(self.notes.keys())
      
```

