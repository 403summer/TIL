# 부록 D. faker로 가짜 데이터 생성하기

- faker는 가짜 데이터를 생성하는 판다스 라이브러리입니다. 이름, 전화번호, 주소, 이메일 등의 리스트를 생성할 수 있습니다. 임의의 숫자 데이터를 생성하는 넘파이와 함께 사용하면 모든 크기, 형태, 유형의 데이터셋을 빠르게 생성할 수 있습니다.



## 01. faker 개요

```python
import pandas as pd
import numpy as np
import faker
```

- faker 패키지에서 Faker 클래스를 사용할 수 있습니다. 이때 클래스 이름은 패키지 이름과 다르게 첫 문자가 대문자 'F'라는 점에 주의하세요. 클래스는 자료구조의 템플릿이며 객체의 청사진입니다. Series와 DataFrame은 판다스의 라이브러리의 클래스이고 Faker는 faker 라이브러리의 클래스 입니다.
- 한 쌍의 괄호를 사용하여 faker 클래스의 인스턴스를 만들고 결과 Faker 객체를 fake 변수에 할당합니다.

```python
fake = faker.Faker()
```

- Faker 객체는 여러 인스턴스 메서드를 지원하며 각 인스턴스 메서드는 지정된 범주에서 임의의 값을 반환합니다. 예를 들어 name 인스턴스 메서드는 사람의 전체 이름이 포함된 문자열을 반환합니다. 
- Faker는 임의의 값을 생성하기 때문에 컴퓨터에서 실행할 때마다 반환 값이 달라질 수 있습니다.

```python
fake.name()
```

```
'Nicole Nguyen'
```

```python
fake.name_male()
```

```
'Andrew Clark'
```

```python
fake.name_female()
```

```
'Jenna Moore'
```

```python
fake.first_name()
```

```
'Ronnie'
```

```python
fake.last_name()
```

```
'Scott'
```

```python
fake.first_name_male()
```

```
'Miguel'
```

```python
fake.first_name_female()
```

```
'Caitlyn'
```

- address 메서드는 거리, 도시, 주와 우편번호를 포함한 완전한 주소가 포함된 문자열을 반환합니다.

```python
fake.address()
```

```
'71728 Jonathan Shore Apt. 584\nNew Rebecca, RI 42061'
```

- Faker는 거리와 주소의 나머지 부분을 줄 바꿈(\n)으로 구분합니다. print 함수로 반환된 주소를 출력하면 주소가 여러 줄에 걸쳐 출력됩니다.

```python
print(fake.address())
```

```
820 Kelly Street Suite 162
North Travis, AZ 99326
```

- street_address, city, state, postcode와 같은 메서드를 사용하면 주소의 개별 구성 요소를 생성할 수 있습니다.

```python
fake.street_address()
```

```
'964 Brian Avenue Apt. 131'
```

```python
fake.city()
```

```
'Brittanyport'
```

```python
fake.state()
```

```
'Oklahoma'
```

```python
fake.postcode()
```

```
'69764'
```

- 비즈니스 관련 데이터를 생성하는 메서드도 있습니다. 다음의 메서드는 임의의 기업 이름, 광고 문구, 직함, URL을 반환합니다.

```python
fake.company()
```

```
'Scott, Cooley and Long'
```

```python
fake.catch_phrase()
```

```
'Triple-buffered demand-driven definition'
```

```python
fake.job()
```

```
'Buyer, industrial'
```

```python
fake.url()
```

```
'https://randall.com/'
```

```python
fake.email()
```

```
'jenniferkoch@example.org'
```

```python
fake.phone_number()
```

```
'(330)548-5785x9119'
```

```python
fake.credit_card_number()
```

```
'676143505466'
```

- Faker 웹사이트는 Faker 객체의 인스턴스 메서드를 설명하는 전체 문서를 제공합니다. 라이브러리는 메서드를 주소, 자동차, 은행과 같은 상위 범주로 그룹화합니다.
- https://faker.reathedocs.io/en/master



## 02. 가짜 값으로 DataFrame 채우기

- 가상의 데이터셋을 채워봅시다. 목표는 이름, 기업, 이메일, 연봉 4개 열이 있는 1000행짜리 DataFrame입니다.

- for 문을 사용하여 각 반복마다 Faker로 가짜 이름, 회사. 이메일 주소를 생성합니다. 또한 넘파이로 연봉을 나타내는 임의의 숫자를 생성합니다.

- Faker가 생성한 데이터에서 몇가지 논리적인 오류를 확인할 수 있습니다. 예를 들어 첫번째 사람의 이름은 Ashley Anderson이지만 이메일은 jessicabrooks@whitaker-crawford.biz 입니다. 이러한 오류는 Faker의 임의성 때문입니다. 다음 예제에서 이러한 논리적 오류를 무시합니다. 하지만 데이터셋을 보다 정확하게 만들고 싶다면  Faker를 일반 파이썬 코드와 결합하여 원하는 값을 생성해야 합니다. Faker로 이름과 성을 생성하고 두 문자열을 결합하여 보다 현실적인 이메일 주소를 만들 수 있습니다.

```python
first_name = fake.first_name_female()
last_name = fake.last_name()
email = first_name + last_name + '@gmail.com'
email
```

```
'KellyRamirez@gmail.com'
```

```python
data = [
    { 'Name': fake.name(),
      'Company': fake.company(),
      'Email': fake.email(),
      'Salary': np.random.randint(50000, 200000)
    }
    for i in range(1000)
]
```

```python
df = pd.DataFrame(data = data)
df
```

<img src="C:\Users\여름\TIL\데이터전처리\image\부록D\D-1.PNG" alt="D-1" style="zoom:80%;" />

