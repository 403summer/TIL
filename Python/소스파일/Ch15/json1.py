import json

with open("json_example.json", "r", encoding = "utf8") as f:
    contents = f.read()                     # 파일 내용 읽어 오기
    json_data = json.loads(contents)        # json 파싱
    print(json_data["employees"])           # 딕셔너리처럼 사용하기
