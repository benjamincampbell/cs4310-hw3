class QueueNode(object):
    def __init__(self, node):
        self.node = node
        self.parent = None
        self.child = None
        
    def __str__(self):
        return "{{{}}}".format(self.node)

class PriQueue(object):
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __str__(self):
        temp = self.head
        ret = "head: "
        while temp != None:
            ret += "{}->".format(temp)
            temp = temp.child
        return ret
        
    def add(self, new_node):
        newnode = QueueNode(new_node)
        if not self.head:
            # No head node, make head.
            self.head = newnode
        else:
            # head node exists, start comparing.
            found = False
            temp = self.head
            
            while not found:
                if (temp.node.count < newnode.node.count):
                    # current node's count is lower, new node
                    # needs to go further down
                    if temp.child:
                        # if the current node has a child, move
                        # to it
                        temp = temp.child
                    else:
                        # current has no child, make the new node
                        # the child
                        temp.child = newnode
                        newnode.parent = temp
                        found = True
                else: # (temp.count >= newnode.count):
                    # current node's count is the same or
                    # higher, new node can go here.
                    if temp.parent:
                        # current is not head:
                        temp.parent.child = newnode
                        newnode.parent = temp.parent
                    else:
                        self.head = newnode
                    temp.parent = newnode
                    newnode.child = temp
                    
                    found = True
        self.size += 1
                    
    def get_min(self):
        ret = self.head
        if self.head.child:
            self.head.child.parent = None
            self.head = self.head.child
        else:
            self.head = None
        self.size -= 1
        
        return ret