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
[x**2 if %2 elsw x for in ex]
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





## 04. 선형대수학



* 파이썬 스타일 코드로 만들 수 있는 대표적인 분야가 선형대수학이다. 간단히 구현해보자



### 4.1 벡터

```python
# 벡터 표현

vector_a = [1,2,10] # 리스트로 표현
vector_b = (1,2,10) # 튜플로 표현
vector_c = {'x':1, 'y':2, 'z':10} # 딕셔너리로 표현
```



#### 1. 벡터의 연산

![9-3](C:\Users\여름\TIL\Python\image\9-3.png)

```python
# 일반적인 방법

u = [2,2]
v = [2,3]
z = [3,5]
result = []

for i in range(len(u)):
    result.append(u[i] + v[i] + z[i])

print(result)
# [7, 10]

# 파이썬 스타일 코드

u = [2,2]
v = [2,3]
z = [3,5]

result = [sum(t) for t in zip(u,v,z)]
print(result)
# [7, 10]
```



#### 2. 별표를 사용한 함수화

```python
def vector_addition(*args):
    return [sum(t) for t in zip(*args)]

u = [2,2]
v = [2,3]
z = [3,5]
vector_addition(u,v,z)
# [7,10]

# 변수 3개를 만들지 않고 해결하는 방법
row_vectors = [[2,2],[2,3],[3,5]]
vector_addition(*row_vectors)
# [7,10]
```



#### 3. 스칼라-벡터 연산

![9-4](C:\Users\여름\TIL\Python\image\9-4.png)

```python
u = [1,2,3]
v = [4,4,4]
alpha = 2

result = [alpha * sum(t) for t in zip(u,v)]
result
# [10, 12, 14]
```



### 4.2 행렬

```python
# 행렬 표현

matrix_a = [[3,6],[4,5]] # 리스트로 표현
matrix_b = [(3,6),(4,5)] # 튜플로 표현
matrix_c = {(0,0):3, (0,1):6, (1,0):4, (1,1):5} # 딕셔너리로 표현
```



#### 1. 행렬의 연산

![9-5](C:\Users\여름\TIL\Python\image\9-5.png)

```python
matrix_a = [[3,6],[4,5]]
matrix_b = [[5,8],[6,7]]
result = [[sum(row) for row in zip(*t) for t in zip(matrix_a,matrix_b)]]

print(result)
# [[8,14],[10,14]]
```



#### 2. 행렬의 동치

```python
matrix_a = [[1,1],[1,1]]
matrix_b = [[1,1],[1,1]]
all([row[0] == value for t in zip(matrix_a,matrix_b) for row in zip(*t) for value in row])

# True
```

* all() 함수는 안에 있는 모든 값이 참일 경우 True 를 반환한다.
* any() 함수는 안에 있는 값 중 하나만 참이어도 True 를 반환한다.

```python
any([False,False,False]) # False
any([False,True,False]) # True
all([False,True,True]) # False
all([True,True,True]) # True
```



#### 3. 전치행렬

![9-6](C:\Users\여름\TIL\Python\image\9-6.png)

```python
matrix_a = [[1,2,3],[4,5,6]]
result = [[element for element in t] for t in zip(*matrix_a)]
result
#[[1,4],[2,5],[3,6]]
```



#### 4. 행렬의 곱셈

![9-7](C:\Users\여름\TIL\Python\image\9-7.png)

```python
matrix_a = [[1,1,2],[2,1,1]]
matrix_b = [[1,1],[2,1],[1,3]]
result = [[sum(a*b for a,b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
result
# [[5,8],[5,6]]
```

