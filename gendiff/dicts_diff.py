

def build_diff_for_key(source_1, source_2, key):
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
            'children': calculate_difference(source_1[key], source_2[key])
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


def calculate_difference(source_1, source_2):
    keys_1, keys_2 = set(source_1.keys()), set(source_2.keys())
    all_keys = sorted(keys_1 | keys_2)
    difference = {}
    for key in all_keys:
        difference[key] = build_diff_for_key(source_1, source_2, key)
    return difference
