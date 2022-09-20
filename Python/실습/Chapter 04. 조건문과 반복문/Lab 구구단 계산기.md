# Lab: 구구단 계산기



## 1. 실습내용



반복문을 이용하여 구구단 계산기를 만들어보자

* 프로그램이 시작되면 '구구단 몇 단을 계산할까' 가 출력된다.
* 사용자는 계산하고 싶은 구구단 숫자를 입력한다.
* 프로그램은 '구구단 n단을 계산한다' 라는 메세지와 함께 구구단의 결과를 출력한다.



## 2. 실행결과

```text
구구단 몇 단을 계산할까?
5
5 x 1 = 5
...
5 x 9 =45
```



## 3. 문제해결

```python
print('구구단 몇 단을 계산할까?')
user_input = input()
print('구구단', user_input, '단을 계산한다')
int_input = int(user_input)
for i in range(1, 10):
    result = int_input * i
    print(user_input, 'X', i, '=', result)
```

