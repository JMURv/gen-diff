from gendiff.cli import get_arguments
from gendiff.dicts_difference import generate_diff


def main():
    arguments = get_arguments()
    print(
        generate_diff(
            arguments.first_file,
            arguments.second_file,
            arguments.format
        )
    )


if __name__ == '__main__':
    main()
