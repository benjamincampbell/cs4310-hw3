from node import Node
from priorityqueue import PriQueue

def compress(filename):
    
    f = open(filename, 'r')
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
    code = get_code(f, key)
    f.close()
    
    return key, code

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

def get_code(f, key):
    
    def find_path(node, char, path):
        if node.char:
            if node.char == char:
                return path
        else:
            f = find_path(node.left, char, path+"1")
            if f:
                return f
            else:
                f = find_path(node.right, char, path+"0")
                return f
    
    f.seek(0)
    code = ""
    
    for c in f.read():
        code += find_path(key, c, "")
    return code