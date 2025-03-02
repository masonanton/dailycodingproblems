class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def serialize(root):
    if not root:
        return ''
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append('null')

    # Remove trailing 'null' values
    while result and result[-1] == 'null':
        result.pop()

    return ','.join(result)

def deserialize(data):
    if not data:
        return None
    nodes = data.split(',')
    root = Node(nodes[0])
    queue = deque([root])
    index = 1

    while queue and index < len(nodes):
        node = queue.popleft()
        if nodes[index] != 'null':
            node.left = Node(nodes[index])
            queue.append(node.left)
        index += 1
        if index < len(nodes) and nodes[index] != 'null':
            node.right = Node(nodes[index])
            queue.append(node.right)
        index += 1

    return root
