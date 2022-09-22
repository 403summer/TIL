# Chapter 9. 파이썬 스타일 코드 2



## 01. 람다 함수

* 람다 함수는 함수의 이름 없이, 함수처럼 사용할 수 있는 익명의 함수를 말한다.
* 람다함수와 맵리듀스는 2.x 버젼에서 많이 사용했지만 요즘은 잘 사용하지 않는다.

```python
# 일반적인 함수

def f(x,y):
    return x+y

print(f(1,4))

# 람다 함수

f = lambda x,y:x+y
print(f(1,4))

# 람다 함수를 표현하는 다른 방식

print((lambda x,y:x+y)(1,4))
```



## 02. 맵리듀스



* 빅 데이터를 처리하기 위한 기본 알고리즘으로 많이 사용한다



### 2.1 map() 함수

* map() 함수는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용한다.

```python
ex = [1,2,3,4,5]
f = lambda x:x**2
print(list(map(f,ex)))

# [1,4,9,16,25]
```

![9-1](C:\Users\여름\TIL\Python\image\9-1.png)



#### 1. 제너레이터의 사용

* 2.x 버젼에서는 `map(f,ex)` 라고 사용하면 리스트로 반환되지만 3.x 버젼에서는 `list(map(f,ex))` 라고 해야 리스트로 반환한다. 이것은 제네레이터 개념이 강화되면서 생긴 추가 코드이다.
* 제너레이터는 시퀀스 자료형의 데이터를 처리할 때, 실행 시점의 값을 생성하여 효율적으로 메모리를 관리할 수 있다는 장점이 있다.



#### 2.리스트 컴프리헨션과의 비교

* 최근에는 람다함수나 맵리듀스를 사용하지 않는다. 굳이 두 함수를 사용하지 않더라도 리스트 컴프리헨션으로 같은 효과를 낼 수 있기 때문이다.

```python
# 리스트 컴프리헨션

ex = [1,2,3,4,5]
[x ** 2 for x in ex]
#[1,4,9,16,25]
```



#### 3. 한 개 이상의 시퀀스 자료형 데이터 처리

```python
# 맵리듀스

ex = [1,2,3,4,5]
f = lambda x,y:x+y
list(map(f,ex,ex))
# [2,4,5,6,8,10]

#리스트 컴프리헨션
[x+y for x,y in zip(ex,ex)]
# [2,4,5,6,8,10]
```



#### 4.필터링 기능

* map() 함수는 리스트 컴프리헨션처럼 필터링 기능을 사용할 수 있다. 리스트 컴프리헨션과 달리 else문을 반드시 작성해 해당 경우가 존재하지 않는 경우를 지정해 주어야 한다.

```python
# map() 함수
list(map(lambda x:x**2 if x%2 == 0 else x,ex)) 
# [1,4,3,16,5]

# 리스트 컴프리헨션
[x**2 if x%2 else x for x in ex]
# [1,4,3,16,5]
```



### 2.2 reduce() 함수

* reduce() 함수는 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수이다.

```python
# 보통의 경우

x=0
for y in [1,2,3,4,5]:
    x += y
print(x)   # 15

# reduce() 함수

from functools import reduce
print(reduce(lambda x,y:x+y,[1,2,3,4,5])) # 15
```

![9-2](C:\Users\여름\TIL\Python\image\9-2.png)



## 03. 별표의 활용



### 3.1 별표의 사용

* *는 곱하기 기호란 뜻도 있지만 컨테이너 속성을 부여하는 기능도 있다.
* 컨테이너란, 일종의 데이터를 담는 그릇이다. 여러 개의 변수를 한꺼번에 넣는 기능을 한다.
* ex) 가변 인수, 키워드 가변 인수



### 3.2 별표의 언패킹 기능

* 컨테이너 속성을 부여하는 기능 외에 한 가지 기능이 더 있다. 여러 개의 데이터를 담는 리스트, 튜플, 딕셔너리와 같은 자료형에서는 해당 데이터를 언패킹 하는 기능을 한다.

```python
# 예시 1

def asterisk_test(a,args):
    print(a, *args) # 언패킹
    print(type(args))
    
asterisk_test(1,(2,3,4,5,6))

# 1 2 3 4 5 6
# <class 'tuple'>

# 예시 1-1

def asterisk_test(a,*args): # 컨테이너
    print(a, args)
    print(type(args))
    
asterisk_test(1,*(2,3,4,5,6))

# 1 (2, 3, 4, 5, 6)
# <class 'tuple'>
```

```python
# 예시 2

a, b, c = ([1,2],[3,4],[5,6])
print(a, b, c)
# [1,2] [3,4] [5,6]

data = ([1,2],[3,4],[5,6])
print(*data)
# [1,2] [3,4] [5,6]
```

```python
# 예시 3

for data in zip(*[[1,2],[3,4],[5,6]]):
    print(data)
    print(type(data))
    
# (1,3,5)
# <class 'tuple'>
# (2,4,6)
# <class 'tuple'>
```

```python
# 예시 4

def asterisk_test(a,b,c,d):
    print(a,b,c,d)
data = {'b':1,'c':2,'d':3}
asterisk_test(10,**data)
# 10 1 2 3
```


