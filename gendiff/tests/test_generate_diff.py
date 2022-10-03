from gendiff import generate_diff
import pytest
import os


def build_fixture_path(filepath):
    return os.path.join('gendiff', 'tests', 'fixtures', filepath)


@pytest.mark.parametrize(
    ('test_1', 'test_2', 'formatter', 'expected'),
    [
        pytest.param(
            'file1_plane.json',
            'file2_plane.json',
            'stylish',
            'first_test.txt'
        ),
        pytest.param(
            'file1_plane.yml',
            'file2_plane.yml',
            'stylish',
            'first_test.txt'
        ),
        pytest.param(
            'file1.json',
            'file2.json',
            'stylish',
            'nested_result'
        ),
        pytest.param(
            'file1.yml',
            'file2.yml',
            'stylish',
            'nested_result'
        ),
        pytest.param(
            'file1.json',
            'file2.json',
            'plain',
            'nested_result_plain'
        ),
        pytest.param(
            'file1.yml',
            'file2.yml',
            'plain',
            'nested_result_plain'
        ),
        pytest.param(
            'file1.json',
            'file2.json',
            'json',
            'nested_result_json'
        ),
        pytest.param(
            'file1.yml',
            'file2.yml',
            'json',
            'nested_result_json'
        )
    ]
)
def test_gen_diff(test_1, test_2, formatter, expected):
    test_1 = build_fixture_path(test_1)
    test_2 = build_fixture_path(test_2)
    expected = build_fixture_path(expected)
    with open(expected, 'r') as f:
        result = f.read()
        assert generate_diff(test_1, test_2, formatter) == result


def test_extension_error():
    with pytest.raises(Exception) as error:
        generate_diff('file.exe', 'file_1.exe')
    assert error.value.args[0] == 'Not valid extension: exe'


def test_formatter_error():
    with pytest.raises(Exception) as error:
        generate_diff(
            build_fixture_path('file1.json'),
            build_fixture_path('file2.json'),
            'error'
        )
    assert error.value.args[0] == 'formatter not found: error'
