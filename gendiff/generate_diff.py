import argparse
import copy
import json


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("-f", '--format', help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(
        generate_diff(args.first_file, args.second_file))


def bool_checker(file1):
    new = {}
    keys = file1.keys()
    for value in keys:
        if type(file1[value]) == bool:
            new[value] = str(file1[value]).lower()
        else:
            new[value] = file1[value]
    return new


def generate_diff(file_path_1, file_path_2):
    source_1 = json.load(open(f'{file_path_1}'))
    source_2 = json.load(open(f'{file_path_2}'))
    source_1 = bool_checker(source_1)
    source_2 = bool_checker(source_2)
    keys_1, keys_2 = set(source_1.keys()), set(source_2.keys())
    all_keys = sorted(keys_1 | keys_2)
    diff = '{\n'
    for key in all_keys:
        if key in keys_1 & keys_2:
            if source_1[key] == source_2[key]:
                diff += f'    {key}: {source_1[key]}\n'
            else:
                diff += f'  - {key}: {source_1[key]}\n'
                diff += f'  + {key}: {source_2[key]}\n'

        elif key in keys_1 and key not in keys_2:
            diff += f'  - {key}: {source_1[key]}\n'

        else:
            diff += f'  + {key}: {source_2[key]}\n'
    diff += '}'
    return diff


# print(generate_diff('test/file1.json', 'test/file2.json'))

