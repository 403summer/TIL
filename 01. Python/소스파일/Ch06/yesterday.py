f = open("yesterday.txt", 'r')
yesterday_lyric = f.readlines()
f.close()

contents = ""
for line in yesterday_lyric:
    contents = contents + line.strip() + "\n"

n_of_yesterday = contents.upper().count("YESTERDAY")
print("Number of a Word 'Yesterday'" , n_of_yesterday)
