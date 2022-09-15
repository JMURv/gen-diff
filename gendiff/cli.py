import argparse
from gendiff.generate_diff import generate_diff


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("-f", '--format', help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(
        generate_diff(args.first_file, args.second_file))
    return args