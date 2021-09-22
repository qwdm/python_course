""" Разбираем конфиг:
key = value

Возможности:
можно пустые строки
распознает int и float значения
"""

## функция, разбирающая одну содержательную строку
def get_key_value(line):
    sep = '='
    k, v = [item.strip() for item in line.split(sep, 1)]

    # конвертирующие функции сложим в список и пробуем по очереди:
    for converter in [int, float]:
        try:
            v = converter(v)
        except ValueError:
            pass
        else:
            break

    return k, v

## функция: принимает имя файла, возвращает словарь конфигурации
def read_cfg(fname):
    cfg = {}
    with open(fname) as f:
        for line in f:
            # пропустим пустую строку
            if not line.rstrip():
                continue
            k, v = get_key_value(line)
            cfg[k] = v
    return cfg

if __name__ == '__main__':
    conf = read_cfg('my.cfg')
    for k, v in conf.items():
        # тут мы применяем форматную строку
        print(f"{k} -> {v} :: {type(v)}")
