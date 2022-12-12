# Lab: 평균 구하기



## 1. 실습내용



반복문과 조건문을 토대로 연속적이 평균 구하기 프로그램을 만들어보자

|   학생    |  A   |  B   |  C   |  D   |  E   |
| :-------: | :--: | :--: | :--: | :--: | :--: |
| 국어 점수 |  49  |  80  |  20  | 100  |  80  |
| 수학 점수 |  43  |  60  |  85  |  30  |  90  |
| 영어 점수 |  49  |  82  |  48  |  50  | 100  |

* 이차원 리스트이므로 각 행을 호출하고 각 열에 있는 값을 더해 학생별 평균을 구한다
* for문 2개를 사용한다



## 2. 실행결과

```text
[47.0, 74.0, 51.0, 60.0, 90.0]
```



## 3. 문제해결

```python
kor_score = [49,80,20,100,80]
math_score = [43,60,85,30,90]
eng_score = [49,82,48,50,100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0,0,0,0,0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score # 학생마다 개별로 교과 점수를 저장
        i += 1 # 학생 인덱스 구분
    i = 0 # 과목이 바뀔 때 학생 인덱스 초기화
else:
    a, b, c, d, e = student_score # 학생별 점수를 언패킹
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)
```



