from gendiff.formatters.stylish import stylish_func
from gendiff.formatters.plain import plain_func
from gendiff.formatters.json import json_formatter


def choose_formatter(difference, formatter='stylish'):
    if formatter == 'stylish':
        return stylish_func(difference)
    elif formatter == 'plain':
        return plain_func(difference)
    elif formatter == 'json':
        return json_formatter(difference)
