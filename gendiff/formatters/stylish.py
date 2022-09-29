INDENT = '    '


def string_converter(value, depth=2):
    if value is None:
        return 'null'
    elif type(value) == str:
        return value
    elif type(value) != dict:
        return str(value).lower()
    result = "{\n"
    for k, v in value.items():
        result += f"{INDENT * depth}{k}: "\
                  f"{string_converter(v, depth + 1)}\n"
    result += f'{INDENT * (depth - 1)}' + '}'
    return result


def string_formatter(key, value, depth):
    result = ''
    tabs = INDENT * depth
    action = value['action']
    if action == 'added':
        result += f"{tabs}  + {key}: "\
                  f"{string_converter(value['value'], depth + 2)}"

    elif action == 'deleted':
        result += f"{tabs}  - {key}: "\
                  f"{string_converter(value['old value'], depth + 2)}"

    elif action == 'changed':
        result += f"{tabs}  - {key}: "\
                  f"{string_converter(value['old value'], depth + 2)}\n"\
                  f"{tabs}  + {key}: "\
                  f"{string_converter(value['new value'], depth + 2)}"

    elif action == 'recursive call':
        result += f"{tabs}    {key}: "\
                  f"{calculate_view(value['children'], depth+1)}"

    elif action == 'not changed':
        result += f"{tabs}    {key}: "\
                  f"{string_converter(value['value'], depth + 2)}"
    return result


def calculate_view(difference, depth=0):
    result = '{\n'
    for key, value in difference.items():
        result += f"{string_formatter(key, value, depth)}\n"
    result += f"{INDENT * depth}" + '}'
    return result


def render_stylish(data):
    return calculate_view(data)
