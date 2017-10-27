from node import Node

def decompress(code, key):
    f = open('output.txt', 'w')
    string = decode_key(f, code, key)
    
    print_paths(f, key)
    
    f.write("\n{}\n\n{}".format(code, string))
    
    f.close()
        
def decode_key(f, code, root):
    temp = root
    ret = ""
    done = False

    
    while not done:
        if temp.char:
            ret += temp.char
            temp = root
            if code == "":
                done = True
        else:
            if code[0] == '0':
                code = code[1:]
                if temp.right:
                    temp = temp.right
            elif code[0] == '1':
                code = code[1:]
                if temp.left:
                    temp = temp.left
                
    return ret

def print_paths(f, node):    
    def traverse(node, path):
        if node.char:
            if node.char == '\n':
                f.write("\\n: {}\n".format(path))
            elif node.char == ' ':
                f.write("space: {}\n".format(path))
            else:
                f.write("{}: {}\n".format(node.char, path))
        else:
            traverse(node.right, path+'0')
            traverse(node.left, path+'1')
            
    traverse(node, "")