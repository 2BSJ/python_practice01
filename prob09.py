# 문제9.
# 주어진 if 문을 dict를 사용해서 수정하세요.
inputmenu = input('menu >>')

menu = {'오뎅':300, '순대':400, '만두':500}

price = menu.get(inputmenu)

print('가격: {0}'.format(menu[inputmenu] if inputmenu in menu else 0))