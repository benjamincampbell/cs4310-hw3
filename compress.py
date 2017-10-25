from node import Node
from priorityqueue import PriQueue

def compress(f):
    # Get count of each letter
    counts = {}
    queue = PriQueue()
    
    for line in f:
        for c in line:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
    # now need to make single-node trees for each letter
    
    for key, value in counts.items():
        queue.add(Node(key, value))
        
    print(queue)
    
    while queue.size > 1:
        print("before: {}".format(queue))
        print("size: {}".format(queue.size))
        min1 = queue.get_min().node
        min2 = queue.get_min().node
        parent = Node(None, 0)
        min1.parent = parent
        min2.parent = parent
        parent.left = min1
        parent.right = min2
        parent.update_count()
        queue.add(parent)
        print("after: {}".format(queue))
        print("size: {}".format(queue.size))
        
    print(queue)