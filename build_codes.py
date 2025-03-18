from argparse import ArgumentParser
from os.path import isfile, isdir


import segno


def parse_config(source_path):

    class Userdata:
        def __init__(self, group):
            self.group = group
            self.check_in_time = None

    with open(source_path, 'r') as _f:
        lines = _f.readlines()

    ids = []
    for line in lines:
        if line.startswith('#'):
            continue
        line = line.rsplit('\n')[0]
        if not line:
            continue
        if line.startswith('@'):
            continue
        ids.append(line)
    return ids


def build_codes(source_path, target_path, scale):

    data = parse_config(source_path)

    if not target_path.endswith('/'):
        target_path = target_path + '/'

    for entry in data:
        qrcode = segno.make_qr(entry)
        qrcode.save(
            f'{target_path}{entry}.png',
            scale=scale,
            border=2,
        )


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "source",
        type=str,
        help="Path to users.txt.",
    )
    parser.add_argument(
        "target",
        type=str,
        help="Path to a directory to store output.",
    )
    parser.add_argument(
        "-s",
        "--scale",
        type=int,
        help="Output file size, defaults to 50.",
        default=50
    )
    args = parser.parse_args()

    if not isfile(args.source):
        print(f"{args.source} not found or isn't a file.")
        exit(10)
    if not isdir(args.target):
        print(f"{args.target} not found or isn't a file.")
        exit(11)

    build_codes(args.source, args.target, args.scale)


if __name__ == '__main__':
    main()
