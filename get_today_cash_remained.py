#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Пользователь
#
# Created:     09.09.2022
# Copyright:   (c) Пользователь 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

USD_RATE = 60.70
EURO_RATE = 60.80

limit = 1000
records = {"today": [200, "2022-09-09", "Magnit"], "yestuday": [1790, "2022-09-10", "five"], "tomorow":[10, "2022-09-10","Lux"]}


def get_today_cash_remained(currency):
    valute = {
                "rub":[1, "руб"],
                "usd":[USD_RATE, "USD"],
                "eur":[EURO_RATE, "Euro"]
    }
    # Округлять до сотых долей
    # balans = limit - sum(records.values())
    spent = 0 # Потрачено
    for value in records.values():
        spent += value[0]
    balans = limit - spent
    balans_valute = round(balans / valute[currency][0], 2)
    balans_string = str(balans_valute).lstrip("-")
    balans_string += " " + str(valute[currency][1])

    if balans > 0:
        return "На сегодня осталось " +  balans_string
    elif balans < 0:
        return "Денег нет, держись: твой долг - " + balans_string
    else:
        return "Денег нет, держись"


print(get_today_cash_remained("rub"))
print(get_today_cash_remained("usd"))
print(get_today_cash_remained("eur"))


