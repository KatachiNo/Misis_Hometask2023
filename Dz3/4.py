def sum_num(x):
    y = str(x)
    sum = 0
    for i in y:
        sum += int(i)
    return sum



print(sum_num("355"))
print(sum_num(355))
