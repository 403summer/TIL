import csv
f = open("./korea_floating_population_data.csv", "r")
reader = csv.reader(
    f,                      # 연결할 대상 파일 객체
    delimiter=',',          # 데이터를 분리하는 기준
    quotechar='"',          # 데이터를 묶을 때 사용하는 문자
    quoting=csv.QUOTE_ALL)  # 데이터를 묶을 정도 쓰는 기준
