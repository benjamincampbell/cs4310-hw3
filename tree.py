class Node(object):
    def __init__(self, char, count):
        self.char = char
        self.count = count
        self.children = {
            '1': None,
            '2': None,
        }
        
class MaxTree(object):
    def __init__(self):
        self.root = None
        
    def add(self, char, count):
        if not self.root:
            # No current root, this is first node
            self.root = Node(char, count)
        else:
            # There already is a root
            temp = self.root