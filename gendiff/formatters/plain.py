

def value_getter(value):
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
        result += plain_func(value['children'], path)
    if action == 'added':
        result += f"Property '{path}' was added with value: " \
                  f"{value_getter(value['value'])}\n"
    if action == 'deleted':
        result += f"Property '{path}' was removed\n"
    if action == 'changed':
        result += f"Property '{path}' was updated. " \
                  f"From {value_getter(value['old value'])} " \
                  f"to {value_getter(value['new value'])}\n"
    return result.strip()


def plain_func(difference, path=''):
    result = ''
    for key, value in difference.items():
        result += string_formatter(value, f"{path}.{key}")
    return result
