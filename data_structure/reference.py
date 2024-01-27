print('Простое присваивание')
shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shop_list  # mylist - лишь еще одно имя, указывающее на тот же объект1

del shop_list[0]

print('shop_list:', shop_list)
print('mylist:', mylist)
# Обратите внимание, что и shop_list, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один объект.

print('Копирование при помощи полной вырезки')
mylist = shop_list[:]  # Создаём копию путём полной вырезки
del mylist[0]

print('shop_list:', shop_list)
print('mylist:', mylist)
# Обратите внимание, что теперь списки разные
