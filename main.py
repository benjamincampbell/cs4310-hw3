import argparse
from compress import compress

parser = argparse.ArgumentParser(description='Compress and Decompress a file.')
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('--compress', dest='action',
                   action='store_const', const='c',
                   help='compress the file')
group.add_argument('--decompress', dest='action',
                   action='store_const', const='d',
                   help='decompress the file')

parser.add_argument('file', help='file to compress or decompress')

args = parser.parse_args()

if args.action == 'c':
    with open(args.file, 'r') as f:
        compress(f)
elif args.action == 'd':
    print('decompress')
else:
    print('neither apparently')