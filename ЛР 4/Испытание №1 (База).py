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

    def description(self):
         return ("Владелец транспортного средства: {0}\nТранспортное средство: {1}\nТип транспортного средства: {2}\n"
              "Гос. номер: {3}\nЦвет транспортного средства: {4}\n".format(self.owner, self.vehicle, self.type_of_vehicle, self.state_number, self.color))

    def description_time(self):
         return("Дата въезда: {0}\nЗарезервировано до: {1}".format(self.date_of_entry, self.paid))

    def cost_and_debt(self, before):
        date_time1 = datetime.datetime.strptime(self.date_of_entry, '%H:%M:%S %d.%m.%Y')
        date_time2 = datetime.datetime.strptime(self.paid, '%H:%M:%S %d.%m.%Y')
        date_time3 = datetime.datetime.strptime(before, '%H:%M:%S %d.%m.%Y')
        null = datetime.timedelta(hours=0)
        discont = datetime.timedelta(days=7)
        stay = date_time2 - date_time1
        debt = date_time3 - date_time2
        stay_hours = stay.seconds / 3600
        debt_hours = debt.seconds / 3600
        cost = 0
        penalty = 0
        while date_time1 < date_time2:
            if stay >= discont:
                x = date_time1
                date_time1 = x + datetime.timedelta(hours=1)
                cost = cost + 93
            else:
                x = date_time1
                date_time1 = x + datetime.timedelta(hours=1)
                cost = cost + 100
        if stay >= discont:
            print("Стоимость за {0} д. и {1} ч. составляет {2} руб.\nПрименена скидка 7% (тариф недельной аренды)".format(stay.days, round(stay_hours), cost))
        else:
            print("Стоимость за {0} д. и {1} ч. составляет {2} руб.".format(stay.days, round(stay_hours), cost))
        print("\nДата отъезда:", before)
        if debt > null:
            while debt > null:
                null = null + datetime.timedelta(hours=1)
                cost = cost + 100
                penalty = penalty + 100
            return ("Задолженность: превышен срок на {0} ч., штраф {1} руб.\nИтого к оплате: {2} руб.".format(round(debt_hours), penalty, cost))
        elif debt < null:
            while debt < null:
                debt = debt + datetime.timedelta(hours=1)
                cost = cost - 100
            return ("Задолженность: отсутствует\nИтого к оплате: {0} руб.".format(cost))
        else:
            return ("Задолженность: отсутствует\nИтого к оплате: {0} руб.".format(cost))


vehicle1 = CarPark("08:00:00 29.06.2022", "Игнатов Владимир Иванович", "TOYOTA Camry VII", "Легковой", "Н 005ЕМ-11", "Черный", "08:00:00 02.07.2022")
print(vehicle1.description())
print(vehicle1.description_time())
print(vehicle1.cost_and_debt('05:00:00 02.07.2022'))
