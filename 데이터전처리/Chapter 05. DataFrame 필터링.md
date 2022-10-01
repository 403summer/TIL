# Chapter 05. DataFrame 필터링



## 01.  데이터셋과 메모리 최적화

* 일단 데이터셋을 가져올 때마다 각 열이 데이터를 가장 최적의 유형으로 저장하는지 확인해야 합니다. 가장 적은 메모리를 사용하거나 가장 많은 유틸리티를 제공하는 데이터 유형이 최적의 데이터 유형입니다. 예를 들어 정수는 대부분의 컴퓨터에서 부동소수점 숫자보다 더 적은 메모리를 차지하기 때문에 데이터셋에 정수가 있다면 부동소수점이 아니라 정수로 데이터셋을 가져오는 것이 이상적입니다. 또 다른 예로 데이터셋에 날짜/시간 이 있다면 문자열이 아닌 날짜/시간으로 데이터셋을 가져오는 것이 좋습니다. 날짜/시간 유형은 문자열과 달리 날짜와 시간에 특화된 연산자를 제공하기 때문입니다.
* 'employees.csv'는 가상의 회사 직원 정보 데이터셋

```python
import pandas as pd
pd.read_csv('employees.csv')
```

```
  First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	8/6/93	NaN	True	Marketing
1	Thomas	Male	3/31/96	61933.0	True	NaN
2	Maria	Female	NaN	130590.0	False	Finance
3	Jerry	NaN	3/4/05	138705.0	True	Finance
4	Larry	Male	1/24/98	101004.0	True	IT
...	...	...	...	...	...	...
996	Phillip	Male	1/31/84	42392.0	False	Finance
997	Russell	Male	5/20/13	96914.0	False	Product
998	Larry	Male	4/20/13	60500.0	False	Business Dev
999	Albert	Male	5/15/12	129949.0	True	Sales
1000	NaN	NaN	NaN	NaN	NaN	NaN
1001 rows × 6 columns
```



* 문자열을 날짜/시간으로 변환하기

```python
pd.read_csv('employees.csv', parse_dates = ['Start Date']).head()
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	NaN	True	Marketing
1	Thomas	Male	1996-03-31	61933.0	True	NaN
2	Maria	Female	NaT	130590.0	False	Finance
3	Jerry	NaN	2005-03-04	138705.0	True	Finance
4	Larry	Male	1998-01-24	101004.0	True	IT
```

```python
employees = pd.read_csv('employees.csv', parse_dates = ['Start Date'])
```



* 메모리 사용량 확인

```python
employees.info()
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1001 entries, 0 to 1000
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype         
---  ------      --------------  -----         
 0   First Name  933 non-null    object        
 1   Gender      854 non-null    object        
 2   Start Date  999 non-null    datetime64[ns]
 3   Salary      999 non-null    float64       
 4   Mgmt        933 non-null    object        
 5   Team        957 non-null    object        
dtypes: datetime64[ns](1), float64(1), object(4)
memory usage: 47.0+ KB
```



### 1.1 astype 메서드를 사용하여 데이터 유형 변환

* 판다스가 관리자 여부(Mgmt) 열의 값을 문자열로 가지고 있습니다. 열은 True와 False의 두 가지 값만 저장합니다.

* astype 메서드는 Series의 값을 다른 데이터 유형으로 변환합니다. 이 메서드는 새로운 데이터 유형을 받아오는 하나의 인수를 가집니다. 데이터 유형 또는 유형의 이름을 나타내는 문자열을 전달할 수 있습니다.

```python
employees['Mgmt'].astype(bool)
```

```
0        True
1        True
2       False
3        True
4        True
        ...  
996     False
997     False
998     False
999      True
1000     True
Name: Mgmt, Length: 1001, dtype: bool
```



* employees의 기존 Mgmt 열을 덮어 쓰겠습니다. DataFrame의 열 업데이트는 딕셔너리에서 키-값 쌍을 설정하는 것과 유하하게 작동합니다. 지정된 이름의 열이 존재하는 경우 판다스는 이를 새 Series로 덮어씁니다. 지정된 이름의 열이 존재하지 않으면 판다스는 새 Series를 생성하고 DataFrame의 오른쪽에 추가합니다. 라이브러리는 공통 인덱스 레이블로 Series와 DataFrame의 행을 연결합니다.
* 파이썬은 할당 연산다(=)의 오른쪽을 먼저 평가합니다. 따라서 아래 코드는 먼저 새 Series를 만든 다음 기존 Mgmt 열을 덮어씁니다.

```python
employees['Mgmt'] = employees['Mgmt'].astype(bool)
employees.tail()
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
996	Phillip	Male	1984-01-31	42392.0	False	Finance
997	Russell	Male	2013-05-20	96914.0	False	Product
998	Larry	Male	2013-04-20	60500.0	False	Business Dev
999	Albert	Male	2012-05-15	129949.0	True	Sales
1000	NaN	NaN	NaT	NaN	True	NaN
```



* 메모리 사용량이 줄은 것은 확인할 수 있다

```python
employees.info()
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1001 entries, 0 to 1000
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype         
---  ------      --------------  -----         
 0   First Name  933 non-null    object        
 1   Gender      854 non-null    object        
 2   Start Date  999 non-null    datetime64[ns]
 3   Salary      999 non-null    float64       
 4   Mgmt        1001 non-null   bool          
 5   Team        957 non-null    object        
dtypes: bool(1), datetime64[ns](1), float64(1), object(3)
memory usage: 40.2+ KB
```



* 원본 csv 파일을 열면 연봉(Salary) 열의 값이 정수로 저장되어 있다. 그러나 판다스는 Salary열의 값을 부동소수점으로 저장합니다. 판다스는 열에 있는 NaN값을 처리하기 위해 부동소수점으로 변환하기 떄문입니다.

```python
employees['Salary'].astype(int)
```

```
IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer
```



* 판다스는 NaN 값을 정수로 변환할 수 없습니다. 이때 NaN 값을 상수 값으로 대체하면 이 문제를 해결할 수 있습니다.
* fillna 메서드는 Series의 null 값을 사용자가 전달한 인수로 대체합니다.
* 다음은 인수 0을 전달하는 예제입니다. 여기서 0은 Salary 열의 null 값이 치환되는 점을 보여주기 위해 선택한 값으로 이번 예제에서만 유효합니다. fillna를 사용할 때 임의의 값을 선택하여 null 값을 대체하면 데이터가 왜곡될 수 있습니다.

```python
employees['Salary'].fillna(0).tail()
```

```
996      42392.0
997      96914.0
998      60500.0
999     129949.0
1000         0.0
Name: Salary, dtype: float64
```

```python
employees['Salary'].fillna(0).astype(int).tail()
```

```
996      42392
997      96914
998      60500
999     129949
1000         0
Name: Salary, dtype: int32
```

```python
employees['Salary'] = employees['Salary'].fillna(0).astype(int)
```



* 판다스에는 범주형(category)이라는 특별한 데이터 유형이 있습니다. 이 유형은 전체 개수에 비해 소수의 고유값으로 구성된 열에 적용하기 좋습니다. 일상에서 흔히 접할 수 있는 성별, 요일, 혈액형, 행성이나 소득층과 같이 값이 제한적인 데이터를 예로 들 수 있습니다. 판다스는 전체 행에 걸쳐 중복된 내용을 저장하지 않고 각 범주 값의 복사본 하나만 저장합니다.
* nunique 메서드는 DataFrame 열의 고유한 값의 개수를 나타냅니다. 결측값(NaN)은 기본적으로 제외하고 개수를 셉니다

```python
employees.nunique()
```

```
First Name    200
Gender          2
Start Date    971
Salary        995
Mgmt            2
Team           10
dtype: int64
```

* 성별(Gender)과 팀(Team) 열은 범주형 값을 저장하기에 적합한 후보입니다

```python
employees['Gender'].astype('category')
```

```
0         Male
1         Male
2       Female
3          NaN
4         Male
         ...  
996       Male
997       Male
998       Male
999       Male
1000       NaN
Name: Gender, Length: 1001, dtype: category
Categories (2, object): ['Female', 'Male']
```

```python
employees['Gender'] = employees['Gender'].astype('category')
```



* 메모리 확인

```python
employees.info()
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1001 entries, 0 to 1000
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype         
---  ------      --------------  -----         
 0   First Name  933 non-null    object        
 1   Gender      854 non-null    category      
 2   Start Date  999 non-null    datetime64[ns]
 3   Salary      1001 non-null   int32         
 4   Mgmt        1001 non-null   bool          
 5   Team        957 non-null    object        
dtypes: bool(1), category(1), datetime64[ns](1), int32(1), object(2)
memory usage: 29.6+ KB
```



```python
employees['Team'] = employees['Team'].astype('category')
```

```python
employees.info()
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1001 entries, 0 to 1000
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype         
---  ------      --------------  -----         
 0   First Name  933 non-null    object        
 1   Gender      854 non-null    category      
 2   Start Date  999 non-null    datetime64[ns]
 3   Salary      1001 non-null   int32         
 4   Mgmt        1001 non-null   bool          
 5   Team        957 non-null    category      
dtypes: bool(1), category(2), datetime64[ns](1), int32(1), object(1)
memory usage: 23.1+ KB
```

* 메모리 사용량을 50% 이상 줄였습니다



## 02. 단일 조건으로 필터링

* 등호 연산자(==)는 파이썬에서 두 객체를 비교하여 같으면 True,  같지 않으면 False를 반환합니다.

```python
'Maria' == 'Maria'

# True

'Maria' == 'Taylor'

# False
```



* 모든 Series 항목을 상수 값과 비교하기 위해 Series를 등호 연산자의 한 쪽에 배치하고 상수 값을 다른 쪽에 배치합니다.

```python
Series == value
```

* 이 구문에 오류가 있다고 생각할 수 있지만, 판다스는 Series 자체가 아니라 각 Series 값을 지정된 문자열과 비교해야한다는 점을 눈치챌 만큼 충분히 똑똑합니다. 2장에서 Series에 더하기 기호와 같은 수학 연산자를 적용했던 것과 비슷하게 작동합니다



* Series를 등호 연산자와 결합하면 판다스는  불리언 Series를 반환합니다.

```python
employees['First Name'] == 'Maria'
```

```
0       False
1       False
2        True
3       False
4       False
        ...  
996     False
997     False
998     False
999     False
1000    False
Name: First Name, Length: 1001, dtype: bool
```



* 위 결과에서 True 값의 행을 employees DataFrame에서 추출할 수 있다면 데이터셋에 있는 'Maria' 레코드를 모두 추출할 수 있습니다. DataFrame 옆에 대괄호를 사용하고 그 사이에 불리언 Series를 넣으면 행을 필터링 할 수 있습니다.

```python
employees[employees['First Name'] == 'Maria']
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
2	Maria	Female	NaT	130590	False	Finance
198	Maria	Female	1990-12-27	36067	True	Product
815	Maria	NaN	1986-01-18	106562	False	HR
844	Maria	NaN	1985-06-19	148857	False	Legal
936	Maria	Female	2003-03-14	96250	False	Business Dev
984	Maria	Female	2011-10-15	43455	False	Engineering
```



* 대괄호를 중첩해서 사용하는 것이 혼란스럽다면 먼저 불리언 Series를 별도의 변수에 할당하고 해당 변수를  DataFrame 옆에 있는 대괄호에 넣으면 됩니다.

```python
marias = employees['First Name'] == 'Maria'
employees[marias]
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
2	Maria	Female	NaT	130590	False	Finance
198	Maria	Female	1990-12-27	36067	True	Product
815	Maria	NaN	1986-01-18	106562	False	HR
844	Maria	NaN	1985-06-19	148857	False	Legal
936	Maria	Female	2003-03-14	96250	False	Business Dev
984	Maria	Female	2011-10-15	43455	False	Engineering
```

* 값의 같음을 비교할 때 초보자가 저지르는 가장 흔한 실수는 등호를 2개가 아닌 하나를 사용하는 것 입니다. 등호를 하나만 쓰면 객체를 변수에 할당하고 2개 쓰면 객체가 같은지 비교합니다.



* 부등호 연산자는 두 값이 같지 않으면 True를 반환하고 같으면 False를 반환합니다

```python
'Finance' != 'Engineering'
```

```
True
```

```python
employees['Team'] != 'Finance'
```

```
0        True
1        True
2       False
3       False
4        True
        ...  
996     False
997      True
998      True
999      True
1000     True
Name: Team, Length: 1001, dtype: bool
```

```python
employees[employees['Team'] != 'Finance']
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	0	True	Marketing
1	Thomas	Male	1996-03-31	61933	True	NaN
4	Larry	Male	1998-01-24	101004	True	IT
5	Dennis	Male	1987-04-18	115163	False	Legal
6	Ruby	Female	1987-08-17	65476	True	Product
...	...	...	...	...	...	...
995	Henry	NaN	2014-11-23	132483	False	Distribution
997	Russell	Male	2013-05-20	96914	False	Product
998	Larry	Male	2013-04-20	60500	False	Business Dev
999	Albert	Male	2012-05-15	129949	True	Sales
1000	NaN	NaN	NaT	0	True	NaN
899 rows × 6 columns
```

* 누락된 값이 있는 행도 결과에 포함됩니다. 판다스는 NaN이 'Finance' 문자열과 같지 않다고 간주합니다



* 기업의 모든 관리자를 검색하려면 어떻게 해야 할까요? 관리자는 관리자 여부(Mgmt) 열에 True 값을 가집니다. employees['Mgmt'] == True를 사용할 수도 있지만 Mgmt는 이미 불리언 Series이기 때문에 그럴 필요가 없습니다. True 값과 False 값으로 판다스가 행을 유지해야 하는지 아니면 버려야 하는지 여부를 알 수 있기 때문입니다. 따라서 대괄호 안에 Mgmt 열을  바로 넣을 수 있습니다.

```python
employees[employees['Mgmt']].head()
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	0	True	Marketing
1	Thomas	Male	1996-03-31	61933	True	NaN
3	Jerry	NaN	2005-03-04	138705	True	Finance
4	Larry	Male	1998-01-24	101004	True	IT
6	Ruby	Female	1987-08-17	65476	True	Product
```



* 어떤 직원이 $ 100,000 이상의 연봉을 받는지 확인해봅시다.

```python
high_earners = employees['Salary'] > 100000
high_earners
```

```
0       False
1       False
2        True
3        True
4        True
        ...  
996     False
997     False
998     False
999      True
1000    False
Name: Salary, Length: 1001, dtype: bool
```

```python
employees[high_earners].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
2	Maria	Female	NaT	130590	False	Finance
3	Jerry	NaN	2005-03-04	138705	True	Finance
4	Larry	Male	1998-01-24	101004	True	IT
5	Dennis	Male	1987-04-18	115163	False	Legal
9	Frances	Female	2002-08-08	139852	True	Business Dev
```



## 03. 다중 조건으로 필터링



### 3.1 AND 조건

* 비즈니스 개발 팀에서 일하는 모든 여성 직원을 찾아보자
* 앰퍼샌드(&)는 AND 논리를 나타냅니다

| 조건 1 | 조건 2 | 평가  |
| :----: | :----: | :---: |
|  True  |  True  | True  |
|  True  | False  | False |
| False  |  True  | False |
| False  | False  | False |

```python
is_female =  employees['Gender'] == 'Female'
in_biz_dev = employees['Team'] == 'Business Dev'
employees[is_female & in_biz_dev].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
9	Frances	Female	2002-08-08	139852	True	Business Dev
33	Jean	Female	1993-12-18	119082	False	Business Dev
36	Rachel	Female	2009-02-16	142032	False	Business Dev
38	Stephanie	Female	1986-09-13	36844	True	Business Dev
61	Denise	Female	2001-11-06	106862	False	Business Dev
```



* 비지니스 개발 팀의 여성 관리자를 찾아보자

```python
is_manager = employees['Mgmt']
employees[is_female & in_biz_dev & is_manager].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
9	Frances	Female	2002-08-08	139852	True	Business Dev
38	Stephanie	Female	1986-09-13	36844	True	Business Dev
66	Nancy	Female	2012-12-15	125250	True	Business Dev
92	Linda	Female	2000-05-25	119009	True	Business Dev
111	Bonnie	Female	1999-12-17	42153	True	Business Dev
```



### 3.2 OR 조건

* 모든 조건이 참일 필요는 없지만 적어도 하나는 참이어야 합니다

| 조건 1 | 조건 2 | 평가  |
| :----: | :----: | :---: |
|  True  |  True  | True  |
|  True  | False  | True  |
| False  |  True  | True  |
| False  | False  | False |



* 연봉(Salary)이 $40,000 미만이거나 입사일(Start Date)이 2015년 1월 1일 이후인 모든 직원을 찾아보자
* 파이프(|)기호를 사용하여 OR 논리를 적용합니다.

```python
earning_below_40k = employees['Salary'] < 40000
started_after_2015 = employees['Start Date'] > '2015-01-01'
employees[earning_below_40k | started_after_2015].tail()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
958	Gloria	Female	1987-10-24	39833	False	Engineering
964	Bruce	Male	1980-05-07	35802	True	Sales
967	Thomas	Male	2016-03-12	105681	False	Engineering
989	Justin	NaN	1991-02-10	38344	False	Legal
1000	NaN	NaN	NaT	0	True	NaN
```



### 3.3 ~ 기호로 반전

* 물결표(~) 기호는 불리언 Series의 값을 반전시킵니다. 모든 True 값은 False가 되고 모든 False 값은 True가 됩니다.

```python
my_series = pd.Series([True, False, True])
my_series
```

```
0     True
1    False
2     True
dtype: bool
```

```python
~my_series
```

```
0    False
1     True
2    False
dtype: bool
```



* 연봉이 $100,000 미만인 직원을 찾는다고 하면 두 가지 방법이 있다

```python
employees[employees['Salary'] < 100000].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	0	True	Marketing
1	Thomas	Male	1996-03-31	61933	True	NaN
6	Ruby	Female	1987-08-17	65476	True	Product
7	NaN	Female	2015-07-20	45906	True	Finance
8	Angela	Female	2005-11-22	95570	True	Engineering
```



```python
employees[~(employees['Salary'] >= 100000)].head()
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	0	True	Marketing
1	Thomas	Male	1996-03-31	61933	True	NaN
6	Ruby	Female	1987-08-17	65476	True	Product
7	NaN	Female	2015-07-20	45906	True	Finance
8	Angela	Female	2005-11-22	95570	True	Engineering
```



### 3.4 불리언 메서드

* 판다스는 연산자보다 메서드를 선호하는 분석가를 위해 또 다른 필터링 구문을 제공합니다

|   연산자    |            산술 구문             |            메서드 구문            |
| :---------: | :------------------------------: | :-------------------------------: |
|    등호     | employees['Team'] == 'Marketing' | employees['Team'].eq('Marketing') |
|   부등호    | employees['Team'] != 'Marketing' | employees['Team'].ne('Marketing') |
|    작음     |   employees['Salary'] < 100000   |  employees['Salary'].lt(100000)   |
| 작거나 같음 |  employees['Salary'] <= 100000   |  employees['Salary'].le(100000)   |
|     큼      |   employees['Salary'] > 100000   |  employees['Salary'].gt(100000)   |
| 크거나 같음 |  employees['Salary'] >= 100000   |  employees['Salary'].ge(100000)   |



## 04. 조건별 필터링

* 일부 필터링 작업은 단순하게 같거나 다름을 비교하는 것보다 더 복잡합니다



### 4.1 isin 메서드

* 영업, 법률, 마케팅팀에 속하는 직원을 추출해보자

```python
sales = employees['Team'] == 'Sales'
legal = employees['Team'] == 'Legal'
mktg = employees['Team'] == 'Marketing'
employees[sales | legal | mktg].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	0	True	Marketing
5	Dennis	Male	1987-04-18	115163	False	Legal
11	Julie	Female	1997-10-26	102508	True	Legal
13	Gary	Male	2008-01-27	109831	False	Sales
20	Lois	NaN	1995-04-22	64714	True	Legal
```



* 만약 3개 팀이 아니라 더 많은 팀을 추출한다면 일일히 위와 같이 선언하기는 어렵다
* isin 메서드에 반복가능한 요소(리스트, 튜플, Series 등)를 인수로 넣어 불리언 Series를 반환받을 수 있다. 반환하는 Series에서 True는 반복 가능한 요소의 값 중에서 행의 값을 찾았음을 나타내고 False는 찾지 못했음을 나타냅니다.

```python
all_star_teams = ['Sales', 'Legal', 'Marketing']
on_all_star_teams = employees['Team'].isin(all_star_teams)
employees[on_all_star_teams].head()
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	0	True	Marketing
5	Dennis	Male	1987-04-18	115163	False	Legal
11	Julie	Female	1997-10-26	102508	True	Legal
13	Gary	Male	2008-01-27	109831	False	Sales
20	Lois	NaN	1995-04-22	64714	True	Legal
```



### 4.2 between 메서드

* 숫자나 날짜를 다룰 때 범위에 속하는 값을 구해야하는 일이 많습니다. $80,000에서 $90,000 사이의 연봉을 받는 직원을 추출해봅시다

```python
higher_than_80 = employees['Salary'] >= 80000
lower_than_90 = employees['Salary'] < 90000
employees[higher_than_80 & lower_than_90].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
19	Donna	Female	2010-07-22	81014	False	Product
31	Joyce	NaN	2005-02-20	88657	False	Product
35	Theresa	Female	2006-10-10	85182	False	Sales
45	Roger	Male	1980-04-17	88010	True	Sales
54	Sara	Female	2007-08-15	83677	False	Engineering
```



* 하한과 상항을 인수로 받아 불리언 Series를 반환하는 between 메서드를 사용해보자

```python
between_80k_and_90k = employees['Salary'].between(80000, 90000)
employees[between_80k_and_90k].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
19	Donna	Female	2010-07-22	81014	False	Product
31	Joyce	NaN	2005-02-20	88657	False	Product
35	Theresa	Female	2006-10-10	85182	False	Sales
45	Roger	Male	1980-04-17	88010	True	Sales
54	Sara	Female	2007-08-15	83677	False	Engineering
```



* 메서드의 첫 번째 및 두 번째 인수에 대한 키워드 매개변수는 각각 left와 right입니다
* 1980년대에 기업에 입사한 직원을 찾아봅시다

```python
eighties_folk = employees['Start Date'].between(
    left = '1980-01-01',
    right = '1990-01-01'
)
employees[eighties_folk].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
5	Dennis	Male	1987-04-18	115163	False	Legal
6	Ruby	Female	1987-08-17	65476	True	Product
10	Louise	Female	1980-08-12	63241	True	NaN
12	Brandon	Male	1980-12-01	112807	True	HR
17	Shawn	Male	1986-12-07	111737	False	Product
```



* 이름이 문자'R'로 시작하는 직원을 필터링 해보자. R을 하한으로 지정하여 범위에 포함하고 S로 상한으로 지정하여 범위에서 제외합니다

```python
name_start_with_r = employees['First Name'].between('R', 'S')
employees[name_start_with_r].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
6	Ruby	Female	1987-08-17	65476	True	Product
36	Rachel	Female	2009-02-16	142032	False	Business Dev
45	Roger	Male	1980-04-17	88010	True	Sales
67	Rachel	Female	1999-08-16	51178	True	Finance
78	Robin	Female	1983-06-04	114797	True	Sales
```



### 4.3 isnull과 notnull 메서드

* 직원 데이터에 결측값이 많습니다
* NaN(not a number), NaT(not a time)

```python
employees.head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	0	True	Marketing
1	Thomas	Male	1996-03-31	61933	True	NaN
2	Maria	Female	NaT	130590	False	Finance
3	Jerry	NaN	2005-03-04	138705	True	Finance
4	Larry	Male	1998-01-24	101004	True	IT
```



* isnull 메서드는 행의 값이 누락되면 True 값을 가지는 불리언 Series를 반환합니다

```python
employees['Team'].isnull().head()
```

```
0    False
1     True
2    False
3    False
4    False
Name: Team, dtype: bool
```



* 판다스는 NaT와 None 값도 null로 간주합니다

```python
employees['Start Date'].isnull().head()
```

```
0    False
1    False
2     True
3    False
4    False
Name: Start Date, dtype: bool
```



* notnull 메서드는 반대의 Series를 반환하며 여기서 True는 행의 값이 있음을 나타냅니다

```python
employees['Team'].notnull().head()
```

```
0     True
1    False
2     True
3     True
4     True
Name: Team, dtype: bool
```



* isnull 메서드에서 반환된 Series를 반전하면 notnull 메서드와 동일한 결과 집합을 생성할 수 있습니다.

```python
(~employees['Team'].isnull()).head()
```

```
0     True
1    False
2     True
3     True
4     True
Name: Team, dtype: bool
```

* notnull이 좀 더 명시적이기 때문에 Series를 반전시키기 보다는 notnull 메서드를 사용하는 것을 권장합니다



* Team 열의 값이 누락된 직원을 호출해보자

```python
no_team = employees['Team'].isnull()
employees[no_team].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
1	Thomas	Male	1996-03-31	61933	True	NaN
10	Louise	Female	1980-08-12	63241	True	NaN
23	NaN	Male	2012-06-14	125792	True	NaN
32	NaN	Male	1998-08-21	122340	True	NaN
91	James	NaN	2005-01-26	128771	False	NaN
```



* First Name 열의 값이 존재하는 직원을 추출하는 예제입니다

```python
has_name = employees['First Name'].notnull()
employees[has_name].head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	0	True	Marketing
1	Thomas	Male	1996-03-31	61933	True	NaN
2	Maria	Female	NaT	130590	False	Finance
3	Jerry	NaN	2005-03-04	138705	True	Finance
4	Larry	Male	1998-01-24	101004	True	IT
```

* isnull 및 notnull 메서드는 하나 이상의 행에서 값이 존재하는 또는 누락된 경우를 필터링하는 가장 좋은 방법입니다



### 4.4 null 값 다루기

```python
employees = pd.read_csv('employees.csv', parse_dates = ['Start Date'])
employees
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	NaN	True	Marketing
1	Thomas	Male	1996-03-31	61933.0	True	NaN
2	Maria	Female	NaT	130590.0	False	Finance
3	Jerry	NaN	2005-03-04	138705.0	True	Finance
4	Larry	Male	1998-01-24	101004.0	True	IT
...	...	...	...	...	...	...
996	Phillip	Male	1984-01-31	42392.0	False	Finance
997	Russell	Male	2013-05-20	96914.0	False	Product
998	Larry	Male	2013-04-20	60500.0	False	Business Dev
999	Albert	Male	2012-05-15	129949.0	True	Sales
1000	NaN	NaN	NaT	NaN	NaN	NaN
1001 rows × 6 columns
```



* dropna 메서드는 값이 NaN인 DataFrame 행을 제거합니다. 행에 NaN 값이 하나라도 있다면 해당 행을 제거합니다.

```python
employees.dropna()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
4	Larry	Male	1998-01-24	101004.0	True	IT
5	Dennis	Male	1987-04-18	115163.0	False	Legal
6	Ruby	Female	1987-08-17	65476.0	True	Product
8	Angela	Female	2005-11-22	95570.0	True	Engineering
9	Frances	Female	2002-08-08	139852.0	True	Business Dev
...	...	...	...	...	...	...
994	George	Male	2013-06-21	98874.0	True	Marketing
996	Phillip	Male	1984-01-31	42392.0	False	Finance
997	Russell	Male	2013-05-20	96914.0	False	Product
998	Larry	Male	2013-04-20	60500.0	False	Business Dev
999	Albert	Male	2012-05-15	129949.0	True	Sales
761 rows × 6 columns
```



* 모든 값이 누락된 행을 제거하고 싶다면 how 매개변수에 인수로 'all'을 전달합니다. 데이터셋에서 마지막 행 하나만 이 조건을 만족합니다

```python
employees.dropna(how = 'all').tail()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
995	Henry	NaN	2014-11-23	132483.0	False	Distribution
996	Phillip	Male	1984-01-31	42392.0	False	Finance
997	Russell	Male	2013-05-20	96914.0	False	Product
998	Larry	Male	2013-04-20	60500.0	False	Business Dev
999	Albert	Male	2012-05-15	129949.0	True	Sales
```



* how 매개변수의 기본 인수는 'any' 입니다. 'any'를 인수로 넘기면 행의 값 중 하나라도 없을때 해당 행을 제거합니다. 995의 행은 Gender 열의 값이 NaN입니다

```python
employees.dropna(how = 'any').tail()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
994	George	Male	2013-06-21	98874.0	True	Marketing
996	Phillip	Male	1984-01-31	42392.0	False	Finance
997	Russell	Male	2013-05-20	96914.0	False	Product
998	Larry	Male	2013-04-20	60500.0	False	Business Dev
999	Albert	Male	2012-05-15	129949.0	True	Sales
```



* 특정 열에 결측값이 있는 행을 지정하여 제거하려면 subset 매개변수를 사용하세요

```python
employees.dropna(subset = ['Gender']).tail()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
994	George	Male	2013-06-21	98874.0	True	Marketing
996	Phillip	Male	1984-01-31	42392.0	False	Finance
997	Russell	Male	2013-05-20	96914.0	False	Product
998	Larry	Male	2013-04-20	60500.0	False	Business Dev
999	Albert	Male	2012-05-15	129949.0	True	Sales
```



* 열의 목록을 subset 매개변수에 전달할 수도 있습니다

```python
employees.dropna(subset = ['Start Date', 'Salary']).head()
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
1	Thomas	Male	1996-03-31	61933.0	True	NaN
3	Jerry	NaN	2005-03-04	138705.0	True	Finance
4	Larry	Male	1998-01-24	101004.0	True	IT
5	Dennis	Male	1987-04-18	115163.0	False	Legal
6	Ruby	Female	1987-08-17	65476.0	True	Product
```



* thresh 매개변수는 판다스가 행을 유지하는 조건으로 행이 최소 몇 개의 null이 아닌 값을 가져야 하는지 결정하는 임계값을 의미합니다.

```python
employees.dropna(how = 'any', thresh = 4).head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	NaN	True	Marketing
1	Thomas	Male	1996-03-31	61933.0	True	NaN
2	Maria	Female	NaT	130590.0	False	Finance
3	Jerry	NaN	2005-03-04	138705.0	True	Finance
4	Larry	Male	1998-01-24	101004.0	True	IT
```



## 05. 중복 처리



### 5.1 duplicated 메서드

```python
employees['Team'].head()
```

```
0    Marketing
1          NaN
2      Finance
3      Finance
4           IT
Name: Team, dtype: object
```



* duplicated 메서드는 열에서 중복값을 식별하는 불리언 Series를 반환합니다. 판다스는 Series를 순회하며 이전에 한번이라도 본 적이 있는 값이라면 True를 반환합니다.

```python
employees['Team'].duplicated().head()
```

```
0    False
1    False
2    False
3     True
4    False
Name: Team, dtype: bool
```



* keep 매개변수는 유지할 중복값의 위치를 나타냅니다. 기본 인수인 'first'는 중복값이 첫 번째로 나타난 인덱스를 False로 표시하여 값을 유지합니다. 다음 예제는 이전 예제와 동일한 결과를 출력합니다

```python
employees['Team'].duplicated(keep = 'first').head()
```

```
0    False
1    False
2    False
3     True
4    False
Name: Team, dtype: bool
```



* 판다스가 열에서 마지막으로 나타나는 값을 중복되지 않은 것으로 표시하도록 요청할 수도 있습니다. keep 매개변수에 'last' 문자열을 전달합니다

```python
employees['Team'].duplicated(keep = 'last')
```

```
0        True
1        True
2        True
3        True
4        True
        ...  
996     False
997     False
998     False
999     False
1000    False
Name: Team, Length: 1001, dtype: bool
```



* 각 팀에서 한 명의 직원을 추출해보자. 단, True가 그 한명이 되도록 반환하자

```python
(~employees['Team'].duplicated()).head()
```

```
0     True
1     True
2     True
3    False
4     True
Name: Team, dtype: bool
```

```python
first_one_in_team = ~employees['Team'].duplicated()
employees[first_one_in_team]
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	NaN	True	Marketing
1	Thomas	Male	1996-03-31	61933.0	True	NaN
2	Maria	Female	NaT	130590.0	False	Finance
4	Larry	Male	1998-01-24	101004.0	True	IT
5	Dennis	Male	1987-04-18	115163.0	False	Legal
6	Ruby	Female	1987-08-17	65476.0	True	Product
8	Angela	Female	2005-11-22	95570.0	True	Engineering
9	Frances	Female	2002-08-08	139852.0	True	Business Dev
12	Brandon	Male	1980-12-01	112807.0	True	HR
13	Gary	Male	2008-01-27	109831.0	False	Sales
40	Michael	Male	2008-10-10	99283.0	True	Distribution
```



### 5.2 drop_duplicated 메서드

* drop_duplicated 메서드는 중복 제거 작업을 편리하게 수행할 수 있는 메서드입니다. 기본적으로 이 메서드는 행의 모든 값이 일치하는 행을 제거합니다. employees에는 6개 열의 값이 모두 동일한 행이 없기 때문에 메서드를 단순히 호출하는 것은 의미가 없습니다.

```python
employees.drop_duplicates()
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	NaN	True	Marketing
1	Thomas	Male	1996-03-31	61933.0	True	NaN
2	Maria	Female	NaT	130590.0	False	Finance
3	Jerry	NaN	2005-03-04	138705.0	True	Finance
4	Larry	Male	1998-01-24	101004.0	True	IT
...	...	...	...	...	...	...
996	Phillip	Male	1984-01-31	42392.0	False	Finance
997	Russell	Male	2013-05-20	96914.0	False	Product
998	Larry	Male	2013-04-20	60500.0	False	Business Dev
999	Albert	Male	2012-05-15	129949.0	True	Sales
1000	NaN	NaN	NaT	NaN	NaN	NaN
1001 rows × 6 columns
```



* 하지만 subset 매개변수에 고유값을 가져야하는  열 목록을 전달하면 특정 열에 대한 중복을 제거할 수 있습니다. 다음은 Team 열에서 각 고유값의 첫번째 항목을 찾는 예제입니다. 여기서 판다스는 Team 열의값이 처음 나타나는 위치의 행만 유지합니다. 첫 번째 값 이후에 나타나는 모든 중복 행은 제거합니다.

```python
employees.drop_duplicates(subset = ['Team'])
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	NaN	True	Marketing
1	Thomas	Male	1996-03-31	61933.0	True	NaN
2	Maria	Female	NaT	130590.0	False	Finance
4	Larry	Male	1998-01-24	101004.0	True	IT
5	Dennis	Male	1987-04-18	115163.0	False	Legal
6	Ruby	Female	1987-08-17	65476.0	True	Product
8	Angela	Female	2005-11-22	95570.0	True	Engineering
9	Frances	Female	2002-08-08	139852.0	True	Business Dev
12	Brandon	Male	1980-12-01	112807.0	True	HR
13	Gary	Male	2008-01-27	109831.0	False	Sales
40	Michael	Male	2008-10-10	99283.0	True	Distribution
```



* 또한 drop_duplicates 메서드에는 keep 매개변수도 있습니다. 각 중복값이 마지막으로 나타난 행을 유지하고 싶다면 keep 매개변수에 'last'를 인수로 전달하세요 

```python
employees.drop_duplicates(subset = ['Team'], keep = 'last')
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
988	Alice	Female	2004-10-05	47638.0	False	HR
989	Justin	NaN	1991-02-10	38344.0	False	Legal
990	Robin	Female	1987-07-24	100765.0	True	IT
993	Tina	Female	1997-05-15	56450.0	True	Engineering
994	George	Male	2013-06-21	98874.0	True	Marketing
995	Henry	NaN	2014-11-23	132483.0	False	Distribution
996	Phillip	Male	1984-01-31	42392.0	False	Finance
997	Russell	Male	2013-05-20	96914.0	False	Product
998	Larry	Male	2013-04-20	60500.0	False	Business Dev
999	Albert	Male	2012-05-15	129949.0	True	Sales
1000	NaN	NaN	NaT	NaN	NaN	NaN
```



* keep 매개변수에는 문자열 인수 외에 불리언형 인수도 전달할 수 있습니다. False를 인수로 전달하면 중복값이 있는 모든 행을 제거할 수 있습니다. 판다스는 동일한 값을 가진 행이 2개 이상이라면 해당 행을 제거합니다. 이 예제의 결과에 포함된 이름은 DataFrame에서 하나만 존재합니다

```python
employees.drop_duplicates(subset = ['First Name'], keep = False)
```

```
	First Name	Gender	Start Date	Salary	Mgmt	Team
5	Dennis	Male	1987-04-18	115163.0	False	Legal
8	Angela	Female	2005-11-22	95570.0	True	Engineering
33	Jean	Female	1993-12-18	119082.0	False	Business Dev
190	Carol	Female	1996-03-19	57783.0	False	Finance
291	Tammy	Female	1984-11-11	132839.0	True	IT
495	Eugene	Male	1984-05-24	81077.0	False	Sales
688	Brian	Male	2007-04-07	93901.0	True	Legal
832	Keith	Male	2003-02-12	120672.0	False	Legal
887	David	Male	2009-12-05	92242.0	False	Legal
```



* 여러 열에 있는 값을 조합하여 중복을 식별해보자

```python
name_is_douglas = employees['First Name'] == 'Douglas'
is_male = employees['Gender'] == 'Male'
employees[name_is_douglas & is_male]
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	NaN	True	Marketing
217	Douglas	Male	1999-09-03	83341.0	True	IT
322	Douglas	Male	2002-01-08	41428.0	False	Product
835	Douglas	Male	2007-08-04	132175.0	False	Engineering
```

```python
employees.drop_duplicates(subset = ['Gender', 'Team']).head()
```

```
First Name	Gender	Start Date	Salary	Mgmt	Team
0	Douglas	Male	1993-08-06	NaN	True	Marketing
1	Thomas	Male	1996-03-31	61933.0	True	NaN
2	Maria	Female	NaT	130590.0	False	Finance
3	Jerry	NaN	2005-03-04	138705.0	True	Finance
4	Larry	Male	1998-01-24	101004.0	True	I
```

