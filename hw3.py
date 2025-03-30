def get_fixed_price(s, a):
    return a / (100 - s) * 100

s = int(input("할인율은? "))
a1 = int(input("A 상품의 할인된 가격은? "))
b1 = int(input("B 상품의 할인된 가격은? "))

a2 = int(get_fixed_price(s, a1))
b2 = int(get_fixed_price(s, b1))

print("A 상품의 정가는", a2, "원")
print("B 상품의 정가는", b2, "원")
