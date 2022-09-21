from gendiff.parser import data_parser


def bool_checker(file1):
    new = {}
    keys = file1.keys()
    for value in keys:
        if type(file1[value]) == bool:
            new[value] = str(file1[value]).lower()
        elif file1[value] is None:
            new[value] = 'null'
        else:
            new[value] = file1[value]
    return new


def open_files_and_check(file_1):
    file_1 = bool_checker(data_parser(file_1))
    return file_1


def generate_keys(source_1, source_2, all_keys):
    diff = {}
    for key in all_keys:
        if key in source_1 and key not in source_2:
            diff[key] = {
                'action': 'deleted',
                'old value': source_1.get(key)
            }
        elif key not in source_1 and key in source_2:
            diff[key] = {
                'action': 'added',
                'value': source_2.get(key)
            }

        elif type(source_1[key]) == dict and type(source_2[key]) == dict:
            diff[key] = {
                'action': 'recursive call',
                'result': generate_diff(source_1[key], source_2[key])
            }

        elif key in source_1 and key in source_2:
            if source_1.get(key) == source_2.get(key):
                diff[key] = {
                    'action': 'not changed',
                    'value': source_2.get(key)
                }

            else:
                diff[key] = {
                    'action': 'changed',
                    'old value': source_1.get(key),
                    'new value': source_2.get(key)
                }
    return diff


def generate_diff(file_path_1, file_path_2):
    source_1 = open_files_and_check(file_path_1)
    source_2 = open_files_and_check(file_path_2)
    keys_1, keys_2 = set(source_1.keys()), set(source_2.keys())
    all_keys = sorted(keys_1 | keys_2)
    return generate_keys(source_1, source_2, all_keys)


# print(generate_diff(
#     'tests/fixture/recursive/file1.json', 'tests/fixture/recursive/file2.json'
# ))
