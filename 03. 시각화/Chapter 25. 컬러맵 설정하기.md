# Chapter 25. 컬러맵 설정하기

![25-1](image/25/25-1.png)

아래의 함수들을 사용해서 그래프의 컬러맵을 설정하는 방식에 대해 소개합니다.

**autumn(), bone(), cool(), copper(), flag(), gray(), hot(), hsv(), inferno(), jet(), magma(), nipy_spectral(),**

**pink(), plasma(), prism(), spring(), summer(), viridis(), winter().**



## 01. 기본 사용

![25-2](image/25/25-2.png)

### 예제

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
arr = np.random.standard_normal((8, 100))

plt.subplot(2, 2, 1)
# plt.scatter(arr[0], arr[1], c=arr[1], cmap='spring')
plt.scatter(arr[0], arr[1], c=arr[1])
plt.spring()
plt.title('spring')

plt.subplot(2, 2, 2)
plt.scatter(arr[2], arr[3], c=arr[3])
plt.summer()
plt.title('summer')

plt.subplot(2, 2, 3)
plt.scatter(arr[4], arr[5], c=arr[5])
plt.autumn()
plt.title('autumn')

plt.subplot(2, 2, 4)
plt.scatter(arr[6], arr[7], c=arr[7])
plt.winter()
plt.title('winter')

plt.tight_layout()
plt.show()
```

**subplot()** 함수를 이용해서 네 영역에 각각의 그래프를 나타내고,

**spring(), summer(), autumn(), winter()** 함수를 이용해서 컬러맵을 다르게 설정했습니다.

![25-3](image/25/25-3.png)



## 02. 컬러바 나타내기

![25-4](image/25/25-4.png)

### 예제

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
arr = np.random.standard_normal((8, 100))

plt.subplot(2, 2, 1)
plt.scatter(arr[0], arr[1], c=arr[1])
plt.viridis()
plt.title('viridis')
plt.colorbar()

plt.subplot(2, 2, 2)
plt.scatter(arr[2], arr[3], c=arr[3])
plt.plasma()
plt.title('plasma')
plt.colorbar()

plt.subplot(2, 2, 3)
plt.scatter(arr[4], arr[5], c=arr[5])
plt.jet()
plt.title('jet')
plt.colorbar()

plt.subplot(2, 2, 4)
plt.scatter(arr[6], arr[7], c=arr[7])
plt.nipy_spectral()
plt.title('nipy_spectral')
plt.colorbar()

plt.tight_layout()
plt.show()
```

**colorbar()** 함수를 사용하면 그래프 영역에 컬러바를 포함할 수 있습니다.

![25-5](image/25/25-5.png)



## 03. 컬러맵 종류

![25-6](image/25/25-6.png)

### 예제

```python
import matplotlib.pyplot as plt
from matplotlib import cm

cmaps = plt.colormaps()
for cm in cmaps:
    print(cm)
```

pyplot 모듈의 **colormaps()** 함수를 사용해서 Matplotlib에서 사용할 수 있는 모든 컬러맵의 이름을 얻을 수 있습니다.

예를 들어, **winter**와 **winter_r**은 순서가 앞뒤로 뒤집어진 컬러맵입니다.



## 04. 컬러맵 예시

아래 그림은 각 컬러맵의 예시를 나타냅니다.

![25-7](image/25/25-7.png)