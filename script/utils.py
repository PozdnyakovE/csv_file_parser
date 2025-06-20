import csv
from tabulate import tabulate

from .validators import argument_structure_check, check_field_name_exists


COMPARE_SYMBOLS = ['=', '>', '<']
WHERE_ARGUMENT_PATTERN = r'\w+[=><].+'
AGGREGATION_ARGUMENT_PATTERN = r'\w+=(min|max|avg)$'


def file_reader(file) -> list[dict]:
    'Функция считывания файла.'
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(
            csvfile,
            delimiter=',',
            quoting=csv.QUOTE_MINIMAL,
        )
        file_contents = [row for row in reader]
        return file_contents


def filter_values(data, argument) -> list[dict]:
    'Фильтрация строк файла по указанному полю.'
    argument_structure_check(WHERE_ARGUMENT_PATTERN, argument)
    for symbol in COMPARE_SYMBOLS:
        if symbol in argument:
            index = argument.find(symbol)
            break
    field_name: str = argument[:index]
    check_field_name_exists(field_name, data)
    value: str = argument[index+1:]
    result: list = []
    for item in data:
        if symbol == '=':
            if item[field_name] == value:
                result.append(item)
        if symbol == '>':
            try:
                if float(item[field_name]) > float(value):
                    result.append(item)
            except ValueError:
                if item[field_name] > value:
                    result.append(item)
        if symbol == '<':
            try:
                if float(item[field_name]) < float(value):
                    result.append(item)
            except ValueError:
                if item[field_name] < value:
                    result.append(item)
    return result


def aggregate_values(data, argument) -> list[dict]:
    'Агрегирование значений.'
    argument_structure_check(AGGREGATION_ARGUMENT_PATTERN, argument)
    index: str = argument.find('=')
    field_name: str = argument[:index]
    check_field_name_exists(field_name, data)
    value: str = argument[index+1:]
    values_for_aggregation = []
    for item in data:
        try:
            values_for_aggregation.append(float(item[field_name]))
        except ValueError:
            raise ValueError(
                'Агрегация доступна только для числовых значений'
            )
    if value == 'min':
        return [{value: min(values_for_aggregation)}]
    if value == 'max':
        return [{value: max(values_for_aggregation)}]
    if value == 'avg':
        return [
            {value: sum(values_for_aggregation)/len(values_for_aggregation)}
            ]


def tabulate_print(value):
    print(tabulate(value, headers='keys', tablefmt="grid"))
