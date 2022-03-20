import datetime
date_time_str1 = '08:00:00 2022-06-29'
date_time_str2 = '08:00:00 2022-06-30'
date_time_obj1 = datetime.datetime.strptime(date_time_str1, '%H:%M:%S %Y-%m-%d')
date_time_obj2 = datetime.datetime.strptime(date_time_str2, '%H:%M:%S %Y-%m-%d')
default = datetime.timedelta(days=1)
discont = datetime.timedelta(days=7)
dvz = date_time_obj1
dot = date_time_obj2
print("Дата въезда", dvz.strftime("%H:%M:%S %d-%m-%Y"))
print("Дата отъезда", dot.strftime("%H:%M:%S %d-%m-%Y"))
delta = date_time_obj2-date_time_obj1
deltas = delta.seconds/3600
cost = 0
while date_time_obj1 < date_time_obj2:
    if delta > discont:
        x = date_time_obj1
        date_time_obj1 = x + datetime.timedelta(hours=1)
        cost = cost + 93
    else:
        x = date_time_obj1
        date_time_obj1 = x + datetime.timedelta(hours=1)
        cost = cost + 100
if delta >= default:
    print("Стоимость за {0} д. и {1} ч. составляет {2} рублей".format(delta.days, round(deltas), cost))
else:
    print("Стоимость за {0} ч. составляет  рублей {1}".format(round(deltas), cost))