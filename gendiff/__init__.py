from gendiff.formatters.main import choose_formatter
from gendiff.build_diff import generate_keys
from gendiff.parser import data_parser


def generate_diff(file_1, file_2, formatter='stylish'):
    data_1 = data_parser(file_1)
    data_2 = data_parser(file_2)
    diff = generate_keys(data_1, data_2)
    return choose_formatter(diff, formatter)

