from script.config import parser_config
from script.utils import (
    aggregate_values,
    file_reader,
    filter_values,
    tabulate_print
)


def main() -> None:
    parser = parser_config()
    args = parser.parse_args()
    result = file_reader(args.file)
    if args.where:
        result = filter_values(result, args.where)
    if args.aggregate:
        result = aggregate_values(result, args.aggregate)
    tabulate_print(result)


if __name__ == '__main__':
    main()
