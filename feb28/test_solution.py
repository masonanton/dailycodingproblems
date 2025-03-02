import pytest
from feb28.solution import Node, serialize, deserialize

def test_serialization():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialized = serialize(node)
    deserialized = deserialize(serialized)
    assert deserialized.left.left.val == 'left.left'
    assert deserialized.left.val == 'left'
    assert deserialized.right.val == 'right'
    assert deserialized.val == 'root'

def test_empty_tree():
    assert deserialize(serialize(None)) is None

def test_single_node():
    node = Node('single')
    serialized = serialize(node)
    deserialized = deserialize(serialized)
    assert deserialized.val == 'single'
    assert deserialized.left is None
    assert deserialized.right is None

def test_balanced_tree():
    node = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f'), Node('g')))
    serialized = serialize(node)
    deserialized = deserialize(serialized)
    assert deserialized.left.val == 'b'
    assert deserialized.right.val == 'c'
    assert deserialized.left.left.val == 'd'
    assert deserialized.left.right.val == 'e'
    assert deserialized.right.left.val == 'f'
    assert deserialized.right.right.val == 'g'

def test_unbalanced_tree():
    node = Node('root', Node('left', Node('left.left', Node('left.left.left'))), Node('right'))
    serialized = serialize(node)
    deserialized = deserialize(serialized)
    assert deserialized.left.left.left.val == 'left.left.left'
    assert deserialized.left.left.val == 'left.left'
    assert deserialized.left.val == 'left'
    assert deserialized.right.val == 'right'

def test_large_tree():
    root = Node('root')
    current = root
    for i in range(1, 20):
        current.left = Node(f'node{i}')
        current = current.left
    serialized = serialize(root)
    deserialized = deserialize(serialized)
    current = deserialized
    for i in range(1, 20):
        assert current.left.val == f'node{i}'
        current = current.left

def test_tree_with_numeric_values():
    node = Node(1, Node(2, Node(3)), Node(4, Node(5), Node(6)))
    serialized = serialize(node)
    deserialized = deserialize(serialized)
    assert deserialized.left.left.val == 3
    assert deserialized.left.val == 2
    assert deserialized.right.val == 4
    assert deserialized.right.left.val == 5
    assert deserialized.right.right.val == 6

def test_tree_with_duplicate_values():
    node = Node('root', Node('child', Node('child'), Node('child')), Node('child'))
    serialized = serialize(node)
    deserialized = deserialize(serialized)
    assert deserialized.left.val == 'child'
    assert deserialized.right.val == 'child'
    assert deserialized.left.left.val == 'child'
    assert deserialized.left.right.val == 'child'
