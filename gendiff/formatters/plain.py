
def convert_to_str(value):
    if value is None:
        return 'null'
    if type(value) == str:
        return f"'{value}'"
    if not isinstance(value, dict):
        return str(value).lower()
    if type(value) == dict:
        return '[complex value]'


def build_line(value, path):
    result = []
    path = path.strip('.')
    action = value['action']
    if action == 'recursive call':
        result.append(build_plain_iter(value['children'], path))
    if action == 'added':
        result.append(f"Property '{path}' was added with value: "
                      f"{convert_to_str(value['value'])}\n")
    if action == 'deleted':
        result.append(f"Property '{path}' was removed\n")
    if action == 'changed':
        result.append(f"Property '{path}' was updated. "
                      f"From {convert_to_str(value['old value'])} "
                      f"to {convert_to_str(value['new value'])}\n")
    return '\n'.join(result)


def build_plain_iter(difference, path=''):
    result = []
    for key, value in difference.items():
        result.append(build_line(value, f"{path}.{key}"))
    return ''.join(result)


def render_plain(data):
    return build_plain_iter(data).strip()
