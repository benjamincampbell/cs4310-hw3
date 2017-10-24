class HeapNode(object):
    def __init__(self, node):
        self.node = node
        self.weight = 1
        
        self.parent = None
        self.left = None
        self.right = None

class MinHeap(object):
    def __init__(self):
        self.root = None
        
    def add(self, newnode):
        
        new_heap_node = HeapNode(newnode)
        if not self.root:
            # no root node, set new node to root
            self.root = new_heap_node
        else:
            # there is a root node
            temp_heap_node = self.root
            found = False
            
            while not found:
                if temp_heap_node.left:
                    if temp_heap_node.right:
                        temp_head_node.weight += 1
                        # it has left and right children, compare them
                        if temp_heap_node.left.weight < temp_heap_node.right.weight:
                            temp_heap_node = temp_heap_node.left
                        else:
                            temp_heap_node = temp_heap_node.right
                    else:
                        # it does not have a right node, place new node there
                        temp_heap_node.right = new_heap_node
                        found = True
                else:
                    # does not have a left child
                    temp_head_node.weight += 1
                    temp_heap_node.left = new_heap_node
                    found = True