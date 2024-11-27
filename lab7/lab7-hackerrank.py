class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

def decode_huff(root, s):
    decoded_string = ""
    current_node = root
    
    for char in s:
        if char == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.left is None and current_node.right is None:
            decoded_string += current_node.data
            current_node = root  
            
    print(decoded_string)
