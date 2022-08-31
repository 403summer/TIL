def a_rectangle_area():         # 매개변수 X , 반환값 X
    print(5 * 7)
def b_rectangle_area(x, y):     # 매개변수 O , 반환값 X
    print(x * y)
def c_rectangle_area():         # 매개변수 X , 반환값 O
    return (5 * 7)
def d_rectangle_area(x , y):    # 매개변수 O , 반환값 O
    return (x * y)

a_rectangle_area()
b_rectangle_area(5, 7)
print(c_rectangle_area())
print(d_rectangle_area(5, 7))
