from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def formatting(difference, formatter='stylish'):
    if formatter == 'stylish':
        return render_stylish(difference)
    elif formatter == 'plain':
        return render_plain(difference)
    elif formatter == 'json':
        return render_json(difference)
    raise Exception(f"formatter not found: {formatter}")
