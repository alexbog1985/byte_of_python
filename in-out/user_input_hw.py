import string


def is_palindrome(text):
    """Проверка на палиндром"""
    return text == text[::-1]


def replace_punctuation(text):
    """Приводит к нижнему регистру и убирает знаки пунктуации"""
    text = text.lower()
    text = text.replace(string.punctuation, '')
    return text


something = replace_punctuation(input('Введите текст: '))

if is_palindrome(something):
    print('Да, это палиндром')
else:
    print("Нет, это не палиндром")
