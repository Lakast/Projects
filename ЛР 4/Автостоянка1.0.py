import datetime


class CarPark:
    def __init__(self, date_of_entry, owner, vehicle, type_of_vehicle, state_number, color, paid):
        self.date_of_entry = date_of_entry
        self.owner = owner
        self.vehicle = vehicle
        self.type_of_vehicle = type_of_vehicle
        self.state_number = state_number
        self.color = color
        self. paid = paid

    def description(self): #описание
        return ("Владелец транспортного средства: {0}\nТранспортное средство: {1}\nТип транспортного средства: {2}\n"
              "Гос. номер: {3}\nЦвет транспортного средства: {4}\n".format(self.owner, self.vehicle, self.type_of_vehicle, self.state_number, self.color))

    def date(self): #дата и время
        return("Дата въезда: {0}\nЗарезервировано до: {1}".format(self.date_of_entry, self.paid))

    def stay(self): #время пребывания
        date_time1 = datetime.datetime.strptime(self.date_of_entry, '%H:%M:%S %d.%m.%Y')
        date_time2 = datetime.datetime.strptime(self.paid, '%H:%M:%S %d.%m.%Y')
        stay = date_time2 - date_time1
        return stay

    def cost(self): #общая стоимость
        null = datetime.timedelta(hours=0)
        discount_week = datetime.timedelta(days=7)
        s = self.stay()
        s_hours = round(s.seconds / 3600)
        self.price = 0
        while self.stay() > null:
            null += datetime.timedelta(hours=1)
            self.price += 100
        if s < discount_week:
            return("Стоимость за {0} д. и {1} ч. составляет {2} руб.".format(s.days, s_hours, self.price))
        else:
            self.discpr = round(self.price - (self.price * 0.07))
            return ("Стоимость за {0} д. и {1} ч. составляет {2} руб.(применен тариф недельной аренды: скидка 7%)".format(
                    s.days, s_hours, self.discpr))


    def debt(self, before): #задолжность
        print("\nДата отъезда:", before)
        date_time2 = datetime.datetime.strptime(self.paid, '%H:%M:%S %d.%m.%Y')
        date_time3 = datetime.datetime.strptime(before, '%H:%M:%S %d.%m.%Y')
        week = datetime.timedelta(days=7)
        null = datetime.timedelta(hours=0)
        debt = date_time3 - date_time2
        debt_hours = debt.seconds / 3600
        if self.stay() >= week:
            dp = self.discpr
            penalty = 0
            if debt > null:
                while debt > null:
                    null = null + datetime.timedelta(hours=1)
                    dp += 100
                    penalty += 100
                return ("Задолженность: превышен срок на {0} д. {1} ч., штраф {2} руб.\nИтого к оплате: {3} руб.".format(debt.days,
                        round(debt_hours), penalty, dp))
            elif debt < null:
                while debt < null:
                    debt = debt + datetime.timedelta(hours=1)
                    dp -= 100
                return ("Задолженность: отсутствует\nИтого к оплате: {0} руб.".format(dp))
            else:
                return ("Задолженность: отсутствует\nИтого к оплате: {0} руб.".format(dp))
        else:
            penalty = 0
            p = self.price
            if debt > null:
                while debt > null:
                    null = null + datetime.timedelta(hours=1)
                    p += 100
                    penalty += 100
                return ("Задолженность: превышен срок на {0} д. и {1} ч., штраф {2} руб.\nИтого к оплате: {3} руб.".format(debt.days,
                        round(debt_hours), penalty, p))
            elif debt < null:
                while debt < null:
                    debt = debt + datetime.timedelta(hours=1)
                    p -= 100
                return ("Задолженность: отсутствует\nИтого к оплате: {0} руб.".format(p))
            else:
                return ("Задолженность: отсутствует\nИтого к оплате: {0} руб.".format(p))


vehicle1 = CarPark("08:00:00 29.06.2022", "Игнатов Владимир Иванович", "TOYOTA Camry VII", "Легковой", "Н 005ЕМ-11", "Черный", "08:00:00 03.07.2022")
print(vehicle1.description())
print(vehicle1.date())
print(vehicle1.cost())
print(vehicle1.debt('09:00:00 04.07.2022'))
print("\n------------------------------------------------------------------------------------------\n")

vehicle2 = CarPark("15:00:00 02.02.2022", "Петров Иван Иванович", "Lada", "Легковой", "Л 450ОХ-54", "Красный", "15:00:00 09.02.2022")
print(vehicle2.description())
print(vehicle2.date())
print(vehicle2.cost())
print(vehicle2.debt('15:00:00 09.02.2022'))
