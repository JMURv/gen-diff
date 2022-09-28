INDENT = '    '


def dict_diff(value, depth=2):
    if value is None:
        return 'null'
    elif type(value) == str:
        return value
    elif type(value) != dict:
        return str(value).lower()
    result = "{\n"
    for k, v in value.items():
        result += f"{INDENT * depth}{k}: "
        result += f"{dict_diff(v, depth + 1)}\n"
    result += INDENT * (depth - 1) + "}"
    return result


def string_formatter(key, value, depth):
    result = ''
    action = value['action']
    if action == 'added':
        result += f"{INDENT * depth}   + {key}: "
        result += f"{dict_diff(value['value'], depth+2)}    "
    elif action == 'deleted':
        result += f"{INDENT * depth}   - {key}: "
        result += f"{dict_diff(value['old value'], depth+2)}    "
    elif action == 'changed':
        result += f"{INDENT * depth}   - {key}: "
        result += f"{dict_diff(value['old value'], depth+2)}{INDENT}\n"
        result += f"{INDENT * depth}   + {key}: "
        result += f"{dict_diff(value['new value'], depth+2)}"
    elif action == 'recursive call':
        result += f"{INDENT * depth}    {key}: "
        result += f"{stylish_func(value['children'], depth+1)}"
    elif action == 'not changed':
        result += f"{INDENT * depth}     {key}: "
        result += f"{dict_diff(value['value'], depth+2)}"
    return result


def stylish_func(difference, depth=0):
    result = '{\n'
    for key, value in difference.items():
        result += string_formatter(key, value, depth) + '\n'
    result += INDENT * depth + "}"
    return result
