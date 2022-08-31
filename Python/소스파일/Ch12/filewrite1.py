f = open("count_log.txt", 'w', encoding = "utf8")
for i in range(1,11):
    data = "%d번째 줄이다.\n"% i
    f.write(data)
f.close()
