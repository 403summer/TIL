# Chapter 16. 막대 그래프 그리기

![16-1](image/16/16-1.png)

**막대 그래프 (Bar graph, Bar chart)**는 범주가 있는 데이터 값을 직사각형의 막대로 표현하는 그래프입니다.



## 01. 기본 사용

![16-2](image/16/16-2.png)

### 예제

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.bar(x, values)
plt.xticks(x, years)

plt.show()
```

이 예제는 연도별로 변화하는 값을 갖는 데이터를 막대 그래프로 나타냅니다.

NumPy의 **np.arange()** 함수는 주어진 범위와 간격에 따라 균일한 값을 갖는 어레이를 반환합니다.

**years**는 X축에 표시될 연도이고, **values**는 막대 그래프의 y 값 입니다.

먼저 **plt.bar()** 함수에 x 값 [0, 1, 2]와 y 값 [100, 400, 900]를 입력해주고,

**xticks()**에 **x**와 **years**를 입력해주면, X축의 눈금 레이블에 ‘2018’, ‘2019’, ‘2020’이 순서대로 표시됩니다.

![16-3](image/16/16-3.png)



## 02. 색상 지정하기

![16-4](image/16/16-4.png)

### 예제1

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.bar(x, values, color='y')
# plt.bar(x, values, color='dodgerblue')
# plt.bar(x, values, color='C2')
# plt.bar(x, values, color='#e35f62')
plt.xticks(x, years)

plt.show()
```

**plt.bar()** 함수의 **color** 파라미터를 사용해서 막대의 색상을 지정할 수 있습니다.

예제에서는 네 가지의 색상을 사용했습니다.

Matplotlib의 다양한 색상에 대해서는 [Matplotlib 색상 지정하기](https://wikidocs.net/92085) 페이지를 참고하세요.

![16-5](image/16/16-5.png)



### 예제2

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]
colors = ['y', 'dodgerblue', 'C2']

plt.bar(x, values, color=colors)
plt.xticks(x, years)

plt.show()
```

**plt.bar()** 함수의 **color** 파라미터에 색상의 이름을 리스트의 형태로 입력하면,

막대의 색상을 각각 다르게 지정할 수 있습니다.

![16-6](image/16/16-6.png)



## 03. 막대 폭 지정하기

![16-7](image/16/16-7.png)

### 예제

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.bar(x, values, width=0.4)
# plt.bar(x, values, width=0.6)
# plt.bar(x, values, width=0.8)
# plt.bar(x, values, width=1.0)
plt.xticks(x, years)

plt.show()
```

**plt.bar()** 함수의 **width** 파라미터는 막대의 폭을 지정합니다.

예제에서는 막대의 폭을 0.4/0.6/0.8/1.0으로 지정했고, 디폴트는 0.8입니다.

![16-8](image/16/16-8.png)



## 04. 스타일 꾸미기

![16-9](image/16/16-9.png)

### 예제

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.bar(x, values, align='edge', edgecolor='lightgray',
        linewidth=5, tick_label=years)

plt.show()
```

이번에는 막대 그래프의 테두리의 색, 두께 등 스타일을 적용해 보겠습니다.

**align**은 눈금과 막대의 위치를 조절합니다. 디폴트 값은 ‘center’이며, ‘edge’로 설정하면 막대의 왼쪽 끝에 눈금이 표시됩니다.

**edgecolor**는 막대 테두리 색, **linewidth**는 테두리의 두께를 지정합니다.

**tick_label**을 리스트 또는 어레이 형태로 지정하면, 틱에 문자열을 순서대로 나타낼 수 있습니다.

![16-10](image/16/16-10.png)