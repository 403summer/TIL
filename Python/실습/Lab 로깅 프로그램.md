# Lab: 로깅 프로그램



## 1. 사전 지식



### 1.1 logging formatter

* formatter는 로그의 결과값을 일정 형식을 지정하여 출력하는 기능이다.

```python
import logging

logger = logging.getLogger('myapp') # Logger 생성
hdlr = logging.FileHandler('myapp.log') # FileHandler 생성

formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s') # Logging Formatter 생성: 시간, 로깅 레벨, 프로세서 ID, 메세지

hdlr.setFormatter(formatter) # FilrHandler에 formatter 등록
logger.addHandler(hdlr) # Logger에 'FIleHandler' 등록
logger.setLevel(logging.INFO) # 로깅 레벨 설정

logger.error('ERROR occurred') # 로깅 정보 출력
logger.info('HERE WE ARE')
logger.info('TEST finished')

#2022-08-30 18:04:25,371 ERROR 4704 ERROR occurred
#2022-08-30 18:04:25,371 INFO 4704 HERE WE ARE
#2022-08-30 18:04:25,371 INFO 4704 TEST finished
```



### 1.2 logging config file

* logging config file은 파일에 로깅과 관련된 정보를 저장하여, 실제 사용할 때 파일을 생성하는 것만으로 로깅을 설정하는 방법이다. 긴 코드를 쓰지 않고 매우 간단하게 로깅을 설정할 수 있는 장점이 있다.

```text
# logging.conf

[loggers]
keys=root

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=concoleHandler

[handler_consoleHandler]
class=StreamHandler
level==DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFromatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
```

* 로깅 설정 파일의 구조는 하나의 section을 만들고, _를 사용해 그 section에서 사용하는 상세한 설정을 구축하는 방식이다. 위 코드를 보면 먼저 loggers, handlers, formatters 라는 section이 있고, 해당 section 에서는 section 별로 기본값을 지정하였다. 그리고 해당 section 의 상세 정보를 logger_root, handler_consoleHandler, formatter_simpleFormatter 에 설정하였다. 코드를 보면 알겠지만, 기존 section 이름에 simpleFormatter와 같은 키의 값을 _를 통해 연결하였다. 그리고 각 도구, 즉 logger, handler, formatter의 상세 정보는 해당 section에 넣었다. 사실 방식이 코드와 다르지는 않다. 하지만 코드를 만디는 것보다 설정 파일을 만지는 것이 사용자 입장에서 훨씬 부담이 덜하고 사용하기 쉽다는 장정이 있다. 실제 설정 파일을 사용하기 위해서는 다음과 같이 설정 파일을 호출 한다.

```python
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()
```



## 2. 실습

```python
import logging
import logging.config
import csv

# 모듈 호출
logging.config.fileConfig('logging.conf') # Logger 생성
logger = logging.getLogger()

line_counter = 0
data_heager = []
employee = []
customer_USA_only_list = []
customer = None

# 변수 선언 등 생략
logger.info('Open file {0}'.format('TEST'))
try:
    with open('customer.csv', 'r') as customer_data:
        customer_reader = csv.reader(customer_data, delimiter=',', quotechar='')
        for customer in customer_reader:
            if customer[10].upper()=='USA': # customer 데이터의 offset 10번째 값
                logger.info('ID {0} added'.format(customer[0],))
                customer_USA_only_list.append(customer) # country 필드가 'USA' 인 것만

except FileNotFoundError as e:
    logger.error('File NOT found {0}'.format(e,))

logger.info('Write USA only data at {0}'.format('customers_USA_only.csv',))
with open('customers_USA_only.csv', 'w') as customer_USA_only_csv:
    for customer in customer_USA_only_list:
        customer_USA_only_csv.write(','.join(customer).strip('\n')+'\n')

logger.info('Program finished')

#2022-08-30 18:44:59,621 - root - INFO - Open file TEST
#2022-08-30 18:44:59,627 - root - ERROR - File NOT found [Errno 2] No such file or directory: 'customer.csv'
#2022-08-30 18:44:59,698 - root - INFO - Write USA only data at customers_USA_only.csv
#2022-08-30 18:44:59,752 - root - INFO - Program finished
```

