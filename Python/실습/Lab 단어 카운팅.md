# Lab: 단어 카운팅



## 1.  실습내용



문자열의 여러 기능을 사용하여 단어 카운팅 프로그램을 만들어 보자



## 2. 실행결과



```python
# Number od a Word 'Yesterday' 9
```



## 3. 문제해결



```python
f = open('yesterday.txt', 'r')
yesterday_lyric = f.readlines()
f.close()

contents = ''
for line in yesterday_lyric:
    cotents = contents + line.strip() + '\n'
    
n_of_yesterday = contents.upper().count('YESTERDAY')
print('Number od a Word 'Yesterday', n_of_yesterday)
```

