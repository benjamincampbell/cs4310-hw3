import argparse

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
    # Get count of each letter
    counts = {}
    with open(args.file, 'r') as f:
        for line in f:
            for c in line:
                if c in counts:
                    counts[c] += 1
                else:
                    counts[c] = 1
    # now need to make single-node trees for each letter
    
elif args.action == 'd':
    print('decompress')
else:
    print('neither apparently')