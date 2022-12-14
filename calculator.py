#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Пользователь
#
# Created:     08.09.2022
# Copyright:   (c) Пользователь 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import datetime as dt

USD_RATE = 60.70
EURO_RATE = 60.80
date_format = '%d.%m.%Y'

class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date =  dt.datetime.strptime(date, date_format)
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
