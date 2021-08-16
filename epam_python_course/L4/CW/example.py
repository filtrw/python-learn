"""
Пример, который приводили в лекции. По его образцу нужно выполнить домашнее задание по рейтингу студентов
(см task4_top_of_students)
Составляется таблица по Аэропортам и прибытию рейсов, рейсы в таблице по каждому аэропорту сортируются по
времени прибытия:

AIRPORT LED
B513       ---> 123121
A213       ---> 123221
AIRPORT MSK
X613       ---> 113212
A618       ---> 133211
A615       ---> 162121
"""


def get_data():
    return [
        {'flight': 'A213', 'arrived_at': 123221, 'airport': 'LED'},
        {'flight': 'B513', 'arrived_at': 123121, 'airport': 'LED'},
        {'flight': 'X613', 'arrived_at': 113212, 'airport': 'MSK'},
        {'flight': 'A615', 'arrived_at': 162121, 'airport': 'MSK'},
        {'flight': 'A618', 'arrived_at': 133211, 'airport': 'MSK'}
    ]


def get_airports(data):
    return {item['airport'] for item in data}


def get_flights(data, airport):
    return sorted([(item['flight'], item['arrived_at']) for item in data if item['airport'] == airport],
                  key=lambda x: x[1])


def get_flights_table(airport):
    return 'AIRPORT {}\n'.format(airport) + \
           '\n'.join('{:10} ---> {:4}'.format(*flight)
                     for flight in get_flights(get_data(), airport))


if __name__ == '__main__':
    print('\n'.join(get_flights_table(airport) for airport in get_airports(get_data())))
