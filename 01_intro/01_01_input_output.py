""" Пример на ввод и вывод """

def explicit():
    # чтение строк
    a = input()
    b = input()

    # преобразование к числам
    a = int(a)
    b = int(b)

    # вычисление суммы
    summa = a + b

    # вывод
    print(summa)


def implicit():
    a = int(input())
    b = int(input())
    print(a + b)


def oneliner():
    print(int(input()) + int(input()))


if __name__ == '__main__':
    oneliner()


