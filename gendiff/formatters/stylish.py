INDENT = '    '
ADDED = '  + '
REMOVED = '  - '


def convert_to_str(value, depth=2):
    if value is None:
        return 'null'
    if type(value) == str:
        return value
    if type(value) != dict:
        return str(value).lower()
    result = "{\n"
    for k, v in value.items():
        result += f"{INDENT * depth}{k}: "\
                  f"{convert_to_str(v, depth + 1)}\n"
    result += f'{INDENT * (depth - 1)}' + '}'
    return result


def build_line(key, value, depth):
    result = []
    tabs = INDENT * depth
    action = value['action']
    if action == 'added':
        result.append(f"{tabs}{ADDED}{key}: "
                      f"{convert_to_str(value['value'], depth + 2)}")

    elif action == 'deleted':
        result.append(f"{tabs}{REMOVED}{key}: "
                      f"{convert_to_str(value['old value'], depth + 2)}")

    elif action == 'changed':
        result.append(f"{tabs}{REMOVED}{key}: "
                      f"{convert_to_str(value['old value'], depth + 2)}\n"
                      f"{tabs}{ADDED}{key}: "
                      f"{convert_to_str(value['new value'], depth + 2)}")

    elif action == 'recursive call':
        result.append(f"{tabs}{INDENT}{key}: "
                      f"{build_stylish_iter(value['children'], depth+1)}")

    elif action == 'not changed':
        result.append(f"{tabs}{INDENT}{key}: "
                      f"{convert_to_str(value['value'], depth + 2)}")
    return '\n'.join(result)


def build_stylish_iter(difference, depth=0):
    result = ['{']
    for key, value in difference.items():
        result.append(f"{build_line(key, value, depth)}")
    result.append(f"{INDENT * depth}" + '}')
    return '\n'.join(result)


def render_stylish(data):
    return build_stylish_iter(data)
