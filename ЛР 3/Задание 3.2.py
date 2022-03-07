def main():
    min_x = check_min_x()
    max_x = check_max_x()
    step = check_step()
    print("\nЗначение x    Значение y")
    while min_x <= max_x:
        y = -0.5 * min_x + min_x
        print("  ", min_x, "        ", y)
        min_x += step

def check_min_x():
    while True:
        try:
            min_x = float(input("Введите минимальное значение x: "))
            if min_x <= 0:
                raise ValueError()
            return min_x
        except ValueError:
            print("Некорректные данные. Пожалуйста, попробуйте еще раз")

def check_max_x():
    while True:
        try:
            max_x = float(input("Введите максимальное значение x: "))
            if max_x <= 0:
                raise ValueError()
            return max_x
        except ValueError:
            print("Некорректные данные. Пожалуйста, попробуйте еще раз")

def check_step():
    while True:
        try:
            step = float(input("Введите значение с каким шагом будет изменяться x: "))
            if step <= 0:
                raise ValueError()
            return step
        except ValueError:
            print("Некорректные данные. Пожалуйста, попробуйте еще раз")

main()