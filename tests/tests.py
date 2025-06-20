import sys
import pytest

from main import main
from script.utils import (
    aggregate_values,
    file_reader,
    filter_values,
    tabulate_print
)
from script.validators import argument_structure_check, check_field_name_exists


def test_check_field_name_exists_ok():
    data = [{'name': 'Alice', 'score': 95}]
    check_field_name_exists('name', data)


def test_check_field_name_exists_error():
    data = [{'name': 'Alice', 'score': 95}]
    with pytest.raises(ValueError, match='Поле не найдено'):
        check_field_name_exists('age', data)


def test_argument_structure_check_ok():
    pattern = r'\w+[=><].+'
    argument = 'rating>4.6'
    argument_structure_check(pattern, argument)


def test_argument_structure_check_error():
    pattern = r'\w+[=><].+'
    argument = 'some_bad_words'
    with pytest.raises(ValueError, match='Аргумент не распознан'):
        argument_structure_check(pattern, argument)


def test_file_reader(tmp_path):
    file_path = tmp_path / 'test.csv'
    file_content = "name,score\nAlice,95\nBob,80"
    file_path.write_text(file_content)

    result = file_reader(str(file_path))
    assert result == [
        {'name': 'Alice', 'score': '95'}, {'name': 'Bob', 'score': '80'}]


def test_filter_values():
    data = [
        {'name': 'Alice', 'score': '95'},
        {'name': 'Bob', 'score': '80'}
    ]
    result_eq = filter_values(data, 'score=95')
    result_gt = filter_values(data, 'score>85')
    result_lt = filter_values(data, 'score<82')
    assert result_eq == [{'name': 'Alice', 'score': '95'}]
    assert result_gt == [{'name': 'Alice', 'score': '95'}]
    assert result_lt == [{'name': 'Bob', 'score': '80'}]


def test_aggregate():
    data = [{'value': '10'}, {'value': '20'}, {'value': '18'}]
    min_res = aggregate_values(data, 'value=min')
    max_res = aggregate_values(data, 'value=max')
    avg_res = aggregate_values(data, 'value=avg')
    assert min_res == [{'min': 10.0}]
    assert max_res == [{'max': 20.0}]
    assert avg_res == [{'avg': 16.0}]


def test_tabulate_print(capsys):
    data = [{'name': 'Alice', 'score': 95}]
    tabulate_print(data)
    captured = capsys.readouterr()
    assert 'Alice' in captured.out


def test_main_with_real_file(tmp_path):
    test_csv = tmp_path / 'test.csv'
    test_csv.write_text("name,score\nAlice,95\nBob,80")
    sys_argv_backup = sys.argv
    sys.argv = [
        'script_name',
        '-f', str(test_csv),
        '-w', 'score>85',
        '-a', 'score=avg'
    ]

    try:
        main()
    finally:
        sys.argv = sys_argv_backup
