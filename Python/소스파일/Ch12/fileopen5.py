with open("dream.txt", "r") as my_file:
    contents = my_file.read()
    word_list = contents.split(" ")             # 빈칸 기준으로 단어를 분리 리스트
    line_list = contents.split("\n")            # 한 줄씩 분리하여 리스트

print("총 글자의 수:", len(contents))
print("총 단어의 수:", len(word_list))
print("총 줄의 수:", len(line_list))
