

def string_converter(value):
    if value is None:
        return 'null'
    elif type(value) == str:
        return f"'{value}'"
    elif not isinstance(value, dict):
        return str(value).lower()
    elif type(value) == dict:
        return '[complex value]'


def string_formatter(value, path):
    result = ''
    path = path[1:] if path[0] == '.' else path
    action = value['action']
    if action == 'recursive call':
        result += calculate_view(value['children'], path) + '\n'
    if action == 'added':
        result += f"Property '{path}' was added with value: " \
                  f"{string_converter(value['value'])}\n"
    if action == 'deleted':
        result += f"Property '{path}' was removed\n"
    if action == 'changed':
        result += f"Property '{path}' was updated. " \
                  f"From {string_converter(value['old value'])} " \
                  f"to {string_converter(value['new value'])}\n"
    return result


def calculate_view(difference, path=''):
    result = ''
    for key, value in difference.items():
        result += string_formatter(value, f"{path}.{key}")
    return result.strip()


def render_plain(data):
    return calculate_view(data)
