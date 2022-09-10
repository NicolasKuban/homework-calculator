#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Пользователь
#
# Created:     10.09.2022
# Copyright:   (c) Пользователь 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал», если лимит limit не достигнут,
#или «Хватит есть!», если лимит достигнут или превышен.

limit = 1000
records = {"today": [200, "2022-09-09", "Magnit"], "yestuday": [90, "2022-09-10", "five"], "tomorow":[10, "2022-09-10","Lux"]}


def get_calories_remained():
    calories_received = 0 # Потрачено
    for value in records.values():
        calories_received += value[0]
    calories_remained = limit - calories_received
    if calories_remained > 0:
        return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал"
    return "Хватит есть!"

print(get_calories_remained())
print(get_calories_remained())
print(get_calories_remained())

