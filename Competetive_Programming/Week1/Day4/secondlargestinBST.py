def find_second_largest(root_node):
    parent = root_node
    current = root_node.right
    if(current == None):
       current=root_node.left
       while(current.right != None):
            current=current.right
       result = current.value
    else:
        while(current.right != None):
            parent = current
            current=current.right
        if(current.left == None):
            result = parent.value
        else:
            result = find_second_largest(current)
    return result
