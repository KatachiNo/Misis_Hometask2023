def print_list(my_list):
    my_dict = {index: value for index, value in enumerate(my_list)}

    for item, amount in my_dict.items():
        print(item,amount)
    pass


def print_dict(my_dict):
    for item, amount in my_dict.items():
        print(item,amount)
    pass


def check(x):
    if type(x) == type([1,2,3]):
        print("Печатаю листик")
        print_list(x)
        print("\n\n")
    elif type(x) == type({1:2}):
        print("Печатаю словарь")
        print_dict(x)
        print("\n\n")
    else:
        print("Печатаю <вставьте>")
        print(x)
        print("\n\n")

def print_overlord(mydict):
    for _, amount in mydict.items():
        check(amount)
    pass


print("Выводим список")
print_list(["я", "не", "в", "отпуск" ])
print("\n\n")

print("Выводим словарь")
print_dict({"key1": 2, "key3": False, "Приветствие": "Hello"})
print("\n\n")


print("Выводим что-то")
check({"key1": 2, "key3": False, "Приветствие": "Hello"})
print("\n\n")

print("Выводим что-то 2")
check(["я", "не", "в", "отпуск" ])
print("\n\n")

print("Выводим что-то, но по заданию ---------------------- \n\n")
print_overlord(dict(
            key1=1,
            key2=[1, 2, 3, 4],
            key3='Hello',
            key4={"ciao":"Mondo", "Привет": "О дивный мир"}))