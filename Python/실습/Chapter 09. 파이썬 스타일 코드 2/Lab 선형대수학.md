# Lab: 선형대수학



* 파이썬 스타일 코드로 만들 수 있는 대표적인 분야가 선형대수학이다. 간단히 구현해보자



## 1. 벡터



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



## 2. 행렬



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
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a,matrix_b)]

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

