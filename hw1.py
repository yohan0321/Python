prompt = "넓이를 구하고자 하는 원의 반지름은? "

def get_radius(prompt) :
    r = int(input(prompt))
    return r

def get_circle_area(r):
    return r * r * 3.14

r = get_radius(prompt)
circle = get_circle_area(r)
print("반지름", r, "인 원의 넓이 = 3.14 x ", r, " x ", r, " = ", circle)




