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



import datetime as dt
date_format = '%d.%m.%Y'

limit = 1000

records = {
            "today":    [200, "09.09.2022", "Magnit"],
            "yestuday": [1790, "10.09.2022", "five"],
            "yestuday1": [90, "10.09.2022", "five"],
            "yestuday2": [17, "10.09.2022", "five"],
            "tomorow":  [10, "08.09.2022","Lux"]
}


def get_today_stats():
    today = dt.datetime.now().date()
    today_stats = 0
    for value in records.values():
        day_of_record = dt.datetime.strptime(value[1], date_format).date()
        if today == day_of_record:
            today_stats += value[0]
    return today_stats

def get_calories_remained():
    calories_received = get_today_stats()
    calories_remained = limit - calories_received
    if calories_remained > 0:
        return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал"
    return "Хватит есть!"

#    if calories_remained > 0:
#        print()
#        #return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал"
#    return "Хватит есть!"


print(get_today_stats())
print(get_calories_remained())
