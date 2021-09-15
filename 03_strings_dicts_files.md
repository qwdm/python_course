## Строки, файлы, словари.

### Строки.

В python присутствуют строки как отдельный тип данных.
Специального типа отдельных символов нет, отдельные символы --- 
просто строки длины 1. Посмотрим, что с ними можно делать.

```python
>>> ## строки обрамляются одинарными кавычками
>>> hello = 'Hello, my name is Vasia!'  

>>> ## или двойными, без разницы
>>> london = "London is the capital of Great Britain"  

## можно разделить строку на отдельные слова
>>> london.split()
['London', 'is', 'the', 'capital', 'of', 'Great', 'Britain']

## разделять строку можно по произвольному символу
>>> row = 'foxtrot|uniform|charlie|kilo'
>>> row.split('|')
['foxtrot', 'uniform', 'charlie', 'kilo']
```

Часто бывает необходимо почистить пробельные символы на краях.
Например, при чтении текстового файла строки обычно имеют
символ новой строки на конце. 

```python
>>> s = '   woops  \t\n'
>>> s.strip()   ## слева и справа
'woops'
>>> s.lstrip()  ## слева
'woops  \t\n'
>>> s.rstrip()  ## справа
'   woops'
```

Для простых случаев обработки строк
подходят встроенные средства 
поиска и замены подстрок.
Если нужно искать целые типы подстрок
по определенным правилам, например,
все телефоны, IP-адреса или слова из трех
слогов, можно воспользоваться
регулярными выражениями (Regular Expressions)
из модуля `re`.


```python
## найти первое вхождение подстроки
>>> s = 'Аблигация или облигация?'
>>> s.find('игац')
3
>>> s.find('штаны')  ## если нет подстроки, выдает -1
-1
>>> s.index('смысл жизни')  ## метод index похож на find, но в случае неуспеха вызывает исключение
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found

## заменить все вхождения подсроки
>>> s = 'Большой кот и кот поменбше'
>>> s.replace('кот', 'пёс')
'Большой пёс и пёс поменбше'
```

Списки строк можно объединять в одну с помощью
метода `join`.

```python
>>> words = ['Let', 'it', 'be']
>>> ' '.join(words)  ## через пробел
'Let it be'

>>> letters = list('oops')  ## превращаем строку в список
>>> letters
['o', 'o', 'p', 's']
>>> letters[0] = 'p'  ## строка неизменяема, а список - изменяем
>>> letters
['p', 'o', 'p', 's']
>>> ''.join(letters)  ## объединяем в строку через пустую строку
'pops'
```

### Файлы.

Посмотрим на простейшие приемы работы с файлами на диске,
не обращая пока внимания на обработку возможных ошибок.
Файл открывается с помощью встроенной функции `open`.
Эта функция возвращает *объект файла*.
и по строкам файла можно теперь проходить циклом `for`.


```python
>>> f = open('/tmp/oops')
>>> for line in f:
...     line = line.rstrip()  ## удаляем проk
...     print(line)
    
Hey Jude, dont make it bad
Take a sad song and make it better
Remember to let her into your heart
Then you can start to make it better
```

Кроме этого, для чтения файла существуют методы 
`read`, `readline`, `readlines`. Можно почитать
про них в документации или же просто 
открыть интерпретатор и попробовать.

Для записи в файл используется второй аргумент
функции `open`: 

* 'w' перезаписывает файл новыми данными
* 'a' добавляет данные в конец файла

```python
>>> f = open('myfile.txt', 'w')
>>> f.write('Goodbye cruel world\n')
>>> f.close()
```


### Словари.

Списки в python предоставляют доступ
к их элементам по целочисленному индексу.
Если же нам хочется иметь в качестве ключа доступа
к данным не просто целые числа, а, например,
строки, то мы используем *словарь* (*dictionary*).

Например, мы хотим для каждой страны хранить ее столицу:

```python
country_capitals = {
    'Russia': 'Moscow',
    'France': 'Paris',
    'Burundi': 'Gitega',
}
print(country_capitals['Russia'])

> Moscow
```

Таким образом мы задаем пары *ключ-значение*.
Словарь в python реализован в
виде т.н. 
[Hash-таблицы](https://ru.wikipedia.org/wiki/%D0%A5%D0%B5%D1%88-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0)
и позволяет быстро (за O(1)) добавлять, читать
и удалять значение по ключу.

Итерации по словарю:
```python
## перебираем **ключи**
for country in country_capitals:
    print(country_capitals[country], 'is the capital of', country)
 
> Moscow is the capital of Russia
> Paris is the capital of France
> Gitega is the capital of Burundi

## перебираем значения
for capital in country_capitals.values():
    print(capital)

> Moscow
> Paris
> Gitega

## перебираем пары ключ-значение
for k, v in country_capitals.items():
    print(k, '->', v)

> Russia -> Moscow
> France -> Paris
> Burundi -> Gitega
```

Также часто словари используются для хранения информации
о каком-либо объекте:
```python
>>> person = {'name': 'Василий', 'age': 24, 'height': 182, 'weight': 79}
>>> person['age']
24
```

Значениями словаря могут быть другие словари, списки
и вообще, произвольные данные:

```python
player = {
    'name': 'Alexander Golovin',
    'age': 25,
    'skills': {
        'pass': 8.0,
        'endurance': 7.0,
        'kick': 8.5,
    },
    'positions': ['midfielder', 'attacking midfielder'],
}

for pos in player['positions']:
    print(pos)

> midfielder
> attacking midfielder
```
