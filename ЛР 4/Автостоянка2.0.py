import datetime


class CarPark:
    def __init__(self):
        print("\nВведите данные о владельце и транспортном средстве")
        self.owner = input("ФИО владельца ТС: ")
        self.vehicle = input("Тип ТС: ")
        self.type_of_vehicle = input("Марка и модель ТС: ")
        self.state_number = input("Гос. номер: ")
        self.color = input("Цвет ТС: ")

        print("\nВведите данные для учета времени")
        self.date_of_entry = input("Дата въезда: ")
        self. paid = input("Зарезервировано до: ")

        print("\nВведите данные для закрытия чека")
        self.before = input("Дата отъезда: ")

    def info(self):
        return self.date_of_entry, self.owner, self.vehicle, self.type_of_vehicle, self.state_number, self.color, self.paid

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
            return("\nСтоимость за {0} д. и {1} ч. составляет {2} руб.\n".format(s.days, s_hours, self.price))
        else:
            self.discpr = round(self.price - (self.price * 0.07))
            return ("\nСтоимость за {0} д. и {1} ч. составляет {2} руб.(применен тариф недельной аренды: скидка 7%)\n".format(
                    s.days, s_hours, self.discpr))


    def debt(self): #задолжность
        date_time2 = datetime.datetime.strptime(self.paid, '%H:%M:%S %d.%m.%Y')
        date_time3 = datetime.datetime.strptime(self.before, '%H:%M:%S %d.%m.%Y')
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

    def check(self):
        return "\n*******************ЧЕК*******************" "\nВладелец транспортного средства: {0}\nТранспортное средство: {1}" \
               "\nТип транспортного средства: {2}\n" "Гос. номер: {3}\nЦвет транспортного средства: {4}\n \nДата въезда:" \
               "{5} \nЗарезервировано до: {6} \n{7} \nДата отъезда: {8} \n{9} \n*****************************************"\
            .format(self.owner, self.vehicle, self.type_of_vehicle, self.state_number, self.color,self.date_of_entry,
                    self.paid, self.cost(), self.before, self.debt())


def print_table(data, cell_sep=' | ', header_separator=True):
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [data[row][col] for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)

    for i, row in enumerate(range(rows)):
        if i == 1 and header_separator:
            print(separator)

        result = []
        for col in range(cols):
            item = data[row][col].rjust(col_width[col])
            result.append(item)

        print(cell_sep.join(result))


def main():
    vehicle1 = CarPark()
    #"08:00:00 29.06.2022", "Игнатов Владимир Иванович", "TOYOTA Camry VII", "Легковой", "Н 005ЕМ-11", "Черный",
    # "08:00:00 03.07.2022"
    print(vehicle1.check())

    table_data = [['Дата въезда', 'Владелец', 'Марка', 'Тип автомобиля', 'Номер', 'Цвет', 'Оплачено до'],
        vehicle1.info()]
    #print_table(table_data)

main()



