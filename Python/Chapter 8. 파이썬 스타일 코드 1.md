# Chapter 8. 파이썬 스타일 코드 1



## 01. 문자열의 분리 및 결합



### 1.1 문자열의 분리: split() 함수

```python
# 빈칸 기준으로 분리
items = 'zero one two three'.split()
print(itmes) #['zero', 'one', 'two', 'three']

# 매개변수 기준으로 분리
items = 'zero,one,two,three'.split(',')
print(itmes) #['zero', 'one', 'two', 'three']

# 언패킹
items = 'zero,one,two,three'
a,b,c,d  = items.split(',')
print(a) # 'zero'
```



### 1.2 문자열의 결합: join() 함수

```python
# 문자열 합치기
items = ['zero', 'one', 'two', 'three']
result = ''.join(items)
print(result) # 'zeroonetwothree'

# 특정 문자열로 합치기
items = ['zero', 'one', 'two', 'three']
result = '-'.join(items)
print(result) # 'zero-one-two-three'
```



## 02. 리스트 컴프리헨션



### 2.1 리스트 컴프리헨션

* 코드가 간결해진다.
* 반복문을 통한 리스트를 만드는 것보다 효율적인 연산을 수행한다.

```python
# 일반적인 반복문 + 리스트
result = []
for i in range(10):
    result.append(i)
    
print(result) # [0,1,2,3,4,5,6,7,8,9]

# 리스트 컴프리헨션
result = [i for i in range(10)]
print(result) # [0,1,2,3,4,5,6,7,8,9]
```



### 2.2 리스트 컴프리헨션 용법



####  1. 필터링

```python
# 일반적인 반복문 + 리스트
result = []
for i in range(10):
    if i%2 == 0:
        result.append(i)
print(result) # [0, 2, 4, 6, 8]

# 리스트 컴프리헨션
result = [i for i in range(10) if i%2==0]
print(result) # [0, 2, 4, 6, 8]
```

```python
# else 문 추가
result = [i if i%2 == 0 else 10 for i in range(10)]
print(result) # [0,10,2,10,4,10,6,10,8,10]
```



#### 2. 중첩 반복문

```python
word_1 = 'Hello'
word_2 = 'World'
result = [i + j for i in word_1 for j in word_2]
print(result)
# ['HW', 'Ho', 'Hr', 'Hl', 'Hd', 'eW', 'eo', 'er', 'el', 'ed', 'lW', 'lo', 'lr', 'll', 'ld', 'lW', 'lo', 'lr', 'll', 'ld', 'oW', 'oo', 'or', 'ol', 'od']
```

```python
case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
result = [i + j for i in case_1 for j in case_2 if not(i==j)]
print(result)
# ['AD', 'AE', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']
```



####  3. 이차원 리스트

 ```python
words = 'The Quick brown fox humps over the lazy dog'.split()
print(words)
# ['The', 'Quick', 'brown', 'fox', 'humps', 'over', 'the', 'lazy', 'dog']
stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for i in stuff:
    print(i)
    
# ['THE', 'the', 3]
# ['QUICK', 'quick', 5]
# ['BROWN', 'brown', 5]
# ['FOX', 'fox', 3]
# ['HUMPS', 'humps', 5]
# ['OVER', 'over', 4]
# ['THE', 'the', 3]
# ['LAZY', 'lazy', 4]
# ['DOG', 'dog', 3]    
 ```

```python
# 1
case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
result = [i + j for i in case_1 for j in case_2]
print(result)
# ['AD', 'AE', 'AA', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']

# 2
result = [[i + j for i in case_1] for j in case_2]
print(result)
# [['AD', 'BD', 'CD'], ['AE', 'BE', 'CE'], ['AA', 'BA', 'CA']]
```



## 03. 다양한 방식의 리스트값 출력



### 3.1 리스트 값에 인덱스를 붙여 출력: enumerate() 함수

```python
for i,j in enumerate(['A','B','C']):
    print(i, j)
    
# 0 A
# 1 B
# 2 C  
```

```python
{i:j for i,j in enumerate('나는 낭만 고양이'.split())}
# {0: '나는', 1: '낭만', 2: '고양이'}
```





### 3.2 리스트값을 병렬로 묶어 출력: zip() 함수

```python
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a,b in zip(alist,blist):
	print(a, b)
# a1 b1
# a2 b2
# a3 b3    
```

```python
a, b, c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c,)
# (1, 10, 100) (2, 20, 200) (3, 30, 300)

[sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
# [111, 222, 333]
```



