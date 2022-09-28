from gendiff.formatters.main import choose_formatter
from gendiff.parser import data_parser


def calculate_difference(source_1, source_2, key):
    if key in source_1 and key not in source_2:
        return {
            'action': 'deleted',
            'old value': source_1[key]
        }
    elif key not in source_1 and key in source_2:
        return {
            'action': 'added',
            'value': source_2[key]
        }
    elif type(source_1[key]) == dict and type(source_2[key]) == dict:
        return {
            'action': 'recursive call',
            'children': generate_keys(source_1[key], source_2[key])
        }
    elif source_1[key] == source_2[key]:
        return {
            'action': 'not changed',
            'value': source_2[key]
        }
    elif source_1[key] != source_2[key]:
        return {
            'action': 'changed',
            'old value': source_1[key],
            'new value': source_2[key]
        }


def generate_keys(source_1, source_2):
    keys_1, keys_2 = set(source_1.keys()), set(source_2.keys())
    all_keys = sorted(keys_1 | keys_2)
    difference = {}
    for key in all_keys:
        difference[key] = calculate_difference(source_1, source_2, key)
    return difference


def generate_diff(file_1, file_2, formatter='stylish'):
    data_1 = data_parser(file_1)
    data_2 = data_parser(file_2)
    diff = generate_keys(data_1, data_2)
    return choose_formatter(diff, formatter)
