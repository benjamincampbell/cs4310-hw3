from compress import compress
from decompress import decompress
import sys
import time

def main():
    key, code = compress(sys.argv[1])
    
    decompress(code, key)
    
    
if __name__ == '__main__':
    results = []
    for i in range(0, 1000):
        start = time.time()
        main()
        finish = time.time()
        results.append(finish - start)
        
    print("Avg run time for 1000 runs: {} milliseconds".format((sum(results) / len(results)) * 1000))