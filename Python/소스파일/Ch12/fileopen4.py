with open("dream.txt", "r") as my_file:
    i = 0
    while 1:
        line = my_file.readline()
        if not line:
            break
        print(str(i)+" === "+ line.replace("\n",""))    # 한 줄씩 값 출력
        i = i + 1
