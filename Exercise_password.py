pw = input("Введите ваш новый пароль: ")

try:
    pw1 = 5/len(pw)
    pw1 = int(pw)
    print("Ваш пароль состоит только из цифр")
except ZeroDivisionError:
    print("Вы ввели пустой пароль")
except ValueError:
    print("Требования к паролю соблюдены !!!")

#print(pw)
#print(len(pw))