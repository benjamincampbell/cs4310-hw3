from node import Node
from priorityqueue import PriQueue

def compress(f):
    # Get count of each letter
    counts = {}
    queue = PriQueue()
    
    for c in f.read():
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    # now need to make single-node trees for each letter
    
    for key, value in counts.items():
        queue.add(Node(key, value))
        
    key = huffify(queue)
    
    write_file(f, key)

def huffify(queue):
    while queue.size > 1:
        min1 = queue.get_min().node
        min2 = queue.get_min().node
        parent = Node(None, 0)
        min1.parent = parent
        min2.parent = parent
        parent.left = min1
        parent.right = min2
        parent.update_count()
        queue.add(parent)
    return queue.head.node

def write_file(f, key):
    
    def find_path(node, char, path):
        if node.char:
            if node.char == char:
                return path
        else:
            f = find_path(node.left, char, path+"1")
            f = find_path(node.right, char, path+"0")
            if f:
                return f
    
    print(find_path(key, 'e', ""))
    f.seek(0)
    
    for c in f:
        print(c)