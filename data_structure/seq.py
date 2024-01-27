shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

# Операция индексирования
print('Элемент 0 -', shop_list[0])
print('Элемент 1 -', shop_list[1])
print('Элемент 2 -', shop_list[2])
print('Элемент 3 -', shop_list[3])
print('Элемент -1 -', shop_list[-1])
print('Элемент -2 -', shop_list[-2])
print('Символ 0 -', name[0])

# Вырезка из списка
print('Элементы с 1 по 3:', shop_list[1:3])
print('Элементы с 2 до конца:', shop_list[2:])
print('Элементы с 1 по -1:', shop_list[1:-1])
print('Элементы от начала до конца:', shop_list[:])

# Вырезка из строки
print('Элементы с 1 по 3:', name[1:3])
print('Элементы с 2 до конца:', name[2:])
print('Элементы с 1 по -1:', name[1:-1])
print('Элементы от начала до конца:', name[:])
