password = input('Введите пароль: ')
result = 0
number = 1

try:
    result = number/len(password)
    result = int(password)
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except ValueError:
    print('Требования к паролю соблюдены')
 