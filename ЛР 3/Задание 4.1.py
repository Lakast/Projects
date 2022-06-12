import random

def main():
    mas = []
    for i in range(0, 10):
        n = random.randint(1, 100)
        mas.append(n)
    print('Массив: ', mas)
    maximum = max(mas)
    minimum = min(mas)
    print('Максимальный элемент массива: ', maximum)
    print('Минимальный элемент массива: ', minimum)
    for i in range(len(mas)):
        if mas[i] == maximum:
            mas[i] = minimum
        elif mas[i] == minimum:
            mas[i] = maximum
    print('Измененный массив: ', mas)

main()