import json
import yaml


def data_parser(data):
    if type(data) == dict:
        return data
    elif data.endswith('.json'):
        return json.load(open(data))
    elif data.endswith('.yml') or data.endswith('.yaml'):
        return yaml.safe_load(open(data))
