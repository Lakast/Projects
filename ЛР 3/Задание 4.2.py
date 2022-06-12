import statistics

def main():
    mas = []
    n = 1
    print('Заполните массив')
    for i in range(10):
        mas.append(int(input('Число {0}: '.format(n))))
        n += 1
    print('\nМассив: ', mas)
    m = statistics.mean(mas)
    print("\nСреднее арефметическое массива: ", m)

    for i in range(len(mas)):
        if mas[i] > m:
            mas[i] = 1

    print('\nИзмененный массив: ', mas)


main()