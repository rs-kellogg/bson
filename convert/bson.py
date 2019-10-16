#!/usr/bin/env python3

from pathlib import Path
import argparse
import sys


def main():
    # parse arguments
    parser = argparse.ArgumentParser(prog="bson2json")
    parser.add_argument(
        "in_dir", help="the directory holding the bson files to be converted"
    )
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )

    if len(sys.argv[1:]) == 0:
        parser.print_usage()  # for just the usage line
        parser.exit()

    args = parser.parse_args()

    # process text files
    bson_files = list((Path(args.in_dir)).glob(f"**/*.bson"))

    with (Path(args.out_file)).open(mode="a") as out:
        for txt_file in txt_files:
            with txt_file.open(mode="r", encoding=args.input_encoding) as f:
                new_header = f.readline()
                if header is None:
                    header = new_header
                    out.write(
                        header.encode(args.output_encoding).decode(args.output_encoding)
                    )
                if args.verbose:
                    print(
                        f"processing file: {f.name} ({len(header.split(args.separator))} fields)"
                    )
                assert new_header == header
                for line in f:
                    # fields = line.split(args.separator)
                    # line = args.separator.join(fields)
                    # if line[len(line)-1] != '\n':
                    #     line += '\n'
                    line = line.replace('true', '1')
                    line = line.replace('false', '0')
                    out.write(
                        line.encode(args.output_encoding).decode(args.output_encoding)
                    )
    sys.exit(0)


if __name__ == "__main__":
    main()
