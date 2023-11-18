

print("Введите первую переменную")
num1 = int(input())

print("Введите вторую переменную")
num2 = int(input())


while True:
    print("Выберите одну из операций и введите её - ' + - * / '")
    operation = input()

    match operation:
        case "+":
            print(num1 + num2)
            break

        case "-":
            print(num1 - num2)
            break

        case "*":
            print(num1 * num2)
            break

        case "/":
            print(num1 / num2)
            break

        case _:
            print("Чет не то, попробуй снова")