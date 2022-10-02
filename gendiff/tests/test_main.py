from gendiff import generate_diff
import pytest
import os


def build_fixture_path(filepath):
    return os.path.join('gendiff', 'tests', 'fixtures', filepath)


@pytest.mark.parametrize(
    ('test_1', 'test_2', 'formatter', 'expected'),
    [
        pytest.param(
            build_fixture_path('file1_plane.json'),
            build_fixture_path('file2_plane.json'),
            'stylish',
            build_fixture_path('first_test.txt')
        ),
        pytest.param(
            build_fixture_path('file1_plane.yml'),
            build_fixture_path('file2_plane.yml'),
            'stylish',
            build_fixture_path('first_test.txt')
        ),
        pytest.param(
            build_fixture_path('file1.json'),
            build_fixture_path('file2.json'),
            'stylish',
            build_fixture_path('nested_result')
        ),
        pytest.param(
            build_fixture_path('file1.yml'),
            build_fixture_path('file2.yml'),
            'stylish',
            build_fixture_path('nested_result')
        ),
        pytest.param(
            build_fixture_path('file1.json'),
            build_fixture_path('file2.json'),
            'plain',
            build_fixture_path('nested_result_plain')
        ),
        pytest.param(
            build_fixture_path('file1.yml'),
            build_fixture_path('file2.yml'),
            'plain',
            build_fixture_path('nested_result_plain')
        ),
        pytest.param(
            build_fixture_path('file1.json'),
            build_fixture_path('file2.json'),
            'json',
            build_fixture_path('nested_result_json')
        ),
        pytest.param(
            build_fixture_path('file1.yml'),
            build_fixture_path('file2.yml'),
            'json',
            build_fixture_path('nested_result_json')
        )
    ]
)
def test_gen_diff(test_1, test_2, formatter, expected):
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
