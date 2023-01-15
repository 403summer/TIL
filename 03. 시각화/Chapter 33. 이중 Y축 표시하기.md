# Chapter 33. 이중 Y축 표시하기

![33-1](image/33/33-1.png)

두 종류의 데이터를 동시에 하나의 그래프에 표시하기 위해 **이중 축**을 표시할 수 있습니다.

이 페이지에서는 Matplotlib 그래프에 두 개의 축을 동시에 표시하는 방법에 대해 소개합니다.



## 01. 기본 사용

![33-2](image/33/33-2.png)

### 예제

```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = 12

x = np.arange(0, 3)
y1 = x + 1
y2 = -x - 1

fig, ax1 = plt.subplots()
ax1.plot(x, y1, color='green')

ax2 = ax1.twinx()
ax2.plot(x, y2, color='deeppink')

plt.show()
```

**ax1.plot(x, y1, color=’green’)**은 첫번째 축에 (x, y1) 데이터를 나타냅니다.

**ax1.twinx()**는 ax1과 x축을 공유하는 새로운 Axes 객체를 만듭니다.

**ax2.plot(x, y2)**는 새로운 Axes 객체에 (x, y2) 데이터를 나타냅니다.

결과는 아래와 같습니다.

![33-3](image/33/33-3.png)



## 02. 축 레이블 표시하기

![33-4](image/33/33-4.png)

### 예제

```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = 12

x = np.arange(0, 3)
y1 = x + 1
y2 = -x - 1

fig, ax1 = plt.subplots()
ax1.set_xlabel('X-Axis')
ax1.set_ylabel('1st Y-Axis')
ax1.plot(x, y1, color='green')

ax2 = ax1.twinx()
ax2.set_ylabel('2nd Y-Axis')
ax2.plot(x, y2, color='deeppink')

plt.show()
```

**set_xlabel()**, **set_ylabel()** 메서드는 각 축에 대한 레이블을 표시하도록 합니다.

([Matplotlib 축 레이블 설정하기](https://wikidocs.net/92081) 페이지를 참고하세요.)

결과는 아래와 같습니다.

![33-5](image/33/33-5.png)



## 03. 범례 표시하기 1

![33-6](image/33/33-6.png)

### 예제

```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = 14

x = np.arange(0, 3)
y1 = x + 1
y2 = -x - 1

fig, ax1 = plt.subplots()
ax1.set_xlabel('X-Axis')
ax1.set_ylabel('1st Y-Axis')
ax1.plot(x, y1, color='green', label='1st Data')
ax1.legend(loc='upper right')

ax2 = ax1.twinx()
ax2.set_ylabel('2nd Y-Axis')
ax2.plot(x, y2, color='deeppink', label='2nd Data')
ax2.legend(loc='lower right')

plt.show()
```

각 축의 데이터 곡선에 대한 범례를 나타내기 위해 **legend()** 메서드를 사용합니다.

([Matplotlib 범례 표시하기](https://wikidocs.net/137778) 페이지를 참고하세요.)

결과는 아래와 같습니다.

![33-7](image/33/33-7.png)



## 04. 범례 표시하기 2

![33-8](image/33/33-8.png)

### 예제

```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = 14

x = np.arange(0, 3)
y1 = x + 1
y2 = -x - 1

fig, ax1 = plt.subplots()
ax1.set_xlabel('X-Axis')
ax1.set_ylabel('1st Y-Axis')
line1 = ax1.plot(x, y1, color='green', label='1st Data')

ax2 = ax1.twinx()
ax2.set_ylabel('2nd Y-Axis')
line2 = ax2.plot(x, y2, color='deeppink', label='2nd Data')

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right')
plt.show()
```

두 축에 대한 범례를 하나의 텍스트 상자에 표시하기 위해서는 위의 예제와 같이

두 곡선을 먼저 합친 후 **legend()** 메서드를 사용하세요.

결과는 아래와 같습니다.

![33-9](image/33/33-9.png)

