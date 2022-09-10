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

import datetime as dt
date_format = '%d.%m.%Y'

records = {
            "today":    [200, "09.09.2022", "Magnit"],
            "yestuday": [1790, "10.09.2022", "five"],
            "tomorow":  [10, "08.09.2022","Lux"]
}

def get_week_stats():
    end_day = dt.datetime.now().date()
    start_day = dt.datetime.now().date() - dt.timedelta(days=6)
    total = 0
    for value in records.values():
        day_of_record = dt.datetime.strptime(value[1], date_format).date()
        if start_day < day_of_record <= end_day:
            total += value[0]
    return total



print(get_week_stats())


