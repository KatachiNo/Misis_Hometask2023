# Нужно проверить, все ли числа в последовательности уникальны.

numbers=[1,4,5]


if len(numbers) == len(set(numbers)):
    print("Уникальны")
else:
    print("не уникальны")