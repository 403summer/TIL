def addition(x, y):
    return x + y

def multiplication(x, y):
    return x * y

def divided_by_2(x):
    return x / 2

# 파이썬 셸에서 호출할 경우 실행되지 않음
if __name__ == '__main__':
    print(addition(10, 5))
    print(multiplication(10, 5))
    print(divided_by_2(50))
