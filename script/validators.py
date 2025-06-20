import re


def check_field_name_exists(field_name, data) -> Exception | None:
    for item in data:
        if field_name not in list(item.keys()):
            raise ValueError(
                'Поле не найдено'
            )


def argument_structure_check(pattern, argument) -> Exception | None:
    if not re.match(pattern, argument):
        raise ValueError(
            'Аргумент не распознан'
        )
