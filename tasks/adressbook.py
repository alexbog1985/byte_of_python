class Person:
    """Записи адресной книги"""
    def __init__(self, name, surname, address, email, phone):
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email
        self.phone = phone


address_book = {}
run = True

while run:
    name = input('Введите имя --> ')
    surname = input('Введите фамилию --> ')
    address = input('Введите адрес --> ')
    email = input('Ведите почту --> ')
    phone = input('Введите телефон --> ')

    address_book[surname] = Person(name, surname, address, email, phone)
    break
print(address_book[surname].__dict__)