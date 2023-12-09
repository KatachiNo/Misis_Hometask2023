## Средний бал и список отстающих учеников

num = 0
le = 0
with open('1.txt', 'r', encoding="UTF-8") as f:
    for e in f:
        le += 1
        num += int(e.split(" ")[2].replace("\n", ""))

average = num / le

print("Средний балл", average)

print("Список отстающих учеников (те у кого ниже среднего балла)")

with open('1.txt', 'r', encoding="UTF") as f:
    for e in f:
        num = int(e.split(" ")[2].replace("\n", ""))
        if num < average:
            print(e.replace("\n", ""))
