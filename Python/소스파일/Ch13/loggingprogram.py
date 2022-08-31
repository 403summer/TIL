import logging
import logging.config
import csv

# 모듈 호출
logging.config.fileConfig('logging.conf')               # Logger 생성
logger = logging.getLogger()

line_counter = 0
data_haeder = [ ]
employee = [ ]
customer_USA_only_list = [ ]
customer = None

# 변수 선언 등 생략
logger.info('Open file {0}'.format("TEST",))
try:
    with open("customers.csv", "r") as customer_data:
        customer_reader = csv.reader(customer_data, delimiter=',', quotechar='"')
        for customer in customer_reader:
            if customer[10].upper()=="USA":             # customer 데이터의 offset 10번째 값
                logger.info('ID {0} added'.format(customer[0],))
                customer_USA_only_list.append(customer) # country 필드가 “USA” 것만
except FileNotFoundError as e:
    logger.error('File NOT found {0}'.format(e,))

logger.info('Write USA only data at {0}'.format("customers_USA_only.csv",))
with open("customers_USA_only.csv", "w") as customer_USA_only_csv:
    for customer in customer_USA_only_list:
        customer_USA_only_csv.write(",".join(customer).strip('\n')+"\n")

logger.info('Program finished')
