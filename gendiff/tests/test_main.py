from gendiff import generate_diff
import pytest


@pytest.mark.parametrize(
    ('test_1', 'test_2', 'expected'),
    [
        pytest.param(
            'gendiff/tests/fixtures/plane/json/file1.json',
            'gendiff/tests/fixtures/plane/json/file2.json',
            'gendiff/tests/fixtures/plane/first_test.txt'
        ),
        pytest.param(
            'gendiff/tests/fixtures/plane/yml/file1.yml',
            'gendiff/tests/fixtures/plane/yml/file2.yml',
            'gendiff/tests/fixtures/plane/first_test.txt'
        ),
    ]
)
def test_flat(test_1, test_2, expected):
    with open(expected, 'r') as f:
        result = f.read()
    assert generate_diff(test_1, test_2) == result


@pytest.mark.parametrize(
    ('test_1', 'test_2', 'expected'),
    [
        pytest.param(
            'gendiff/tests/fixtures/nested/json/file1.json',
            'gendiff/tests/fixtures/nested/json/file2.json',
            'gendiff/tests/fixtures/nested/nested_result'
        ),
        pytest.param(
            'gendiff/tests/fixtures/nested/yml/file1.yml',
            'gendiff/tests/fixtures/nested/yml/file2.yml',
            'gendiff/tests/fixtures/nested/nested_result'
        )
    ]
)
def test_nested_stylish(test_1, test_2, expected):
    with open(expected, 'r') as f:
        result = f.read()
    assert generate_diff(test_1, test_2) == result


@pytest.mark.parametrize(
    ('test_1', 'test_2', 'formatter', 'expected'),
    [
        pytest.param(
            'gendiff/tests/fixtures/nested/json/file1.json',
            'gendiff/tests/fixtures/nested/json/file2.json',
            'plain',
            'gendiff/tests/fixtures/nested/nested_result_plain'
        ),
        pytest.param(
            'gendiff/tests/fixtures/nested/yml/file1.yml',
            'gendiff/tests/fixtures/nested/yml/file2.yml',
            'plain',
            'gendiff/tests/fixtures/nested/nested_result_plain'
        )
    ]
)
def test_nested_plain(test_1, test_2, formatter, expected):
    with open(expected, 'r') as f:
        result = f.read()
    assert generate_diff(test_1, test_2, formatter='plain') == result


@pytest.mark.parametrize(
    ('test_1', 'test_2', 'formatter', 'expected'),
    [
        pytest.param(
            'gendiff/tests/fixtures/nested/json/file1.json',
            'gendiff/tests/fixtures/nested/json/file2.json',
            'json',
            'gendiff/tests/fixtures/nested/nested_result_json'
        ),
        pytest.param(
            'gendiff/tests/fixtures/nested/yml/file1.yml',
            'gendiff/tests/fixtures/nested/yml/file2.yml',
            'json',
            'gendiff/tests/fixtures/nested/nested_result_json'
        )
    ]
)
def test_nested_json(test_1, test_2, formatter, expected):
    with open(expected, 'r') as f:
        result = f.read()
    assert generate_diff(test_1, test_2, formatter='json') == result


def test_format_error():
    with pytest.raises(Exception):
        generate_diff('file.exe', 'file_1.exe')


def test_formatter_error():
    with pytest.raises(Exception):
        generate_diff(
            'gendiff/tests/fixtures/nested/yml/file1.yml',
            'gendiff/tests/fixtures/nested/yml/file2.yml',
            'error'
        )
