from gendiff.formatters import formatting
from gendiff.dicts_diff import build_diff_for_key
from gendiff.parser import data_parser


def generate_diff(file_1, file_2, formatter='stylish'):
    data_1 = data_parser(file_1)
    data_2 = data_parser(file_2)
    diff = build_diff_for_key(data_1, data_2)
    return formatting(diff, formatter)
