# Chapter 03. 2차원 데이터 정리

2장에서는 영어 시험 점수를 사용하여 학생 1명에게 점수 하나가 대응되는 1차원 데이터를 정리하는 방법에 대해 배웠습니다. 정리 방법으로는 평균과 분산이라는 지표, 히스토그램과 상자그림이라는 그래프를 사용했습니다. 이 장에서는 영어 시험 점수와 수학 시험 점수를 사용하여, 학생 1명에게 두 과목의 점수가 대응되는 2차원 데이터의 정리 방법을 설명합니다. 2차원 데이터로 정리하면 '수학 점수가 높은 학생이 영어 점수도 높은가'와 같은 데이터의 상관성을 파악할 수 있습니다.

2차원 데이터를 정리하는 방법 역시 수치를 사용한 지표로 정리하는 방법과 그림으로 정리하는 방법으로 나눕니다. 우선 3.1 절에서 2차원 데이터에 이용되는 공분산과 상관계수라는 수치에 대한 지표를 살펴보고, 3.2절에서는 2차원 데이터를 시각화하는 방법인 산점도와 회귀직선에 관해서 학습합니다.

이 주제로 들어가기 전에 라이브러리와 데이터를 준비해둡시다.

```python
import numpy as np
import pandas as pd

%precision 3
pd.set_option('precision', 3)
np.set_printoptions(precision=3)
```



이 장에서도 2장과 마찬가지로 ch2_scores_em.csv를 사용합니다. 2장에서는 영어 점수에 대한 데이터만 사용했으나 이 장에서는 영어 점수와 수학 점수에 대한 데이터를 둘다 사용합니다.

```python
df = pd.read_csv('ch2_scores_em.csv', index_col = 'student number')
```



3.1절에서는 df의 처음 10명에 해당하는 데이터를 사용합니다. 2장과 마찬가지로 NumPy의 array와 Pandas의 DataFrame을 둘 다 준비하여, DataFrame에는 각 학생에게 A, B, ... 라는 이름을 부여합니다.

```python
en_scores = np.array(df['english'])[:10]
ma_scores = np.array(df['mathematics'])[:10]

scores_df = pd.DataFrame({'english':en_scores, 'mathematics':ma_scores},
                        index = pd.Index(['A', 'B', 'C', 'D', 'E', "F", 'G', 'H', 'I', 'J'], name = 'student'))
scores_df
```

<img src="image/3/3-1.png" alt="3-2" style="zoom:80%;" />



## 01. 두 데이터 사이의 관계를 나타내는 지표

영어 점수가 높은 학생일수록 수학 점수도 높은 경향이 있다면, 영어 점수와 수학 점수는 **양의 상관관계**에 있다고 합니다. 거꾸로 영어 점수가 높은 학생일수록 수학 점수가 낮은 경향이 있다면, 영어 점수와 수학 점수는 **음의 상관관계**에 있다고 합니다. 또한 그 어느 쪽에도 해당하지 않고 영어 점수가 수학 점수에 직접적으로 영향을 미치지 않을 때,  영어 점수와 수학 점수는 **무상관**이라고 합니다. 이와 같은 상관을 구치에 대한 지표로 표현하는 것이 이 절의 목표입니다.


### 1.1 공분산

우선 영어와 수학점수가 어떻게 분포되어 있는지 살펴봅시다. 다음 그림을 통해 각 학생의 수학 시험 점수(mathematics score)와 영어 시험 점수(english score)를 알 수 잇습니다. A 학생은 영어가 42점이고 수학이 65점입니다. 또한 가운데의 가로선과 세로선은 각각 수학과 영어의 평균 점수를 나타내고 있습니다. 이 그림을 살펴보면, 영어  점수가 높은 학생일수록 수학 점수도 높은 선형 관계성이 있는 것 같습니다. 결국 영어 점수와 수학 점수는 양의 상관관계에 있다고 말할 수 있습니다. 

<img src="image/3/3-2.png" alt="3-3" style="zoom:80%;" />

이처럼 양의 상관관계에 있다고 생각되는 데이터의 관계성을 어떻게 수치화하면 좋을까요?  여기에는 **공분산**(covariance)라는 지표를 사용합니다. 공분산은 분산에 가까운 지표입니다.

공분산을 쉽게 이해하려면 분산의 경우와 마찬가지로 면적을 생각하면 됩니다. 다음 그림은은 위의 그림의 C, E, H 학생에 대해서 각 점수와 평균 점수로 직사각형을에 그린 것입니다. 여기서 직사각형의 가로 길이는 영어 점수의 편차, 세로 길이는수학 점수의 편차입니다.

![3-3](image/3/3-3.png)

공분산이 분산과 다른 점은, 가로축과 세로축의 데이터가 다르기 때문에 편차들로 만든 도형이 직사각형이 될 뿐만 아니라 음의 면적도 얻을 수 있다는 점입니다. 분산은 가령 편차가 음의 값이 되어도 면적은 제곱값이므로 항상 양의 값이 됩니다. 그러나 공분산에서는 가로와 세로의 데이터가 다르므로 한쪽은 편차가 양의 값이고 다른 한쪽은 편차가 음의 값인 경우에 면적이 음의 값이 되어버립니다. 이번 데이터에서 E 학생은 면적이 양의 값이지만, C 학생은 면적이 음의 값으로 되어 있습니다.

이처럼 '부호를 붙인 면적'이라는 관점에서 위에 그림을 살펴보면, 면적이 양의 값이 되는 것은 영어 점수와 수학 점수가 모두 평균 점수보다 높거나 모두 평균 점수보다 낮은 경우이기 때문에, 점수의 상관관계를 잘 나타낸다고 볼 수 있습니다. 따라서 부호를 붙인 면적의 평균은 상관의 지표가 됩니다. 이것이 공분산입니다.

공분산이 양의 값이면 면적이 양의 값이 되는 데이터가 많다는 뜻이므로 양의 상관관계에 있고, 반대로 공분산이 음의 값이면 면적이 음의 값이 되는 데이터가 많다는 뜻이므로 음의 상관관계에 있다고 할 수 있다고 할 수 있습니다. 그 어느 쪽도 아니고 공분산이 0에 가까우면 무상관을 나타냅니다.

DataFrame으로 정리하면서 공분산을 계산해봅시다. 

```python
summary_df = scores_df.copy()
summary_df['english_deviation'] = \
    summary_df['english'] - summary_df['english'].mean()
summary_df['mathematics_deviation'] = \
    summary_df['mathematics'] - summary_df['mathematics'].mean()
summary_df['product of deviations'] = \
    summary_df['english_deviation'] * summary_df['mathematics_deviation']
summary_df
```

<img src="image/3/3-4.png" alt="3-5" style="zoom:80%;" />

```python
summary_df['product of deviations'].mean()
```

```
62.800
```

영어 점수와 수학 점수는 양의 상관고나계에 있다고 할 수 있습니

다.

수식으로 정리해봅시다. 공분산은 흔히 S~xy~로 표기합니다. 이것은 변수 x와 변수 y의 공분산임을 나타냅니다. 여기는 변수 x는 영어, 변수 y는 수학에 대응됩니다. 또한 공분산은 변수 x와 변수 y를 서로 바꾸어도 값이 변하지 않습니다. 

<img src="image/3/3-5.png" alt="3-6" style="zoom:80%;" />

NumPy의 경우, 공분산은 cov 함수로 구할 수 있습니다. 다만 반환값은 공분산값이 아닌 **공분산 행렬**(covariance matrix) 또는 **분산공분산 행렬**(variance-covariance matrix)이라고 부르는 행렬입니다.

```python
cov_mat = np.cov(en_scores, ma_scores, ddof = 0)
cov_mat
```

```python
array([[86.  , 62.8 ],
       [62.8 , 68.44]])
```

이 행렬의 첫번째 행과 첫번째과 첫번째 열이 첫번째 인수인 영어, 두번째 행과 두번째 열이 두번째 인수인 수학에 각각 대응하고, 이것들을 교차하여 1행 2열의 성분과 2행 1열의 성분이 영어와 수학의 공분산에 해당합니다. 파이썬의 인덱스는 0으로 시작하므로, 결국 cov_mat의  [0, 1] 성분과 [1, 0] 성분이 공분산이 됩니다.

```python
cov_mat[0, 1], cov_mat[1, 0]
```

```python
(62.800, 62.800)
```



나머지 성분은 무엇인가요?  [0, 0] 성분은 영어와 영어의 공분산이 됩니다. 수식으로 살펴보면 쉽게 이해할 수 있는데, 동일한 변수들의 공분산은 해당 변수의 분산과 같습니다. 결국 [0. 0] [1, 1] 성분은 수학의 분산이 된다.

```python
cov_mat[0, 0], cov_mat[1, 1]
```

```python
(86.0, 68.44000000000001)
```



영어와 수학의 분산도 계산해봅시다.

```python
np.var(en_scores, ddof = 0), np.var(ma_scores, ddof = 0)
```

```
(86.0, 68.440)
```



분산과 일치함을 확인할 수 있습니다.

DataFrame에도 cov 메서드가 있지만 var 메서드와 달리 ddof 인수를 취하지 않고 불편분산만 계산할 수 있으므로 여기선 실행하지 않습니다.



### 1.2 상관계수

앞에서 공분산을 계산하여 데이터의 상관관계를 표현습니다. 이번과 같은 시험 점수들 간에 공분산은 (점수x점수)라는 단위를 사용합니다. 학생의 키와 시험 점수의 상관관계를 살펴본다면, 공분산은  (cm x 점수)라는 단위가 됩니다. 분산의 경우와 마찬가지로 이런 단위는 직감적으로 이해하기 어렵습니다.

따라서 단위에 의존하지 않는 상관을 나타내는 지표가 필요합니다. 공분산은 각 데이터의 단위를 곱한것이므로, 공분산을 각 데이터의 표준편차로 나누어 단위에 의존하지 않는 지표를 정의할 수 있습니다.

<img src="image/3/3-6.png" alt="3-7" style="zoom:80%;" />

이와 같이 정의된 지표 r~xy~ 를 **상관계수**(correlation coefficient)라고 합니다. 상관계수는 반드시 -1과 1사이의 값을 취하고, 데이터가 양의 상관관계에 놓여 있을수록 1에 가까워지고, 음의 상관관계에 놓여 있을수록 -1에 가깝워집니다. 무상관이면 0이 됩니다. 또한 상관계수가 -1일 때와 1일 때에는 데이터가 완전히 직선상에 놓입니다. 다음 그림은 몇가지 상관계수에 대응하는 산점도입니다.

<img src="image/3/3-7.png" alt="3-8" style="zoom:80%;" />



그러면 영어 점수와 수학 점수의 상관계수를 구해봅시다. 수식대로 계산하면 다음과 같습니다.

```python
np.cov(en_scores, ma_scores, ddof = 0)[0, 1]/(np.std(en_scores) * np.std(ma_scores))
```

```
0.819
```

상관계수는 0.819로 1에 가까운 값입니다. '상관계수가 어느 정도이면 상관이 있다.'라는 명확한 기준은 없지만, 위에 그림을 보면 알 수 있듯이 상관계수가 0.8인 데이터는 강한 상관을 가지고 있습니다. 이로부터 이로부터 영어 점수와 수학 점수에는 강한 양의 상관이 있음을 알 수 있습니다.

NumPy의 경우, 상관계수는 corrcoef 함수로 계산할 수 있습니다. 다만, 반환값은 공분산의 경우와 마찬가지로 **상관행렬**(correlation matrix)이라고 부르는 행렬입니다.

```python
np.corrcoef(en_scores, ma_scores)
```

```
array([[1.   , 0.819],
       [0.819, 1.   ]])
```

상관행렬의 [0, 1] 성분과 [1, 0] 성분이 영어와 수학의 상관계수에 대응하고 있습니다. 나머지 [0, 0] 성분은 영어와 영어의 상관계수, [1, 1] 성분은 수학과 수학의 상관계수에 대응하므로 1입니다.

DataFrame의 경우, corr 메서드와 동일한 결과를 얻을 수 있습니다.

```python
scores_df.corr()
```

<img src="image/3/3-8.png" alt="3-9" style="zoom:80%;" />



## 02. 2차원 데이터 시각화

이 절에서는 2차원 데이터를 시각화하는 방법에 대해 살펴봅니다. 이제까지 학습하였듯이 2차원 데이터를 그릴 때는 산점도가 매우 편리합니다. 여기서는 산점도와 함께 데이터의 관계를 표현하는 직선인 회귀직선과 히스토그램의 2차원 버전인 히트맵에 관해서 설명합니다.

matplotlib을 준비해둡시다.

```python
import matplotlib.pyplot as plt

%matplotlib inline
```



### 2.1 산점도

matplotlib에서는 scatter 메서드를 사용하여 산점도를  그릴 수 있습니다. scatter의 첫번째 인수가 x축의 데이터, 두번째 인수가 y축의 데이터입니다.

```python
english_scores = np.array(df['english'])
math_scores = np.array(df['mathematics'])

fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(111)
# 산점도
ax.scatter(english_scores, math_scores)
ax.set_xlabel('english')
ax.set_ylabel('mathematics')

plt.show()
```

<img src="image/3/3-9.png" alt="3-10" style="zoom:80%;" />

산점도를 통해 영어 점수가 높은 사람일수록 수학 점수도 높은 경향이 있다는 것을 알 수 있습니다.



### 2.2 회귀직선

**회귀직선**(regression line)은 두 데이터 사이의 관계를 더욱 잘 나타내는 직선입니다. Matplotlib에는 회귀직선을 직접 그리는 메서드가 없기 때문에 여기서는 NumPy를 사용해서 회귀직선을 구합니다. 간단히 설명하면, np.polyfit 함수와 np.poly1d 함수를 사용하여 영어 점수를 x, 수학 점수를 y로 했을 때 회귀직선 y = β~0~ + β~1~x를 구할 수 있습니다. 회귀직선이 준비되었으면, 이제 plot 메서드로 그리기만 하면 됩니다.  

회귀직선과 산점도를 함께 그려봅시다. 회귀직선으로 데이터의 경향을 더 쉽게 이해할 수 있습니다.

```python
# 계수 β_0과 β_1을 구한다
poly_fit = np.polyfit(english_scores, math_scores, 1)
# β_0+β_1 x를 반환하는 함수를 작성
poly_1d = np.poly1d(poly_fit)
# 직선을 그리기 위해 x좌표를 생성
xs = np.linspace(english_scores.min(), english_scores.max())
# xs에 대응하는 y좌표를 구한다
ys = poly_1d(xs)

fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(111)
ax.scatter(english_scores, math_scores, label = 'score')
ax.plot(xs, ys, color = 'gray', label = f'{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x')
ax.set_xlabel('english')
ax.set_ylabel('mathmatics')
# 범례 표시
ax.legend(loc = 'upper left')

plt.show()
```

<img src="image/3/3-10.png" alt="3-11" style="zoom:80%;" />



### 2.3 히트맵

**히트맵**(heap map)은 히스토그래므이 2차원 버전으로 색을 이용해 표현할 수 있는 그래프입니다. hist2d 메서드로 작성할 수 있습니다. 인수도 hist  메서드와 거의 동일합니다. 여기서는 영어 점수가 35점부터 80점까지 5점 간격, 수학 점수가 55점부터 95점까지 5점 간격이 되도록 bins와 range를 지정했습니다. 색이 진한 영역일수록 많은 학생이 분포되어 있음을 나타냅니다. 영어 점수가 55~60점, 수학 점수가 80~85점인 학생이 가장 많다는 것을 알 수 있습니다.

```python
fig = plt.figure(figsize = (10, 8))
ax = fig.add_subplot(111)

c = ax.hist2d(english_scores, math_scores, bins = [9, 8], range = [(35, 80), (55, 95)])
ax.set_xlabel('english')
ax.set_ylabel('mathmatics')
ax.set_xticks(c[1])
ax.set_yticks(c[2])
# 컬러 바 표시
fig.colorbar(c[3], ax = ax)
plt.show()
```

<img src="image/3/3-11.png" alt="3-12" style="zoom:80%;" />



## 03. 앤스컴의 예

2장과 3장에서는 데이터의 다양한 특징을 평균이나, 분산, 상관계수라는 수치 지표를 통해 분석하는 방법을 배웠습니다. 그런데 수치로 데이터를 정리하면 많은 정보를 잃어버릴 수 있으므로 주의해야 합니다. 동일해 보이는 지표를 가진 데이터라도 그림으로 나타내면 종종 전혀 다른 데이터가 되곤 합니다. 여기서는 이처럼 동일한 지표를 가지고 있지만 전혀 다른 데이터가 되는 예로 앤스컴의 예라고 부르는 데이터를 사용해서 살펴보겠습니다.

(앤스컴의 예는 평균, 표본 분산, 상관, 선형회귀선, 결정계수 등의 기술 통계량은 동일하지만 분포나 그래프를 이용하여 시각화하면 전혀 다른 4개의 데이터셋을 의미한다. 앤스컴의 예로 데이터 분석 전 시각화의 중요성을 보여주기 위해 만들어졌다고 한다.)

```python
# npy 형식으로 저장된 NumPy array를 읽어 들인다
anscombe_data = np.load('ch3_anscombe.npy')
print(anscombe_data.shape)
anscombe_data[0]
```

```
(4, 11, 2)
array([[10.  ,  8.04],
       [ 8.  ,  6.95],
       [13.  ,  7.58],
       [ 9.  ,  8.81],
       [11.  ,  8.33],
       [14.  ,  9.96],
       [ 6.  ,  7.24],
       [ 4.  ,  4.26],
       [12.  , 10.84],
       [ 7.  ,  4.82],
       [ 5.  ,  5.68]])
```

각 데이터의 평균, 분산, 상관계수, 회귀직선을 계산하여 DataFrame으로 정리합니다.

```python
stats_df = pd.DataFrame(index = ['X_mean', 'X_variance', 'Y_mean', 'Y_variance', 'X&Y_correlation', 'X&Y_regression line'])

for i, data in enumerate(anscombe_data):
    dataX = data[:, 0]
    dataY = data[:, 1]
    poly_fit = np.polyfit(dataX, dataY, 1)
    stats_df[f'data{i+1}'] = \
        [f'{np.mean(dataX):.2f}',
         f'{np.var(dataX):.2f}',
         f'{np.mean(dataY):.2f}',
         f'{np.var(dataY):.2f}',
         f'{np.corrcoef(dataX, dataY)[0, 1]:.2f}',
         f'{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x']
stats_df
```

<img src="image/3/3-12.png" alt="3-13" style="zoom:80%;" />

모든 데이터가 평균부터 회귀직선 식까지 전부 일치합니다. 결국 지표상으로 보면 이 네 가지 데이터는 모두 동일합니다.

이 네가지 데이터가 완전히 동일한지 확인하기 위해 산점도를 그려봅시다.

```python
# 그래프를 그리기 위한 영역을 2x2개 생성
fig, axes = plt.subplots(nrows = 2, ncols=2, figsize = (10, 10), sharex = True, sharey = True)

xs = np.linspace(0, 30, 100)
for i, data in enumerate(anscombe_data):
    poly_fit = np.polyfit(data[:, 0], data[:, 1], 1)
    poly_1d = np.poly1d(poly_fit)
    ys = poly_1d(xs)
    # 그리는 영역을 선택
    ax = axes[i//2, i%2]
    ax.set_xlim([4, 20])
    ax.set_ylim([3, 13])
    # 타이틀 부여
    ax.set_title(f'data{i+1}')
    ax.scatter(data[:, 0], data[:, 1])
    ax.plot(xs, ys, color = 'gray')
    
# 그래프 사이의 간격을 좁힌다
plt.tight_layout()
plt.show()
```

<img src="image/3/3-13.png" alt="3-14" style="zoom:80%;" />

그림에서 볼 수 있듯이, 이들 데이터는 전혀 다른 분포를 띠고 있습니다. 평균이나 분산이라는 지표가 많은 의미를 갖지만, 이러한 지표들을 과신하면 안 됩니다. 앤스컴의 예는 데이터를 분석할 때는 가능하면 그림을 그려야 한다는 것을 알려주고 있습니다.