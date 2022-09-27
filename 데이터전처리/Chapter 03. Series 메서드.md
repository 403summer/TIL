# Chapter 03. Series 메서드



## 01. read_csv 함수로 데이터셋 가져오기

* pokemon.csv -> 포켓몬 데이터
* google_stock.csv -> 구글 주가를 수집한 데이터
* revolutionary_war.csv -> 미국 독립 전쟁 중에 발생한 전투 기록 데이터



```python
import pandas as pd

# 다음 두 줄은 결과가 동일합니다.
pd.read_csv(filepath_or_buffer = 'pokemon.csv')
pd.read_csv('pokemon.csv')
```

```
	Pokemon	Type
0	Bulbasaur	Grass / Poison
1	Ivysaur	Grass / Poison
2	Venusaur	Grass / Poison
3	Charmander	Fire
4	Charmeleon	Fire
...	...	...
804	Stakataka	Rock / Steel
805	Blacephalon	Fire / Ghost
806	Zeraora	Electric
807	Meltan	Steel
808	Melmetal	Steel

809 rows × 2 columns
```



* 데이터셋의 열 개수와 관계없이 read_csv 함수는 항상 데이터를 여러 행과 열을 지원하는 2차원 판다스 자료구조인 DataFrame으로 가져옵니다. 지금은 Series를 연습하는 장이므로 Series로 변환하겠습니다.
* 원래 pokemon.csv 데이터 셋에 2개의 열(pokemon, Type)이 있지만 Series는 데이터 열을 하나만 지원합니다. 그래서 index_col 매개변수를 사용하여 인덱스 열을 설정하면 1개 열로 줄어듭니다. 
* Pokemon 열은 Series 인덱스로 설정하는 것을 성공했지만 판다스는 여전히 기본적으로 데이터를 DataFrame으로 가져옵니다. 여러 데이터 열을 보유할 수 있는 컨테이너는 기술적으로 하나의 데이터 열만 보유할 수 도 있기 때문입니다.
* squeeze 매개변수는 하나의 열을 가지는 DataFrame을 Series로 강제 변환합니다.

```python
pokemon = pd.read_csv('pokemon.csv', index_col = 'Pokemon', squeeze = True)
pokemon
```

```
Pokemon
Bulbasaur      Grass / Poison
Ivysaur        Grass / Poison
Venusaur       Grass / Poison
Charmander               Fire
Charmeleon               Fire
                    ...      
Stakataka        Rock / Steel
Blacephalon      Fire / Ghost
Zeraora              Electric
Meltan                  Steel
Melmetal                Steel
Name: Type, Length: 809, dtype: object
```



```python
pd.read_csv('google_stocks.csv').head()
```

```
Date	Close
0	2004-08-19	49.98
1	2004-08-20	53.95
2	2004-08-23	54.50
3	2004-08-24	52.24
4	2004-08-25	52.80
```



* 데이터셋을 가져올 때 판다스는 각 열에 가장 적합한 데이터 유형을 유추합니다. 
* 판다스에게 값을 날짜/시간으로 처리하도록 지시하지 않으면 기본적으로 값을 문자열로 가져옵니다. 문자열은 모든 값을 나타낼 수 있습니다.
* parse_dates 매개변수는 문자열 리스트를 인수로 받아 날짜/시간로 변환하는 변수입니다.

```python
google = pd.read_csv(
    'google_stocks.csv',
    parse_dates = ['Date'],
    index_col = 'Date',
    squeeze = True
)

google
```

```
Date
2004-08-19      49.98
2004-08-20      53.95
2004-08-23      54.50
2004-08-24      52.24
2004-08-25      52.80
               ...   
2019-10-21    1246.15
2019-10-22    1242.80
2019-10-23    1259.13
2019-10-24    1260.99
2019-10-25    1265.13
Name: Close, Length: 3824, dtype: float64
```



```python
pd.read_csv('revolutionary_war.csv').tail()
```

```
Battle	Start Date	State
227	Siege of Fort Henry	9/11/1782	Virginia
228	Grand Assault on Gibraltar	9/13/1782	NaN
229	Action of 18 October 1782	10/18/1782	NaN
230	Action of 6 December 1782	12/6/1782	NaN
231	Action of 22 January 1783	1/22/1783	Virginia
```



* usecols 매개변수는 판다스가 가져와야 하는 열 목록을 인자로 받습니다. 

```python
battles = pd.read_csv(
    'revolutionary_war.csv',
    index_col = 'Start Date',
    parse_dates = ['Start Date'],
    usecols = ['State', 'Start Date'],
    squeeze = True
)

battles
```

```
Start Date
1774-09-01    Massachusetts
1774-12-14    New Hampshire
1775-04-19    Massachusetts
1775-04-19    Massachusetts
1775-04-20         Virginia
                  ...      
1782-09-11         Virginia
1782-09-13              NaN
1782-10-18              NaN
1782-12-06              NaN
1783-01-22         Virginia
Name: State, Length: 232, dtype: object
```





## 02. Series 정렬



### 2.1 sort_values 메서드를 사용하여 값 기준으로 정렬

* sort_values 메서드는 값이 오름차순으로 정렬된 새 Series를 반환합니다.

```python
google.sort_values().head()
```

```
Date
2004-09-03      49.82
2004-09-01      49.94
2004-08-19      49.98
2004-09-02      50.57
2004-09-07      50.60
Name: Close, Length: 3824, dtype: float64
```



* 오름차순은 알파벳의 시작부터 끝까지 순서를 의미합니다
* 판다스는 대문자를 소문자보다 먼저 정렬합니다.

```python
pokemon.sort_values()
```

```
Pokemon
Illumise                Bug
Silcoon                 Bug
Pinsir                  Bug
Burmy                   Bug
Wurmple                 Bug
                  ...      
Tirtouga       Water / Rock
Relicanth      Water / Rock
Corsola        Water / Rock
Carracosta     Water / Rock
Empoleon      Water / Steel
Name: Type, Length: 809, dtype: object
```



* ascending 매개변수는 정렬 순서를 설정하며 기본 인수는 True입니다.
* 내림차순으로 정렬하려면 ascending = False

```python
google.sort_values(ascending = False).head()
```

```
Date
2004-08-23    54.50
2004-08-20    53.95
2004-08-25    52.80
2004-08-24    52.24
2004-08-19    49.98
Name: Close, dtype: float64
```



* na_position 매개변수는 반환된 Series에서 NaN 값을 어디에 배치할지를 결정하며 기본 인수로 'last' 를 갖습니다. 기본적으로 판다스는 정렬된 Series의 마지막에 결측값을 배치합니다.

```python
# 다음 두 줄은 결과가 동일합니다.
battles.sort_values()
battles.sort_values(na_position = 'last')
```

```
Start Date
1781-09-06    Connecticut
1779-07-05    Connecticut
1777-04-27    Connecticut
1777-09-03       Delaware
1777-05-17        Florida
                 ...     
1782-08-08            NaN
1782-08-25            NaN
1782-09-13            NaN
1782-10-18            NaN
1782-12-06            NaN
Name: State, Length: 232, dtype: object
```



```python
battles.sort_values(na_position = 'first')
```

```
Start Date
1775-09-17         NaN
1775-12-31         NaN
1776-03-03         NaN
1776-03-25         NaN
1776-05-18         NaN
                ...   
1781-07-06    Virginia
1781-07-01    Virginia
1781-06-26    Virginia
1781-04-25    Virginia
1783-01-22    Virginia
Name: State, Length: 232, dtype: object
```



* dropna 메서드는 결측값이 모두 제거된 Series를 반환합니다.

```python
battles.dropna().sort_values()
```

```
tart Date
1781-09-06    Connecticut
1779-07-05    Connecticut
1777-04-27    Connecticut
1777-09-03       Delaware
1777-05-17        Florida
                 ...     
1781-07-06       Virginia
1781-07-01       Virginia
1781-06-26       Virginia
1781-04-25       Virginia
1783-01-22       Virginia
Name: State, Length: 162, dtype: object
```



### 2.2 sort_index 메서드를 사용하여 인덱스 기준으로 정렬

```python
# 다음 두 줄은 결과가 동일합니다.
pokemon.sort_index()
pokemon.sort_index(ascending = True)
```

```
Pokemon
Abomasnow        Grass / Ice
Abra                 Psychic
Absol                   Dark
Accelgor                 Bug
Aegislash      Steel / Ghost
                  ...       
Zoroark                 Dark
Zorua                   Dark
Zubat        Poison / Flying
Zweilous       Dark / Dragon
Zygarde      Dragon / Ground
Name: Type, Length: 809, dtype: object
```



* 판다스는 누락된 날짜 값 대신 다른 넘파이 객체인 NaT('Not a time')를 사용합니다.

```python
battles.sort_index()
```

```
Start Date
1774-09-01    Massachusetts
1774-12-14    New Hampshire
1775-04-19    Massachusetts
1775-04-19    Massachusetts
1775-04-20         Virginia
                  ...      
1783-01-22         Virginia
NaT              New Jersey
NaT                Virginia
NaT                     NaN
NaT                     NaN
Name: State, Length: 232, dtype: object
```



```python
battles.sort_index(na_position = 'first').head()
```

```
Start Date
NaT              New Jersey
NaT                Virginia
NaT                     NaN
NaT                     NaN
1774-09-01    Massachusetts
Name: State, dtype: object
```



### 2.3 nsmallest와 nlargest 메서드

* nlarget 메서드는 Series에서 가장 큰 값을 반환합니다.

```python
# 다음 두 줄은 결과가 동일합니다.
google.nlargest(n = 5)
google.nlargest()
```

```
Date
2019-04-29    1287.58
2019-04-26    1272.18
2018-07-26    1268.33
2019-10-25    1265.13
2019-04-23    1264.55
Name: Close, dtype: float64
```



* nsmallest 메서드는 오름차순으로 정렬된 Series에서 가장 작은 값을 반환합니다.

```python
# 다음 두 줄은 결과가 동일합니다.
google.nsmallest(n = 5)
google.nsmallest(5)
```

```
Date
2004-09-03    49.82
2004-09-01    49.94
2004-08-19    49.98
2004-09-02    50.57
2004-09-07    50.60
Name: Close, dtype: float64
```



## 03. inplace 매개변수로 Series 덮어쓰기

* 여기서 호출하는 모든 메서드는 새로운 Series를 반환합니다. 원본 Series 객체는 지금까지 작업에 영향을 받지 않고 원본을 유지하고 있습니다.

```python
battles.head(3)

# Start Date
# 1774-09-01    Massachusetts
# 1774-12-14    New Hampshire
# 1775-04-19    Massachusetts
# Name: State, dtype: object

battles.sort_values().head(3)

# Start Date
# 1781-09-06    Connecticut
# 1779-07-05    Connecticut
# 1777-04-27    Connecticut
# Name: State, dtype: object

battles.head(3)

# Start Date
# 1774-09-01    Massachusetts
# 1774-12-14    New Hampshire
# 1775-04-19    Massachusetts
# Name: State, dtype: object
```



* inplace 매개변수는 기존 객체를 수정하는 것 매개변수 입니다. 

```python
battles.head(3)

# Start Date
# 1774-09-01    Massachusetts
# 1774-12-14    New Hampshire
# 1775-04-19    Massachusetts
# Name: State, dtype: object

battles.sort_values(inplace = True)

battles.head(3)

# Start Date
# 1781-09-06    Connecticut
# 1779-07-05    Connecticut
# 1777-04-27    Connecticut
# Name: State, dtype: object
```



* inplace 매개변수를 사용하더라도 판다스는 메서드를 호출할 때 마다 객체의 복사본을 만듭니다. 판다스 라이브러리는 항상 복사본을 생성합니다. inplace 매개변수는 기존 변수를 새 객체에 할당합니다. 사실 inplace 매개변수는 성능상의 이점을 제공하지 않습니다. 다음 두 줄은 기술적으로 동일합니다.

```python
battles.sort_values(inplace = True)
battles = battles.sort_values()
```

* 항상 복사본을 만드는 이유는 불변 자료구조가 버그를 줄이는 경향이 있기 때문입니다. 변경할 수 없는 객체를 복사하고 복사본을 조작할 수는 있지만 원본 객체를 변경할 수 없습니다.



## 04. value_counts 메서드로 값 계산하기

```python
pokemon.head()
```

```
Pokemon
Bulbasaur     Grass / Poison
Ivysaur       Grass / Poison
Venusaur      Grass / Poison
Charmander              Fire
Charmeleon              Fire
Name: Type, dtype: object
```



* value_counts 메서드는 각 Series 값의 발생 횟수를 계산합니다.

```python
pokemon.value_counts()
```

```
Normal                65
Water                 61
Grass                 38
Psychic               35
Fire                  30
                      ..
Fire / Psychic         1
Normal / Ground        1
Psychic / Fighting     1
Dark / Ghost           1
Fire / Ghost           1
Name: Type, Length: 159, dtype: int64
```



* value_count Series의 길이는 pokemon Series의 고유값 수와 값습니다.
* 하지만 value_count Series 고유값의 길이는 pokemon Series의 고유값 수 보다 작습니다.

```python
len(pokemon.value_counts())

# 159

pokemon.nunique()

# 159

pokemon.value_counts().nunique()

# 23
```



* normalize 매개변수는 각 고유값의 빈도를 반환합니다.
* round 메서드는 값을 반올림합니다. 첫번째 매개변수인 decimals는 소수점 뒤에 남겨둘 자릿수를 결정합니다.

```python
pokemon.value_counts(normalize = True).head()
```

```
Normal     0.080346
Water      0.075402
Grass      0.046972
Psychic    0.043263
Fire       0.037083
Name: Type, dtype: float64
```

```python
pokemon.value_counts(normalize = True).head() * 100
```

```
Normal     8.034611
Water      7.540173
Grass      4.697157
Psychic    4.326329
Fire       3.708282
Name: Type, dtype: float64
```

```python
(pokemon.value_counts(normalize = True).head() * 100).round(2)
```

```
Normal     8.03
Water      7.54
Grass      4.70
Psychic    4.33
Fire       3.71
Name: Type, dtype: float64
```



```python
google.value_counts().head()
```

```
287.68    3
194.27    3
307.10    3
288.92    3
290.41    3
Name: Close, dtype: int64
```

```python
google.max()

# 1287.58

google.min()

# 49.82
```



* bin 매개변수는 버킷을 정하고 그룹화하는 변수입니다.
* 메서드를 순서대로 호출하는 기술을 메서드 체이닝이라고 합니다.

```python
buckets = [0, 200, 400, 600, 800, 1000, 1200, 1400]
google.value_counts(bins = buckets)
```

```
(200.0, 400.0]      1568
(-0.001, 200.0]      595
(400.0, 600.0]       575
(1000.0, 1200.0]     406
(600.0, 800.0]       380
(800.0, 1000.0]      207
(1200.0, 1400.0]      93
Name: Close, dtype: int64
```

```python
# 메서드 체이닝
google.value_counts(bins = buckets).sort_index()
```

```
(-0.001, 200.0]      595
(200.0, 400.0]      1568
(400.0, 600.0]       575
(600.0, 800.0]       380
(800.0, 1000.0]      207
(1000.0, 1200.0]     406
(1200.0, 1400.0]      93
Name: Close, dtype: int64
```

```python
google.value_counts(bins = buckets, sort = False)
```

```
(-0.001, 200.0]      595
(200.0, 400.0]      1568
(400.0, 600.0]       575
(600.0, 800.0]       380
(800.0, 1000.0]      207
(1000.0, 1200.0]     406
(1200.0, 1400.0]      93
Name: Close, dtype: int64
```

* bin 매개변수가 있는 value_counts 메서드는 반개구간을 반환합니다.
* 폐구간에는 두 끝점이 모두 포함됩니다. 예를 들어 [5,10]은 5 이상, 10이하의 구간을 나타냅니다.
* 개구간은 두 끝점을 모두 제외합니다. 예를 들어 (5,10)은 5보다 크고 10보다 작은 구간을 나타냅니다.



* bins 매개변수는 정수도 허용합니다. 정수가 입력되면 최댓값과 최솟값 차이는 자동으로 계산하고 범위를 지정된 수의 빈으로 나눕니다.

```python
google.value_counts(bins = 6, sort = False)
```

```
(48.581, 256.113]      1204
(256.113, 462.407]     1104
(462.407, 668.7]        507
(668.7, 874.993]        380
(874.993, 1081.287]     292
(1081.287, 1287.58]     337
Name: Close, dtype: int64
```



```python
battles.value_counts().head()
```

```
South Carolina    31
New York          28
New Jersey        24
Virginia          21
Massachusetts     11
Name: State, dtype: int64
```



* value_counts 메서드는 기본적으로 NaN 값을 제외합니다. null 값을 고유한 범주로 계산하려면 dripna 매개변수에 False 인수를 전달합니다.

```python
battles.value_counts(dropna = False).head()
```

```
NaN               70
South Carolina    31
New York          28
New Jersey        24
Virginia          21
Name: State, dtype: int64
```



* value_count 메서드는 Series 인덱스도 지원합니다.

```python
battles.index
```

```
DatetimeIndex(['1781-09-06', '1779-07-05', '1777-04-27', '1777-09-03',
               '1777-05-17', '1779-09-10', '1779-09-07', '1780-03-02',
               '1778-06-30', '1781-01-07',
               ...
               '1782-05-06', '1782-05-25', '1782-05-28', '1782-07-01',
               '1782-07-06', '1782-08-08', '1782-08-25', '1782-09-13',
               '1782-10-18', '1782-12-06'],
              dtype='datetime64[ns]', name='Start Date', length=232, freq=None)
```

```python
battles.index.value_counts()
```

```
1781-05-22    2
1775-04-19    2
1778-09-07    2
1780-08-18    2
1782-03-16    2
             ..
1777-10-06    1
1777-09-19    1
1777-08-16    1
1777-08-06    1
1782-12-06    1
Name: Start Date, Length: 217, dtype: int64
```



## 05. apply 메서드를 사용하여 모든 Series 값에 대한 함수 호출

* 함수는 파이썬에서 일급객체입니다. 즉, 파이썬이 함수를 다른 데이터 유형처럼 취급합니다.
* 일급 객체를 이해하는 가장 간단한 방법은 다음과 같습니다. 숫자로 할 수 있는 모든 것을 함수로 할 수 있습니다. 예를 들어 다음과 같은 모든 작업을 수행할 수 있습니다.
  * 함수를 리스트에 저장합니다.
  * 딕셔너리 키에 대한 값으로 함수를 할당합니다
  * 함수를 다른 함수에 인수로 할당합니다
  * 다른 함수에서 함수를 반환합니다
* 함수와 함수 호출을 구분하자. 함수는 출력을 생성하는 일력의 명령입니다. 아직 요리되지 않은 레시피 입니다. 함수 호출은 명령어의 실제 실행입니다. 레시피에 맞춰 요리하는 것 입니다.

```python
funcs = [len, max, min]
for current_func in funcs:
    print(current_func(google))
```

```
3824
1287.58
49.82
```





* 함수를 파이썬의 다른 객체처럼 취급할 수 있다는 점을 판다스에서는 다음과 같이 활용할 수 있다.

```python
round(99.2)

# 99

round(99.49)

# 99 

round(99.5)

# 100
```

* apply 메서드는 각 Series 값에 대해 한 번씩 함수를 호출하고 함수 호출의 반환 값으로 구성된 새 Series를 반환한다.
* apply 메서드에게 전달하는 인자는 호출되지 않은 round 함수이다.

```python
# 다음 두 줄을 결과가 동일합니다.
google.apply(func = round)
google.apply(round)
```

```
Date
2004-08-19      50
2004-08-20      54
2004-08-23      54
2004-08-24      52
2004-08-25      53
              ... 
2019-10-21    1246
2019-10-22    1243
2019-10-23    1259
2019-10-24    1261
2019-10-25    1265
Name: Close, Length: 3824, dtype: int64
```



* apply 메서드는 사용자 정의 함수도 허용합니다.

```python
def single_or_multi(pokemon_type):
    if '/' in pokemon_type:
        return 'Multi'
    
    return 'Single'
```

```python
pokemon.head(4)
```

```
Pokemon
Bulbasaur     Grass / Poison
Ivysaur       Grass / Poison
Venusaur      Grass / Poison
Charmander              Fire
Name: Type, dtype: object
```

```python
pokemon.apply(single_or_multi)
```

```
Pokemon
Bulbasaur       Multi
Ivysaur         Multi
Venusaur        Multi
Charmander     Single
Charmeleon     Single
                ...  
Stakataka       Multi
Blacephalon     Multi
Zeraora        Single
Meltan         Single
Melmetal       Single
Name: Type, Length: 809, dtype: object
```

```python
pokemon.apply(single_or_multi).value_counts()
```

```
Multi     405
Single    404
Name: Type, dtype: int64
```

