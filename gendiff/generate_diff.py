import json


def bool_checker(file1):
    new = {}
    keys = file1.keys()
    for value in keys:
        if type(file1[value]) == bool:
            new[value] = str(file1[value]).lower()
        else:
            new[value] = file1[value]
    return new


# def generate_diff(file_path_1, file_path_2):
#     source_1 = json.load(open(f'{file_path_1}'))
#     source_2 = json.load(open(f'{file_path_2}'))
#     source_1 = bool_checker(source_1)
#     source_2 = bool_checker(source_2)
#     keys_1, keys_2 = set(source_1.keys()), set(source_2.keys())
#     all_keys = sorted(keys_1 | keys_2)
#     diff = '{\n'
#     for key in all_keys:
#         if key in keys_1 & keys_2:
#             if source_1[key] == source_2[key]:
#                 diff += f'    {key}: {source_1[key]}\n'
#             else:
#                 diff += f'  - {key}: {source_1[key]}\n'
#                 diff += f'  + {key}: {source_2[key]}\n'
#
#         elif key in keys_1 and key not in keys_2:
#             diff += f'  - {key}: {source_1[key]}\n'
#
#         else:
#             diff += f'  + {key}: {source_2[key]}\n'
#     diff += '}'
#     return diff


def generate_diff(file_path_1, file_path_2):
    source_1 = json.load(open(f'{file_path_1}'))
    source_2 = json.load(open(f'{file_path_2}'))
    source_1 = bool_checker(source_1)
    source_2 = bool_checker(source_2)
    keys_1, keys_2 = set(source_1.keys()), set(source_2.keys())
    all_keys = sorted(keys_1 | keys_2)
    diff = {}
    for key in all_keys:
        if key in keys_1 & keys_2:
            if source_1[key] == source_2[key]:
                diff[key] = {
                    'action': 'nothing',
                    'value': source_1[key]
                }
            else:
                diff[key] = {
                    'action': 'changed',
                    'old value': source_1[key],
                    'new value': source_2[key]
                }
        elif key in keys_1 and key not in keys_2:
            diff[key] = {
                'action': 'deleted',
                'old value': source_1[key]
            }
        else:
            diff[key] = {
                'action': 'added',
                'value': source_2[key]
            }
    return diff


# print(generate_diff('tests/fixture/file1.json', 'tests/fixture/file2.json'))
