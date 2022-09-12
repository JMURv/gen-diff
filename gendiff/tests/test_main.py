from gendiff.generate_diff import generate_diff
import pytest

perem = generate_diff('gendiff/tests/fixture/file1.json', 'gendiff/tests/fixture/file1.json')

expected = 'gendiff/tests/fixture/result.txt'
with open(expected, 'r') as file:
    result = file.read()


def test_main():
    assert perem == result
