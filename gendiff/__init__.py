from gendiff.formatters import formatting
from gendiff.dicts_diff import calculate_difference
from gendiff.parser import data_parser
FORMATS = ('json', 'yml', 'yaml')


def data_open(path):
    format = path.split('.')[-1]
    if format in FORMATS:
        with open(path, "r") as f:
            return data_parser(f.read(), format)
    else:
        raise Exception(f"Not valid format: {format}")


def generate_diff(file_1, file_2, formatter='stylish'):
    data_1 = data_open(file_1)
    data_2 = data_open(file_2)
    diff = calculate_difference(data_1, data_2)
    return formatting(diff, formatter)
