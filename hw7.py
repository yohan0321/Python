shopping_bag = {}
print("[구입]")
while True:
    item = input("상품명? ")
    if item == "":
        print()
        break
    quantity = int(input("수량은? "))
    shopping_bag[item] = quantity
    print(f'장바구니에 {item} {quantity} 개가 담겼습니다.\n')

print(f'>>> 장바구니 보기: {shopping_bag}\n')

print('[검색]')
key = input("장바구니에서 확인하고자 하는 상품은?")
if key in shopping_bag:
    print(f'{key}은(는) {shopping_bag[key]}개 담겨있습니다.)')
else:
    print(f'{key}은(는) 장바구니에 없습니다.')
