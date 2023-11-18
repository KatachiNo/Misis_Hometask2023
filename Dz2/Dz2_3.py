# Задача 3 Проверка расширения файла

file='Моя диссертац.gif'
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

tmp = file.split(".")
if tmp[1] in extensions:
    print("Все ок")
else:
    print("Ваше расширение не подходит")