print("구구단 몇 단을 계산할까?")
user_input = input()
print("구구단", user_input, "단을 계산한다.")
int_input = int(user_input)
for i in range(1, 10):
    result = int_input * i
    print(user_input, "x", i, "=", result)
