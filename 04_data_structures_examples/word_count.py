## Дана строка, подсчитать частоту употребления каждого слова

s = """
Родился на улице Герцена, в гастрономе номер двадцать два. Известный
экономист, по призванию своему — библиотекарь. В народе — колхозник. В
магазине — продавец. В экономике, так сказать, необходим. Это, так
сказать, система… э-э-э… в составе ста двадцати единиц. Фотографируете
Мурманский полуостров и получаете «Те-ле-фун-кен». И бухгалтер
работает по другой линии — по линии библиотекаря. Потому что не воздух
будет, академик будет! Ну вот можно сфотографировать Мурманский
полуостров. Можно стать воздушным асом.  Можно стать воздушной
планетой. И будешь уверен, что эту планету примут по учебнику. Значит,
на пользу физике пойдёт одна планета. Величина, оторванная в область
дипломатии, даёт свои колебания на всю дипломатию. А Илья Муромец даёт
колебания только на семью на свою. Спичка в библиотеке работает. В
кинохронику ходят и зажигают в кинохронике большой лист. В библиотеке
маленький лист разжигают. Огонь… э-э-э… будет вырабатываться гораздо
легче, чем учебник крепкий. А крепкий учебник будет весомее, чем
гастроном на улице Герцена. А на улице Герцена будет расщеплённый
учебник. Тогда учебник будет проходить через улицу Герцена, через
гастроном номер двадцать два, и замещаться там по формуле
экономического единства. Вот в магазине двадцать два она может
расщепиться, экономика! На экономистов, на диспетчеров, на продавцов,
на культуру торговли… Так что, в эту сторону двинется вся экономика.
Библиотека двинется в сторону ста двадцати единиц, которые будут…
э-э-э… предмет укладывать на предмет. Сто двадцать единиц — предмет
физика. Электрическая лампочка горит от ста двадцати кирпичей, потому
что структура, так сказать, похожа у неё на кирпич. Илья Муромец
работает на стадионе «Динамо». Илья Муромец работает у себя дома. Вот
конкретная дипломатия! Открытая дипломатия — то же самое. Ну, берём
телевизор, вставляем в Мурманский полуостров, накручиваем там… э-э-э…
всё время чёрный хлеб… Так что же, будет Муромец, что ли, вырастать?
Илья Муромец, что ли, будет вырастать из этого?
"""

## Нормализуем строку:

s = s.lower()  # теперь все буквы строчные
# оставим  только буквы и пробелы
s_list = [c for c in s if c.isalpha() or c.isspace()]
s = ''.join(s_list)  # теперь это опять строка

## Подсчитаем вхождение каждого слова.
## Будем счетчик каждого слова хранить в словаре:

word_count = {}
for word in s.split():
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

for w, c in sorted(word_count.items(), key=lambda item: -item[1]):
    print(w, c)
