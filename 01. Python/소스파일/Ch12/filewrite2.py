with open("count_log.txt", 'a', encoding = "utf8") as f:
    for i in range(1, 11):
        data = "%d번째 줄이다.\n"% i
        f.write(data)
