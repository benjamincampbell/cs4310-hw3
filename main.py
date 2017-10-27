from compress import compress
from decompress import decompress
import sys

key, code = compress(sys.argv[1])
    
decompress(code, key)