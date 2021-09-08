""" Умножитель на 2 """

while True:
    ans = int(input('Введите число, для завершения 0: '))
    if not ans:
        print('До свидания!')
        break
    print(ans, '* 2 =', ans * 2)
