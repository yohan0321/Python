def get_integer() :
    x = int(input("동전으로 교환하고자 하는 금액은? "))
    return x

def exchange(x) :
    a500 = x // 500
    x %= 500
    a100 = x // 100
    x %= 100
    a50 = x // 50
    x %= 50
    a10 = x // 10

    print("500원 동전의 개수: ", a500)
    print("100원 동전의 개수: ", a100)
    print("50원 동전의 개수: ", a50)
    print("10원 동전의 개수: ", a10)

x = get_integer()
exchange(x)