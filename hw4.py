x = str(input("Input his/her name: "))
x = "Hello " + x
y = "Welcome to Seoul."



def draw_line_string(x, y) :
    if (len(x) >= len(y)):
        nstr = len(x)
    else:
        nstr = len(y)

    line = "-" * (nstr + 1)
    
    print(line)
    print(x)
    print(y)
    print(line)

draw_line_string(x, y)


