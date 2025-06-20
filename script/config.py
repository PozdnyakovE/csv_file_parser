import argparse


def parser_config():
    'Конфигурация аргументов для запуска скрипта.'
    parser = argparse.ArgumentParser(description='Обработка csv-файла')
    parser.add_argument(
        '-f', '--file', type=str, help='Путь к файлу', required=True)
    parser.add_argument(
        '-w', '--where', type=str,
        help=('Фильтрация по полю (больше, меньше, равно). '
              'Пример: raiting>4.6.'))
    parser.add_argument(
        '-a', '--aggregate', type=str,
        help=('Агрегация с расчетом среднего, минимального,'
              'максимального значения. Пример: raiting=min.'))
    return parser
