def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == text[::-1]


something = input('Введите текст: ')

if is_palindrome(something):
    print('Да, это палиндром')
else:
    print("Нет, это не палиндром")
