"""
The Common Log Format --- standardized text file format
used by web servers when generating server log files.

host ident authuser date request status bytes
127.0.0.1 - - [27/Sep/2021 22:44:12] "GET /some/data.html HTTP/1.1" 200 -
"""

import random
import time
import datetime

NUM_LINES = 1024


start_timestamp = time.time() - 86400 * 300


def _weighted_choice(seq, weights=None):
    if isinstance(seq, dict):
        value_weights = seq.items()
        values = [vw[0] for vw in value_weights]
        weights = [vw[1] for vw in value_weights]
        return random.choices(values, weights=weights)[0]
    else:
        return random.choices(seq, weights=weights)[0]



def host():
    subnet = '192.168.0.'
    host = str(random.randint(1, 127))
    return subnet + host


def ident():
    return '-'


def authuser():
    return '-'


def date(_timestamp=[start_timestamp]):
    d = datetime.datetime.fromtimestamp(_timestamp[0])
    _timestamp[0] += 4 * random.random()
    return d.strftime('[%d/%b/%Y %H:%M:%S]')


def request():
    def method():
        return _weighted_choice({
                'GET': 9,
                'POST': 1,
        })


    def path(method):

        random_path = "{}/{}/{}".format(
            random.choice(['user', 'message', 'comment']),
            random.randint(132, 4322),
            _weighted_choice({'': 20, 'update': 3, 'delete': 1}),
        )

        if method == 'POST':
            return random_path
        elif method == 'GET':
            return _weighted_choice({
                '/': 100,
                '/static/style.css': 100,
                '/user/profile': 10,
                '/newsfeed': 20,
                random_path: 50,
            })


    method = method()
    path = path(method)

    return f'"{method} {path} HTTP/1.1"'


def status():
    return str(_weighted_choice({
        200: 100,
        400: 5,
        403: 2,
        404: 5,
        500: 1,
    }))


def bytes():
    return '-'


def create_log_line():
    return f"{host()} {ident()} {authuser()} {date()} {request()} {status()} {bytes()}"


if __name__ == '__main__':
    for _ in range(NUM_LINES):
        print(create_log_line())
