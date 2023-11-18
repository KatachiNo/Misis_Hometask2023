## Задача 1 Какой месяц

import datetime

month = 1

monthString = datetime.date(1900, month, 1).strftime('%B')

print(monthString)
