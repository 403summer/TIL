# Chapter 04. DataFrame 객체



## 01. DataFrame의 개요



* 판다스 DataFrame은 행과 열이 있는 2차원 데이터 테이블입니다. Series와 마찬가지로 판다스는 인덱스 레이블과 인덱스 위치를 각 DataFrame 행에 할당합니다. 판다스는 또한 각 열에 레이블과 위치를 할당합니다. DataFrame은 데이터셋에서 값을 추출하기 위해 행과 열이라는 2개의 참조점을 사용하기 때문에 2차원입니다.

```python
import pandas as pd
import numpy as np
```



### 1.1 딕셔너리에서 DataFrame 생성

* DataFrame 자료구조는 Series와 다르게 렌더링됩니다. 하지만 여기서는 텍스트만 보여주겠습니다.

```python
city_data = {
    'City': ['New York City', 'Paris', 'Barcelona', 'Rome'],
    'Country': ['United States', 'France', 'Spain', 'Italy'],
    'Population': pd.Series([8600000, 2141000, 5515000, 2873000])
}

cities = pd.DataFrame(city_data)
cities
```

```
         City	      Country	   Population
0	New York City	United States	8600000
1	     Paris	       France	    2141000
2	   Barcelona	    Spain	    5515000
3	     Rome	        Italy	    2873000
```



* 열 헤더를 인덱스 레이블로 바꾸려면?

```python
# 다음 두 줄은 결과가 동일합니다
cities.transpose()
cities.T
```

```
              0	          1	         2	      3
City	New York City	Paris	Barcelona	Rome
Country	United States	France	  Spain	    Italy
Population	8600000	   2141000	 5515000   2873000
```



### 1.2 넘파이 ndarray로 DataFrame 생성

```python
random_data = np.random.randint(1, 101, [3,5])
random_data
```

```
array([[43, 18, 67, 90, 43],
       [58, 45, 22, 30, 54],
       [ 7, 51, 35, 19, 23]])
```



* ndarray는 행 레이블과 열 레이블이 없습니다. 따라서 판다스는 행 축과 열 축에 대해 모두 숫자 인덱스를 부여합니다.

```python
pd.DataFrame(data = random_data)
```

```
    0	1	2	3	4
0	43	18	67	90	43
1	58	45	22	30	54
2	7	51	35	19	23
```



* DataFrame 생성자의 index 매개변수에 리스트, 튜플 또는 ndarray와 같은 반복 가능한 객체를 넘길 수 있으며 이 매개변수를 사용하면 원하는 행 레이블을 설정할 수 있습니다. 반복 가능한 객체의 길이는 반드시 데이터 셋의 행 개수와 동일해야 합니다.

```python
row_labels = ['Morning', 'Afternoon', 'Evening']
temperatures = pd.DataFrame(
    data = random_data,
    index = row_labels
)

temperatures
```

```
           0	1	2	3	4
Morning	   43	18	67	90	43
Afternoon  58	45	22	30	54
Evening	    7	51	35	19	23
```



* columns 매개변수를 사용하여 열 이름을 설정할 수 있습니다.  

```python
row_labels = ['Morning', 'Afternoon', 'Evening']
column_labels = (
    'Monday',
    'Tuesday',
    'Wedneday',
    'Thursday',
    'Friday'
)

pd.DataFrame(
    data = random_data,
    index = row_labels,
    columns = column_labels
)
```

```
              Monday	Tuesday	  Wedneday	Thursday	Friday
Morning	        43	       18	    67	      90	     43
Afternoon	    58	       45	    22	      30	     54
Evening	         7	       51	    35	      19	     23
```



* 판다스는 중복된 행 인덱스와 열 인덱스를 허용합니다.

```python
row_labels = ['Morning', 'Afternoon', 'Morning']
column_labels = (
    'Monday',
    'Tuesday',
    'Wedneday',
    'Thursday',
    'Friday'
)

pd.DataFrame(
    data = random_data,
    index = row_labels,
    columns = column_labels
)
```

```
              Monday	Tuesday	  Wedneday	Tuesday	   Friday
Morning	        43	       18	    67	      90	     43
Afternoon	    58	       45	    22	      30	     54
Morning	         7	       51	    35	      19	     23
```



## 02. Series와 DataFrame의 유사점



### 2.1 read_csv 함수로 DataFrame 가져오기

* nba.csv는 미국의 프로농구 선수의 목록 데이터셋입니다.

```python
pd.read_csv(
    'nba.csv',
    parse_dates = ['Birthday']  
)
```

```
Name	Team	Position	Birthday	Salary
0	Shake Milton	Philadelphia 76ers	SG	1996-09-26	1445697
1	Christian Wood	Detroit Pistons	PF	1995-09-27	1645357
2	PJ Washington	Charlotte Hornets	PF	1998-08-23	3831840
3	Derrick Rose	Detroit Pistons	PG	1988-10-04	7317074
4	Marial Shayok	Philadelphia 76ers	G	1995-07-26	79568
...	...	...	...	...	...
445	Austin Rivers	Houston Rockets	PG	1992-08-01	2174310
446	Harry Giles	Sacramento Kings	PF	1998-04-22	2578800
447	Robin Lopez	Milwaukee Bucks	C	1988-04-01	4767000
448	Collin Sexton	Cleveland Cavaliers	PG	1999-01-04	4764960
449	Ricky Rubio	Phoenix Suns	PG	1990-10-21	16200000
450 rows × 5 columns
```

```python
nba = pd.read_csv('nba.csv', parse_dates = ['Birthday'])
```



### 2.2 Series와 DataFrame 속성의 유사점과 차이점

* Series에서는 dtype, DataFrame에서는 dtypes
* DataFrame의 dtypes 속성은 열은 인덱스 레이블로, 데이터 유형을 값으로 가지는 Series를 반환합니다.

```python
pd.Series([1, 2, 3]).dtype

# dtype('int64')

nba.dtypes

# Name                object
# Team                object
# Position            object
# Birthday    datetime64[ns]
# Salary               int64
# dtype: object
```

```python
nba.dtypes.value_counts()
```

```
object            3
datetime64[ns]    1
int64             1
dtype: int64
```



* index 속성은 DataFrame의 인덱스를 나타냅니다.
* index 속성은 Series와 DataFrame이 공통적으로 가지는 속성입니다.

```python
nba.index
```

```
RangeIndex(start=0, stop=450, step=1)
```



* columns 속성으로 열 인덱스에 접근할 수 있습니다.
* columns 속성은 DataFrame만 가지는 속성입니다.

```python
nba.columns
```

```
Index(['Name', 'Team', 'Position', 'Birthday', 'Salary'], dtype='object')
```



* ndim 속성은 판다스 객체의 차원 수를 반환합니다.

```python
nba.ndim

# 2
```



* shape 속성은 DataFrame의 차원을 튜플 형태로 반환합니다.

```python
nba.shape

# (450, 5)
```



* size 속성은 데이터셋에 있는 값의 전체 개수를 반환합니다. NaN과 같은 결측값도 개수에 포함됩니다.

```python
nba.size

# 2250
```



* count 메서드는 결측값을 제외한 유효한 값의 개수를 나타내는 Series를 반환합니다

```python
nba.count()
```

```
Name        450
Team        450
Position    450
Birthday    450
Salary      450
dtype: int64
```



* sum 메서드를 사용하여 Series에 있는 결측값이 아닌 모든 값의 개수를 더할 수 있습니다.

```python
nba.count().sum()

# 2250
```



* size 속성과 count 메서드의 차이를 예를 들어 설명하겠습니다
* size 속성은 4개의 셀을 가지기 때문에 4. count 메서드는 유효한 값을 계산하기에 3을 반환한다.

```python
data = {
    'A': [1, np.nan],
    'B': [2, 3]
}

df = pd.DataFrame(data)
df
```

```
     A	B
0	1.0	2
1	NaN	3
```

```python
df.size

# 4

df.count()

# A    1
# B    2
# dtype: int64

df.count().sum()

# 3
```



### 2.3 Series와 DataFrame의 공통 메서드

* head()

```python
nba.head(2)
```

```
        Name	Team	Position	Birthday	Salary
0	Shake Milton	Philadelphia 76ers	SG	1996-09-26	1445697
1	Christian Wood	Detroit Pistons	PF	1995-09-27	1645357
```



* tail()

```python
nba.tail(n = 3)
```

```
        Name	Team	Position	Birthday	Salary
447	Robin Lopez	Milwaukee Bucks	C	1988-04-01	4767000
448	Collin Sexton	Cleveland Cavaliers	PG	1999-01-04	4764960
449	Ricky Rubio	Phoenix Suns	PG	1990-10-21	16200000
```



* sample 메서드는 DataFrame에서 임의의 행을 추출합니다.

```python
nba.sample(3)
```

```
        Name	Team	Position	Birthday	Salary
355	Tristan Thompson	Cleveland Cavaliers	C	1991-03-13	18539130
299	Mike Scott	Philadelphia 76ers	PF	1988-07-16	4767000
158	Cristiano Felicio	Chicago Bulls	C	1992-07-07	8156500
```



* nunique 메서드를 사용하여 Series에 있는 고유한 값의 개수를 구했습니다

```python
nba.nunique()
```

```
Name        450
Team         30
Position      9
Birthday    430
Salary      269
dtype: int64
```



* max 메서드는 각 열에 있는 최댓값을 min 메서드는 각 열에 있는 최소값을 Series로 반환합니다

```python
nba.max()
```

```
Name             Zylan Cheatham
Team         Washington Wizards
Position                     SG
Birthday    2000-12-23 00:00:00
Salary                 40231758
dtype: object
```

```python
nba.min()
```

```
Name               Aaron Gordon
Team              Atlanta Hawks
Position                      C
Birthday    1977-01-26 00:00:00
Salary                    79568
dtype: object
```



+ nlargest 메서드는 DataFrame의 주어진 열에서 가장 큰 값을 가지는 행의 집합을 n 매개변수로 몇개의 행을 추출할지 설정하고 columns 매개변수로 정렬할 열을 선택합니다.

```python
nba.nlargest(n = 4, columns = 'Salary')
```

```
Name	Team	Position	Birthday	Salary
205	Stephen Curry	Golden State Warriors	PG	1988-03-14	40231758
38	Chris Paul	Oklahoma City Thunder	PG	1985-05-06	38506482
219	Russell Westbrook	Houston Rockets	PG	1988-11-12	38506482
251	John Wall	Washington Wizards	PG	1990-09-06	38199000
```



* nsmallest 메서드는 주어진 열에서 가장 작은 값을 가지는 행의 집합을 반환한다
* nlargest와 nsmallest 메서드는 숫자 또는 날짜/시간 열에서만 작동한다.

```python
nba.nsmallest(n = 3, columns = ['Birthday'])
```

```
        Name	Team	Position	Birthday	Salary
98	Vince Carter	Atlanta Hawks	PF	1977-01-26	2564753
196	Udonis Haslem	Miami Heat	C	1980-06-09	2564753
262	Kyle Korver	Milwaukee Bucks	PF	1981-03-17	6004753
```



* NBA 연봉의 총 합을 구하고 싶다면?

```python
nba.sum()
```

```
Name        Shake MiltonChristian WoodPJ WashingtonDerrick...
Team        Philadelphia 76ersDetroit PistonsCharlotte Hor...
Position    SGPFPFPGGPFSGSFCSFPGPGFCPGSGPFCCPFPFSGPFPGSGSF...
Salary                                             3444112694
dtype: object
```

* 숫자로 합한 결과만 보고 싶다면 sum 메서드의 numeric_only 매개변수에 True를 설정하세요

```python
nba.sum(numeric_only = True)

# Salary    3444112694
# dtype: int64
```

* 평균 연봉은 mean 메서드로 구할 수 있습니다

```python
nba.mean(numeric_only = True)
```

```
Salary    7.653584e+06
dtype: float64
```

* 중앙값, 최빈값 및 표준편차

```python
nba.median(numeric_only = True)

# Salary    3303074.5
# dtype: float64

nba.mode(numeric_only = True)

#   Salary
# 0	 79568

nba.std(numeric_only = True)

# Salary    9.288810e+06
# dtype: float64
```



## 03. DataFrame 정렬



### 3.1 단일 열 기준으로 정렬

* by 매개변수는 정렬할 기준이 되는 열을 설정합니다

```python
# 다음 두 줄을 결과가 동일합니다.
nba.sort_values('Name')
nba.sort_values(by = 'Name')
```

```
     Name	Team	Position	Birthday	Salary
52	Aaron Gordon	Orlando Magic	PF	1995-09-16	19863636
101	Aaron Holiday	Indiana Pacers	PG	1996-09-30	2239200
437	Abdel Nader	Oklahoma City Thunder	SF	1993-09-25	1618520
81	Adam Mokoka	Chicago Bulls	G	1998-07-18	79568
399	Admiral Schofield	Washington Wizards	SF	1997-03-30	1000000
...	...	...	...	...	...
159	Zach LaVine	Chicago Bulls	PG	1995-03-10	19500000
302	Zach Norvell	Los Angeles Lakers	SG	1997-12-09	79568
312	Zhaire Smith	Philadelphia 76ers	SG	1999-06-04	3058800
137	Zion Williamson	New Orleans Pelicans	F	2000-07-06	9757440
248	Zylan Cheatham	New Orleans Pelicans	SF	1995-11-17	79568
450 rows × 5 columns
```



* ascending 매개변수는 정렬 순서를 결정합니다.

```python
nba.sort_values('Name', ascending = False).head()
```

```
     Name	Team	Position	Birthday	Salary
248	Zylan Cheatham	New Orleans Pelicans	SF	1995-11-17	79568
137	Zion Williamson	New Orleans Pelicans	F	2000-07-06	9757440
312	Zhaire Smith	Philadelphia 76ers	SG	1999-06-04	3058800
302	Zach Norvell	Los Angeles Lakers	SG	1997-12-09	79568
159	Zach LaVine	Chicago Bulls	PG	1995-03-10	19500000
```



### 3.2 다중 열 기준으로 정렬

* by 매개변수에 리스트를 전달하여 여러 열을 정렬할 수 있습니다. 판다스는 리스트에 나타나는 순서대로 열을 연속적으로 정렬합니다.

```python
nba.sort_values(by = ['Team', 'Name'])
```

```
        Name	Team	Position	Birthday	Salary
359	Alex Len	Atlanta Hawks	C	1993-06-16	4160000
167	Allen Crabbe	Atlanta Hawks	SG	1992-04-09	18500000
276	Brandon Goodwin	Atlanta Hawks	PG	1995-10-02	79568
438	Bruno Fernando	Atlanta Hawks	C	1998-08-15	1400000
194	Cam Reddish	Atlanta Hawks	SF	1999-09-01	4245720
...	...	...	...	...	...
418	Jordan McRae	Washington Wizards	PG	1991-03-28	1645357
273	Justin Robinson	Washington Wizards	PG	1997-10-12	898310
428	Moritz Wagner	Washington Wizards	C	1997-04-26	2063520
21	Rui Hachimura	Washington Wizards	PF	1998-02-08	4469160
36	Thomas Bryant	Washington Wizards	C	1997-07-31	8000000
```



* ascending 매개변수에 리스트를 전달하면 각 열을 다른 순서로 정렬할 수 있습니다

```python
nba.sort_values(
    by = ["Team", "Salary"], 
    ascending = [True, False]
)
```

```
         Name	Team	Position	Birthday	Salary
111	Chandler Parsons	Atlanta Hawks	SF	1988-10-25	25102512
28	Evan Turner	Atlanta Hawks	PG	1988-10-27	18606556
167	Allen Crabbe	Atlanta Hawks	SG	1992-04-09	18500000
213	De'Andre Hunter	Atlanta Hawks	SF	1997-12-02	7068360
339	Jabari Parker	Atlanta Hawks	PF	1995-03-15	6500000
...	...	...	...	...	...
80	Isaac Bonga	Washington Wizards	PG	1999-11-08	1416852
399	Admiral Schofield	Washington Wizards	SF	1997-03-30	1000000
273	Justin Robinson	Washington Wizards	PG	1997-10-12	898310
283	Garrison Mathews	Washington Wizards	SG	1996-10-24	79568
353	Chris Chiozza	Washington Wizards	PG	1995-11-21	79568
450 rows × 5 columns
```

```python
nba = nba.sort_values(
    by = ["Team", "Salary"], 
    ascending = [True, False]
)
```





## 04. 인덱스별 정렬

```python
nba.head()
```

```
        Name	Team	Position	Birthday	Salary
111	Chandler Parsons	Atlanta Hawks	SF	1988-10-25	25102512
28	Evan Turner	Atlanta Hawks	PG	1988-10-27	18606556
167	Allen Crabbe	Atlanta Hawks	SG	1992-04-09	18500000
213	De'Andre Hunter	Atlanta Hawks	SF	1997-12-02	7068360
339	Jabari Parker	Atlanta Hawks	PF	1995-03-15	6500000
```



### 4.1 행 인덱스 기준으로 정렬

```python
# 다음 두 줄은 결과가 동일합니다.
nba.sort_index().head()
nba.sort_index(ascending = True).head()
```

```
Name	Team	Position	Birthday	Salary
0	Shake Milton	Philadelphia 76ers	SG	1996-09-26	1445697
1	Christian Wood	Detroit Pistons	PF	1995-09-27	1645357
2	PJ Washington	Charlotte Hornets	PF	1998-08-23	3831840
3	Derrick Rose	Detroit Pistons	PG	1988-10-04	7317074
4	Marial Shayok	Philadelphia 76ers	G	1995-07-26	79568
```

```python
nba = nba.sort_index()
```



### 4.2 열 인덱스 기준으로 정렬

```python
# 다음 두 줄은 결과가 동일합니다.
nba.sort_index(axis = 'columns').head()
nba.sort_index(axis = 1).head()
```

```
      Birthday	Name	Position	Salary	Team
0	1996-09-26	Shake Milton	SG	1445697	Philadelphia 76ers
1	1995-09-27	Christian Wood	PF	1645357	Detroit Pistons
2	1998-08-23	PJ Washington	PF	3831840	Charlotte Hornets
3	1988-10-04	Derrick Rose	PG	7317074	Detroit Pistons
4	1995-07-26	Marial Shayok	G	79568	Philadelphia 76ers
```



```python
nba.sort_index(axis = 'columns', ascending = False).head()
```

```
     Team	Salary	Position	Name	Birthday
0	Philadelphia 76ers	1445697	SG	Shake Milton	1996-09-26
1	Detroit Pistons	1645357	PF	Christian Wood	1995-09-27
2	Charlotte Hornets	3831840	PF	PJ Washington	1998-08-23
3	Detroit Pistons	7317074	PG	Derrick Rose	1988-10-04
4	Philadelphia 76ers	79568	G	Marial Shayok	1995-07-26
```



## 05. 새 인덱스 설정

+ set_index 메서드는 지정된 열이 인덱스로 설정된 새 DataFrame을 반환합니다

```python
# 다음 두 줄은 결과가 동일합니다.
nba.set_index(keys = 'Name')
nba.set_index('Name')
```

```
    Name	       Team	Position	Birthday	Salary				
Shake Milton	Philadelphia 76ers	SG	1996-09-26	1445697
Christian Wood	Detroit Pistons	PF	1995-09-27	1645357
PJ Washington	Charlotte Hornets	PF	1998-08-23	3831840
Derrick Rose	Detroit Pistons	PG	1988-10-04	7317074
Marial Shayok	Philadelphia 76ers	G	1995-07-26	79568
...	...	...	...	...
Austin Rivers	Houston Rockets	PG	1992-08-01	2174310
Harry Giles	Sacramento Kings	PF	1998-04-22	2578800
Robin Lopez	Milwaukee Bucks	C	1988-04-01	4767000
Collin Sexton	Cleveland Cavaliers	PG	1999-01-04	4764960
Ricky Rubio	Phoenix Suns	PG	1990-10-21	16200000
450 rows × 4 columns
```



* 데이터셋을 가져올 때 인덱스를 설정할 수 도 있다

```python
nba = pd.read_csv(
    'nba.csv',
    parse_dates = ['Birthday'],
    index_col = 'Name'
)
```



## 06. DataFrame에서 열과 행 선택



### 6.1 DataFrame에서 단일 열 선택

* 속성으로 접근하는 방법

```python
nba.Salary
```

```
Name
Shake Milton       1445697
Christian Wood     1645357
PJ Washington      3831840
Derrick Rose       7317074
Marial Shayok        79568
                    ...   
Austin Rivers      2174310
Harry Giles        2578800
Robin Lopez        4767000
Collin Sexton      4764960
Ricky Rubio       16200000
Name: Salary, Length: 450, dtype: int64
```



* 대괄호로 접근하는 방법

```python
nba['Position']
```

```
Name
Shake Milton      SG
Christian Wood    PF
PJ Washington     PF
Derrick Rose      PG
Marial Shayok      G
                  ..
Austin Rivers     PG
Harry Giles       PF
Robin Lopez        C
Collin Sexton     PG
Ricky Rubio       PG
Name: Position, Length: 450, dtype: object
```



* 대괄호 구문의 장점은 공백이 있는 열 이름을 지원하는 것 입니다.

```
nba['Player Position'] # O
nba.Player Position # X
```



### 6.2 DataFrame에서 다중 열 선택

* DataFrame에서 여러 개의 열을 추출하려면 리스트를 열 이름으로 전달하세요. 리스트 요소와 동일한 순서의 열로 구성된 DataFrame을 결과로 얻을 수 있습니다.

```python
nba[['Salary', 'Birthday']].head()
```

```
     Name        Salary	  Birthday		
Shake Milton	1445697	1996-09-26
Christian Wood	1645357	1995-09-27
PJ Washington	3831840	1998-08-23
Derrick Rose	7317074	1988-10-04
Marial Shayok	79568	1995-07-26
```



* select_dtypes 메서드를 사용하여 데이터 유형에 따라 열을 선택할 수도 있습니다.
* include 매개변수를 포함하는 유형을 나타내는 단일 문자열 또는 리스트를 받습니다.
* exclude 매개변수는 제외하는 유형을 나타내는 단일 문자열 또는 리스트를 받습니다.

```python
nba.select_dtypes(include = 'object')
```

```
     Name	        Team	    Position		
Shake Milton	Philadelphia 76ers	SG
Christian Wood	Detroit Pistons	PF
PJ Washington	Charlotte Hornets	PF
Derrick Rose	Detroit Pistons	PG
Marial Shayok	Philadelphia 76ers	G
...	...	...
Austin Rivers	Houston Rockets	PG
Harry Giles	Sacramento Kings	PF
Robin Lopez	Milwaukee Bucks	C
Collin Sexton	Cleveland Cavaliers	PG
Ricky Rubio	Phoenix Suns	PG
450 rows × 2 columns
```

```python
nba.select_dtypes(exclude = ['object', 'int'])
```

```
     Name	     Birthday
Shake Milton	1996-09-26
Christian Wood	1995-09-27
PJ Washington	1998-08-23
Derrick Rose	1988-10-04
Marial Shayok	1995-07-26
...	...
Austin Rivers	1992-08-01
Harry Giles	1998-04-22
Robin Lopez	1988-04-01
Collin Sexton	1999-01-04
Ricky Rubio	1990-10-21
450 rows × 1 columns
```



## 07. DataFrame에서 행 선택



### 7.1 인덱스 레이블로 행 추출

* loc 속성(location)은 레이블별로 행을 추출합니다

```python
nba.loc['LeBron James']
```

```
Team         Los Angeles Lakers
Position                     PF
Birthday    1984-12-30 00:00:00
Salary                 37436858
Name: LeBron James, dtype: object
```



+ 여러 행을 추출하려면 리스트를 전달하세요
+ 인덱스 레이블이 리스트에 나타나는 순서대로 행을 구성합니다.

```python
nba.loc[['Kawhi Leonard', 'Paul George']]
```

```
Name    Team	Position	Birthday	Salary				
Kawhi Leonard	Los Angeles Clippers	SF	1991-06-29	32742000
Paul George	Los Angeles Clippers	SF	1990-05-02	33005556
```



+ loc을 사용하여 인덱스 레이블 시퀀스를 추출할 수 있습니다.
+ loc 접근자는 파이썬의 리스트 슬라이싱 구문과 몇 가지 차이점이 있습니다. 예를 들어 loc 접근자는 상한에 있는 레이블을 범위에 포함하는 반면에 파이썬의 리스트 슬라이싱 구문은 상한에 있는 값을 범위에 제외합니다

```python
nba.sort_index().loc['Otto Porter':'Patrick Beverley']
```

```
Name Team	Position	Birthday	Salary				
Otto Porter	Chicago Bulls	SF	1993-06-03	27250576
PJ Dozier	Denver Nuggets	PG	1996-10-25	79568
PJ Washington	Charlotte Hornets	PF	1998-08-23	3831840
Pascal Siakam	Toronto Raptors	PF	1994-04-02	2351838
Pat Connaughton	Milwaukee Bucks	SG	1993-01-06	1723050
Patrick Beverley	Los Angeles Clippers	PG	1988-07-12	12345680
```

```python
players = ['Otto Porter', 'PJ Dozier', 'PJ Washington']
players[0:2]
```

```
['Otto Porter', 'PJ Dozier']
```



* loc을 사용하여 DataFrame의 중간에서 끝까지 행을 가져올 수 있습니다

```python
nba.sort_index().loc['Zach Collins':]
```

```
Name Team	Position	Birthday	Salary				
Zach Collins	Portland Trail Blazers	C	1997-11-19	4240200
Zach LaVine	Chicago Bulls	PG	1995-03-10	19500000
Zach Norvell	Los Angeles Lakers	SG	1997-12-09	79568
Zhaire Smith	Philadelphia 76ers	SG	1999-06-04	3058800
Zion Williamson	New Orleans Pelicans	F	2000-07-06	9757440
Zylan Cheatham	New Orleans Pelicans	SF	1995-11-17	79568
```



* 반대로 loc 슬라이싱을 사용하여 DataFrame의 시작 부분에서 특정 인덱스 레이블까지 행을 가져올 수 있습니다

```python
nba.sort_index().loc[:'Al Horford']
```

```
Name Team	Position	Birthday	Salary			
Aaron Gordon	Orlando Magic	PF	1995-09-16	19863636
Aaron Holiday	Indiana Pacers	PG	1996-09-30	2239200
Abdel Nader	Oklahoma City Thunder	SF	1993-09-25	1618520
Adam Mokoka	Chicago Bulls	G	1998-07-18	79568
Admiral Schofield	Washington Wizards	SF	1997-03-30	1000000
Al Horford	Philadelphia 76ers	C	1986-06-03	28000000
```



### 7.2 인덱스 위치로 행 추출

* iloc(index location) 접근자는 인덱스 위치별로 행을 추출합니다

```python
nba.iloc[300]
```

```
Team             Denver Nuggets
Position                     PF
Birthday    1999-04-03 00:00:00
Salary                  1416852
Name: Jarred Vanderbilt, dtype: object
```



* iloc 접근자는 또한 여러 레코드를 담은 인덱스 위치 리스트도 허용합니다

```python
nba.iloc[[100, 200, 300, 400]]
```

```
Name Team	Position	Birthday	Salary			
Brian Bowen	Indiana Pacers	SG	1998-10-02	79568
Marco Belinelli	San Antonio Spurs	SF	1986-03-25	5846154
Jarred Vanderbilt	Denver Nuggets	PF	1999-04-03	1416852
Louis King	Detroit Pistons	F	1999-04-06	79568
```



* iloc 접근자와 리스트 슬라이싱 구문을 함께 사용할 수도 있습니다. 그러나 판다스는 콜론 뒤의 인덱스 위치를 범위에서 제외합니다

```python
nba.iloc[400:404]
```

```
Name Team	Position	Birthday	Salary			
Louis King	Detroit Pistons	F	1999-04-06	79568
Kostas Antetokounmpo	Los Angeles Lakers	PF	1997-11-20	79568
Rodions Kurucs	Brooklyn Nets	PF	1998-02-05	1699236
Spencer Dinwiddie	Brooklyn Nets	PG	1993-04-06	10605600
```



* DataFrame의 시작 부분에서부터 행을 가져오려면 콜론 앞의 숫자를 생략합니다

```python
nba.iloc[:2]
```

```
Name Team	Position	Birthday	Salary				
Shake Milton	Philadelphia 76ers	SG	1996-09-26	1445697
Christian Wood	Detroit Pistons	PF	1995-09-27	1645357
```



* 콜론 뒤의 숫자를 제거하여 DataFrame의 끝까지 행을 가져올 수 있습니다

```python
nba.iloc[447:]
```

```
Name Team	Position	Birthday	Salary			
Robin Lopez	Milwaukee Bucks	C	1988-04-01	4767000
Collin Sexton	Cleveland Cavaliers	PG	1999-01-04	4764960
Ricky Rubio	Phoenix Suns	PG	1990-10-21	16200000
```



* 값 중 하나 또는 두 값 모두에 음수를 사용할 수도 있습니다. 다음 예에서는 마지막에서 10번째 행부터 마지막 6번 째 행까지(범위에 포함하지 않음) 추출합니다

```python
nba.iloc[-10:-6]
```

```
Name Team	Position	Birthday	Salary				
Jared Dudley	Los Angeles Lakers	PF	1985-07-10	2564753
Max Strus	Chicago Bulls	SG	1996-03-28	79568
Kevon Looney	Golden State Warriors	C	1996-02-06	4464286
Willy Hernangomez	Charlotte Hornets	C	1994-05-27	1557250
```



* 대괄호 안에 세 번째 숫자를 넣어 인접한 모든 인덱스 위치의 간격이 동일하도록 단계 시퀀스를 지정할 수 있습니다. 인덱스 위치가 0, 2, 4, 6, 8행이 포함됩니다

```python
nba.iloc[0:10:2]
```

```
Name	Team	Position	Birthday	Salary			
Shake Milton	Philadelphia 76ers	SG	1996-09-26	1445697
PJ Washington	Charlotte Hornets	PF	1998-08-23	3831840
Marial Shayok	Philadelphia 76ers	G	1995-07-26	79568
Kendrick Nunn	Miami Heat	SG	1995-08-03	1416852
Brook Lopez	Milwaukee Bucks	C	1988-04-01	12093024
```



### 7.3 특정 열에서 값 추출

* loc과 iloc 속성은 모두 두 번째 인수로 추출할 열을 받습니다. loc을 사용한다면 열 이름을 입력하면 됩니다. iloc을 사용한다면 열 위치를 입력하세요

```python
nba.loc['Giannis Antetokounmpo', 'Team']
```

```
'Milwaukee Bucks'
```



* 여러 개의 값을 추출하려면 loc 접근자에 하나 혹은 2개의 리스트를 전달하면 됩니다
* 판다스는 Series를 반환합니다

```python
nba.loc['James Harden', ['Position', 'Birthday']]
```

```
Position                     PG
Birthday    1989-08-26 00:00:00
Name: James Harden, dtype: object
```



* 여러 개의 행 레이블과 여러 개의 열을 전달하는 예제입니다

```python
nba.loc[
    ['Russell Westbrook', 'Anthony Davis'],
    ['Team', 'Salary']
]
```

```
Name Team	Salary	
Russell Westbrook	Houston Rockets	38506482
Anthony Davis	Los Angeles Lakers	27093019
```



* 리스트 슬라이싱 구문을 사용하면 열의 이름을 명시하지 않고도 여러 개의 열을 추출할 수 있습니다.
* 주어진 데이터셋에는 4개의 열(Team, Position, Birthday, Salary)이 있습니다. Position에서 Salary까지의 범위에 있는 모든 열을 추출하겠습니다

```python
nba.loc['Joel Embiid', 'Position':'Salary']
```

```
Position                      C
Birthday    1994-03-16 00:00:00
Salary                 27504630
Name: Joel Embiid, dtype: object
```



* DataFrame에서 보여지는 순서에 맞춰 열의 이름을 전달해야합니다 . Salary 열이 Position 열보다 뒤에 있지만 Salary를 먼저 입력하여 빈 결과가 반환됩니다.

```python
nba.loc['Joel Embiid', 'Salary':'Position']
```

```
Series([], Name: Joel Embiid, dtype: object)
```



* 열의 이름 말고 순서에 따라 추출할 열을 선택하고 싶다고 가정하겠습니다.
* nba에서 Team 열은 인덱스0, Position은 인덱스 1, 나머지 열도 같은 규칙으로 인덱스를 가집니다
* 열의 인덱스를 iloc에 두 번째 인수로 전달할 수 있습니다.

```python
nba.iloc[57,3]
```

```
796806
```



* 리스트 슬라이싱 구문도 사용할 수 있습니다

```python
nba.iloc[100:104, :3]
```

```
Name Team	Position	Birthday		
Brian Bowen	Indiana Pacers	SG	1998-10-02
Aaron Holiday	Indiana Pacers	PG	1996-09-30
Troy Daniels	Los Angeles Lakers	SG	1991-07-15
Buddy Hield	Sacramento Kings	SG	1992-12-17
```

* iloc과 loc 접근자는 매우 다양합니다. 대괄호에는 단일 값, 값 리스트, 리스트 슬라이스 등을 사용할 수 있습니다. 하지만 이러한 유연성도 단점이 있습니다. 추가 오버헤드가 필요하다는 점입니다. 판다스는 사용자가 iloc 또는 loc에 어떤 종류의 입력을 넣었는지 알아내야 합니다.



* DataFrame에서 단일 값을 추출할 때는 loc나 iloc 대신 at과 iat이라는 두가 지 속성을 사용할 수 있습니다. 판다스는 단일 값을 찾을 때 검색 알고리즘을 최적화할 수 있기 때문에 at과 iat가 loc이나 iloc보다 빠릅니다.

```python
nba.at['Austin Rivers', 'Birthday']

# Timestamp('1992-08-01 00:00:00')

nba.iat[263,1]

# 'PF'
```



* 주피터 노트북은 개발자 경험을 향상시키는  몇 가지 매직 메서드를 제공합니다. %% 접두사를 사용하여 매직 메서드를 선언할 수 있으며 일반 파이썬 코드와 함께 입력합니다. 한 가지 예를 들어 %%timit은 셀에서 코드를 실행하고 실행하는데 걸리는 평균 시간을 계산하는 매직 메서드입니다. %%timeit은 때때로 셀을 100,000번까지 실행합니다

```python
%%timeit
nba.at['Austin Rivers', 'Birthday']

# 17.7 µs ± 2.79 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
nba.loc['Austin Rivers', 'Birthday']

# 20.2 µs ± 1.21 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
nba.iat[263,1]

# 34.5 µs ± 2.07 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
nba.iloc[263,1]

# 41.3 µs ± 2.51 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```



## 08. Series에서 값 추출

* loc, iloc, at, iat 접근자는 Series 객체에서도 사용할 수 있습니다.

```python
nba['Salary'].loc['Damian Lillard']

# 29802321

nba['Salary'].at['Damian Lillard']

# 29802321

nba['Salary'].iloc[234]

# 2033160

nba['Salary'].iat[234]

# 2033160
```



## 09. 열 또는 행 이름 바꾸기

* columns 속성은 DataFrame의 열 이름을 저장하는 Index객체를 나타냅니다

```python
nba.columns
```

```
Index(['Team', 'Position', 'Birthday', 'Salary'], dtype='object')
```



* columns 속성에 열의 새 이름을 담은 리스트를 할당하여 DataFrame의 일부 또는 전체 열의 이름을 바꿀 수 있습니다. 다음은 Salary 열의 이름을 Pay로 변경하는 예제입니다

```python
nba.columns = ['Team', 'Position', 'Date of Birth', 'Pay']
nba.head(1)
```



* rename 메서드도 열의 이름을 변경할 수 있습니다. 키가 기존 열의 이름이고 값이 새 이름인 딕셔너리를 columns 매개변수에 전달합니다. 다음은 Date of Birth 열의 이름을 Birthday로 변경합니다

```python
nba.rename(columns = {'Date of Birth':'Birthday'})
```

```

Name	Team	Position	Birthday	Pay			
Shake Milton	Philadelphia 76ers	SG	1996-09-26	1445697
Christian Wood	Detroit Pistons	PF	1995-09-27	1645357
PJ Washington	Charlotte Hornets	PF	1998-08-23	3831840
Derrick Rose	Detroit Pistons	PG	1988-10-04	7317074
Marial Shayok	Philadelphia 76ers	G	1995-07-26	79568
...	...	...	...	...
Austin Rivers	Houston Rockets	PG	1992-08-01	2174310
Harry Giles	Sacramento Kings	PF	1998-04-22	2578800
Robin Lopez	Milwaukee Bucks	C	1988-04-01	4767000
Collin Sexton	Cleveland Cavaliers	PG	1999-01-04	4764960
Ricky Rubio	Phoenix Suns	PG	1990-10-21	16200000
450 rows × 4 columns
```

```
nba = nba.rename(columns = {'Date of Birth':'Birthday'})
```



* 메서드의 index 매개변수에 딕셔너리를 전달하여 인덱스 레이블의 이름을 바꿀 수도 있습니다. 이 때도 마찬가지로 딕셔너리의 키는 이전 레이블이고 값은 새 레이블입니다. 다음은 'Giannis Antetokounmpo' 를 그의 인기있는 별명인 'Greek Freak'으로 바꿉니다

```python
nba = nba.rename(
    index = {'Giannis Antetokounmpo':'Greek Freak'}
)
```

```python
nba.loc['Greek Freak']
```

```
Team            Milwaukee Bucks
Position                     PF
Birthday    1994-12-06 00:00:00
Pay                    25842697
Name: Greek Freak, dtype: object
```



## 10. 인덱스 재설정

```python
nba.set_index('Team').head()
```

```
Team Position	Birthday	Pay	
Philadelphia 76ers	SG	1996-09-26	1445697
Detroit Pistons	PF	1995-09-27	1645357
Charlotte Hornets	PF	1998-08-23	3831840
Detroit Pistons	PG	1988-10-04	7317074
Philadelphia 76ers	G	1995-07-26	79568
```



* 다른 열을 DataFrame의 인덱스로 설정하고 싶을 때가 있습니다. set_index 메서드를 호출할 수 있지만 현재인덱스로 설정해 놓은 이름을 잃게 됩니다. 선수의 이름을 보존하려면 먼저 기존 인덱스를 DataFrame의 일반열로 다시 통합해야합니다
* reset_index 메서드는 현재 인덱스를 DataFrame 열로 이동하고 인덱스를 판다스의 숫자 인덱스로 변경합니다.

```python
nba.reset_index().head()
```

```
Name	Team	Position	Birthday	Pay
0	Shake Milton	Philadelphia 76ers	SG	1996-09-26	1445697
1	Christian Wood	Detroit Pistons	PF	1995-09-27	1645357
2	PJ Washington	Charlotte Hornets	PF	1998-08-23	3831840
3	Derrick Rose	Detroit Pistons	PG	1988-10-04	7317074
4	Marial Shayok	Philadelphia 76ers	G	1995-07-26	79568
```



```python
nba.reset_index().set_index('Team').head()
```

```
Team Name	Position	Birthday	Pay			
Philadelphia 76ers	Shake Milton	SG	1996-09-26	1445697
Detroit Pistons	Christian Wood	PF	1995-09-27	1645357
Charlotte Hornets	PJ Washington	PF	1998-08-23	3831840
Detroit Pistons	Derrick Rose	PG	1988-10-04	7317074
Philadelphia 76ers	Marial Shayok	G	1995-07-26	79568
```

```
nba = nba.reset_index().set_index('Team')
```



