from sys import exit  # to exit the program from the menu
from collections import defaultdict  # for convenient initialization


def print_menu() -> None:
    """
    Вывод на экран меню для дальнейшего выбора пользователем
    необходимого функционала.
    """
    print("Выберите необходимое действие:")
    print("1 - Вывести иерархию команд")
    #  департамент и все команды, входящие в него
    print("2 - Вывести на экран сводный отчёт по департаментам")
    #  название, численность, вилка зп, ср. зп
    print("3 - Сохранить сводный отчёт в файл 'output.csv'")
    #  команду 2 перед этим вызывать необязательно
    print("4 - Завершить программу")


def choice():
    """
    Выполнение действий, необходимых пользователю.
    Предполагается, что работа не прекращается до тех пор, пока
    пользователь сам не закроет программу (нажатием цифры 4).
    """
    choose = int(input())
    match choose:
        case 1:
            dep_and_teams()
        case 2:
            print_report_to_screen(create_report())
        case 3:
            print_report_to_file(create_report())
        case 4:
            exit()
        case _:
            print('Неверный ввод. Повторите попытку.\n')
    print_menu()
    choice()


def dep_and_teams() -> dict | None:
    """
    Вывод на экран информации о каждом департаменте
    (название и перечень всех его команд).
    Инофрмацию берём из входного файла. Игнорируем первую строку
    с заголовоками столбцов (в функции для этого введён EXAMPLE)
    Возвращает ничего или словарь, где ключи - названия департаментов,
    а значения - списки из относящихся к данному департаменту команд
    """
    deps = defaultdict(set)
    EXAMPLE = 'Департамент'
    with open('Corp_Summary.csv', 'r', encoding='utf-8') as table:
        for line in table:
            line = line.strip().split(';')
            cur_dep, cur_team = line[1], line[2]
            if cur_dep != EXAMPLE:  # чтобы игнорировать шапку таблицы
                deps[cur_dep].add(cur_team)
    for dep, team in deps.items():
        print(f' {dep}: ', end='\n')
        for cur_team in team:
            print(f'\t->{cur_team}', end='\n')
        print()
    return deps


def create_report() -> dict:
    """
    Создаётся отчёт в виде словаря, где ключами являются названия команд,
    а значениями - списки, несущие информацию о:
    -> количестве сотрудников в департаменте
    -> минимальной зп в департаменте
    -> максимальной зп в департаменте
    -> общей зп, выделяемой на весь департамент
    -> средней зп на одного сотрудника департамента
    Инофрмацию берём из входного файла. Игнорируем первую строку
    с заголовоками столбцов (в функции для этого введён EXAMPLE)
    """
    deps = {}
    EXAMPLE = 'Департамент'
    with open('Corp_Summary.csv', 'r', encoding='utf-8') as table:
        for line in table:
            line = line.strip().split(';')
            cur_dep = line[1]
            if cur_dep != EXAMPLE:
                cur_wage = int(line[5])
                if cur_dep not in deps:
                    deps[cur_dep] = {'num_employees': 1,
                                     'min_salary': cur_wage,
                                     'max_salary': cur_wage,
                                     'total_salary': cur_wage
                                     }
                    #  численность, мин. зп, макс. зп, общая зп на весь департ.
                else:
                    deps[cur_dep]['num_employees'] += 1
                    if cur_wage < deps[cur_dep]['min_salary']:
                        deps[cur_dep]['min_salary'] = cur_wage
                    if cur_wage > deps[cur_dep]['max_salary']:
                        deps[cur_dep]['max_salary'] = cur_wage
                    deps[cur_dep]['total_salary'] += cur_wage
    for dep_values in deps.values():
        dep_values['average_salary'] = round(dep_values['total_salary'] /
                                             dep_values['num_employees'], 2)
        #  добавляем информацию о средней зп в каждом департаменте
    return deps


def print_report_to_screen(deps: dict) -> None:
    """
    Вывод сгенерированного отчёта на экран. На входе словарь специального вида,
    описанный в функции create_report. На выходе - ничего
    """
    for dep, data in deps.items():
        print(f'Департамент: {dep}\n'
              f'Численность: {data['num_employees']}\n'
              f'Минимальная зарплата: {data['min_salary']}\n'
              f'Максимальная зарплата: {data['max_salary']}\n'
              f'Общая зарплата, выделяемая на департамент: {data['total_salary']}\n'
              f'Средняя зарплата: {data['average_salary']}\n\n'
              )


def print_report_to_file(deps: dict, output: str = 'output.csv') -> None:
    """
    Вывод сгенерированного отчёта в файл. На входе словарь специального вида,
    описанный в функции create_report. На выходе - ничего
    """
    with open(output, 'w', encoding='utf-16') as out_file:
        for dep, data in deps.items():
            out_file.write(
                f'Департамент: {dep}\n'
                f'Численность: {data['num_employees']}\n'
                f'Минимальная зарплата: {data['min_salary']}\n'
                f'Максимальная зарплата: {data['max_salary']}\n'
                f'Общая зарплата, выделяемая на департамент: {data['total_salary']}\n'
                f'Средняя зарплата: {data['average_salary']}\n\n'
                )


if __name__ == '__main__':
    print_menu()
    choice()
