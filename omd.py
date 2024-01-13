def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'В баре сказали: "С зонтиками вход запрещён!"\n'
        'К счастью, у утки были с собой с собой краски\n'
        'Она залила зонтик жёлтым цветом и снова пошла в бар\n'
        'Все подумали, что утка принесла солнышко, и с радостью обслужили её\n'
        'Конец!\n'
    )


def step2_no_umbrella():
    print(
        'Выпив камышовый фреш и закусив моллюсками, героиня собралась домой\n'
        'Как назло, в этот момент начался сильный ливень\n'
        'Наша уточка очень боялась замочить краски и инструменты,'
        'которые взяла в бар с собой\n'
        'Поэтому решила заказать птиц-такси\n'
        'Оказалось, в этот день для всех маляров пролёт сделали бесплатным, '
        'и уточка, счастливая и сухая, быстро добралась до дома\n'
        'Конец!\n'
    )


if __name__ == '__main__':
    step1()