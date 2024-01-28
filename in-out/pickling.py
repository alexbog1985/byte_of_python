import pickle

# имя файла, в котором мы сохраним объект
shoplist_file = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplist_file, 'wb')
pickle.dump(shoplist, f)  # помещаем объект в файл
f.close()

del shoplist

# Считываем из хранилища
f = open(shoplist_file, 'rb')
shoplist = pickle.load(f)  # загружаем объект из файла
print(shoplist)
