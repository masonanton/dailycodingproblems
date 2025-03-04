import pytest
from mar3.solution import XORLinkedList

def test_add_and_get_single_element():
    xor_list = XORLinkedList()
    xor_list.add(10)
    assert xor_list.get(0) == 10

def test_add_multiple_elements():
    xor_list = XORLinkedList()
    elements = [5, 15, 25, 35, 45]
    for elem in elements:
        xor_list.add(elem)
    for i, elem in enumerate(elements):
        assert xor_list.get(i) == elem

def test_get_out_of_bounds():
    xor_list = XORLinkedList()
    xor_list.add(10)
    with pytest.raises(IndexError):
        xor_list.get(1)
    with pytest.raises(IndexError):
        xor_list.get(-1)

def test_add_and_get_edge_cases():
    xor_list = XORLinkedList()
    # Edge cases with 0 and negative numbers
    xor_list.add(0)
    xor_list.add(-10)
    xor_list.add(-20)
    assert xor_list.get(0) == 0
    assert xor_list.get(1) == -10
    assert xor_list.get(2) == -20

def test_large_list():
    xor_list = XORLinkedList()
    large_number = 1000
    for i in range(large_number):
        xor_list.add(i)
    for i in range(large_number):
        assert xor_list.get(i) == i

def test_get_from_empty_list():
    xor_list = XORLinkedList()
    with pytest.raises(IndexError):
        xor_list.get(0)

def test_add_none_value():
    xor_list = XORLinkedList()
    xor_list.add(None)
    assert xor_list.get(0) is None

def test_alternate_add_and_get():
    xor_list = XORLinkedList()
    xor_list.add(1)
    assert xor_list.get(0) == 1
    xor_list.add(2)
    assert xor_list.get(1) == 2
    xor_list.add(3)
    assert xor_list.get(2) == 3
    xor_list.add(4)
    assert xor_list.get(3) == 4

@pytest.mark.parametrize("elements", [
    [1],
    [1, 2, 3],
    [100, 200, 300, 400, 500],
    [-1, -2, -3, -4],
    [0, 1, -1, 2, -2],
    list(range(100)),
])
def test_parametrized_add_and_get(elements):
    xor_list = XORLinkedList()
    for elem in elements:
        xor_list.add(elem)
    for i, elem in enumerate(elements):
        assert xor_list.get(i) == elem

def test_memory_edge_case():
    xor_list = XORLinkedList()
    xor_list.add(0)
    xor_list.add(0)
    assert xor_list.get(0) == 0
    assert xor_list.get(1) == 0