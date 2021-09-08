""" примеры на цикл for """

## массив

a = [1, 23, 37, 48, 11, 34]
print(a)

## сумма и произведение элементов

summa = 0
product = 1
for n in a:
    summa += n
    product *= n

print('Сумма =', summa)
print('Произведение =', product)

## разделим на два списка: четных и нечетных
odd = []
even = []
for n in a:
    if n % 2:
        odd.append(n)
    else:
        even.append(n)

print('Четные:', even)
print('Heчетные:', odd)

print()  # отделим мух от котлет
## линейный поиск: есть ли в списке слово, начинающееся на 'ку'
words = ['пряник', 'прокрастинация', 'кусок', 'куролесить']
print(words)
for w in words:
    if w.startswith('ку'):
        print('Есть! Вот на ку:', w)
        break
else:  ## в том случае, если break никогда не случился
    print('Таких слов не имеется')
