from gendiff.formatters import formatting
from gendiff.dicts_diff import calculate_difference
from gendiff.parser import data_parser
VALID_EXTENSIONS = ('json', 'yml', 'yaml')


def get_data(path):
    extension = path.split('.')[-1]
    if extension in VALID_EXTENSIONS:
        with open(path, "r") as f:
            return data_parser(f.read(), extension)
    raise Exception(f"Not valid extension: {extension}")


def generate_diff(file_1, file_2, formatter='stylish'):
    data_1 = get_data(file_1)
    data_2 = get_data(file_2)
    diff = calculate_difference(data_1, data_2)
    return formatting(diff, formatter)
