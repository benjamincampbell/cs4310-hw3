class Node(object):
    def __init__(self, char, count):
        self.char = char
        self.count = count
        
        self.parent = None
        self.left = None
        self.right = None