from gendiff.generate_diff import generate_diff, generate_keys
import pytest

perem = generate_diff('gendiff/tests/fixture/file1.json', 'gendiff/tests/fixture/file2.json')

expected = 'gendiff/tests/fixture/result.txt'
with open(expected, 'r') as file:
    result = file.read()


def test_main():
    assert str(perem) == str(result)
