# Chapter 12. 판다스 설정

- 설정은 판다스가 표시하는 형식만 변경한다. 판다스는 DataFrame 안에서 기존 값을 유지한다. 



## 데이터셋

- 세계 국가의 행복순위(happiness)

![12-1](C:\Users\여름\Desktop\2회차\image\12\12-1.PNG)



## 01. 전체 설정



### (예시)

- describe_option 메서드는 설정에 대한 설명을 문서로 반환한다
- 판다스는 문자열 인수와 일치하는 모든 라이브러리 설정을 출력합니다. 

```python
pd.describe_option('max_col')
```

```
display.max_columns : int
    If max_cols is exceeded, switch to truncate view. Depending on
    `large_repr`, objects are either centrally truncated or printed as
    a summary view. 'None' value means unlimited.

    In case python/IPython is running in a terminal and `large_repr`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the width of the terminal and print a truncated object which fits
    the screen width. The IPython notebook, IPython qtconsole, or IDLE
    do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    [default: 20] [currently: 20]
display.max_colwidth : int or None
    The maximum width in characters of a column in the repr of
    a pandas data structure. When the column overflows, a "..."
    placeholder is embedded in the output. A 'None' value means unlimited.
    [default: 50] [currently: 50]
```



- 현재 설정값을 가져오는 방법은 두 가지가 있다

```python
# 다음 두 줄의 결과는 동일합니다.
pd.get_option('display.max_rows')
pd.options.display.max_rows
```

```
60
```



- 설정값을 변경하는 방법도 두 가지가 있다

```python
# 다음 두 줄의 결과는 동일합니다.
pd.set_option('display.max_rows', 6)
pd.options.display.max_rows = 6
```



- 설정을 리셋하는 방법

```python
pd.reset_option('display.max_rows')
```



### (정리)

|      메서드       |             설명             |
| :---------------: | :--------------------------: |
| describe_option() | 설정을 검색 또는 문서로 반환 |
|   get_option()    | 현재 설정값을 반환 또는 변경 |
|  reset_option()   |         설정을 리셋          |



- 설정 인수

|          인수          |                             설명                             |
| :--------------------: | :----------------------------------------------------------: |
|    display.max_rows    |               자르기 전에 출력할 최대 행의 수                |
|  display.max_columns   |               자르기 전에 출력할 최대 열의 수                |
|   display.precision    |                        소수점 자릿수                         |
|  display.max_colwidth  |                   셀에 출력할 최대 문자수                    |
| display.chop_threshold | 최소 임계값을 설정. 판다스는 임계값보다 작은 모든 값을 0으로 표시 |



## 02. 부분 설정

- 지금까지 변경한 설정은 모두 전역적이다. 변경하면 이후에 실행되는 모든 주피터 노트북 셀의 출력이 영향을 받는다 
- 하나의 셀에 대한 출력설정을 변경할 수 있다



### (예시)

- with 키워드를 사용했기 때문에 이 세가지 설정값은 전체 노트북의 설정값을 변경하지 않는다. 전체 노트북의 설정은 기존 값을 그대로 유지한다.
- option_context 메서드는 서로 다른 행에 서로 다른 설정을 할당하고 싶을 때 유용하다. 모든 출력 결과가 동일한 형식을 갖게 하고 싶다면 주피터 노트북 상단의 셀에서 옵션을 한번에 설정하는 것이 좋다.

```python
with pd.option_context(
    'display.max_columns', 5,
    'display.max_rows', 10,
    'display.precision', 3
): 
    display(happiness)
```

<img src="C:\Users\여름\Desktop\2회차\image\12\12-2.PNG" alt="12-2" style="zoom:80%;" />