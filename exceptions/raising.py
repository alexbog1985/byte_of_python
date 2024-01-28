class ShortInputException(Exception):
    """Пользовательский класс исключения."""
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input("Введите что-нибудь --> ")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Здесь может проходить обычная работа
except EOFError:
    print("Ну зачем вы сделали мне EOF?")
except ShortInputException as ex:
    print(f'ShortInputException: Длина введенной строки -- {ex.length}; '
          f'ожидалось, как минимум, {ex.atleast}')
else:
    print('Не было исключений.')
