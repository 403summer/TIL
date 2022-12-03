# Chapter 10. 날짜 및 시간



## 01. Timestamp 객체



### 1.1 파이썬의 날짜/시간

```python
import datetime as dt
```



### (예시1)

* date 객체는 하나의 날짜를 모델링한다

```python
# 다음 두 줄은 결과가 동일합니다.
birthday = dt.date(1991, 4, 12)
birthday = dt.date(year = 1991, month = 4, day = 12)
birthday
```

````
datetime.date(1991, 4, 12)
````



* date 객체는 불변 객체로 생성한 후에는 내부 상태를 변경할 수 없다

```python
birthday.month = 10
```

```
AttributeError
```



### (정리)

| 매개변수 | 설명 |
| :------: | :--: |
|   year   | 연도 |
|  month   |  월  |
|   day    |  일  |

| 속성  | 설명 |
| :---: | :--: |
| year  | 연도 |
| month |  월  |
|  day  |  일  |



### (예시2)

* time 객체는 하나의 시간을 모델링한다
* time 객체는 변경할 수 없다

```python
# 다음 두 줄을 결과가 동일합니다.
alarm_clock = dt.time(19, 43, 22)
alarm_clock = dt.time(hour = 19, minute = 43, second = 22)
alarm_clock
```

```
datetime.time(19, 43, 22)
```



* 세 매개변수의 기본 인수는 0 이다

```python
dt.time(hour = 9, second = 42)
```

```
datetime.time(9, 0, 42)
```



### (정리)

| 매개변수 | 설명 |
| :------: | :--: |
|   hour   | 시간 |
|  minute  |  분  |
|  second  |  초  |

|  속성  | 설명 |
| :----: | :--: |
|  hour  | 시간 |
| minute |  분  |
| second |  초  |



### (예시3)

* time 객체는 날짜와 시간을 모델링한다

* 날짜 매개변수는 필수사항이고, 시간과 매개변수는 선택사항이며 기본값은 0이다

```python
# 다음 두 줄은 결과가 동일합니다.
moon_landing = dt.datetime(1969, 7, 20, 22, 56, 20)
moon_landing = dt.datetime(
    year = 1969,
    month = 7,
    day = 20,
    hour = 22,
    minute = 56,
    second = 20
)

moon_landing
```

```
datetime.datetime(1969, 7, 20, 22, 56, 20)
```



### (예시4)

* timedelta 객체는 시간차를 모델링한다
* 시간의 길이를 합하여 총 시간을 계산한다
* 모든 매개변수는 선택사항이며 기본값은 0 이다

```python
dt.timedelta(
    weeks = 8,
    days = 6,
    hours = 3,
    minutes = 58,
    seconds = 12
)
```

```
datetime.timedelta(days=62, seconds=14292)
```



### 1.2 판다스의 날짜/시간

* 파이썬의 datetime 모듈은 기억해야하는 클래스가 많다
* 판다스의 Timestamp는 기본 datetime 객체에 몇 가지 기능을 추가한 객체이다

* Timestamp객체는 datetime 객체와 매개변수가 동일하다



### (예시1)

```python
# 다음 두 줄은 결과가 동일합니다.
pd.Timestamp(1991, 4, 12)
pd.Timestamp(year = 1991, month = 4, day = 12)
```

```
Timestamp('1991-04-12 00:00:00')
```



* 판다스는 두 객체가 동일한 정보를 저장하는 경우 Timestamp를 date의 datetime과 같다고 간주한다

```python
(pd.Timestamp(year = 1991, month = 4, day = 12) == dt.date(year = 1991, month = 4, day = 12))
```

```
True
```



### (예시2)

* Timestamp 객체는다양한 입력을 허용한다

```python
pd.Timestamp('2015-03-31')
```

```python
pd.Timestamp('2015/03/31')
```

```python
pd.Timestamp('03/31/2015')
```



```python
pd.Timestamp('2021-03-08 08:35:15')
```

```python
pd.Timestamp('2021-03-08 6:13:29 PM')
```



* Timestamp 객체는 파이썬의 date, time, datetime 객체도 허용한다

```python
pd.Timestamp(dt.datetime(2000, 2, 3, 21, 35, 22))
```

```
Timestamp('2000-02-03 21:35:22')
```



## 02.  DatetimeIndex



### (예시1)

* DatetimeIndex는 Timestamp 객체를 저장하는 인덱스이다

```python
timestamps = [
    pd.Timestamp('2020-01-01'),
    pd.Timestamp('2020-02-01'),
    pd.Timestamp('2020-03-01')
]
pd.Series([1, 2, 3], index = timestamps).index
```

```
DatetimeIndex(['2020-01-01', '2020-02-01', '2020-03-01'], dtype='datetime64[ns]', freq=None)
```



### (예시2)

* DatetimeIndex 자체를 생성할 수도 있다

```python
mixed_dates = [
    dt.date(2018, 1, 2),
    '2016/04/12',
    pd.Timestamp(2009, 9, 7)
]
dt_index = pd.DatetimeIndex(mixed_dates)
dt_index
```

```
DatetimeIndex(['2018-01-02', '2016-04-12', '2009-09-07'], dtype='datetime64[ns]', freq=None)
```



## 03. 날짜/시간으로 변환



### 데이터셋

* 디즈니의 약 60년치 주가(disney)

<img src="image/10/10-1.PNG" alt="10-1" style="zoom:80%;" />



### (예시1)

* read_csv 함수의 parse_dates 매개변수를 사용할 수 있다

```python
 pd.read_csv('disney.csv', parse_dates = ['Date'])
```



### (예시2)

* to_datetime 메서드를 사용할 수 있다
* 반복 가능한 객체(예를 들어 파이썬의 리스트, 튜플 , Series 또는 인덱스)를 입력받는다

```python
pd.to_datetime(disney['Date']).head()
```

```
0   1962-01-02
1   1962-01-03
2   1962-01-04
3   1962-01-05
4   1962-01-08
Name: Date, dtype: datetime64[ns]
```



## 04. DatetimeProperties 객체

* 날짜/시간 Series는 DatetimeProperties 객체에 접근할 수 있는 특별한 속성 dt를 가진다. 날짜/시간의 dt 속성은 문자열의 str 속성과 같은 역활을 한다



### (예시)

```python
disney['Date'].head(3)
```

```
0   1962-01-02
1   1962-01-03
2   1962-01-04
Name: Date, dtype: datetime64[ns]
```



```python
disney['Date'].dt.day.head()
```

```
0    2
1    3
2    4
3    5
4    8
Name: Date, dtype: int64
```



### (정리)

|       속성       |                   설명                    |
| :--------------: | :---------------------------------------: |
|       day        |                    일                     |
|      month       |                    월                     |
|       year       |                    년                     |
|    dayofweek     |            요일을 숫자로 반환             |
| is_quarter_start |  행의 날짜가 분기의 시작 날짜인지를 반환  |
|  is_quarter_end  | 행의 날짜가 분기의 마지막 날짜인지를 반환 |
|  is_month_start  |   행의 날짜가 월의 시작 날짜인지를 반환   |
|   is_month_end   |  행의 날짜가 월의 마지막 날짜인지를 반환  |
|  is_year_start   |   행의 날짜가 년의 시작 날짜인지를 반환   |
|   is_year_end    |  행의 날짜가 년의 마지막 날짜인지를 반환  |

|    메서드    |        설명        |
| :----------: | :----------------: |
|  day_name()  | 요일을 문자로 반환 |
| month_name() |  월을 문자로 반환  |



## 05. DateOffset



### 5.1 시간의 덧셈과 뺄셈

* DateOffset 객체를 사용하여 시간을 더하거나 뺄 수 있다



### (예시)

```python
disney['Date'].head()
```

```
0   1962-01-02
1   1962-01-03
2   1962-01-04
3   1962-01-05
4   1962-01-08
Name: Date, dtype: datetime64[ns]
```



```python
(disney['Date'] + pd.DateOffset(days = 5)).head()
```

```
0   1962-01-07
1   1962-01-08
2   1962-01-09
3   1962-01-10
4   1962-01-13
Name: Date, dtype: datetime64[ns]
```



### 5.2 메서드



### (예시)

* 다음은 각 날짜/시간을 월의 말일로 올린 새로운 Series를 반환하는 예제이다
* 이미 월의 말일인 경우 라이브러리는 해당 날짜를 다음 달의 말일로 올린다

```python
disney['Date'].tail()
```

```
14722   2020-06-26
14723   2020-06-29
14724   2020-06-30
14725   2020-07-01
14726   2020-07-02
Name: Date, dtype: datetime64[ns]
```



```python
(disney['Date'] + pd.offsets.MonthEnd()).tail()
```

```
14722   2020-06-30
14723   2020-06-30
14724   2020-07-31
14725   2020-07-31
14726   2020-07-31
Name: Date, dtype: datetime64[ns]
```



### (정리)

|    메서드     |                설명                 |
| :-----------: | :---------------------------------: |
| MonthBegin()  |      월의 첫 번째 날짜로 변환       |
|  MonthEnd()   |       월의 마지막 날짜로 변환       |
| BMonthBegin() | (주말 제외)월의 첫 번째 날짜로 변환 |
|  BMonthEnd()  | (주말 제외)월의 마지막 날짜로 변환  |



## 07. Timedelta 객체

* 파이썬의 timedelta  객체는 시간차를 모델링한다

* 판다스의 Timedelta 객체는 시간차를 모델링한다



### (예시1)

* 일반적으로 Timedelta 객체는 처음부터 생성되는 경우보다 파생되는 경우가 많다

```python
pd.Timestamp('1999-02-05') - pd.Timestamp('1998-05-24')
```

```
Timedelta('257 days 00:00:00')
```



### (예시2)

* Timedelta 자체를 생성할 수도 있다

```python
pd.Timedelta(
    days = 8,
    hours = 7,
    minutes = 6,
    seconds = 5
)
```

```
Timedelta('8 days 07:06:05')
```



### (예시3)

* to_timedelta 메서드는 인수를 Timedelta 객체로 변환한다
* 리스트와 같은 반복 가능한 객체도 전달 가능하다
* 문자열도 전달 가능하다

```python
pd.to_timedelta('3 hours, 5 minutes, 12 seconds')
```

```
Timedelta('0 days 03:05:12')
```



* unit 매개변수는 숫자가 나타내는 시간 단위를 정의한다. 유효한 인수는 시를 나타내는 'hour', 일을 나타내는 'day', 분을 나타내는 'minute'이다

```python
pd.to_timedelta([5, 10, 15], unit = 'day')
```

```
TimedeltaIndex(['5 days', '10 days', '15 days'], dtype='timedelta64[ns]', freq=None)
```

