# Перепишите ваш код для проверки расширения из прошлого ДЗ в функцию которая принимает список расширений и имя файла

def check_ext(ext, name):
    tmp = file.split(".")
    if tmp[1] in extensions:
        return "Все ок"
    else:
        return "Ваше расширение не подходит"

file = 'Моя диссертац.gif'
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

print(check_ext(extensions,file))
