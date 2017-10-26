from compress import compress
import sys

with open(sys.argv[1], 'r') as f:
    compress(f)
    
print('decompress')
