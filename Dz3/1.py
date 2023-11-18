# Напишите функцию, извлекающую корень n-й степени из числа x. По умолчанию def будет извлекать квадратный корень:
import math
def sqrt_new(x, n=2):
    print(math.pow(x,1/n))


sqrt_new(4,2)


sqrt_new(4)

sqrt_new(4,4)