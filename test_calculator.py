#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Пользователь
#
# Created:     11.09.2022
# Copyright:   (c) Пользователь 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import datetime as dt

USD_RATE = 60.70
EURO_RATE = 60.80
date_format = '%d.%m.%Y'

print(dt.datetime.now().date())
#limit = 1000

class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date =  dt.datetime.strptime(date, date_format)  # перевести в тип данных дата?
        self.comment = comment

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        print(self.limit)
        self.records = []

    def get_today_stats(self):
        today = dt.datetime.now().date()
        today_stats = 0
        for record in self.records:
#            day_of_record = dt.datetime.strptime(value[1], date_format).date()
            if today == record.date.date():
                today_stats += record.amount
        return today_stats

    def get_week_stats(self):
        end_day = dt.datetime.now().date()
        start_day = dt.datetime.now().date() - dt.timedelta(days=6)
        week_stats = 0
        for record in self.records:
            if start_day < record.date.date() <= end_day:
                week_stats += record.amount
        return week_stats

    def add_record(self, record):
        self.records.append(record)


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_received = self.get_today_stats()
        calories_remained = self.limit - calories_received
        if calories_remained > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал"
        return "Хватит есть!"

class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency):
        valute = {
                    "rub":[1, "руб"],
                    "usd":[USD_RATE, "USD"],
                    "eur":[EURO_RATE, "Euro"]
        }
        # Округлять до сотых долей
        # balans = limit - sum(records.values())
        today_cash_spent = self.get_today_stats()
        today_cash_remained = self.limit - today_cash_spent
        balans_valute = round(today_cash_remained / valute[currency][0], 2)
        balans_string = str(balans_valute).lstrip("-")
        balans_string += " " + str(valute[currency][1])

        if today_cash_remained > 0:
            return "На сегодня осталось " +  balans_string
        elif today_cash_remained < 0:
            return "Денег нет, держись: твой долг - " + balans_string
        else:
            return "Денег нет, держись"



cash_calc = CashCalculator(2222)
r5 = Record(amount=23, comment="Безудержный шопинг", date="09.09.2022")
r6 = Record(amount=111, comment="Наполнение потребительской корзины", date="11.09.2022")
r7 = Record(amount=2222, comment="Катание на такси", date="11.09.2022")
cash_calc.add_record(r5)
cash_calc.add_record(r6)
cash_calc.add_record(r7)
print(cash_calc.records[0].comment)
print(cash_calc.get_week_stats())
print(cash_calc.get_today_stats())
print(cash_calc.get_today_cash_remained("rub"))
print(cash_calc.get_today_cash_remained("usd"))
print(cash_calc.get_today_cash_remained("eur"))

calcal = CaloriesCalculator(2200)
r14 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="11.09.2022")
r15 = Record(amount=84, comment="Йогурт.", date="10.09.2022")
r16 = Record(amount=1140, comment="Баночка чипсов.", date="01.09.2022")
for r in [r14, r15, r16]:
    calcal.add_record(r)

print(calcal.records[0].comment)
print(calcal.get_week_stats())
print(calcal.get_today_stats())
print(calcal.get_calories_remained())