# Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.

import re

dict = {}

with open('5.txt', 'r', encoding="UTF-8") as f:
    for e in f:
        clean_text = re.sub(r'[^\w\s]', '', e)
        splited_text = clean_text.split(" ")
        for word in splited_text:
            lword = word.lower()
            lword = lword.replace("\n","")
            if lword not in dict:
                dict[lword] = 1
            else:
                dict[lword] += 1

print("Самое частовстречающееся слово  .. ", max(dict, key=dict.get), " .. оно встречается ", dict[max(dict, key=dict.get)],"раз")


max_l = 0
w = ""
for word in dict:
    if len(word) > max_l:
        w = word
        max_l = len(word)

print("самое длинное слово",w,"его длина ", max_l)



print("-------------")
print(dict)