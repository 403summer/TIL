# Chapter 08. 색상 지정하기

![8-1](image/8/8-1.png)

## 01. 포맷 문자열 사용하기

![8-2](image/8/8-2.png)

### 예제

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], 'r')
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], 'g')
plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], 'b')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
```

**plot()** 함수의 **포맷 문자열 (Format string)**을 사용해서 실선의 색상을 지정했습니다.

![8-3](image/8/8-3.png)



## 02. color 키워드 인자 사용하기

![8-4](image/8/8-4.png)

### 예제

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], color='limegreen')
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], color='violet')
plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], color='dodgerblue')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
```

**color** 키워드 인자를 사용해서 더 다양한 색상의 이름을 지정할 수 있습니다.

**plot()** 함수에 **color=’limegreen’**과 같이 입력하면, limegreen에 해당하는 색깔이 표시됩니다.

![8-5](image/8/8-5.png)



## 03. Hex code 사용하기

![8-6](image/8/8-6.png)

### 예제

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2, 3, 5, 10], color='#e35f62',
         marker='o', linestyle='--')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
```

**16진수 코드 (Hex code)**로 더욱 다양한 색상을 지정할 수 있습니다.

이번에는 **선의 색상**과 함께 **마커와 선의 종류**까지 모두 지정해 보겠습니다.

**marker**는 마커 스타일, **linestyle**는 선의 스타일을 지정합니다.

선의 색상은 Hex code **‘#e35f62’**로, 마커는 **원형 (Circle)**, 선 종류는 **대시 (Dashed)**로 지정했습니다.

![8-7](image/8/8-7.png)



## 04. matplotlib 색상들



### 4.1 Cycler 색상

색상을 지정하지 않으면 기본적으로 아래의 10개의 색상이 반복적으로 표시됩니다.

![8-8](image/8/8-8.png)



### 4.2 기본 색상

아래의 색상은 간단한 문자열을 사용해서 색상을 지정하도록 합니다.

![8-9](image/8/8-9.png)



### 4.3 Tableau 색상

Matplotlib은 Tableau의 색상들을 지원하며, 이는 Cycler의 색상과 같습니다.

![8-10](image/8/8-10.png)



### 4.4 CSS 색상

아래와 같이 색상의 이름을 사용해서 색상을 지정할 수 있습니다.

![8-11](image/8/8-11.png)