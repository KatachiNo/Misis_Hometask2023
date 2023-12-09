#Посчитать количество определенных слов в файле

lec = 0
pract = 0
lab = 0

with open('2.txt', 'r', encoding="UTF-8") as f:
    for e in f:
        if "лекц." in e:
            lec += 1
        elif "практ." in e:
            pract += 1
        elif "лаб." in e:
            lab += 1

print('Лекций:', lec)
print('Практических:', pract)
print('Лабораторных:', lab)