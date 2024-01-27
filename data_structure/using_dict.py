# 'ab' - сокращение от 'a'ddress'b'ook

ab = {'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'mats@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }

print("Адрес Swaroop'a:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']

print(f'\nВ адресной книге {len(ab)} контакта\n')

for name, address in ab.items():
    print(f'Контакт {name} с адресом {address}')

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])
