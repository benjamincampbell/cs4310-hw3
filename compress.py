import node

def compress(f):
    # Get count of each letter
    counts = {}
    forest = []
    for line in f:
        for c in line:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
    print(counts)
    # now need to make single-node trees for each letter
    
    for key, value in counts.items():
        print("{}: {}".format(key, value))
        forest.append(node.Node(key, value))
        
    print(forest)