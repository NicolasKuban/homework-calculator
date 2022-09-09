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
moment = dt.datetime.strptime('16.12.2019', date_format)
day = moment.date()
now = dt.datetime.now()
day = now.date()

class Record:
     def __inti__():
        self.amount = 0
        self.date =  dt.datetime.now().date() # перевести в тип данных дата?
        self.comment = "пустая запись"

class Calculator(limit):
    def __init__():
        self.limit = limit
        self.records = []

    def get_today_stats():
        day = dt.datetime.now().date()
        total = 0
        for record in self.records:
            if record.date == day:
                total += record.amount
        return total

    def get_week_stats():
        stop_day = dt.datetime.now().date()
        start_day = dt.datetime.now().date() - 7
        total = 0
        for record in self.records:
            if stop_day > record > start_day:
                total += record.amount
        return total


    def add_record(record):
        self.records.append(record)





class CashCalculator(Calculator):

    def get_today_cash_remained(currency):
        valute = {"rub":1, "usd":USD_RATE,"eur":EURO_RATE}
        # Округлять до сотых долей
        ostatok = limit - sum(records.values)
        if current_sum > 0:
            return f"На сегодня осталось {ostatok} руб/USD/Euro"
        elif current_sum < 0:
            return f"Денег нет, держись: твой долг - {ostatok} руб/USD/Euro"
        else:
            return "Денег нет, держись"



class CaloriesCalculator(Calculator):
    def add_record():
        pass

    def get_today_stats():
        pass

    def get_calories_remained():
        # Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал», если лимит limit не достигнут,
        #или «Хватит есть!», если лимит достигнут или превышен.
        pass

    def get_week_stats():
        pass









# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))

print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб

cash_calculator = CashCalculator(1000)

r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

cash_calculator = CaloriesCalculator(1000)

r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")