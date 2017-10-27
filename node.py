class Node(object):
    def __init__(self, char, count):
        self.char = char
        self.count = count
        
        self.parent = None
        self.left = None
        self.right = None
        
    def __str__(self):
        return "{}: {}".format(self.char, self.count)
    
    def update_count(self):
        self.count = self.left.count + self.right.count
    
class HuffTree(object):
    def __init__(self):
        self.root = None