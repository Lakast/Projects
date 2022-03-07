import math

def main():
    a = check_a()
    b = check_b()
    c = check_c()
    if a+b > c:
        if a+c > b:
            if b+c > a:
                print("Треугольник существует")
                p = (a + b + c)/2
                S = math.sqrt(p*(p-a)*(p-b)*(p-c))
                print("Площадь треугольника: ", round(S, 2))
            else:
                print("Треугольник не существует")
        else:
            print("Треугольник не существует")
    else:
        print("Треугольник не существует")


def check_a():
    while True:
        try:
            a = float(input("Длина стороны a: "))
            if a <= 0:
                raise ValueError()
            return a
        except ValueError:
            print("Некорректные данные. Пожалуйста, попробуйте еще раз")

def check_b():
    while True:
        try:
            b = float(input("Длина стороны b: "))
            if b <= 0:
                raise ValueError()
            return b
        except ValueError:
            print("Некорректные данные. Пожалуйста, попробуйте еще раз")

def check_c():
    while True:
        try:
            c = float(input("Длина стороны c: "))
            if c <= 0:
                raise ValueError()
            return c
        except ValueError:
            print("Некорректные данные. Пожалуйста, попробуйте еще раз")
main()
