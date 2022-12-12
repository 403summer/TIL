import json

dict_data ={'Name':'Zara','Age':7,'Class':'First'} # 딕셔너리 생성

with open("data.json", "w") as f:
    json.dump(dict_data, f)
