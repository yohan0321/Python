def read_single_digit(a) :
    if(a == 1):
        print("일", end = ' ')
    elif (a == 2):
        print("이", end = ' ')
    elif (a == 3):
        print("삼", end = ' ')
    elif (a == 4):
        print("사", end = ' ')
    elif (a == 5):
        print("오", end = ' ')
    elif (a == 6):
        print("육", end = ' ')
    elif (a == 7):
        print("칠", end = ' ')
    elif (a == 8):
        print("팔", end = ' ')
    elif (a == 9):
        print("구", end = ' ')
    elif (a == 0):
        print("영", end = ' ')

def read_number(x):
    for i in range(len(str(x))) :
        x_str = str(x)
        a = x_str[i]
        a = int(a)
        read_single_digit(a)


x = int(input("세 자리 정수 입력: "))
read_number(x)