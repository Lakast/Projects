import sqlite3
import datetime
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import *
from tkinter import ttk


class Main:
    def __init__(self):
        root = Tk()
        self.master = root
        self.master.title("Автостоянка")
        screenWidth = self.master.winfo_screenwidth()  # Получить ширину зоны отображения
        screenHeight = self.master.winfo_screenheight()  # Получить высоту области отображения
        width = 553  # Установите ширину окна
        height = 500  # Установите высоту окна
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        # Ширина х высота + x смещение + y смещение
        # Указанное окно - положение смещения окна относительно верхнего левого угла экрана на основе установки ширины и высоты.
        self.master.geometry("%dx%d+%d+%d" % (width, height, left, top))
        img_png = PhotoImage(file='Park.png', width=550)
        label_img = Label(root, image=img_png)
        label_img.place(x=0, y=0)

        menu = Menu(self.master)
        new_item = Menu(menu)
        new_item.add_command(label='Новый')
        new_item.add_separator()
        new_item.add_command(label='Изменить')
        menu.add_cascade(label='Файл', menu=new_item)
        menu.add_cascade(label='Отчеты')
        menu.add_cascade(label='Правка')
        menu.add_cascade(label='Помощь')

        self.master.config(menu=menu)

        BtEntry = Button(self.master, text="Въезд", background="#484A47", foreground="#FFFFFF", width=10, height=1,
                         font='Arial 18', command=self.new_window)
        BtEntry.place(x=67, y=50)

        BtLeave = Button(self.master, text="Выезд", background="#484A47", foreground="#FFFFFF", width=10, height=1,
                         font="Arial 18", command=self.leave)
        BtLeave.place(x=217, y=50)

        BtReport = Button(self.master, text="Отчет", background="#484A47", foreground="#FFFFFF", width=10, height=1,
                          font="Arial 18", command=self.report)
        BtReport.place(x=367, y=50)

        self.master.mainloop()

    def new_window(self):
        self.master.destroy()
        Entry_record()

    def leave(self):
        self.master.destroy()
        Leave_record()

    def report(self):
        table = Table(Tk())
        table.pack(expand=1, fill=BOTH)
        table.mainloop()

def validate(new_value):
    return new_value == "" or new_value.isnumeric()

class Entry_record:
    def __init__(self):
        root = Tk()
        self.entry = root
        self.entry.title("Запись нового клиента")
        screenWidth = self.entry.winfo_screenwidth()
        screenHeight = self.entry.winfo_screenheight()
        width = 520
        height = 510
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.entry.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.entry.configure(bg='#484A47')

        LabDat = Label(self.entry, text="Данные о транспортном средстве", background='#484A47', foreground="#FFFFFF", font="Roboto 16")
        LabDat.place(x=20, y=10)

        LabSt_num = Label(self.entry, text="Гос. номер:",  background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabSt_num.place(x=20, y=45)
        self.EntSt_num = Entry(self.entry, width=15, font="Roboto 14")
        self.EntSt_num.place(x=20, y=75)

        LabVeh_type = Label(self.entry, text="Тип ТС:", background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabVeh_type.place(x=220, y=45)
        self.ComVeh_type = Combobox(self.entry, width=15, font="Roboto 14", state='readonly')
        self.ComVeh_type['values'] = ("Легковой", "Мотоцикл", "Грузовой", "Автобус")
        self.ComVeh_type.current(0)
        self.ComVeh_type.place(x=220, y=75)

        LabVehMake = Label(self.entry, text="Марка и модель ТС:", background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabVehMake.place(x=20, y=115)
        self.EntVehMake = Entry(self.entry, width=25, font="Roboto 14")
        self.EntVehMake.place(x=20, y=145)

        LabVehMake = Label(self.entry, text="Цвет ТС:", background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabVehMake.place(x=330, y=115)
        self.EntVehColor = Entry(self.entry, width=15, font="Roboto 14")
        self.EntVehColor.place(x=330, y=145)

        LabDat = Label(self.entry, text="Данные о владельце", background='#484A47', foreground="#FFFFFF", font="Roboto 16")
        LabDat.place(x=20, y=190)

        LabFIO = Label(self.entry, text="ФИО владельца:", background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabFIO.place(x=20, y=225)
        self.EntFIO = Entry(self.entry, width=43, font="Roboto 14")
        self.EntFIO.place(x=20, y=255)

        LabTel = Label(self.entry, text="Телефон владельца:", background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabTel.place(x=20, y=295)
        self.v = (self.entry.register(validate), '%P')
        self.EntTel = Entry(self.entry, width=43, font="Roboto 14", validate='key', validatecommand=self.v)
        self.EntTel.place(x=20, y=325)

        LabDatEnt = Label(self.entry, text="Дата въезда:", background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabDatEnt.place(x=20, y=365)
        self.EntDatEnt = EntryWithPlaceholder(self.entry, "ЧЧ:ММ ДД.ММ.ГГ")
        self.EntDatEnt.place(x=20, y=395, height=27, width=225)
        self.EntDatEnt["font"] = "14"
        self.EntDatEnt["validate"] = "key"

        LabRes = Label(self.entry, text="Зарезирвировано до:", background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabRes.place(x=272, y=365)
        self.EntRes = EntryWithPlaceholder(self.entry, "ЧЧ:ММ ДД.ММ.ГГ")
        self.EntRes.place(x=272, y=395, height=27, width=225)
        self.EntRes["font"] = "14"

        self.Record = Button(self.entry, text="Записать", background="#008000", foreground="#FFFFFF", font="Roboto 14",
                             height=2, width=20, command=self.new_record)
        self.Record.place(x=20, y=440)

        self.BtBack = Button(self.entry, text="Главное меню", background="#D5AB22", foreground="#FFFFFF", font="Roboto 14",
                             height=2, width=20, command=self.back)
        self.BtBack.place(x=272, y=440)



    def new_record(self):
        try:
            connenction = sqlite3.connect("base.db")
            cursor = connenction.cursor()
            print("Подключен к SQLite")

            parking = [(self.EntFIO.get(), self.EntTel.get(), self.ComVeh_type.get(), self.EntVehMake.get(),
                        self.EntSt_num.get(), self.EntVehColor.get(), self.EntDatEnt.get(), self.EntRes.get(), '')]
            cursor.executemany('''INSERT INTO parking VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', parking)
            connenction.commit()
            print("Запись успешно обновлена")
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if connenction:
                connenction.close()
                print("Соединение с SQLite закрыто")
                self.entry.destroy()
                Main()

    def back(self):
        self.entry.destroy()
        Main()

class Leave_record:
    def __init__(self):
        root = Tk()
        self.leave = root
        screenWidth = self.leave.winfo_screenwidth()
        screenHeight = self.leave.winfo_screenheight()
        width = 250
        height = 250
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.leave.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.leave.configure(bg='#484A47')
        self.leave.title("Запись выезда клиента")


        LabSt_num = Label(self.leave, text="Гос. номер ТС:", background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabSt_num.place(x=5, y=2)
        self.EntSt_num = Entry(self.leave, width=20, font="Roboto 14")
        self.EntSt_num.place(x=10, y=30)

        LabSt_num = Label(self.leave, text="Время выезда:", background='#484A47', foreground="#FFFFFF", font="Roboto 14")
        LabSt_num.place(x=5, y=70)
        self.EntLeave = Entry(self.leave, width=20, font="Roboto 14")
        self.EntLeave.place(x=10, y=100)

        self.BtAddLeave = Button(self.leave, text="Запись", background="#008000", foreground="#FFFFFF", height=1,
                                 width=15, font="Roboto 14", command=self.update_table)
        self.BtAddLeave.place(x=40, y=150)

        self.BtAddLeave = Button(self.leave, text="Главное меню", background="#D5AB22", foreground="#FFFFFF", height=1,
                                 width=15, font="Roboto 14", command=self.back)
        self.BtAddLeave.place(x=40, y=200)

    def update_table(self):
        try:
            sqlite_connection = sqlite3.connect('base.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")
            sql_update_query = """Update parking set leave = ? where state_number = ?"""
            data = (self.EntLeave.get(), self.EntSt_num.get())
            cursor.execute(sql_update_query, data)
            sqlite_connection.commit()
            print("Запись успешно обновлена")
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                num = self.EntSt_num.get()
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
                self.leave.destroy()
                Check(num)

    def back(self):
        self.leave.destroy()
        Main()



class Check():
    def __init__(self, p):
        root = Tk()
        self.check = root
        screenWidth = self.check.winfo_screenwidth()
        screenHeight = self.check.winfo_screenheight()
        width = 500
        height = 560
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.check.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.check.configure(bg='#FFFFFF')
        self.check.title("Чек клиента")


        self.Lab = Label(self.check, text="****************************ЧЕК******************************",
                         background="#FFFFFF", foreground="#000000", font="Roboto 16")
        self.Lab.place(x=0, y=2)

        self.check.LabFIO = Label(self.check, text="ФИО владельца:", background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.LabFIO.place(x=5, y=40)
        self.check.FIO = Label(self.check, background="#FFFFFF", foreground="#000000", font="Roboto 11")
        self.check.FIO.place(x=140, y=41)

        self.check.LabTel = Label(self.check, text="Телефон владельца:", background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.LabTel.place(x=5, y=80)
        self.check.Tel = Label(self.check, background="#FFFFFF", foreground="#000000", font="Roboto 11")
        self.check.Tel.place(x=170, y=81)

        self.check.LabVeh_type = Label(self.check, text="Тип ТС:", background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.LabVeh_type.place(x=5, y=120)
        self.check.Veh_type = Label(self.check, background="#FFFFFF", foreground="#000000", font="Roboto 11")
        self.check.Veh_type.place(x=66, y=121)

        self.check.LabVehMake = Label(self.check, text="Марка и модель ТС:", background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.LabVehMake.place(x=5, y=160)
        self.check.VehMake = Label(self.check, background="#FFFFFF", foreground="#000000", font="Roboto 11")
        self.check.VehMake.place(x=164, y=161)

        self.check.LabSt_num = Label(self.check, text="Гос. номер:", background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.LabSt_num.place(x=5, y=200)
        self.check.St_num = Label(self.check, background="#FFFFFF", foreground="#000000", font="Roboto 11")
        self.check.St_num.place(x=98, y=201)

        self.check.LabVehColor = Label(self.check, text="Цвет ТС:", background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.LabVehColor.place(x=5, y=240)
        self.check.VehColor = Label(self.check, background="#FFFFFF", foreground="#000000", font="Roboto 11")
        self.check.VehColor.place(x=78, y=241)

        self.check.LabDatEnt = Label(self.check, text="Дата въезда:", background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.LabDatEnt.place(x=5, y=280)
        self.check.DatEnt = Label(self.check, background="#FFFFFF", foreground="#000000", font="Roboto 11")
        self.check.DatEnt.place(x=112, y=281)

        self.check.LabRes = Label(self.check, text="Зарезирвировано до:", background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.LabRes.place(x=5, y=320)
        self.check.Res = Label(self.check, background="#FFFFFF", foreground="#000000", font="Roboto 11")
        self.check.Res.place(x=172, y=321)

        self.check.Cost = Label(self.check, width=0, background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.Cost.place(x=5, y=360)

        self.check.LabLea = Label(self.check, text="Дата выезда:", background="#FFFFFF", foreground="#000000", font="Roboto 13")
        self.check.LabLea.place(x=5, y=400)
        self.check.Lea = Label(self.check, background="#FFFFFF", foreground="#000000", font="Roboto 11")
        self.check.Lea.place(x=112, y=401)


        self.check.Debt = Label(self.check, width=55, background="#FFFFFF", foreground="#000000", font="Roboto 11 bold")
        self.check.Debt.place(x=0, y=440)

        self.BtBack = Button(self.check, text="Печать", background="#008000", foreground="#FFFFFF", height=1,
                                 width=15, font="Roboto 14", command=self.back)
        self.BtBack.place(x=165, y=510)


        try:
            sqlite_connection = sqlite3.connect('base.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")
            t = (p,)
            cursor.execute("SELECT * FROM parking WHERE state_number=?", t)
            info = cursor.fetchone()
            self.check.owner = info[0]
            self.check.phone = info[1]
            self.check.vehicle_type = info[2]
            self.check.make_and_model = info[3]
            self.check.state_number = info[4]
            self.check.color = info[5]
            self.check.entry = info[6]
            self.check.reserved = info[7]
            self.check.leave = info[8]

            self.check.FIO['text'] = self.check.owner
            self.check.FIO['text'] = self.check.owner
            self.check.Tel['text'] = self.check.phone
            self.check.Veh_type['text'] = self.check.vehicle_type
            self.check.VehMake['text'] = self.check.make_and_model
            self.check.St_num['text'] = self.check.state_number
            self.check.VehColor['text'] = self.check.color
            self.check.DatEnt['text'] = self.check.entry
            self.check.Res['text'] = self.check.reserved
            self.check.Lea['text'] = self.check.leave
            self.check.Cost['text'] = self.cost()
            self.check.Debt['text'] = self.debt()
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    def back(self):
        self.check.destroy()
        Main()


    def stay(self): #время пребывания
        date_time1 = datetime.datetime.strptime(self.check.entry, '%H:%M %d.%m.%Y')
        date_time2 = datetime.datetime.strptime(self.check.reserved, '%H:%M %d.%m.%Y')
        stay = date_time2 - date_time1
        return stay

    def cost(self): #общая стоимость
        null = datetime.timedelta(hours=0)
        discount_week = datetime.timedelta(days=7)
        self.s = self.stay()
        self.s_hours = round(self.s.seconds / 3600)
        self.price = 0
        while self.stay() > null:
                null += datetime.timedelta(hours=1)
                self.price += 100
        if self.s < discount_week:
            self.result = "Стоимость за {0} д. и {1} ч. составляет {2} руб.".format(self.s.days, self.s_hours, self.price)
            return self.result
        else:
            self.price = round(self.price - (self.price * 0.07))
            self.result = "Стоимость за {0} д. и {1} ч. составляет {2} руб.(применен тариф недельной аренды: скидка 7%)".format(
                    self.s.days, self.s_hours, self.price)
            return self.result


    def debt(self): #задолженность
        date_time2 = datetime.datetime.strptime(self.check.reserved, '%H:%M %d.%m.%Y')
        date_time3 = datetime.datetime.strptime(self.check.leave, '%H:%M %d.%m.%Y')
        week = datetime.timedelta(days=7)
        null = datetime.timedelta(hours=0)
        debt = date_time3 - date_time2
        debt_hours = debt.seconds / 3600
        if self.stay() >= week:
            dp = self.price
            penalty = 0
            if debt > null:
                while debt > null:
                    null = null + datetime.timedelta(hours=1)
                    dp += 100
                    penalty += 100
                return ("Задолженность: превышен срок на {0} д. {1} ч., штраф {2} руб.\n\nИтого к оплате: {3} руб.".format(debt.days,
                        round(debt_hours), penalty, dp))
            elif debt < null:
                while debt < null:
                    debt = debt + datetime.timedelta(hours=1)
                    dp -= 100
                return ("Задолженность: отсутствует\n\nИтого к оплате: {0} руб.".format(dp))
            else:
                return ("Задолженность: отсутствует\n\nИтого к оплате: {0} руб.".format(dp))
        else:
            penalty = 0
            p = self.price
            if debt > null:
                while debt > null:
                    null = null + datetime.timedelta(hours=1)
                    p += 100
                    penalty += 100
                return ("Задолженность: превышен срок на {0} д. и {1} ч., штраф {2} руб.\n\nИтого к оплате: {3} руб.".format(debt.days,
                        round(debt_hours), penalty, p))
            elif debt < null:
                while debt < null:
                    debt = debt + datetime.timedelta(hours=1)
                    p -= 100
                return ("Задолженность: отсутствует\n\nИтого к оплате: {0} руб.".format(p))
            else:
                return ("Задолженность: отсутствует\n\nИтого к оплате: {0} руб.".format(p))

class Table(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        screenWidth = parent.winfo_screenwidth()  # Получить ширину зоны отображения
        screenHeight = parent.winfo_screenheight()  # Получить высоту области отображения
        width = 600  # Установите ширину окна
        height = 300  # Установите высоту окна
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        # Ширина х высота + x смещение + y смещение
        # Указанное окно - положение смещения окна относительно верхнего левого угла экрана на основе установки ширины и высоты.
        parent.geometry("%dx%d+%d+%d" % (width, height, left, top))
        parent.title("История клиентов")


        with sqlite3.connect('base.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM parking")
            data = (row for row in cursor.fetchall())
        headings = ('ФИО', 'Телефон', 'Тип ТС', 'Марка и модель', 'Гос. номер', 'Цвет', 'Въезд',
                    'Забронировано', 'Выезд')
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(0, anchor=tk.CENTER, width=200)
            table.column(1, anchor=tk.CENTER, width=80)
            table.column(2, anchor=tk.CENTER, width=80)
            table.column(3, anchor=tk.CENTER, width=120)
            table.column(4, anchor=tk.CENTER, width=80)
            table.column(5, anchor=tk.CENTER, width=70)
            table.column(6, anchor=tk.CENTER, width=120)
            table.column(7, anchor=tk.CENTER, width=120)
            table.column(8, anchor=tk.CENTER, width=120)

        for row in data:
            table.insert('', tk.END, values=tuple(row))

        # scrollbar
        scrolltable_y = tk.Scrollbar(table, orient='vertical')
        scrolltable_x = Scrollbar(table, orient='horizontal')
        table.configure(yscrollcommand=scrolltable_y.set, xscrollcommand=scrolltable_x.set)

        scrolltable_y.pack(side=RIGHT, fill=tk.Y,)
        scrolltable_x.pack(side=BOTTOM, fill=tk.X,)
        scrolltable_x.config(command=table.xview)
        scrolltable_y.config(command=table.yview)
        table.pack(expand=1, fill=BOTH)

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


if __name__ == '__main__':
    Main()
