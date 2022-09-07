from gendiff.generate_diff import generate_diff
import pytest


def test_main(file_1, file_2, expected):
    with open(expected, 'r') as file:
        result = file.read()
    assert generate_diff(file_1, file_2) == result
