# Chapter 05. 함수



## 01. 함수 기초



### 1.1 함수의 개념과 장점

* 함수는 어떤 일을 수행하는 코드의 묶음
* 함수의 장점
  * 반복 작업을 단축화할 수 있다
  * 논리적인 단위로 분할 가능
  * 코드의 캡슐화 : 만들어 둔 함수는 다른 사람이 쉽게 사용할 수 있다



### 1.2 함수



### (예시)

```python
# 함수 선언
def sum_abc (a,b,c):
    return a+b+c
```

```python
# 함수 호출
sum_abc(1,2,3)
```

```
6
```



### 1.3 매개변수와 인수

|   구분   |                             설명                             |         예시         |
| :------: | :----------------------------------------------------------: | :------------------: |
| 매개변수 | 함수의 인터페이스 정의에 있어 어떤 변수를 사용하는지를 정의하는 것 | sum_abc() 에서 a,b,c |
|   인수   |                 실제 매개변수에 대입되는 값                  | sum_abc() 에서 1,2,3 |



### 1.4 함수의 형태



### (예시)

```python
def sum_abc_1 (): # 매개변수x, 반환값x
    print('테스트')
    
def sum_abc_2 (a,b,c): # 매개변수o, 반환값x
    print(a,b,c)
    
def sum_abc_3 (): # 매개변수x, 반환값o
    return a+b+c

def sum_abc_4 (a,b,c): # 매개변수o, 반환값o
    return a+b+c

# 반환값이 없는 함수 자체는 None 값을 가진다.
```



## 02. 함수 심화



## 2.1 함수의 호출 방식

- 파이썬은 객체 호출(call by object reference)을 사용한다



### (예시)

```python
def spam(eggs):
    eggs.append(1) # 기존 객체의 주소값에 [1] 추가
    eggs = [2,3] # 새로운 객체 생성
    
ham = [0]
spam(ham)
print(ham)
```

```
[0,1]
```



### 2.2 변수의 사용 범위

|   구분    |          설명          |
| :-------: | :--------------------: |
| 지역 변수 |   함수 안에서만 사용   |
| 전역 변수 | 프로그램 전체에서 사용 |



### (예시)

```python
# 함수 안에 s는 지역 변수, 함수 밖에 s는 전역 변수
def f():
    s = 'I love London!'
    print(s)
    
s = 'I love Paris!'
f()
print(s)
```

```
I love London!
I love Paris!
```



```python
# 전역 변수를 사용려면 global을 사용한다
def f():
    global s
    s = 'I love London!'
    print(s)
    
s = 'I love Paris!'
f()
print(s)
```

```
I love London!
I love London!
```



### 2.3 재귀 함수

- 재귀 함수는 함수가 자기 자신을 다시 부르는 함수이다



### (예시)

```python
# 팩토리얼
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)    
```



## 03. 함수의 인수

|      종류       |                             내용                             |
| :-------------: | :----------------------------------------------------------: |
|   키워드 인수   | 함수의 인터페이스에 지정된 변수명을 사용하여 함수의 인수를 지정하는 방법 |
|   디폴트 인수   | 별도의 인수값이 입력되지 않을 때, 인터페이스 선언에서 지정한 초깃값을 사용하는 방법 |
|    가변인수     | 함수의 인터페이스에 지정된 변수 이외의 추가 변수를 함수에 입력할 수 있게 지원하는 방법 |
| 키워드 가변인수 |      매개변수의 이름을 따로 지정하지 않고 입력하는 방법      |



### (예시1)

- 키워드 인수

```python
def print_something(name, age, city):
	print(name, age, city)

# 변수의 입력 순서를 알아야한다.
print_something('summer', 4, 'busan' )

# 키워드 인수를 사용하면 순서를 알아야 할 필요가 없다. 
print_something(city = 'busan', age = 4, name = 'summer') 
```

```
'summer' 4 'busan'
```



### (예시2)

- 디폴트 인수

```python
def print_something(name, age = '4', city = 'busan'): 
	print(name, age, city)

# age = '4', city = 'busan' 디폴트값    
print_something('summer')    
```

```
'summer' 4 'busan'
```



### (예시3)

- 가변인수
- 코드를 작성할 때, 가끔 함수의 매개변수 개수가 정해지지 않고 진행해야하는 경우가 있다. 이때 사용하는 것이 가변 인수이다
- 가변 인수* 는 반드시 일반적인 키워드 인수가 모두 끝난 후 넣어야 한다.  리스트와 비슷한 튜플 형태로 함수 안에서 사용할 수 있으므로 인덱스를 사용하여, 즉 args[0], args[1] 등으로 변수에 접근할 수 있다.

```python
def asterisk_test(a, b, *args):
    print(a, b)
    print(args)
    
asterisk_test(1,2,3,4,5)
```

```
1, 2
(3,4,5)
```



### (예시4)

- 키워드 가변인수

* 가변인수에 키워드를 지정하는 방법이다. ** 를 사용하여 함수의 매개변수를 표시한다. 그리고 입력된 값은 딕셔너리 자료형으로 사용할 수 있다

```python
def kwargs_test(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)
    
kwargs_test(1,2,3,4,5, name = 'summer', age = 4)
```

```
1 2
(3,4,5)
{'name': 'summer', 'age':4}
```

