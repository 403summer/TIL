# Lab: 텍스트 마이닝 프로그램



## 1. 실습내용



각 문장에 있는 단어의 개수를 파악하는 프로그램



* 문장의 단어 개수를 파악하는 코드를 작성한다.
* defaultdict 모듈을 사용한다.
* 단어의 출현 횟수를 기준으로 정렬된 결과를 보여 주기 위해 OrderdDict 모듈을 사용한다.



## 2. 실행결과



```python
# and 3
# press 2
# ...
```



## 3. 문제해결



```python
text = ''' '''.lower().split()

from collections import defaultdict

word_count = defaultdict(lambda: 0) # Default 값을 0으로 설정
for word in text:
    word_count[word] += 1
    
from collections import OrderedDict
for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse = True)).items():
	print(i,v)
```

