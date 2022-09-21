from gendiff.generate_diff import generate_diff

json_func = generate_diff(
    'gendiff/tests/fixture/file1.json',
    'gendiff/tests/fixture/file2.json'
)
json_expected = 'gendiff/tests/fixture/result.txt'


def test_json():
    with open(json_expected, 'r') as file:
        result = file.read()
    assert json_func == result


yml_func = generate_diff(
    'gendiff/tests/fixture/file1.yml',
    'gendiff/tests/fixture/file2.yml'
)


def test_yml():
    with open(json_expected, 'r') as file:
        result = file.read()
    assert yml_func == result


json_expected_recursive = 'gendiff/tests/fixture/recursive/result.txt'
json_recursive = generate_diff(
    'gendiff/tests/fixture/recursive/file1.json',
    'gendiff/tests/fixture/recursive/file2.json'
)


def test_json_recursive():
    with open(json_expected_recursive, 'r') as file:
        result = file.read()
    assert json_recursive == result
