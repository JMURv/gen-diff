from gendiff.gendiff import generate_diff

json_test = generate_diff(
    'gendiff/tests/fixtures/plane/json/file1.json',
    'gendiff/tests/fixtures/plane/json/file2.json'
)
yml_test = generate_diff(
    'gendiff/tests/fixtures/plane/yml/file1.yml',
    'gendiff/tests/fixtures/plane/yml/file2.yml'
)

json_and_yml_expected = 'gendiff/tests/fixtures/plane/first_test.txt'


def test_flat():
    with open(json_and_yml_expected, 'r') as file:
        result = file.read()
    assert json_test == result
    assert yml_test == result


expected_nested = 'gendiff/tests/fixtures/nested/nested_result.txt'
json_nested = generate_diff(
    'gendiff/tests/fixtures/nested/json/file1.json',
    'gendiff/tests/fixtures/nested/json/file2.json'
)
yml_nested = generate_diff(
    'gendiff/tests/fixtures/nested/yml/file1.yml',
    'gendiff/tests/fixtures/nested/yml/file2.yml'
)


def test_nested():
    with open(expected_nested, 'r') as file:
        result = file.read()
    assert json_nested == result
    assert yml_nested == result


expected_nested_plain = 'gendiff/tests/fixtures/nested/nested_result_plain.txt'
json_nested_plain = generate_diff(
    'gendiff/tests/fixtures/nested/json/file1.json',
    'gendiff/tests/fixtures/nested/json/file2.json',
    formatter='plain'
)
yml_nested_plain = generate_diff(
    'gendiff/tests/fixtures/nested/yml/file1.yml',
    'gendiff/tests/fixtures/nested/yml/file2.yml',
    formatter='plain'
)


def test_nested_plain():
    with open(expected_nested_plain, 'r') as file:
        result = file.read()
    assert json_nested_plain == result
    assert yml_nested_plain == result


expected_nested_json = 'gendiff/tests/fixtures/nested/nested_result_json.txt'
json_nested_json = generate_diff(
    'gendiff/tests/fixtures/nested/json/file1.json',
    'gendiff/tests/fixtures/nested/json/file2.json',
    formatter='json'
)
yml_nested_json = generate_diff(
    'gendiff/tests/fixtures/nested/yml/file1.yml',
    'gendiff/tests/fixtures/nested/yml/file2.yml',
    formatter='json'
)


def test_nested_json():
    with open(expected_nested_json, 'r') as file:
        result = file.read()
    assert json_nested_json == result
    assert yml_nested_json == result
