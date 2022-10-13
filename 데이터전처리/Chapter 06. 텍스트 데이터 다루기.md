# Chapter 06. 텍스트 데이터 다루기



* 데이터를 정리하는 과정을 랭글링(wrangling) 또는 먼징(munging)이라고 합니다

* 시카고 시 전연에서 실시한 식당의 검사 목록

## 01. 대소문자 변환과 공백

```python
import pandas as pd

inspections = pd.read_csv('chicago_food_inspections.csv')
inspections
```

```

Name	Risk
0	MARRIOT MARQUIS CHICAGO	Risk 1 (High)
1	JETS PIZZA	Risk 2 (Medium)
2	ROOM 1520	Risk 3 (Low)
3	MARRIOT MARQUIS CHICAGO	Risk 1 (High)
4	CHARTWELLS	Risk 1 (High)
...	...	...
153805	WOLCOTT'S	Risk 1 (High)
153806	DUNKIN DONUTS/BASKIN-ROBBINS	Risk 2 (Medium)
153807	Cafe 608	Risk 1 (High)
153808	mr.daniel's	Risk 1 (High)
153809	TEMPO CAFE	Risk 1 (High)
153810 rows × 2 columns
```



* Name 열에 공백이 존재함

``` python
inspections['Name'].head()
```

```
0     MARRIOT MARQUIS CHICAGO   
1                    JETS PIZZA 
2                     ROOM 1520 
3      MARRIOT MARQUIS CHICAGO  
4                  CHARTWELLS   
Name: Name, dtype: object
```

```python
inspections['Name'].head().values
```

```

array([' MARRIOT MARQUIS CHICAGO   ', ' JETS PIZZA ', '   ROOM 1520 ',
       '  MARRIOT MARQUIS CHICAGO  ', ' CHARTWELLS   '], dtype=object)
```



* Series 객체의 str 속성을 사용하면 강력한 문자열 처리 메서드를 제공하는 StringMethods 객체에 접근할 수 있다.

```python
inspections['Name'].str
```

```
<pandas.core.strings.accessor.StringMethods at 0x1c0498f02e0>
```



* strip 계열의 메서드를 사용하면 문자열에서 공백을 제거할 수 있습니다
* lstrip (l은 left를 상징) 메서드는 문자열의 시작 부분에서 공백을 제거합니다.

```python
dessert = '     cheesecake     '
dessert.lstrip()
```

```
'cheesecake     '
```



* rstrip(r은 right를 상징) 메서드는 문자열 끝에서 공백을 제거합니다.

```python
dessert.rstrip()
```

```
'     cheesecake'
```



* strip 메서드는 문자열의 양쪽 끝에서 공백을 제거합니다

```python
dessert.strip()
```

```
'cheesecake'
```



```python
inspections['Name'].str.strip().head()
```

```
0    MARRIOT MARQUIS CHICAGO
1                 JETS PIZZA
2                  ROOM 1520
3    MARRIOT MARQUIS CHICAGO
4                 CHARTWELLS
Name: Name, dtype: object
```

```python
nspections['Name'] = inspections['Name'].str.strip()
```



* 열의 개수가 많은 데이터셋의 경우,  DataFrame의 열 이름의 목록을 나타내는 반복 가능한 Index 객체를 반환하는 columns 속성을 활용할 수 있습니다

```python
inspections.columns
```

```
Index(['Name', 'Risk'], dtype='object')
```

```python
for columns in inspections.columns:
    inspections[columns] = inspections[columns].str.strip()
```



* StringMethods 객체에서 파이썬의 모든 대소문자 변환 메서드를 사용할 수 있습니다.
* lower 메서드는 문자열의 모든 문자를 소문자로 변환합니다.

```python
inspections['Name'].str.lower().head()
```

```
0    marriot marquis chicago
1                 jets pizza
2                  room 1520
3    marriot marquis chicago
4                 chartwells
Name: Name, dtype: object
```



* str.upper 메서드는 문자열의 모든 문자를 대문자로 변환한 Series를 반환합니다

```python
steaks = pd.Series(['porterhouse', 'filet mignon', 'ribeye'])
steaks
```

```
0     porterhouse
1    filet mignon
2          ribeye
dtype: object
```

```python
steaks.str.upper()
```

```
0     PORTERHOUSE
1    FILET MIGNON
2          RIBEYE
dtype: object
```



* str.capitalize 메서드는 Series에서 각 문자열의 첫 번째 문자를 대문자로 표시합니다

```python
inspections['Name'].str.capitalize().head()
```

```
0    Marriot marquis chicago
1                 Jets pizza
2                  Room 1520
3    Marriot marquis chicago
4                 Chartwells
Name: Name, dtype: object
```



* str.title 메서드는 각 단어의 첫 번째 문자를 대문자로 표시합니다. 판다스는 공백을 기준으로 단어를 구분합니다

```python
inspections['Name'].str.title().head()
```

```
0    Marriot Marquis Chicago
1                 Jets Pizza
2                  Room 1520
3    Marriot Marquis Chicago
4                 Chartwells
Name: Name, dtype: object
```



## 02. 문자열 슬라이싱

```python
inspections['Risk'].head()
```

```
0      Risk 1 (High)
1    Risk 2 (Medium)
2       Risk 3 (Low)
3      Risk 1 (High)
4      Risk 1 (High)
Name: Risk, dtype: object
```



```python
len(inspections)
```

```
153810
```



* 모든 행이 동일한 형식있지 확인

```python
inspections['Risk'].unique()
```

```
array(['Risk 1 (High)', 'Risk 2 (Medium)', 'Risk 3 (Low)', 'All', nan],
      dtype=object)
```



* NaN값 제거

```python
inspections = inspections.dropna(subset = ['Risk'])
```



* All은 Risk 4 (Extreme) 으로 치환
* DataFrame의 replace 메서드를 사용. 첫번째 매개변수인 to_place로 검색할 값을 지정하고, 두번째 매개변수인 value로 각 항목을 대체할 항목을 지정합니다

```python
inspections = inspections.replace(to_replace = 'All', value = 'Risk 4 (Extreme)')
```

```python
inspections['Risk'].unique()
```

```

array(['Risk 1 (High)', 'Risk 2 (Medium)', 'Risk 3 (Low)',
       'Risk 4 (Extreme)'], dtype=object)
```



## 03. 문자열 슬라이싱과 문자 치환

* StringMethods 객체의 slice 메서드를 사용하면 인덱스 위치를 기반으로 문자열에서 하위 문자열을 추출할 수 있습니다. 이 메서드는 시작 인덱스와 끝 인덱스를 인수로 받습니다. 하한(시작점)은 범위에 포함되고 상한(끝점)은 범위에 포함되지 않습니다.

```python
inspections['Risk'].str.slice(5, 6).head()
```

```
0    1
1    2
2    3
3    1
4    1
Name: Risk, dtype: object
```



* 파이썬의 리스트 슬라이싱 구문으로 slice 메서드를 대체할 수도 있습니다. 

```python
inspections['Risk'].str[5:6].head()
```

```
0    1
1    2
2    3
3    1
4    1
Name: Risk, dtype: object
```



* 각 행의 범주형 위험도 유형('High', 'Medium', 'Low', 'All')을 추출해보자

````python
# 다음 두 줄의 결과는 동일합니다.
inspections['Risk'].str.slice(8).head()
inspections['Risk'].str[8:].head()
````

```
0      High)
1    Medium)
2       Low)
3      High)
4      High)
Name: Risk, dtype: object
```

```python
# 다음 두 줄의 결과는 동일합니다.
inspections['Risk'].str.slice(8, -1).head()
inspections['Risk'].str[8: -1].head()
```

```
0      High
1    Medium
2       Low
3      High
4      High
Name: Risk, dtype: object
```



* replace를 이용하는 방법

```python
inspections['Risk'].str.slice(8).str.replace(')', '').head()
```

```
0      High
1    Medium
2       Low
3      High
4      High
Name: Risk, dtype: object
```



## 04. 불리언 메서드

* StringMethods 객체에는 불리언 Series를 반환하는 메서드도 있습니다. 이러한 메서드는 DataFrame을 필터링할 때 특히 유용합니다

* 문자열 검색에서 가장 큰 문제는 대소문자를 구분하는 것 입니다.

```python
'Pizza' in 'Jets Pizza'
```

```
True
```

```python
'pizza' in 'Jets Pizza'
```

```
False
```



* 대소문자를 통일하고  문자열이 포함되어 있는지 확인
* contains 메서드는 각 Series 값에 하위 문자열이 포함되어 있는지 확인합니다

```python
inspections['Name'].str.lower().str.contains('pizza').head()
```

```
0    False
1     True
2    False
3    False
4    False
Name: Name, dtype: bool
```



* 필터링

```python
has_pizza = inspections['Name'].str.lower().str.contains('pizza')
inspections[has_pizza]
```

```
Name	Risk
1	JETS PIZZA	Risk 2 (Medium)
19	NANCY'S HOME OF STUFFED PIZZA	Risk 1 (High)
27	NARY'S GRILL & PIZZA ,INC.	Risk 1 (High)
29	NARYS GRILL & PIZZA	Risk 1 (High)
68	COLUTAS PIZZA	Risk 1 (High)
...	...	...
153756	ANGELO'S STUFFED PIZZA CORP	Risk 1 (High)
153764	COCHIAROS PIZZA #2	Risk 1 (High)
153772	FERNANDO'S MEXICAN GRILL & PIZZA	Risk 1 (High)
153788	REGGIO'S PIZZA EXPRESS	Risk 1 (High)
153801	State Street Pizza Company	Risk 1 (High)
3992 rows × 2 columns
```

* 판다스는 원본 Name 열 값의 원본 대소문자를 유지합니다. lower 메서드는 새 Series를 반홥합니다



* str.startswith 메서드는 문자열이 인수로 시작하면 True를 반환하는 메서드

```python
starts_with_tacos = inspections['Name'].str.lower().str.startswith('tacos')
inspections[starts_with_tacos]
```

```
	Name	Risk
69	TACOS NIETOS	Risk 1 (High)
556	TACOS EL TIO 2 INC.	Risk 1 (High)
675	TACOS DON GABINO	Risk 1 (High)
958	TACOS EL TIO 2 INC.	Risk 1 (High)
1036	TACOS EL TIO 2 INC.	Risk 1 (High)
...	...	...
143587	TACOS DE LUNA	Risk 1 (High)
144026	TACOS GARCIA	Risk 1 (High)
146174	Tacos Place's 1	Risk 1 (High)
147810	TACOS MARIO'S LIMITED	Risk 1 (High)
151191	TACOS REYNA	Risk 1 (High)
105 rows × 2 columns
```



* str.endswith 메서드는 하위 문자열이 문자열의 끝에 있는지 확인합니다

```python
ends_with_tacos = inspections['Name'].str.lower().str.endswith('tacos')
inspections[ends_with_tacos]
```

```

Name	Risk
382	LAZO'S TACOS	Risk 1 (High)
569	LAZO'S TACOS	Risk 1 (High)
2652	FLYING TACOS	Risk 3 (Low)
3250	JONY'S TACOS	Risk 1 (High)
3812	PACO'S TACOS	Risk 1 (High)
...	...	...
151121	REYES TACOS	Risk 1 (High)
151318	EL MACHO TACOS	Risk 1 (High)
151801	EL MACHO TACOS	Risk 1 (High)
153087	RAYMOND'S TACOS	Risk 1 (High)
153504	MIS TACOS	Risk 1 (High)
304 rows × 2 columns
```



## 05. 문자열 분할

```python
customers = pd.read_csv('customers.csv')
customers.head()
```

```
Name	Address
0	Frank Manning	6461 Quinn Groves, East Matthew, New Hampshire...
1	Elizabeth Johnson	1360 Tracey Ports Apt. 419, Kyleport, Vermont,...
2	Donald Stephens	19120 Fleming Manors, Prestonstad, Montana, 23495
3	Michael Vincent III	441 Olivia Creek, Jimmymouth, Georgia, 82991
4	Jasmine Zamora	4246 Chelsey Ford Apt. 310, Karamouth, Utah, 7...
```



* str.len 메서드를 사용하면 각 행의 문자열 길이를 반환할 수 있습니다

```python
customers['Name'].str.len().head()
```

```
0    13
1    17
2    15
3    19
4    14
Name: Name, dtype: int64
```



* 이름과 성을 구분해보자

* str.split 메서드는 Series의 각 행에 대해 파이썬의 split 메서드를 적용합니다. 메서드의 첫 번째 매개변수인 pat(pattern의 약자)에 구분 기호를 전달합니다.

```python
# 다음 두 줄은 결과가 동일합니다
customers['Name'].str.split(pat = ' ').head()
customers['Name'].str.split(' ').head()
```

```
0           [Frank, Manning]
1       [Elizabeth, Johnson]
2         [Donald, Stephens]
3    [Michael, Vincent, III]
4          [Jasmine, Zamora]
Name: Name, dtype: object
```



* MD, Jr 과 같은 접미사때문에 세 단어 이상으로 구성되는  문제 발생

```python
customers['Name'].str.split(' ').str.len().head()
```

```
0    2
1    2
2    2
3    3
4    2
Name: Name, dtype: int64
```



* 모든 리스트가 동일한 개수의 요소를 가지도록 분할하는 개수를 제한할 수 있습니다. 분할의 최대 임계값을 1로 설정하면 판다스는 첫 번째 공백에서 문자열을 분할하고 중지합니다.

```python
customers['Name'].str.split(pat = ' ', n = 1).head()
```

```
0          [Frank, Manning]
1      [Elizabeth, Johnson]
2        [Donald, Stephens]
3    [Michael, Vincent III]
4         [Jasmine, Zamora]
Name: Name, dtype: object
```



* str.get을 사용하여 인덱스 위치를 기반으로 각 행의 리스트에서 값을 가져올 수 있습니다

```python
customers['Name'].str.split(pat = ' ', n = 1).str.get(0).head()
```

```
0        Frank
1    Elizabeth
2       Donald
3      Michael
4      Jasmine
Name: Name, dtype: object
```

```python
customers['Name'].str.split(pat = ' ', n = 1).str.get(1).head()
```

```
0        Manning
1        Johnson
2       Stephens
3    Vincent III
4         Zamora
Name: Name, dtype: object
```

```python
customers['Name'].str.split(pat = ' ', n = 1).str.get(-1).head()
```

```
0        Manning
1        Johnson
2       Stephens
3    Vincent III
4         Zamora
Name: Name, dtype: object
```



* 2개의 독립적인 Series를 얻기 위해 get 메서드를 두 번 호출해야하는 것도 좋지만 str.split 메서드는 expand라는 매개변수를 제공하여 이 매개변수에 인수로 True를 전달하면 이 메서드는 리스트 Series 대신 새로운 DataFrame을 반환합니다

```python
customers['Name'].str.split(pat = ' ', n = 1, expand = True).head()
```

```

0	1
0	Frank	Manning
1	Elizabeth	Johnson
2	Donald	Stephens
3	Michael	Vincent III
4	Jasmine	Zamora
```



* 주의해야할 점, 매개변수n으로 분할 개수를 제한하지 않으면 판다스는 요소가 불출분한 행에 None 값을 배치합니다

```python
customers['Name'].str.split(pat = ' ', expand = True).head()
```

```
0	1	2
0	Frank	Manning	None
1	Elizabeth	Johnson	None
2	Donald	Stephens	None
3	Michael	Vincent	III
4	Jasmine	Zamora	None
```



* 기존 DataFrame에 연결해보자

```python
customers[['First Name', 'Last Name']] = customers['Name'].str.split(pat = ' ', n = 1, expand = True)

customers
```

```
Name	Address	First Name	Last Name
0	Frank Manning	6461 Quinn Groves, East Matthew, New Hampshire...	Frank	Manning
1	Elizabeth Johnson	1360 Tracey Ports Apt. 419, Kyleport, Vermont,...	Elizabeth	Johnson
2	Donald Stephens	19120 Fleming Manors, Prestonstad, Montana, 23495	Donald	Stephens
3	Michael Vincent III	441 Olivia Creek, Jimmymouth, Georgia, 82991	Michael	Vincent III
4	Jasmine Zamora	4246 Chelsey Ford Apt. 310, Karamouth, Utah, 7...	Jasmine	Zamora
...	...	...	...	...
9956	Dana Browning	762 Andrew Views Apt. 254, North Paul, New Mex...	Dana	Browning
9957	Amanda Anderson	44188 Day Crest Apt. 901, Lake Marcia, Maine, ...	Amanda	Anderson
9958	Eric Davis	73015 Michelle Squares, Watsonville, West Virg...	Eric	Davis
9959	Taylor Hernandez	129 Keith Greens, Haleyfurt, Oklahoma, 98916	Taylor	Hernandez
9960	Sherry Nicholson	355 Griffin Valley, Davidtown, New Mexico, 17581	Sherry	Nicholson
9961 rows × 4 columns
```



* 기존에 있는 Name 열을 삭제
* drop 메서드를 사용하면 열을 삭제할 수 있습니다. 열 이름을 매개변수 labels에 전달하고 매개변수 axis에 'columns'를 인수로 전달합니다. 판다스가 행 대신 열에서 Name 레이블을 찾도록 지시하고 싶다면 매개변수 axis를 지정해야 합니다

```python
customers = customers.drop(labels = 'Name', axis = 'columns')
customers.head()
```

```
Address	First Name	Last Name
0	6461 Quinn Groves, East Matthew, New Hampshire...	Frank	Manning
1	1360 Tracey Ports Apt. 419, Kyleport, Vermont,...	Elizabeth	Johnson
2	19120 Fleming Manors, Prestonstad, Montana, 23495	Donald	Stephens
3	441 Olivia Creek, Jimmymouth, Georgia, 82991	Michael	Vincent III
4	4246 Chelsey Ford Apt. 310, Karamouth, Utah, 7...	Jasmine	Zamora
```



## 06. 정규 표현식에 대한 참고 사항

* 연습문제 코드를 참고
* 판다스가 대부분의 문자열 메서드에서 정규 표현식 인수를 지원한다

```python
customers['Street'].head()
```

```
0             6461 Quinn Groves
1    1360 Tracey Ports Apt. 419
2          19120 Fleming Manors
3              441 Olivia Creek
4    4246 Chelsey Ford Apt. 310
Name: Street, dtype: object
```

```python
customers['Street'].str.replace('\d{4,}', '*', regex = True)
```

```
1         * Tracey Ports Apt. 419
2                * Fleming Manors
3                441 Olivia Creek
4         * Chelsey Ford Apt. 310
                  ...            
9956    762 Andrew Views Apt. 254
9957         * Day Crest Apt. 901
9958           * Michelle Squares
9959             129 Keith Greens
9960           355 Griffin Valley
Name: Street, Length: 9961, dtype: object
```

